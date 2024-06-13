# Generated from C:/Users/Lee/Desktop/masf-final2/mash.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by mashParser#increment_statement.
    def visitIncrement_statement(self, ctx:mashParser.Increment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#decrement_statement.
    def visitDecrement_statement(self, ctx:mashParser.Decrement_statementContext):
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


    # Visit a parse tree produced by mashParser#int_expression.
    def visitInt_expression(self, ctx:mashParser.Int_expressionContext):
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


    # Visit a parse tree produced by mashParser#var_declar.
    def visitVar_declar(self, ctx:mashParser.Var_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#type.
    def visitType(self, ctx:mashParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#assignment.
    def visitAssignment(self, ctx:mashParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#while_statement.
    def visitWhile_statement(self, ctx:mashParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#for_statement.
    def visitFor_statement(self, ctx:mashParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#if_statement.
    def visitIf_statement(self, ctx:mashParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#elif_block.
    def visitElif_block(self, ctx:mashParser.Elif_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#else_block.
    def visitElse_block(self, ctx:mashParser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#function_declar.
    def visitFunction_declar(self, ctx:mashParser.Function_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#parameters.
    def visitParameters(self, ctx:mashParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#parameter.
    def visitParameter(self, ctx:mashParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#return_type.
    def visitReturn_type(self, ctx:mashParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#function_call.
    def visitFunction_call(self, ctx:mashParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#arguments.
    def visitArguments(self, ctx:mashParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#return_statement.
    def visitReturn_statement(self, ctx:mashParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#statement_list.
    def visitStatement_list(self, ctx:mashParser.Statement_listContext):
        return self.visitChildren(ctx)



del mashParser