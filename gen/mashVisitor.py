# Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mashParser import mashParser
else:
    from mashParser import mashParser

# This class defines a complete generic visitor for a parse tree produced by mashParser.

class mashVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mashParser#program.
    def visitProgram(self, ctx:mashParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#statement.
    def visitStatement(self, ctx:mashParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#echo_function.
    def visitEcho_function(self, ctx:mashParser.Echo_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#expression.
    def visitExpression(self, ctx:mashParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#string_expression.
    def visitString_expression(self, ctx:mashParser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:mashParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#additive_expression.
    def visitAdditive_expression(self, ctx:mashParser.Additive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#multiplicative_expression.
    def visitMultiplicative_expression(self, ctx:mashParser.Multiplicative_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#primary_expression.
    def visitPrimary_expression(self, ctx:mashParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#logical_expression.
    def visitLogical_expression(self, ctx:mashParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#comparison_expression.
    def visitComparison_expression(self, ctx:mashParser.Comparison_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#type.
    def visitType(self, ctx:mashParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#var_declar.
    def visitVar_declar(self, ctx:mashParser.Var_declarContext):
        return self.visitChildren(ctx)



del mashParser