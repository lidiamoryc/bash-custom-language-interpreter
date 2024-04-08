// Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class mashParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, INTEGER=37, DIGIT=38, 
		LETTER=39, COMMENT=40, WS=41;
	public static final int
		RULE_program = 0, RULE_var_declar = 1, RULE_array_declaration = 2, RULE_type = 3, 
		RULE_value = 4, RULE_string_value = 5, RULE_array_value = 6, RULE_int_value = 7, 
		RULE_bool_value = 8, RULE_operation = 9, RULE_arithmetic_operation = 10, 
		RULE_expression = 11, RULE_sign = 12, RULE_logical_operation = 13, RULE_condition = 14, 
		RULE_logic_operator = 15, RULE_loop = 16, RULE_for_loop = 17, RULE_while_loop = 18, 
		RULE_function = 19, RULE_function_definition = 20, RULE_function_call = 21, 
		RULE_arguments = 22, RULE_echo_statement = 23, RULE_sentence = 24, RULE_identifier = 25, 
		RULE_string_var = 26, RULE_array_var = 27, RULE_int_var = 28, RULE_bool_var = 29;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declar", "array_declaration", "type", "value", "string_value", 
			"array_value", "int_value", "bool_value", "operation", "arithmetic_operation", 
			"expression", "sign", "logical_operation", "condition", "logic_operator", 
			"loop", "for_loop", "while_loop", "function", "function_definition", 
			"function_call", "arguments", "echo_statement", "sentence", "identifier", 
			"string_var", "array_var", "int_var", "bool_var"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'string_var'", "'int_var'", "'bool_var'", "'\"'", "'('", 
			"','", "')'", "'true'", "'false'", "'$(('", "'))'", "'+'", "'-'", "'*'", 
			"'if'", "'then'", "'else'", "'fi'", "'['", "'=='", "'!='", "']'", "'<'", 
			"'>'", "'&&'", "'||'", "'for'", "'in'", "'do'", "'done'", "'while'", 
			"'{'", "'}'", "'echo'", "'array_var'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "INTEGER", "DIGIT", "LETTER", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "mash.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public mashParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public List<Var_declarContext> var_declar() {
			return getRuleContexts(Var_declarContext.class);
		}
		public Var_declarContext var_declar(int i) {
			return getRuleContext(Var_declarContext.class,i);
		}
		public List<Array_declarationContext> array_declaration() {
			return getRuleContexts(Array_declarationContext.class);
		}
		public Array_declarationContext array_declaration(int i) {
			return getRuleContext(Array_declarationContext.class,i);
		}
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public List<LoopContext> loop() {
			return getRuleContexts(LoopContext.class);
		}
		public LoopContext loop(int i) {
			return getRuleContext(LoopContext.class,i);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<Logical_operationContext> logical_operation() {
			return getRuleContexts(Logical_operationContext.class);
		}
		public Logical_operationContext logical_operation(int i) {
			return getRuleContext(Logical_operationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 657398499356L) != 0)) {
				{
				setState(66);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__1:
				case T__2:
				case T__3:
					{
					setState(60);
					var_declar();
					}
					break;
				case T__35:
					{
					setState(61);
					array_declaration();
					}
					break;
				case T__10:
				case T__34:
					{
					setState(62);
					operation();
					}
					break;
				case T__27:
				case T__31:
					{
					setState(63);
					loop();
					}
					break;
				case LETTER:
					{
					setState(64);
					function();
					}
					break;
				case T__15:
					{
					setState(65);
					logical_operation();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declarContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public Var_declarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterVar_declar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitVar_declar(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitVar_declar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var_declarContext var_declar() throws RecognitionException {
		Var_declarContext _localctx = new Var_declarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			type();
			setState(72);
			identifier();
			setState(73);
			match(T__0);
			setState(74);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_declarationContext extends ParserRuleContext {
		public Array_varContext array_var() {
			return getRuleContext(Array_varContext.class,0);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Array_valueContext array_value() {
			return getRuleContext(Array_valueContext.class,0);
		}
		public Array_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterArray_declaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitArray_declaration(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitArray_declaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_declarationContext array_declaration() throws RecognitionException {
		Array_declarationContext _localctx = new Array_declarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_array_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			array_var();
			setState(77);
			type();
			setState(78);
			identifier();
			setState(79);
			match(T__0);
			setState(80);
			array_value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 28L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public String_valueContext string_value() {
			return getRuleContext(String_valueContext.class,0);
		}
		public Int_valueContext int_value() {
			return getRuleContext(Int_valueContext.class,0);
		}
		public Bool_valueContext bool_value() {
			return getRuleContext(Bool_valueContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitValue(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitValue(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_value);
		try {
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				string_value();
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				int_value();
				}
				break;
			case T__8:
			case T__9:
				enterOuterAlt(_localctx, 3);
				{
				setState(86);
				bool_value();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class String_valueContext extends ParserRuleContext {
		public List<TerminalNode> LETTER() { return getTokens(mashParser.LETTER); }
		public TerminalNode LETTER(int i) {
			return getToken(mashParser.LETTER, i);
		}
		public List<TerminalNode> DIGIT() { return getTokens(mashParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(mashParser.DIGIT, i);
		}
		public String_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterString_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitString_value(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitString_value(this);
			else return visitor.visitChildren(this);
		}
	}

	public final String_valueContext string_value() throws RecognitionException {
		String_valueContext _localctx = new String_valueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_string_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(T__4);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIGIT || _la==LETTER) {
				{
				{
				setState(90);
				_la = _input.LA(1);
				if ( !(_la==DIGIT || _la==LETTER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_valueContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public Array_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterArray_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitArray_value(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitArray_value(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_valueContext array_value() throws RecognitionException {
		Array_valueContext _localctx = new Array_valueContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_array_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(T__5);
			setState(99);
			value();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(100);
				match(T__6);
				setState(101);
				value();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(T__7);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Int_valueContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(mashParser.INTEGER, 0); }
		public Int_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterInt_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitInt_value(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitInt_value(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_valueContext int_value() throws RecognitionException {
		Int_valueContext _localctx = new Int_valueContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_int_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(INTEGER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Bool_valueContext extends ParserRuleContext {
		public Bool_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_value; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterBool_value(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitBool_value(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitBool_value(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_valueContext bool_value() throws RecognitionException {
		Bool_valueContext _localctx = new Bool_valueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_bool_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			_la = _input.LA(1);
			if ( !(_la==T__8 || _la==T__9) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationContext extends ParserRuleContext {
		public Arithmetic_operationContext arithmetic_operation() {
			return getRuleContext(Arithmetic_operationContext.class,0);
		}
		public Echo_statementContext echo_statement() {
			return getRuleContext(Echo_statementContext.class,0);
		}
		public OperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitOperation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitOperation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final OperationContext operation() throws RecognitionException {
		OperationContext _localctx = new OperationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_operation);
		try {
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				arithmetic_operation();
				}
				break;
			case T__34:
				enterOuterAlt(_localctx, 2);
				{
				setState(114);
				echo_statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Arithmetic_operationContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Arithmetic_operationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic_operation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterArithmetic_operation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitArithmetic_operation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitArithmetic_operation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Arithmetic_operationContext arithmetic_operation() throws RecognitionException {
		Arithmetic_operationContext _localctx = new Arithmetic_operationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_arithmetic_operation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			match(T__10);
			setState(118);
			expression();
			setState(119);
			match(T__11);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<SignContext> sign() {
			return getRuleContexts(SignContext.class);
		}
		public SignContext sign(int i) {
			return getRuleContext(SignContext.class,i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			value();
			setState(127);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) {
				{
				{
				setState(122);
				sign();
				setState(123);
				value();
				}
				}
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SignContext extends ParserRuleContext {
		public SignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterSign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitSign(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitSign(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SignContext sign() throws RecognitionException {
		SignContext _localctx = new SignContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_sign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 57344L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logical_operationContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<OperationContext> operation() {
			return getRuleContexts(OperationContext.class);
		}
		public OperationContext operation(int i) {
			return getRuleContext(OperationContext.class,i);
		}
		public Logical_operationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_operation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterLogical_operation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitLogical_operation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitLogical_operation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logical_operationContext logical_operation() throws RecognitionException {
		Logical_operationContext _localctx = new Logical_operationContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_logical_operation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(T__15);
			setState(133);
			condition();
			setState(134);
			match(T__16);
			setState(135);
			operation();
			setState(136);
			match(T__17);
			setState(137);
			operation();
			setState(138);
			match(T__18);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public List<Bool_valueContext> bool_value() {
			return getRuleContexts(Bool_valueContext.class);
		}
		public Bool_valueContext bool_value(int i) {
			return getRuleContext(Bool_valueContext.class,i);
		}
		public Logic_operatorContext logic_operator() {
			return getRuleContext(Logic_operatorContext.class,0);
		}
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitCondition(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitCondition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_condition);
		int _la;
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				match(T__19);
				setState(141);
				bool_value();
				setState(142);
				_la = _input.LA(1);
				if ( !(_la==T__20 || _la==T__21) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(143);
				bool_value();
				setState(144);
				match(T__22);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(146);
				match(T__19);
				setState(149);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case T__8:
				case T__9:
				case INTEGER:
					{
					setState(147);
					value();
					}
					break;
				case LETTER:
					{
					setState(148);
					identifier();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(151);
				logic_operator();
				setState(154);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
				case T__8:
				case T__9:
				case INTEGER:
					{
					setState(152);
					value();
					}
					break;
				case LETTER:
					{
					setState(153);
					identifier();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(156);
				match(T__22);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logic_operatorContext extends ParserRuleContext {
		public Logic_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logic_operator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterLogic_operator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitLogic_operator(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitLogic_operator(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logic_operatorContext logic_operator() throws RecognitionException {
		Logic_operatorContext _localctx = new Logic_operatorContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_logic_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 257949696L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public For_loopContext for_loop() {
			return getRuleContext(For_loopContext.class,0);
		}
		public While_loopContext while_loop() {
			return getRuleContext(While_loopContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitLoop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_loop);
		try {
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__27:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				for_loop();
				}
				break;
			case T__31:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				while_loop();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_loopContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Array_valueContext array_value() {
			return getRuleContext(Array_valueContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public For_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterFor_loop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitFor_loop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitFor_loop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final For_loopContext for_loop() throws RecognitionException {
		For_loopContext _localctx = new For_loopContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_for_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(T__27);
			setState(167);
			identifier();
			setState(168);
			match(T__28);
			setState(169);
			array_value();
			setState(170);
			match(T__29);
			setState(171);
			operation();
			setState(172);
			match(T__30);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_loopContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public While_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_loop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterWhile_loop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitWhile_loop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitWhile_loop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final While_loopContext while_loop() throws RecognitionException {
		While_loopContext _localctx = new While_loopContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_while_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(T__31);
			setState(175);
			condition();
			setState(176);
			match(T__29);
			setState(177);
			operation();
			setState(178);
			match(T__30);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public Function_definitionContext function_definition() {
			return getRuleContext(Function_definitionContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitFunction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_function);
		try {
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(180);
				function_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(181);
				function_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_definitionContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public OperationContext operation() {
			return getRuleContext(OperationContext.class,0);
		}
		public Function_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_definition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterFunction_definition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitFunction_definition(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitFunction_definition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_definitionContext function_definition() throws RecognitionException {
		Function_definitionContext _localctx = new Function_definitionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_function_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			identifier();
			setState(185);
			match(T__5);
			setState(186);
			match(T__7);
			setState(187);
			match(T__32);
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__10 || _la==T__34) {
				{
				setState(188);
				operation();
				}
			}

			setState(191);
			match(T__33);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_callContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterFunction_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitFunction_call(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitFunction_call(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			identifier();
			setState(194);
			arguments();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentsContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterArguments(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitArguments(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitArguments(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			value();
			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438955040L) != 0)) {
				{
				{
				setState(197);
				value();
				}
				}
				setState(202);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Echo_statementContext extends ParserRuleContext {
		public SentenceContext sentence() {
			return getRuleContext(SentenceContext.class,0);
		}
		public Echo_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_echo_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterEcho_statement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitEcho_statement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitEcho_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Echo_statementContext echo_statement() throws RecognitionException {
		Echo_statementContext _localctx = new Echo_statementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_echo_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(203);
			match(T__34);
			setState(204);
			sentence();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SentenceContext extends ParserRuleContext {
		public List<ValueContext> value() {
			return getRuleContexts(ValueContext.class);
		}
		public ValueContext value(int i) {
			return getRuleContext(ValueContext.class,i);
		}
		public SentenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentence; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterSentence(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitSentence(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitSentence(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SentenceContext sentence() throws RecognitionException {
		SentenceContext _localctx = new SentenceContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_sentence);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			value();
			setState(210);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 137438955040L) != 0)) {
				{
				{
				setState(207);
				value();
				}
				}
				setState(212);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierContext extends ParserRuleContext {
		public List<TerminalNode> LETTER() { return getTokens(mashParser.LETTER); }
		public TerminalNode LETTER(int i) {
			return getToken(mashParser.LETTER, i);
		}
		public List<TerminalNode> DIGIT() { return getTokens(mashParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(mashParser.DIGIT, i);
		}
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_identifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(LETTER);
			setState(217);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIGIT || _la==LETTER) {
				{
				{
				setState(214);
				_la = _input.LA(1);
				if ( !(_la==DIGIT || _la==LETTER) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(219);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class String_varContext extends ParserRuleContext {
		public String_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterString_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitString_var(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitString_var(this);
			else return visitor.visitChildren(this);
		}
	}

	public final String_varContext string_var() throws RecognitionException {
		String_varContext _localctx = new String_varContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_string_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Array_varContext extends ParserRuleContext {
		public Array_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterArray_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitArray_var(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitArray_var(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_varContext array_var() throws RecognitionException {
		Array_varContext _localctx = new Array_varContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_array_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(T__35);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Int_varContext extends ParserRuleContext {
		public Int_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterInt_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitInt_var(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitInt_var(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Int_varContext int_var() throws RecognitionException {
		Int_varContext _localctx = new Int_varContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_int_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Bool_varContext extends ParserRuleContext {
		public Bool_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_var; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).enterBool_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof mashListener ) ((mashListener)listener).exitBool_var(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof mashVisitor ) return ((mashVisitor<? extends T>)visitor).visitBool_var(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Bool_varContext bool_var() throws RecognitionException {
		Bool_varContext _localctx = new Bool_varContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_bool_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001)\u00e5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0005\u0000C\b\u0000"+
		"\n\u0000\f\u0000F\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0003\u0004X\b\u0004\u0001\u0005\u0001\u0005\u0005\u0005\\\b\u0005\n"+
		"\u0005\f\u0005_\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0005\u0006g\b\u0006\n\u0006\f\u0006j\t\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0003\tt\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0005\u000b~\b\u000b\n\u000b\f\u000b\u0081"+
		"\t\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0096"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u009b\b\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u009f\b\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0003\u0010\u00a5\b\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0003\u0013\u00b7\b\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00be\b\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0005\u0016\u00c7\b\u0016\n\u0016\f\u0016\u00ca\t\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0005\u0018\u00d1\b\u0018\n"+
		"\u0018\f\u0018\u00d4\t\u0018\u0001\u0019\u0001\u0019\u0005\u0019\u00d8"+
		"\b\u0019\n\u0019\f\u0019\u00db\t\u0019\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0000\u0000\u001e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:\u0000\u0006\u0001\u0000"+
		"\u0002\u0004\u0001\u0000&\'\u0001\u0000\t\n\u0001\u0000\r\u000f\u0001"+
		"\u0000\u0015\u0016\u0002\u0000\u0015\u0016\u0018\u001b\u00db\u0000D\u0001"+
		"\u0000\u0000\u0000\u0002G\u0001\u0000\u0000\u0000\u0004L\u0001\u0000\u0000"+
		"\u0000\u0006R\u0001\u0000\u0000\u0000\bW\u0001\u0000\u0000\u0000\nY\u0001"+
		"\u0000\u0000\u0000\fb\u0001\u0000\u0000\u0000\u000em\u0001\u0000\u0000"+
		"\u0000\u0010o\u0001\u0000\u0000\u0000\u0012s\u0001\u0000\u0000\u0000\u0014"+
		"u\u0001\u0000\u0000\u0000\u0016y\u0001\u0000\u0000\u0000\u0018\u0082\u0001"+
		"\u0000\u0000\u0000\u001a\u0084\u0001\u0000\u0000\u0000\u001c\u009e\u0001"+
		"\u0000\u0000\u0000\u001e\u00a0\u0001\u0000\u0000\u0000 \u00a4\u0001\u0000"+
		"\u0000\u0000\"\u00a6\u0001\u0000\u0000\u0000$\u00ae\u0001\u0000\u0000"+
		"\u0000&\u00b6\u0001\u0000\u0000\u0000(\u00b8\u0001\u0000\u0000\u0000*"+
		"\u00c1\u0001\u0000\u0000\u0000,\u00c4\u0001\u0000\u0000\u0000.\u00cb\u0001"+
		"\u0000\u0000\u00000\u00ce\u0001\u0000\u0000\u00002\u00d5\u0001\u0000\u0000"+
		"\u00004\u00dc\u0001\u0000\u0000\u00006\u00de\u0001\u0000\u0000\u00008"+
		"\u00e0\u0001\u0000\u0000\u0000:\u00e2\u0001\u0000\u0000\u0000<C\u0003"+
		"\u0002\u0001\u0000=C\u0003\u0004\u0002\u0000>C\u0003\u0012\t\u0000?C\u0003"+
		" \u0010\u0000@C\u0003&\u0013\u0000AC\u0003\u001a\r\u0000B<\u0001\u0000"+
		"\u0000\u0000B=\u0001\u0000\u0000\u0000B>\u0001\u0000\u0000\u0000B?\u0001"+
		"\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000BA\u0001\u0000\u0000\u0000"+
		"CF\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000DE\u0001\u0000\u0000"+
		"\u0000E\u0001\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000GH\u0003"+
		"\u0006\u0003\u0000HI\u00032\u0019\u0000IJ\u0005\u0001\u0000\u0000JK\u0003"+
		"\b\u0004\u0000K\u0003\u0001\u0000\u0000\u0000LM\u00036\u001b\u0000MN\u0003"+
		"\u0006\u0003\u0000NO\u00032\u0019\u0000OP\u0005\u0001\u0000\u0000PQ\u0003"+
		"\f\u0006\u0000Q\u0005\u0001\u0000\u0000\u0000RS\u0007\u0000\u0000\u0000"+
		"S\u0007\u0001\u0000\u0000\u0000TX\u0003\n\u0005\u0000UX\u0003\u000e\u0007"+
		"\u0000VX\u0003\u0010\b\u0000WT\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000"+
		"\u0000WV\u0001\u0000\u0000\u0000X\t\u0001\u0000\u0000\u0000Y]\u0005\u0005"+
		"\u0000\u0000Z\\\u0007\u0001\u0000\u0000[Z\u0001\u0000\u0000\u0000\\_\u0001"+
		"\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000"+
		"^`\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000`a\u0005\u0005\u0000"+
		"\u0000a\u000b\u0001\u0000\u0000\u0000bc\u0005\u0006\u0000\u0000ch\u0003"+
		"\b\u0004\u0000de\u0005\u0007\u0000\u0000eg\u0003\b\u0004\u0000fd\u0001"+
		"\u0000\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000"+
		"hi\u0001\u0000\u0000\u0000ik\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000"+
		"\u0000kl\u0005\b\u0000\u0000l\r\u0001\u0000\u0000\u0000mn\u0005%\u0000"+
		"\u0000n\u000f\u0001\u0000\u0000\u0000op\u0007\u0002\u0000\u0000p\u0011"+
		"\u0001\u0000\u0000\u0000qt\u0003\u0014\n\u0000rt\u0003.\u0017\u0000sq"+
		"\u0001\u0000\u0000\u0000sr\u0001\u0000\u0000\u0000t\u0013\u0001\u0000"+
		"\u0000\u0000uv\u0005\u000b\u0000\u0000vw\u0003\u0016\u000b\u0000wx\u0005"+
		"\f\u0000\u0000x\u0015\u0001\u0000\u0000\u0000y\u007f\u0003\b\u0004\u0000"+
		"z{\u0003\u0018\f\u0000{|\u0003\b\u0004\u0000|~\u0001\u0000\u0000\u0000"+
		"}z\u0001\u0000\u0000\u0000~\u0081\u0001\u0000\u0000\u0000\u007f}\u0001"+
		"\u0000\u0000\u0000\u007f\u0080\u0001\u0000\u0000\u0000\u0080\u0017\u0001"+
		"\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0082\u0083\u0007"+
		"\u0003\u0000\u0000\u0083\u0019\u0001\u0000\u0000\u0000\u0084\u0085\u0005"+
		"\u0010\u0000\u0000\u0085\u0086\u0003\u001c\u000e\u0000\u0086\u0087\u0005"+
		"\u0011\u0000\u0000\u0087\u0088\u0003\u0012\t\u0000\u0088\u0089\u0005\u0012"+
		"\u0000\u0000\u0089\u008a\u0003\u0012\t\u0000\u008a\u008b\u0005\u0013\u0000"+
		"\u0000\u008b\u001b\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0014\u0000"+
		"\u0000\u008d\u008e\u0003\u0010\b\u0000\u008e\u008f\u0007\u0004\u0000\u0000"+
		"\u008f\u0090\u0003\u0010\b\u0000\u0090\u0091\u0005\u0017\u0000\u0000\u0091"+
		"\u009f\u0001\u0000\u0000\u0000\u0092\u0095\u0005\u0014\u0000\u0000\u0093"+
		"\u0096\u0003\b\u0004\u0000\u0094\u0096\u00032\u0019\u0000\u0095\u0093"+
		"\u0001\u0000\u0000\u0000\u0095\u0094\u0001\u0000\u0000\u0000\u0096\u0097"+
		"\u0001\u0000\u0000\u0000\u0097\u009a\u0003\u001e\u000f\u0000\u0098\u009b"+
		"\u0003\b\u0004\u0000\u0099\u009b\u00032\u0019\u0000\u009a\u0098\u0001"+
		"\u0000\u0000\u0000\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001"+
		"\u0000\u0000\u0000\u009c\u009d\u0005\u0017\u0000\u0000\u009d\u009f\u0001"+
		"\u0000\u0000\u0000\u009e\u008c\u0001\u0000\u0000\u0000\u009e\u0092\u0001"+
		"\u0000\u0000\u0000\u009f\u001d\u0001\u0000\u0000\u0000\u00a0\u00a1\u0007"+
		"\u0005\u0000\u0000\u00a1\u001f\u0001\u0000\u0000\u0000\u00a2\u00a5\u0003"+
		"\"\u0011\u0000\u00a3\u00a5\u0003$\u0012\u0000\u00a4\u00a2\u0001\u0000"+
		"\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000\u0000\u00a5!\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a7\u0005\u001c\u0000\u0000\u00a7\u00a8\u00032\u0019\u0000"+
		"\u00a8\u00a9\u0005\u001d\u0000\u0000\u00a9\u00aa\u0003\f\u0006\u0000\u00aa"+
		"\u00ab\u0005\u001e\u0000\u0000\u00ab\u00ac\u0003\u0012\t\u0000\u00ac\u00ad"+
		"\u0005\u001f\u0000\u0000\u00ad#\u0001\u0000\u0000\u0000\u00ae\u00af\u0005"+
		" \u0000\u0000\u00af\u00b0\u0003\u001c\u000e\u0000\u00b0\u00b1\u0005\u001e"+
		"\u0000\u0000\u00b1\u00b2\u0003\u0012\t\u0000\u00b2\u00b3\u0005\u001f\u0000"+
		"\u0000\u00b3%\u0001\u0000\u0000\u0000\u00b4\u00b7\u0003(\u0014\u0000\u00b5"+
		"\u00b7\u0003*\u0015\u0000\u00b6\u00b4\u0001\u0000\u0000\u0000\u00b6\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b7\'\u0001\u0000\u0000\u0000\u00b8\u00b9\u0003"+
		"2\u0019\u0000\u00b9\u00ba\u0005\u0006\u0000\u0000\u00ba\u00bb\u0005\b"+
		"\u0000\u0000\u00bb\u00bd\u0005!\u0000\u0000\u00bc\u00be\u0003\u0012\t"+
		"\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00bd\u00be\u0001\u0000\u0000"+
		"\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005\"\u0000\u0000"+
		"\u00c0)\u0001\u0000\u0000\u0000\u00c1\u00c2\u00032\u0019\u0000\u00c2\u00c3"+
		"\u0003,\u0016\u0000\u00c3+\u0001\u0000\u0000\u0000\u00c4\u00c8\u0003\b"+
		"\u0004\u0000\u00c5\u00c7\u0003\b\u0004\u0000\u00c6\u00c5\u0001\u0000\u0000"+
		"\u0000\u00c7\u00ca\u0001\u0000\u0000\u0000\u00c8\u00c6\u0001\u0000\u0000"+
		"\u0000\u00c8\u00c9\u0001\u0000\u0000\u0000\u00c9-\u0001\u0000\u0000\u0000"+
		"\u00ca\u00c8\u0001\u0000\u0000\u0000\u00cb\u00cc\u0005#\u0000\u0000\u00cc"+
		"\u00cd\u00030\u0018\u0000\u00cd/\u0001\u0000\u0000\u0000\u00ce\u00d2\u0003"+
		"\b\u0004\u0000\u00cf\u00d1\u0003\b\u0004\u0000\u00d0\u00cf\u0001\u0000"+
		"\u0000\u0000\u00d1\u00d4\u0001\u0000\u0000\u0000\u00d2\u00d0\u0001\u0000"+
		"\u0000\u0000\u00d2\u00d3\u0001\u0000\u0000\u0000\u00d31\u0001\u0000\u0000"+
		"\u0000\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d5\u00d9\u0005\'\u0000\u0000"+
		"\u00d6\u00d8\u0007\u0001\u0000\u0000\u00d7\u00d6\u0001\u0000\u0000\u0000"+
		"\u00d8\u00db\u0001\u0000\u0000\u0000\u00d9\u00d7\u0001\u0000\u0000\u0000"+
		"\u00d9\u00da\u0001\u0000\u0000\u0000\u00da3\u0001\u0000\u0000\u0000\u00db"+
		"\u00d9\u0001\u0000\u0000\u0000\u00dc\u00dd\u0005\u0002\u0000\u0000\u00dd"+
		"5\u0001\u0000\u0000\u0000\u00de\u00df\u0005$\u0000\u0000\u00df7\u0001"+
		"\u0000\u0000\u0000\u00e0\u00e1\u0005\u0003\u0000\u0000\u00e19\u0001\u0000"+
		"\u0000\u0000\u00e2\u00e3\u0005\u0004\u0000\u0000\u00e3;\u0001\u0000\u0000"+
		"\u0000\u0010BDW]hs\u007f\u0095\u009a\u009e\u00a4\u00b6\u00bd\u00c8\u00d2"+
		"\u00d9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}