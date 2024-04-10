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


    # Visit a parse tree produced by mashParser#var_declar.
    def visitVar_declar(self, ctx:mashParser.Var_declarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#array_declaration.
    def visitArray_declaration(self, ctx:mashParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#type.
    def visitType(self, ctx:mashParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#value.
    def visitValue(self, ctx:mashParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#string_value.
    def visitString_value(self, ctx:mashParser.String_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#array_value.
    def visitArray_value(self, ctx:mashParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#int_value.
    def visitInt_value(self, ctx:mashParser.Int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#bool_value.
    def visitBool_value(self, ctx:mashParser.Bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#operation.
    def visitOperation(self, ctx:mashParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#arithmetic_operation.
    def visitArithmetic_operation(self, ctx:mashParser.Arithmetic_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#expression.
    def visitExpression(self, ctx:mashParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#sign.
    def visitSign(self, ctx:mashParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#logical_operation.
    def visitLogical_operation(self, ctx:mashParser.Logical_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#condition.
    def visitCondition(self, ctx:mashParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#logic_operator.
    def visitLogic_operator(self, ctx:mashParser.Logic_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#loop.
    def visitLoop(self, ctx:mashParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#for_loop.
    def visitFor_loop(self, ctx:mashParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#while_loop.
    def visitWhile_loop(self, ctx:mashParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#function.
    def visitFunction(self, ctx:mashParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#function_definition.
    def visitFunction_definition(self, ctx:mashParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#function_call.
    def visitFunction_call(self, ctx:mashParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#arguments.
    def visitArguments(self, ctx:mashParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#echo_statement.
    def visitEcho_statement(self, ctx:mashParser.Echo_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#sentence.
    def visitSentence(self, ctx:mashParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#identifier.
    def visitIdentifier(self, ctx:mashParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#string_var.
    def visitString_var(self, ctx:mashParser.String_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#array_var.
    def visitArray_var(self, ctx:mashParser.Array_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#int_var.
    def visitInt_var(self, ctx:mashParser.Int_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#bool_var.
    def visitBool_var(self, ctx:mashParser.Bool_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mashParser#print_string_statement.
    def visitPrint_string_statement(self, ctx:mashParser.Print_string_statementContext):
        return self.visitChildren(ctx)



del mashParser