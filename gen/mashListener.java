// Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link mashParser}.
 */
public interface mashListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link mashParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(mashParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(mashParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#var_declar}.
	 * @param ctx the parse tree
	 */
	void enterVar_declar(mashParser.Var_declarContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#var_declar}.
	 * @param ctx the parse tree
	 */
	void exitVar_declar(mashParser.Var_declarContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(mashParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(mashParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#value}.
	 * @param ctx the parse tree
	 */
	void enterValue(mashParser.ValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#value}.
	 * @param ctx the parse tree
	 */
	void exitValue(mashParser.ValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#string_value}.
	 * @param ctx the parse tree
	 */
	void enterString_value(mashParser.String_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#string_value}.
	 * @param ctx the parse tree
	 */
	void exitString_value(mashParser.String_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#array_value}.
	 * @param ctx the parse tree
	 */
	void enterArray_value(mashParser.Array_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#array_value}.
	 * @param ctx the parse tree
	 */
	void exitArray_value(mashParser.Array_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#int_value}.
	 * @param ctx the parse tree
	 */
	void enterInt_value(mashParser.Int_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#int_value}.
	 * @param ctx the parse tree
	 */
	void exitInt_value(mashParser.Int_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#bool_value}.
	 * @param ctx the parse tree
	 */
	void enterBool_value(mashParser.Bool_valueContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#bool_value}.
	 * @param ctx the parse tree
	 */
	void exitBool_value(mashParser.Bool_valueContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#operation}.
	 * @param ctx the parse tree
	 */
	void enterOperation(mashParser.OperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#operation}.
	 * @param ctx the parse tree
	 */
	void exitOperation(mashParser.OperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#arithmetic_operation}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic_operation(mashParser.Arithmetic_operationContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#arithmetic_operation}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic_operation(mashParser.Arithmetic_operationContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(mashParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(mashParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#sign}.
	 * @param ctx the parse tree
	 */
	void enterSign(mashParser.SignContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#sign}.
	 * @param ctx the parse tree
	 */
	void exitSign(mashParser.SignContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#logical_operation}.
	 * @param ctx the parse tree
	 */
	void enterLogical_operation(mashParser.Logical_operationContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#logical_operation}.
	 * @param ctx the parse tree
	 */
	void exitLogical_operation(mashParser.Logical_operationContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(mashParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(mashParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#logic_operator}.
	 * @param ctx the parse tree
	 */
	void enterLogic_operator(mashParser.Logic_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#logic_operator}.
	 * @param ctx the parse tree
	 */
	void exitLogic_operator(mashParser.Logic_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#loop}.
	 * @param ctx the parse tree
	 */
	void enterLoop(mashParser.LoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#loop}.
	 * @param ctx the parse tree
	 */
	void exitLoop(mashParser.LoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#for_loop}.
	 * @param ctx the parse tree
	 */
	void enterFor_loop(mashParser.For_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#for_loop}.
	 * @param ctx the parse tree
	 */
	void exitFor_loop(mashParser.For_loopContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void enterWhile_loop(mashParser.While_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void exitWhile_loop(mashParser.While_loopContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(mashParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(mashParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void enterFunction_definition(mashParser.Function_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void exitFunction_definition(mashParser.Function_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(mashParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(mashParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(mashParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(mashParser.ArgumentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#echo_statement}.
	 * @param ctx the parse tree
	 */
	void enterEcho_statement(mashParser.Echo_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#echo_statement}.
	 * @param ctx the parse tree
	 */
	void exitEcho_statement(mashParser.Echo_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#sentence}.
	 * @param ctx the parse tree
	 */
	void enterSentence(mashParser.SentenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#sentence}.
	 * @param ctx the parse tree
	 */
	void exitSentence(mashParser.SentenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(mashParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(mashParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#string_var}.
	 * @param ctx the parse tree
	 */
	void enterString_var(mashParser.String_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#string_var}.
	 * @param ctx the parse tree
	 */
	void exitString_var(mashParser.String_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#array_var}.
	 * @param ctx the parse tree
	 */
	void enterArray_var(mashParser.Array_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#array_var}.
	 * @param ctx the parse tree
	 */
	void exitArray_var(mashParser.Array_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#int_var}.
	 * @param ctx the parse tree
	 */
	void enterInt_var(mashParser.Int_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#int_var}.
	 * @param ctx the parse tree
	 */
	void exitInt_var(mashParser.Int_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link mashParser#bool_var}.
	 * @param ctx the parse tree
	 */
	void enterBool_var(mashParser.Bool_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link mashParser#bool_var}.
	 * @param ctx the parse tree
	 */
	void exitBool_var(mashParser.Bool_varContext ctx);
}