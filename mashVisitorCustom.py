import warnings

from antlr4 import *

from gen.mashParser import mashParser
from gen.mashVisitor import mashVisitor


class mashVisitorCustom(mashVisitor):
    def __int__(self):
        self.variables = {}
        self.functions = {}

    def visitProgram(self, ctx: mashParser.ProgramContext):
        result = []
        for statement in ctx.statement():
            result.append(self.visit(statement))
        return result

    def visitStatement(self, ctx: mashParser.StatementContext):
        return self.visitChildren(ctx)

    def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
        # echoed_value = self.visit(ctx.expression())
        # print(echoed_value)
        # expression = ctx.expression()
        result = self.visit(ctx.expression())

        if isinstance(result, str):
            print(result.strip('"'))  # Strip quotes if it's a string
        elif isinstance(result, int):
            print(result)
        return result

    def visitExpression(self, ctx: mashParser.ExpressionContext):
        if ctx.arithmetic_expression():
            return self.visit(ctx.arithmetic_expression())
        elif ctx.string_expression():
            return self.visit(ctx.string_expression())
        elif ctx.logical_expression():
            return self.visit(ctx.logical_expression())
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

    def visitPrimary_expression(self, ctx: mashParser.Primary_expressionContext):
        # # If there's an INTEGER, convert to integer
        # if ctx.INTEGER():
        #     return int(ctx.INTEGER().getText())
        # # Otherwise, recursively evaluate nested expressions
        # return self.visit(ctx.getChild(0))
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.getChildCount() == 3:  # Handles brackets (e.g., (expression))
            return self.visit(ctx.getChild(1))  # Visit the inner expression

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

