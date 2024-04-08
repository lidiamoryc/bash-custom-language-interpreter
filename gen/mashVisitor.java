// Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link mashParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface mashVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link mashParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(mashParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#var_declar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_declar(mashParser.Var_declarContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(mashParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitValue(mashParser.ValueContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#string_value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString_value(mashParser.String_valueContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#array_value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_value(mashParser.Array_valueContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#int_value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_value(mashParser.Int_valueContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#bool_value}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_value(mashParser.Bool_valueContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#operation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperation(mashParser.OperationContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#arithmetic_operation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArithmetic_operation(mashParser.Arithmetic_operationContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(mashParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#sign}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSign(mashParser.SignContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#logical_operation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogical_operation(mashParser.Logical_operationContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#condition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCondition(mashParser.ConditionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#logic_operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogic_operator(mashParser.Logic_operatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#loop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoop(mashParser.LoopContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#for_loop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_loop(mashParser.For_loopContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#while_loop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile_loop(mashParser.While_loopContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#function}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction(mashParser.FunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#function_definition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_definition(mashParser.Function_definitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#function_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_call(mashParser.Function_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#arguments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArguments(mashParser.ArgumentsContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#echo_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEcho_statement(mashParser.Echo_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#sentence}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSentence(mashParser.SentenceContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#identifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdentifier(mashParser.IdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#string_var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString_var(mashParser.String_varContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#array_var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_var(mashParser.Array_varContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#int_var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInt_var(mashParser.Int_varContext ctx);
	/**
	 * Visit a parse tree produced by {@link mashParser#bool_var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBool_var(mashParser.Bool_varContext ctx);
}