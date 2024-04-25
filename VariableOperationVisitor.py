from antlr4 import *
from gen.VariableLangLexer import VariableLangLexer
from gen.VariableLangParser import VariableLangParser
from gen.VariableLangVisitor import VariableLangVisitor

class VariableOperationVisitor(VariableLangVisitor):
    def __init__(self, variables):
        self.variables = variables

    def visitAssignment(self, ctx:VariableLangParser.AssignmentContext):
        identifier = ctx.IDENTIFIER().getText()
        if identifier not in self.variables:
            raise Exception(f"Zmienna '{identifier}' nie została jeszcze zadeklarowana")
        value = self.visit(ctx.expr())
        self.variables[identifier] = value
        return value

    def visitExpr(self, ctx:VariableLangParser.ExprContext):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            operator = ctx.getChild(1).getText()
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
        elif ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()
            if identifier not in self.variables:
                raise Exception(f"Zmienna '{identifier}' nie została jeszcze zadeklarowan")
            return self.variables[identifier]
        return 0
