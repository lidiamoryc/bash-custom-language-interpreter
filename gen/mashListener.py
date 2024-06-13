# Generated from C:/Users/Lee/Desktop/masf-final2/mash.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by mashParser#increment_statement.
    def enterIncrement_statement(self, ctx:mashParser.Increment_statementContext):
        pass

    # Exit a parse tree produced by mashParser#increment_statement.
    def exitIncrement_statement(self, ctx:mashParser.Increment_statementContext):
        pass


    # Enter a parse tree produced by mashParser#decrement_statement.
    def enterDecrement_statement(self, ctx:mashParser.Decrement_statementContext):
        pass

    # Exit a parse tree produced by mashParser#decrement_statement.
    def exitDecrement_statement(self, ctx:mashParser.Decrement_statementContext):
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


    # Enter a parse tree produced by mashParser#int_expression.
    def enterInt_expression(self, ctx:mashParser.Int_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#int_expression.
    def exitInt_expression(self, ctx:mashParser.Int_expressionContext):
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


    # Enter a parse tree produced by mashParser#logical_expression.
    def enterLogical_expression(self, ctx:mashParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#logical_expression.
    def exitLogical_expression(self, ctx:mashParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#comparison_expression.
    def enterComparison_expression(self, ctx:mashParser.Comparison_expressionContext):
        pass

    # Exit a parse tree produced by mashParser#comparison_expression.
    def exitComparison_expression(self, ctx:mashParser.Comparison_expressionContext):
        pass


    # Enter a parse tree produced by mashParser#var_declar.
    def enterVar_declar(self, ctx:mashParser.Var_declarContext):
        pass

    # Exit a parse tree produced by mashParser#var_declar.
    def exitVar_declar(self, ctx:mashParser.Var_declarContext):
        pass


    # Enter a parse tree produced by mashParser#type.
    def enterType(self, ctx:mashParser.TypeContext):
        pass

    # Exit a parse tree produced by mashParser#type.
    def exitType(self, ctx:mashParser.TypeContext):
        pass


    # Enter a parse tree produced by mashParser#assignment.
    def enterAssignment(self, ctx:mashParser.AssignmentContext):
        pass

    # Exit a parse tree produced by mashParser#assignment.
    def exitAssignment(self, ctx:mashParser.AssignmentContext):
        pass


    # Enter a parse tree produced by mashParser#while_statement.
    def enterWhile_statement(self, ctx:mashParser.While_statementContext):
        pass

    # Exit a parse tree produced by mashParser#while_statement.
    def exitWhile_statement(self, ctx:mashParser.While_statementContext):
        pass


    # Enter a parse tree produced by mashParser#for_statement.
    def enterFor_statement(self, ctx:mashParser.For_statementContext):
        pass

    # Exit a parse tree produced by mashParser#for_statement.
    def exitFor_statement(self, ctx:mashParser.For_statementContext):
        pass


    # Enter a parse tree produced by mashParser#if_statement.
    def enterIf_statement(self, ctx:mashParser.If_statementContext):
        pass

    # Exit a parse tree produced by mashParser#if_statement.
    def exitIf_statement(self, ctx:mashParser.If_statementContext):
        pass


    # Enter a parse tree produced by mashParser#elif_block.
    def enterElif_block(self, ctx:mashParser.Elif_blockContext):
        pass

    # Exit a parse tree produced by mashParser#elif_block.
    def exitElif_block(self, ctx:mashParser.Elif_blockContext):
        pass


    # Enter a parse tree produced by mashParser#else_block.
    def enterElse_block(self, ctx:mashParser.Else_blockContext):
        pass

    # Exit a parse tree produced by mashParser#else_block.
    def exitElse_block(self, ctx:mashParser.Else_blockContext):
        pass


    # Enter a parse tree produced by mashParser#function_declar.
    def enterFunction_declar(self, ctx:mashParser.Function_declarContext):
        pass

    # Exit a parse tree produced by mashParser#function_declar.
    def exitFunction_declar(self, ctx:mashParser.Function_declarContext):
        pass


    # Enter a parse tree produced by mashParser#parameters.
    def enterParameters(self, ctx:mashParser.ParametersContext):
        pass

    # Exit a parse tree produced by mashParser#parameters.
    def exitParameters(self, ctx:mashParser.ParametersContext):
        pass


    # Enter a parse tree produced by mashParser#parameter.
    def enterParameter(self, ctx:mashParser.ParameterContext):
        pass

    # Exit a parse tree produced by mashParser#parameter.
    def exitParameter(self, ctx:mashParser.ParameterContext):
        pass


    # Enter a parse tree produced by mashParser#return_type.
    def enterReturn_type(self, ctx:mashParser.Return_typeContext):
        pass

    # Exit a parse tree produced by mashParser#return_type.
    def exitReturn_type(self, ctx:mashParser.Return_typeContext):
        pass


    # Enter a parse tree produced by mashParser#function_call.
    def enterFunction_call(self, ctx:mashParser.Function_callContext):
        pass

    # Exit a parse tree produced by mashParser#function_call.
    def exitFunction_call(self, ctx:mashParser.Function_callContext):
        pass


    # Enter a parse tree produced by mashParser#arguments.
    def enterArguments(self, ctx:mashParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by mashParser#arguments.
    def exitArguments(self, ctx:mashParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by mashParser#return_statement.
    def enterReturn_statement(self, ctx:mashParser.Return_statementContext):
        pass

    # Exit a parse tree produced by mashParser#return_statement.
    def exitReturn_statement(self, ctx:mashParser.Return_statementContext):
        pass


    # Enter a parse tree produced by mashParser#statement_list.
    def enterStatement_list(self, ctx:mashParser.Statement_listContext):
        pass

    # Exit a parse tree produced by mashParser#statement_list.
    def exitStatement_list(self, ctx:mashParser.Statement_listContext):
        pass



del mashParser