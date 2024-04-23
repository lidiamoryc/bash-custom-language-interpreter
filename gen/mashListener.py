# Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .mashParser import mashParser
else:
    from mashParser import mashParser

# This class defines a complete listener for a parse tree produced by mashParser.
class mashListener(ParseTreeListener):

    # Enter a parse tree produced by mashParser#program.
    def enterProgram(self, ctx:mashParser.ProgramContext):
        pass

    # Exit a parse tree produced by mashParser#program.
    def exitProgram(self, ctx:mashParser.ProgramContext):
        pass


    # Enter a parse tree produced by mashParser#statement.
    def enterStatement(self, ctx:mashParser.StatementContext):
        pass

    # Exit a parse tree produced by mashParser#statement.
    def exitStatement(self, ctx:mashParser.StatementContext):
        pass


    # Enter a parse tree produced by mashParser#echo_function.
    def enterEcho_function(self, ctx:mashParser.Echo_functionContext):
        pass

    # Exit a parse tree produced by mashParser#echo_function.
    def exitEcho_function(self, ctx:mashParser.Echo_functionContext):
        pass


    # Enter a parse tree produced by mashParser#expression.
    def enterExpression(self, ctx:mashParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mashParser#expression.
    def exitExpression(self, ctx:mashParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mashParser#string_expression.
    def enterString_expression(self, ctx:mashParser.String_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#string_expression.
    def exitString_expression(self, ctx:mashParser.String_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:mashParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:mashParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#additive_expression.
    def enterAdditive_expression(self, ctx:mashParser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#additive_expression.
    def exitAdditive_expression(self, ctx:mashParser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:mashParser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:mashParser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#primary_expression.
    def enterPrimary_expression(self, ctx:mashParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#primary_expression.
    def exitPrimary_expression(self, ctx:mashParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#type.
    def enterType(self, ctx:mashParser.TypeContext):
        pass

    # Exit a parse tree produced by mashParser#type.
    def exitType(self, ctx:mashParser.TypeContext):
        pass


    # Enter a parse tree produced by mashParser#var_declar.
    def enterVar_declar(self, ctx:mashParser.Var_declarContext):
        pass

    # Exit a parse tree produced by mashParser#var_declar.
    def exitVar_declar(self, ctx:mashParser.Var_declarContext):
        pass



del mashParser