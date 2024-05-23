import warnings

from antlr4 import *

from gen.mashParser import mashParser
from gen.mashVisitor import mashVisitor
import sys


class mashVisitorCustom(mashVisitor):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def visitProgram(self, ctx: mashParser.ProgramContext):
        result = []
        for statement in ctx.statement():
            result.append(self.visit(statement))
        return result

    def visitStatement(self, ctx: mashParser.StatementContext):
        return self.visitChildren(ctx)

    # def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
    #     result = self.visit(ctx.expression())
    #
    #     if isinstance(result, str):
    #         print(result.strip('"'))
    #     elif isinstance(result, int):
    #         print(result)
    #     return result

    def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
        if ctx.expression():
            result = self.visit(ctx.expression())
        else:
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                raise Exception(f"Variable '{var_name}' is not declared.")
            result = self.variables[var_name]["value"]

        if isinstance(result, str):
            print(result.strip('"'))
        elif isinstance(result, int):
            print(result)
        elif isinstance(result, bool):
            print("true" if result else "false")
        return result

    # def visitExpression(self, ctx: mashParser.ExpressionContext):
    #     if ctx.arithmetic_expression():
    #         return self.visit(ctx.arithmetic_expression())
    #     elif ctx.string_expression():
    #         return self.visit(ctx.string_expression())
    #     elif ctx.logical_expression():
    #         return self.visit(ctx.logical_expression())
    #     return None
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
            if var_name not in self.variables:
                raise Exception(f"Variable '{var_name}' is not declared.")
            return self.variables[var_name]["value"]
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
                raise ValueError("Division by zero!")
            return int(left / right)

    # def visitPrimary_expression(self, ctx: mashParser.Primary_expressionContext):
    #     if ctx.INTEGER():
    #         return int(ctx.INTEGER().getText())
    #     elif ctx.getChildCount() == 3:
    #         return self.visit(ctx.getChild(1))
    #
    #     return None

    def visitPrimary_expression(self, ctx: mashParser.Primary_expressionContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name not in self.variables:
                raise Exception(f"Variable '{var_name}' is not declared.")
            return self.variables[var_name]["value"]
        elif ctx.getChildCount() == 3:
            return self.visit(ctx.getChild(1))
        return None

    def visitString_expression(self, ctx: mashParser.String_expressionContext):
        return ctx.STRING().getText()

    def visitLogical_expression(self, ctx: mashParser.Logical_expressionContext):
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

    # def visitVar_declar(self, ctx: mashParser.Var_declarContext):
    #     var_name = ctx.IDENTIFIER().getText()
    #     if ctx.expression():
    #         value = self.visit(ctx.expression())
    #         self.variables[var_name] = value
    #     return var_name

    def visitVar_declar(self, ctx: mashParser.Var_declarContext):
        var_type = ctx.type_().getText()
        var_name = ctx.IDENTIFIER(0).getText()
        if var_name in self.variables:
            print(f"Error: Variable '{var_name}' is already declared.", file=sys.stderr)
            return None
        self.variables[var_name] = {"type": var_type, "value": None}

        if ctx.expression():
            value = self.visit(ctx.expression())
            if var_type == "int_var" and not isinstance(value, int):
                print(f"Error: Variable '{var_name}' must be assigned an integer.", file=sys.stderr)
                return None
            elif var_type == "string_var" and not isinstance(value, str):
                print(f"Error: Variable '{var_name}' must be assigned a string.", file=sys.stderr)
                return None
            self.variables[var_name]["value"] = value
        elif ctx.IDENTIFIER(1):
            assigned_var_name = ctx.IDENTIFIER(1).getText()
            if assigned_var_name not in self.variables:
                print(f"Error: Variable '{assigned_var_name}' is not declared.", file=sys.stderr)
                return None
            value = self.variables[assigned_var_name]["value"]
            if var_type == "int_var" and not isinstance(value, int):
                print(f"Error: Variable '{var_name}' must be assigned an integer.", sys.stderr)
                return None
            elif var_type == "string_var" and not isinstance(value, str):
                print(f"Error: Variable '{var_name}' must be assigned a string.", sys.stderr)
                return None
            self.variables[var_name]["value"] = value

        return None

    def visitAssignment(self, ctx: mashParser.AssignmentContext):
        var_name = ctx.IDENTIFIER(0).getText()
        if var_name not in self.variables:
            print(f"Error: Variable '{var_name}' is not declared.", file=sys.stderr)
            return None
        var_type = self.variables[var_name]["type"]

        if ctx.IDENTIFIER(1):
            assigned_var_name = ctx.IDENTIFIER(1).getText()
            if assigned_var_name not in self.variables:
                print(f"Error: Variable '{assigned_var_name}' is not declared.", sys.stderr)
                return None
            value = self.variables[assigned_var_name]["value"]
        else:
            value = self.visit(ctx.expression())

        if var_type == "int_var" and not isinstance(value, int):
            print(f"Error: Variable '{var_name}' must be assigned an integer.", sys.stderr)
            return None
        elif var_type == "string_var" and not isinstance(value, str):
            print(f"Error: Variable '{var_name}' must be assigned a string.", sys.stderr)
            return None
        self.variables[var_name]["value"] = value
        return value

    def visitWhile_statement(self, ctx: mashParser.While_statementContext):
        while self.visit(ctx.logical_expression()):
            for statement in ctx.statement():
                self.visit(statement)
        return None

    def visitFor_statement(self, ctx: mashParser.For_statementContext):
        self.visit(ctx.assignment(0))

        while self.visit(ctx.logical_expression()):
            for statement in ctx.statement():
                self.visit(statement)

            self.visit(ctx.assignment(1))

        return None

    # def visitFunction_declar(self, ctx: mashParser.Function_declarContext):
    #     func_name = ctx.IDENTIFIER().getText()
    #     params = ctx.parameters()
    #     param_list = []
    #     if params:
    #         for param in params.parameter():
    #             param_type = param.type_().getText()
    #             param_name = param.IDENTIFIER().getText()
    #             param_list.append((param_type, param_name))
    #
    #     return_type = None
    #     if ctx.return_type():
    #         return_type = ctx.return_type().type_().getText()
    #
    #     func_body = ctx.statement()
    #     self.functions[func_name] = {
    #         "params": param_list,
    #         "return_type": return_type,
    #         "body": func_body
    #     }
    #     return None
    #
    # def visitFunction_call(self, ctx: mashParser.Function_callContext):
    #     func_name = ctx.IDENTIFIER().getText()
    #     if func_name not in self.functions:
    #         raise Exception(f"Function '{func_name}' is not declared.")
    #
    #     func = self.functions[func_name]
    #     args = ctx.arguments()
    #     if args:
    #         arg_values = [self.visit(arg) for arg in args.expression()]
    #     else:
    #         arg_values = []
    #
    #     if len(arg_values) != len(func["params"]):
    #         raise Exception(f"Function '{func_name}' expects {len(func['params'])} arguments, got {len(arg_values)}.")
    #
    #     local_vars = {}
    #     for (param_type, param_name), arg_value in zip(func["params"], arg_values):
    #         if param_type == "int_var" and not isinstance(arg_value, int):
    #             raise Exception(f"Function '{func_name}' parameter '{param_name}' expects an integer.")
    #         elif param_type == "string_var" and not isinstance(arg_value, str):
    #             raise Exception(f"Function '{func_name}' parameter '{param_name}' expects a string.")
    #         local_vars[param_name] = {"type": param_type, "value": arg_value}
    #
    #     old_vars = self.variables
    #     self.variables = local_vars
    #
    #     result = None
    #     for statement in func["body"]:
    #         result = self.visit(statement)
    #
    #     self.variables = old_vars
    #
    #     if func["return_type"]:
    #         if func["return_type"] == "int_var" and not isinstance(result, int):
    #             raise Exception(f"Function '{func_name}' must return an integer.")
    #         elif func["return_type"] == "string_var" and not isinstance(result, str):
    #             raise Exception(f"Function '{func_name}' must return a string.")
    #
    #     return result


        # def visitFunctionCall(self, ctx: MithonParser.FunctionCallContext):
        #     function_name = ctx.IDENTIFIER().getText()
        #     argument_list = ctx.argumentList() if ctx.argumentList() else []
        #     argument_list = ctx.argumentList(0) if ctx.argumentList() else []
        #
        #     if function_name in self.function_declarations:
        #         function_info = self.function_declarations[function_name]
        #         parameter_list = function_info['parameters']
        #         # print(parameter_list)
        #         function_body = function_info['body']
        #
        #         if len(argument_list) != len(parameter_list):
        #             if len(argument_list.expression()) != len(parameter_list):
        #                 raise Exception(
        #                     f"Function '{function_name}' expects {len(parameter_list)} arguments, but {len(argument_list)} were provided")
        #
        #         argument_list = argument_list.expression()
        #
        #         self.pushScope()
        #
        #         for parameter, argument in zip(parameter_list, argument_list):
        #             print(parameter, argument)
        #             arg_value = self.visit(argument)
        #             self.addVariable(parameter, None, arg_value)
        #             if type(arg_value).__name__ != parameter[0]:
        #                 raise Exception(
        #                     f"Argument {parameter[1]} expected type: {parameter[0]}. Got: {type(arg_value).__name__} instead.")
        #             self.addVariable(parameter[1], parameter[0], arg_value)
        #
        #         print(self.scopes)
        #
        #         return_value = self.visit(function_body)
        #
        #         self.popScope()
        #
        #         return return_value  # Return the result of the function call
        #     else:
        #         raise Exception(f"Function '{function_name}' is not defined")

    # def visitStatement_list(self, ctx: mashParser.Statement_listContext):
    #     # for statement in ctx.statement():
    #     #     return self.visit(statement)
    #
    #     return_value = None
    #
    #     for statement in self.visitChildren(ctx):
    #         return_value = self.visitStatement(statement)
    # 
    #         if return_value == 'break':
    #             return 'break'
    #
    #         if return_value == 'continue':
    #             return 'continue'
    #
    #         if return_value is not None:
    #             return return_value
    #
    #     return return_value

    def visitFunction_declar(self, ctx: mashParser.Function_declarContext):
        func_name = ctx.IDENTIFIER().getText()
        params = ctx.parameters()
        param_list = []
        if params:
            for param in params.parameter():
                param_type = param.type_().getText()
                param_name = param.IDENTIFIER().getText()
                param_list.append((param_type, param_name))

        return_type = None
        if ctx.return_type():
            return_type = ctx.return_type().type_().getText()

        func_body = ctx.statement()
        self.functions[func_name] = {
            "params": param_list,
            "return_type": return_type,
            "body": func_body
        }
        return None

    def visitFunction_call(self, ctx: mashParser.Function_callContext):
        func_name = ctx.IDENTIFIER().getText()
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")

        func = self.functions[func_name]
        args = ctx.arguments()
        if args:
            arg_values = [self.visit(arg) for arg in args.expression()]
        else:
            arg_values = []

        if len(arg_values) != len(func["params"]):
            raise Exception(f"Function '{func_name}' expects {len(func['params'])} arguments, got {len(arg_values)}.")

        local_vars = {}
        for (param_type, param_name), arg_value in zip(func["params"], arg_values):
            if param_type == "int_var" and not isinstance(arg_value, int):
                raise Exception(f"Function '{func_name}' parameter '{param_name}' expects an integer.")
            elif param_type == "string_var" and not isinstance(arg_value, str):
                raise Exception(f"Function '{func_name}' parameter '{param_name}' expects a string.")
            local_vars[param_name] = {"type": param_type, "value": arg_value}

        old_vars = self.variables
        self.variables = local_vars

        result = None
        for statement in func["body"]:
            result = self.visit(statement)

        self.variables = old_vars

        if func["return_type"]:
            if func["return_type"] == "int_var" and not isinstance(result, int):
                raise Exception(f"Function '{func_name}' must return an integer.")
            elif func["return_type"] == "string_var" and not isinstance(result, str):
                raise Exception(f"Function '{func_name}' must return a string.")

        return result

    #
    #
    # def visitFunction_declar(self, ctx: mashParser.Function_declarContext):
    #     print("deklaracja")
    #     func_name = ctx.IDENTIFIER().getText()
    #     param_list = []
    #     for param in ctx.parameters().parameter():
    #         param_type = param.type_().getText()
    #         param_name = param.IDENTIFIER().getText()
    #         param_list.append((param_type, param_name))
    #
    #     return_type = ctx.return_type().type_().getText() if ctx.return_type() else None
    #     #func_body = self.visitStatement_list(ctx)
    #     print(ctx)
    #     #func_body = self.visitStatement_list(ctx.statement_list())
    #     # func_body = ctx.statement_list()
    #     func_body = ctx.statement_list()
    #
    #     # print("Nazwa funkcji: " + func_name)
    #     # print("Parametry funkcji: ")
    #     # print(param_list)
    #     # print("Zwracający typ: " + return_type)
    #     # print("Instrukcja: ")
    #     # print(type(func_body))
    #     # print(func_body)
    #
    #     self.functions[func_name] = {
    #         "params": param_list,
    #         "return_type": return_type,
    #         "body": func_body
    #     }
    #     # if return_type != 'None' and not self.doesFunctionReturn(func_body):
    #     #     raise Exception(f"Function '{func_name}' must return a value of type {return_type}")
    #
    # def doesFunctionReturn(self, ctx):
    #     for statement in ctx.statement():
    #         if 'return' in statement.getText():
    #             return True
    #     return False
    #
    # def visitFunction_call(self, ctx: mashParser.Function_callContext):
    #     func_name = ctx.IDENTIFIER().getText()
    #     if func_name not in self.functions:
    #         raise Exception(f"Function '{func_name}' is not declared.")
    #
    #     func = self.functions[func_name]
    #     args = ctx.arguments().expression() if ctx.arguments() else []
    #     # print(args)
    #     arg_values = [self.visit(arg) for arg in args]
    #     # print(arg_values)
    #
    #
    #
    #
    #     if len(arg_values) != len(func["params"]):
    #         raise Exception(f"Function '{func_name}' expects {len(func['params'])} arguments, got {len(arg_values)}.")
    #
    #     local_vars = {}
    #     for (param_type, param_name), arg_value in zip(func["params"], arg_values):
    #         if param_type == "int_var" and not isinstance(arg_value, int):
    #             raise Exception(f"Function '{func_name}' parameter '{param_name}' expects an integer.")
    #         elif param_type == "string_var" and not isinstance(arg_value, str):
    #             raise Exception(f"Function '{func_name}' parameter '{param_name}' expects a string.")
    #         local_vars[param_name] = {"type": param_type, "value": arg_value}
    #
    #     old_vars = self.variables
    #     self.variables = local_vars
    #
    #     result = None
    #
    #     for statement in func["body"]:
    #         result = self.visit(statement)
    #
    #     self.variables = old_vars
    #
    #     # if func["return_type"]:
    #     #     if func["return_type"] == "int_var" and not isinstance(result, int):
    #     #         raise Exception(f"Function '{func_name}' must return an integer.")
    #     #     elif func["return_type"] == "string_var" and not isinstance(result, str):
    #     #         raise Exception(f"Function '{func_name}' must return a string.")
    #
    #     # --------------------
    #     # if func["return_type"] and func["return"]:
    #     #     if func["return_type"] == "int_var":
    #     #         if func["return"] not isinstance(result, int):
    #     #           raise Exception(f"Function '{func_name}' must return an integer.")
    #     #     elif func["return_type"] == "string_var":
    #     #         if func["return"] not isinstance(result, str):
    #     #           raise Exception(f"Function '{func_name}' must return a string.")
    #     #     -----------------------------------
    #
    #     # if func["return_type"] == "int_var" and isinstance(result,int):
    #     #     return int(result)
    #     # elif func["return_type"] == "string_var" and isinstance(result, str):
    #     #     return str(result)
    #
    #     return result

    # def visitReturn_statement(self, ctx: mashParser.Return_statementContext):
    #     return self.visit(ctx.expression())

