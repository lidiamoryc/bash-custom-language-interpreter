from antlr4 import *
from gen.mashParser import mashParser
from gen.mashVisitor import mashVisitor
import sys

class Function:
    def __init__(self, return_type, parameters, body):
        self.return_type = return_type
        self.parameters = parameters
        self.body = body

class Variable:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class VariableNotDeclaredError(Exception):
    def __init__(self, variable_name, line):
        self.variable_name = variable_name
        self.line = line
        super().__init__(f"Line {line}: Variable '{variable_name}' is not declared.")

class FunctionNotDeclaredError(Exception):
    def __init__(self, function_name, line):
        self.function_name = function_name
        self.line = line
        super().__init__(f"Line {line}: Function '{function_name}' is not declared.")

class CustomTypeError(Exception):
    def __init__(self, message, line):
        self.line = line
        super().__init__(f"Line {line}: {message}")

class CustomSyntaxError(Exception):
    def __init__(self, message, line):
        self.line = line
        super().__init__(f"Line {line}: {message}")

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class mashVisitorCustom(mashVisitor):
    def __init__(self):
        self.scopes = [{}]
        self.functions = {}
        super().__init__()

    def pushScope(self):
        self.scopes.append({})

    def popScope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()

    def addVariable(self, name, type_, value):
        if name in self.functions:
            raise Exception("Variable name cannot be the same as a function name.")
        self.scopes[-1][name] = Variable(type_, value)

    def lookupVariable(self, name, line):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise VariableNotDeclaredError(name, line)

    def updateVariable(self, name, value, line):
        for scope in reversed(self.scopes):
            if name in scope:
                var_type = scope[name].type
                if var_type in ("int_var", "float_var"):
                    value = self.convert_to_numeric_type(var_type, value)
                scope[name].value = value
                return
        raise VariableNotDeclaredError(name, line)

    def is_variable(self, name):
        return any(name in scope for scope in self.scopes)

    def visitProgram(self, ctx: mashParser.ProgramContext):
        for statement in ctx.statement():
            if statement.function_declar():
                self.visit(statement)
        for statement in ctx.statement():
            if not statement.function_declar():
                self.visit(statement)

    def visitStatement(self, ctx: mashParser.StatementContext):
        try:
            return self.visitChildren(ctx)
        except ReturnValue as rv:
            raise rv
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
        line = ctx.start.line
        if ctx.expression():
            result = self.visit(ctx.expression())
        else:
            var_name = ctx.IDENTIFIER().getText()
            var = self.lookupVariable(var_name, line)
            result = var.value

        if isinstance(result, str):
            print(result.strip('"'))
        elif isinstance(result, int):
            print(result)
        elif isinstance(result, bool):
            print("true" if result else "false")
        return result

    def visitExpression(self, ctx: mashParser.ExpressionContext):
        if ctx.arithmetic_expression():
            return self.visit(ctx.arithmetic_expression())
        elif ctx.string_expression():
            return self.visit(ctx.string_expression())
        elif ctx.logical_expression():
            return self.visit(ctx.logical_expression())
        elif ctx.int_expression():
            return int(ctx.int_expression().getText())
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            line = ctx.start.line
            var = self.lookupVariable(var_name, line)
            return var.value
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        return None

    def visitArithmetic_expression(self, ctx: mashParser.Arithmetic_expressionContext):
        return self.visit(ctx.additive_expression())

    def visitAdditive_expression(self, ctx: mashParser.Additive_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right

    def visitMultiplicative_expression(self, ctx: mashParser.Multiplicative_expressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        if operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ZeroDivisionError("Division by zero!")
            return int(left / right)

    def visitPrimary_expression(self, ctx: mashParser.Primary_expressionContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            line = ctx.start.line
            var = self.lookupVariable(var_name, line)
            return var.value
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        return None

    def visitString_expression(self, ctx: mashParser.String_expressionContext):
        return ctx.STRING().getText()

    def visitLogical_expression(self, ctx: mashParser.Logical_expressionContext):
        line = ctx.start.line
        if ctx.getText() == "true" or ctx.getText() == "1":
            return True
        elif ctx.getText() == "false" or ctx.getText() == "0":
            return False

        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if operator == 'and':
                return left and right
            elif operator == 'or':
                return left or right

        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == 'not':
            expr = self.visit(ctx.getChild(1))
            return not expr

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        if ctx.comparison_expression():
            return self.visit(ctx.comparison_expression())

        return None

    def visitComparison_expression(self, ctx: mashParser.Comparison_expressionContext):
        left = self.visit(ctx.arithmetic_expression(0))
        right = self.visit(ctx.arithmetic_expression(1))
        operator = ctx.getChild(1).getText()

        if operator == '<':
            return left < right
        elif operator == '>':
            return left > right
        elif operator == '==':
            return left == right
        elif operator == '!=':
            return left != right

    def visitVar_declar(self, ctx: mashParser.Var_declarContext):
        line = ctx.start.line
        var_type = ctx.type_().getText()
        var_name = ctx.IDENTIFIER(0).getText()
        #print(f"Declaring variable: {var_name} of type: {var_type}")
        if var_name in self.scopes[-1]:
            raise CustomSyntaxError(f"Variable '{var_name}' is already declared.", line)
        self.addVariable(var_name, var_type, None)

        if ctx.expression():
            value = self.visit(ctx.expression())
            var = self.lookupVariable(var_name, line)
            var.value = value
        elif len(ctx.IDENTIFIER()) > 1:
            assigned_var_name = ctx.IDENTIFIER(1).getText()
           # print(f"Assigning value from variable: {assigned_var_name} to {var_name}")
            assigned_var = self.lookupVariable(assigned_var_name, line)
            var = self.lookupVariable(var_name, line)
            var.value = assigned_var.value

        return None

    def visitAssignment(self, ctx: mashParser.AssignmentContext):
        line = ctx.start.line
        var_name = ctx.IDENTIFIER(0).getText()
        #print(f"Assigning value to variable: {var_name}")
        var = self.lookupVariable(var_name, line)

        if len(ctx.IDENTIFIER()) > 1:
            assigned_var_name = ctx.IDENTIFIER(1).getText()
            #print(f"Assigning value from variable: {assigned_var_name} to {var_name}")
            assigned_var = self.lookupVariable(assigned_var_name, line)
            var.value = assigned_var.value
        else:
            value = self.visit(ctx.expression())
            var.value = value

        return var.value

    def visitFunction_declar(self, ctx: mashParser.Function_declarContext):
        line = ctx.start.line
        func_name = ctx.IDENTIFIER().getText()
        params = ctx.parameters()
        param_list = []
        if params:
            for param in params.parameter():
                param_type = param.type_()
                if param_type is None:
                    raise CustomSyntaxError(
                        f"Line {line}: Missing type for parameter '{param.IDENTIFIER().getText()}' in function '{func_name}'.")
                param_name = param.IDENTIFIER().getText()
                param_list.append((param_type.getText(), param_name))

        return_type = None
        if ctx.return_type():
            return_type = ctx.return_type().type_().getText()

        func_body = ctx.statement_list()
        self.functions[func_name] = Function(return_type, param_list, func_body)
        return None

    def visitFunction_call(self, ctx: mashParser.Function_callContext):
        function_name = ctx.IDENTIFIER().getText()
        arguments = [self.visit(arg) for arg in ctx.arguments().expression()] if ctx.arguments() else []

        if function_name in self.functions:
            function_info = self.functions[function_name]
            function_params = function_info.parameters
            function_body = function_info.body

            self.pushScope()

            for (param_type, param_name), arg in zip(function_params, arguments):
                self.addVariable(param_name, param_type, arg)

            try:
                self.visit(function_body)
            except ReturnValue as rv:
                self.popScope()
                return rv.value
            self.popScope()
        else:
            raise FunctionNotDeclaredError(function_name, ctx.start.line)

    def visitReturn_statement(self, ctx: mashParser.Return_statementContext):
        value = self.visit(ctx.expression())
        raise ReturnValue(value)

    def visitArguments(self, ctx: mashParser.ArgumentsContext):
        return self.visitChildren(ctx)

    def visitIf_statement(self, ctx: mashParser.If_statementContext):
        condition = self.visit(ctx.logical_expression())
        if condition:
            for statement in ctx.statement():
                self.visit(statement)
        else:
            for elifCtx in ctx.elif_block():
                if self.visit(elifCtx.logical_expression()):
                    for statement in elifCtx.statement():
                        self.visit(statement)
                    return
            if ctx.else_block():
                for statement in ctx.else_block().statement():
                    self.visit(statement)
        return None

    def visitWhile_statement(self, ctx: mashParser.While_statementContext):
        while self.visit(ctx.logical_expression()):
            for statement in ctx.statement():
                self.visit(statement)
        return None

    def visitFor_statement(self, ctx: mashParser.For_statementContext):
        # Inicjalizacja (assignment lub var_declar)
        if ctx.assignment(0):
            self.visit(ctx.assignment(0))
        elif ctx.var_declar():
            self.visit(ctx.var_declar())

        # Pętla
        while self.visit(ctx.logical_expression()):
            # Ciało pętli
            for statement in ctx.statement():
                self.visit(statement)

            # Krok pętli (increment_statement, assignment lub decrement_statement)
            if ctx.increment_statement():
                self.visit(ctx.increment_statement())
            elif ctx.assignment(1):
                self.visit(ctx.assignment(1))
            elif ctx.decrement_statement():
                self.visit(ctx.decrement_statement())

        return None

    def convert_to_numeric_type(self, var_type, value):
        try:
            if var_type == "int_var":
                return int(value)
            elif var_type == "float_var":
                return float(value)
        except ValueError:
            raise CustomTypeError(f"Cannot convert {value} to {var_type}", -1)

    def visitIncrement_statement(self, ctx: mashParser.Increment_statementContext):
        line = ctx.start.line
        var_name = ctx.IDENTIFIER().getText()
        var = self.lookupVariable(var_name, line)

        if var.type in ("int_var", "float_var"):
            var.value = self.convert_to_numeric_type(var.type, var.value) + 1
        else:
            raise CustomTypeError(f"Cannot increment variable of type '{var.type}'", line)

        return var.value

    def visitDecrement_statement(self, ctx: mashParser.Decrement_statementContext):
        line = ctx.start.line
        var_name = ctx.IDENTIFIER().getText()
        var = self.lookupVariable(var_name, line)

        if var.type in ("int_var", "float_var"):
            var.value = self.convert_to_numeric_type(var.type, var.value) - 1
        else:
            raise CustomTypeError(f"Cannot decrement variable of type '{var.type}'", line)

        return var.value
