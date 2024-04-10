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


    # Enter a parse tree produced by mashParser#var_declar.
    def enterVar_declar(self, ctx:mashParser.Var_declarContext):
        pass

    # Exit a parse tree produced by mashParser#var_declar.
    def exitVar_declar(self, ctx:mashParser.Var_declarContext):
        pass


    # Enter a parse tree produced by mashParser#array_declaration.
    def enterArray_declaration(self, ctx:mashParser.Array_declarationContext):
        pass

    # Exit a parse tree produced by mashParser#array_declaration.
    def exitArray_declaration(self, ctx:mashParser.Array_declarationContext):
        pass


    # Enter a parse tree produced by mashParser#type.
    def enterType(self, ctx:mashParser.TypeContext):
        pass

    # Exit a parse tree produced by mashParser#type.
    def exitType(self, ctx:mashParser.TypeContext):
        pass


    # Enter a parse tree produced by mashParser#value.
    def enterValue(self, ctx:mashParser.ValueContext):
        pass

    # Exit a parse tree produced by mashParser#value.
    def exitValue(self, ctx:mashParser.ValueContext):
        pass


    # Enter a parse tree produced by mashParser#string_value.
    def enterString_value(self, ctx:mashParser.String_valueContext):
        pass

    # Exit a parse tree produced by mashParser#string_value.
    def exitString_value(self, ctx:mashParser.String_valueContext):
        pass


    # Enter a parse tree produced by mashParser#array_value.
    def enterArray_value(self, ctx:mashParser.Array_valueContext):
        pass

    # Exit a parse tree produced by mashParser#array_value.
    def exitArray_value(self, ctx:mashParser.Array_valueContext):
        pass


    # Enter a parse tree produced by mashParser#int_value.
    def enterInt_value(self, ctx:mashParser.Int_valueContext):
        pass

    # Exit a parse tree produced by mashParser#int_value.
    def exitInt_value(self, ctx:mashParser.Int_valueContext):
        pass


    # Enter a parse tree produced by mashParser#bool_value.
    def enterBool_value(self, ctx:mashParser.Bool_valueContext):
        pass

    # Exit a parse tree produced by mashParser#bool_value.
    def exitBool_value(self, ctx:mashParser.Bool_valueContext):
        pass


    # Enter a parse tree produced by mashParser#operation.
    def enterOperation(self, ctx:mashParser.OperationContext):
        pass

    # Exit a parse tree produced by mashParser#operation.
    def exitOperation(self, ctx:mashParser.OperationContext):
        pass


    # Enter a parse tree produced by mashParser#arithmetic_operation.
    def enterArithmetic_operation(self, ctx:mashParser.Arithmetic_operationContext):
        pass

    # Exit a parse tree produced by mashParser#arithmetic_operation.
    def exitArithmetic_operation(self, ctx:mashParser.Arithmetic_operationContext):
        pass


    # Enter a parse tree produced by mashParser#expression.
    def enterExpression(self, ctx:mashParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mashParser#expression.
    def exitExpression(self, ctx:mashParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mashParser#sign.
    def enterSign(self, ctx:mashParser.SignContext):
        pass

    # Exit a parse tree produced by mashParser#sign.
    def exitSign(self, ctx:mashParser.SignContext):
        pass


    # Enter a parse tree produced by mashParser#logical_operation.
    def enterLogical_operation(self, ctx:mashParser.Logical_operationContext):
        pass

    # Exit a parse tree produced by mashParser#logical_operation.
    def exitLogical_operation(self, ctx:mashParser.Logical_operationContext):
        pass


    # Enter a parse tree produced by mashParser#condition.
    def enterCondition(self, ctx:mashParser.ConditionContext):
        pass

    # Exit a parse tree produced by mashParser#condition.
    def exitCondition(self, ctx:mashParser.ConditionContext):
        pass


    # Enter a parse tree produced by mashParser#logic_operator.
    def enterLogic_operator(self, ctx:mashParser.Logic_operatorContext):
        pass

    # Exit a parse tree produced by mashParser#logic_operator.
    def exitLogic_operator(self, ctx:mashParser.Logic_operatorContext):
        pass


    # Enter a parse tree produced by mashParser#loop.
    def enterLoop(self, ctx:mashParser.LoopContext):
        pass

    # Exit a parse tree produced by mashParser#loop.
    def exitLoop(self, ctx:mashParser.LoopContext):
        pass


    # Enter a parse tree produced by mashParser#for_loop.
    def enterFor_loop(self, ctx:mashParser.For_loopContext):
        pass

    # Exit a parse tree produced by mashParser#for_loop.
    def exitFor_loop(self, ctx:mashParser.For_loopContext):
        pass


    # Enter a parse tree produced by mashParser#while_loop.
    def enterWhile_loop(self, ctx:mashParser.While_loopContext):
        pass

    # Exit a parse tree produced by mashParser#while_loop.
    def exitWhile_loop(self, ctx:mashParser.While_loopContext):
        pass


    # Enter a parse tree produced by mashParser#function.
    def enterFunction(self, ctx:mashParser.FunctionContext):
        pass

    # Exit a parse tree produced by mashParser#function.
    def exitFunction(self, ctx:mashParser.FunctionContext):
        pass


    # Enter a parse tree produced by mashParser#function_definition.
    def enterFunction_definition(self, ctx:mashParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by mashParser#function_definition.
    def exitFunction_definition(self, ctx:mashParser.Function_definitionContext):
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


    # Enter a parse tree produced by mashParser#echo_statement.
    def enterEcho_statement(self, ctx:mashParser.Echo_statementContext):
        pass

    # Exit a parse tree produced by mashParser#echo_statement.
    def exitEcho_statement(self, ctx:mashParser.Echo_statementContext):
        pass


    # Enter a parse tree produced by mashParser#sentence.
    def enterSentence(self, ctx:mashParser.SentenceContext):
        pass

    # Exit a parse tree produced by mashParser#sentence.
    def exitSentence(self, ctx:mashParser.SentenceContext):
        pass


    # Enter a parse tree produced by mashParser#identifier.
    def enterIdentifier(self, ctx:mashParser.IdentifierContext):
        pass

    # Exit a parse tree produced by mashParser#identifier.
    def exitIdentifier(self, ctx:mashParser.IdentifierContext):
        pass


    # Enter a parse tree produced by mashParser#string_var.
    def enterString_var(self, ctx:mashParser.String_varContext):
        pass

    # Exit a parse tree produced by mashParser#string_var.
    def exitString_var(self, ctx:mashParser.String_varContext):
        pass


    # Enter a parse tree produced by mashParser#array_var.
    def enterArray_var(self, ctx:mashParser.Array_varContext):
        pass

    # Exit a parse tree produced by mashParser#array_var.
    def exitArray_var(self, ctx:mashParser.Array_varContext):
        pass


    # Enter a parse tree produced by mashParser#int_var.
    def enterInt_var(self, ctx:mashParser.Int_varContext):
        pass

    # Exit a parse tree produced by mashParser#int_var.
    def exitInt_var(self, ctx:mashParser.Int_varContext):
        pass


    # Enter a parse tree produced by mashParser#bool_var.
    def enterBool_var(self, ctx:mashParser.Bool_varContext):
        pass

    # Exit a parse tree produced by mashParser#bool_var.
    def exitBool_var(self, ctx:mashParser.Bool_varContext):
        pass



del mashParser