# Generated from C:/Users/diana/PycharmProjects/mash/mash.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,
        3,43,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        58,8,6,10,6,12,6,61,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,
        72,8,7,10,7,12,7,75,9,7,1,8,1,8,1,8,1,8,1,8,3,8,82,8,8,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,94,8,10,1,10,0,2,12,14,
        11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,10,12,93,0,25,1,0,0,0,2,32,
        1,0,0,0,4,34,1,0,0,0,6,42,1,0,0,0,8,44,1,0,0,0,10,46,1,0,0,0,12,
        48,1,0,0,0,14,62,1,0,0,0,16,81,1,0,0,0,18,83,1,0,0,0,20,93,1,0,0,
        0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,
        33,3,4,2,0,31,33,3,20,10,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,
        0,0,34,35,5,1,0,0,35,36,3,6,3,0,36,5,1,0,0,0,37,38,5,2,0,0,38,39,
        3,10,5,0,39,40,5,3,0,0,40,43,1,0,0,0,41,43,3,8,4,0,42,37,1,0,0,0,
        42,41,1,0,0,0,43,7,1,0,0,0,44,45,5,16,0,0,45,9,1,0,0,0,46,47,3,12,
        6,0,47,11,1,0,0,0,48,49,6,6,-1,0,49,50,3,14,7,0,50,59,1,0,0,0,51,
        52,10,2,0,0,52,53,5,4,0,0,53,58,3,14,7,0,54,55,10,1,0,0,55,56,5,
        5,0,0,56,58,3,14,7,0,57,51,1,0,0,0,57,54,1,0,0,0,58,61,1,0,0,0,59,
        57,1,0,0,0,59,60,1,0,0,0,60,13,1,0,0,0,61,59,1,0,0,0,62,63,6,7,-1,
        0,63,64,3,16,8,0,64,73,1,0,0,0,65,66,10,2,0,0,66,67,5,6,0,0,67,72,
        3,16,8,0,68,69,10,1,0,0,69,70,5,7,0,0,70,72,3,16,8,0,71,65,1,0,0,
        0,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,15,
        1,0,0,0,75,73,1,0,0,0,76,82,5,14,0,0,77,78,5,8,0,0,78,79,3,12,6,
        0,79,80,5,9,0,0,80,82,1,0,0,0,81,76,1,0,0,0,81,77,1,0,0,0,82,17,
        1,0,0,0,83,84,7,0,0,0,84,19,1,0,0,0,85,86,3,18,9,0,86,87,5,15,0,
        0,87,88,5,13,0,0,88,89,3,6,3,0,89,94,1,0,0,0,90,91,3,18,9,0,91,92,
        5,15,0,0,92,94,1,0,0,0,93,85,1,0,0,0,93,90,1,0,0,0,94,21,1,0,0,0,
        9,25,32,42,57,59,71,73,81,93
    ]

class mashParser ( Parser ):

    grammarFileName = "mash.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'echo'", "'$(('", "'))'", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'string_var'", "'int_var'", 
                     "'bool_var'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INTEGER", "IDENTIFIER", 
                      "STRING", "DIGIT", "LETTER", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_echo_function = 2
    RULE_expression = 3
    RULE_string_expression = 4
    RULE_arithmetic_expression = 5
    RULE_additive_expression = 6
    RULE_multiplicative_expression = 7
    RULE_primary_expression = 8
    RULE_type = 9
    RULE_var_declar = 10

    ruleNames =  [ "program", "statement", "echo_function", "expression", 
                   "string_expression", "arithmetic_expression", "additive_expression", 
                   "multiplicative_expression", "primary_expression", "type", 
                   "var_declar" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INTEGER=14
    IDENTIFIER=15
    STRING=16
    DIGIT=17
    LETTER=18
    COMMENT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(mashParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mashParser.StatementContext)
            else:
                return self.getTypedRuleContext(mashParser.StatementContext,i)


        def getRuleIndex(self):
            return mashParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = mashParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7170) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(mashParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def echo_function(self):
            return self.getTypedRuleContext(mashParser.Echo_functionContext,0)


        def var_declar(self):
            return self.getTypedRuleContext(mashParser.Var_declarContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = mashParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.echo_function()
                pass
            elif token in [10, 11, 12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.var_declar()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Echo_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(mashParser.ExpressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_echo_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEcho_function" ):
                listener.enterEcho_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEcho_function" ):
                listener.exitEcho_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEcho_function" ):
                return visitor.visitEcho_function(self)
            else:
                return visitor.visitChildren(self)




    def echo_function(self):

        localctx = mashParser.Echo_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_echo_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(mashParser.T__0)
            self.state = 35
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_expression(self):
            return self.getTypedRuleContext(mashParser.Arithmetic_expressionContext,0)


        def string_expression(self):
            return self.getTypedRuleContext(mashParser.String_expressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = mashParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(mashParser.T__1)
                self.state = 38
                self.arithmetic_expression()
                self.state = 39
                self.match(mashParser.T__2)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.string_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(mashParser.STRING, 0)

        def getRuleIndex(self):
            return mashParser.RULE_string_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_expression" ):
                listener.enterString_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_expression" ):
                listener.exitString_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = mashParser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_string_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(mashParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_expression(self):
            return self.getTypedRuleContext(mashParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_arithmetic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expression" ):
                listener.enterArithmetic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expression" ):
                listener.exitArithmetic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression" ):
                return visitor.visitArithmetic_expression(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_expression(self):

        localctx = mashParser.Arithmetic_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arithmetic_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.additive_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative_expression(self):
            return self.getTypedRuleContext(mashParser.Multiplicative_expressionContext,0)


        def additive_expression(self):
            return self.getTypedRuleContext(mashParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_additive_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_expression" ):
                listener.enterAdditive_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_expression" ):
                listener.exitAdditive_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_expression" ):
                return visitor.visitAdditive_expression(self)
            else:
                return visitor.visitChildren(self)



    def additive_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mashParser.Additive_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_additive_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.multiplicative_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = mashParser.Additive_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 52
                        self.match(mashParser.T__3)
                        self.state = 53
                        self.multiplicative_expression(0)
                        pass

                    elif la_ == 2:
                        localctx = mashParser.Additive_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additive_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 55
                        self.match(mashParser.T__4)
                        self.state = 56
                        self.multiplicative_expression(0)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplicative_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self):
            return self.getTypedRuleContext(mashParser.Primary_expressionContext,0)


        def multiplicative_expression(self):
            return self.getTypedRuleContext(mashParser.Multiplicative_expressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_multiplicative_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_expression" ):
                listener.enterMultiplicative_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_expression" ):
                listener.exitMultiplicative_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_expression" ):
                return visitor.visitMultiplicative_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicative_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mashParser.Multiplicative_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_multiplicative_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.primary_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = mashParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 66
                        self.match(mashParser.T__5)
                        self.state = 67
                        self.primary_expression()
                        pass

                    elif la_ == 2:
                        localctx = mashParser.Multiplicative_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicative_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 69
                        self.match(mashParser.T__6)
                        self.state = 70
                        self.primary_expression()
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Primary_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(mashParser.INTEGER, 0)

        def additive_expression(self):
            return self.getTypedRuleContext(mashParser.Additive_expressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = mashParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primary_expression)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(mashParser.INTEGER)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(mashParser.T__7)
                self.state = 78
                self.additive_expression(0)
                self.state = 79
                self.match(mashParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mashParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = mashParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(mashParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(mashParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(mashParser.ExpressionContext,0)


        def getRuleIndex(self):
            return mashParser.RULE_var_declar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declar" ):
                listener.enterVar_declar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declar" ):
                listener.exitVar_declar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declar" ):
                return visitor.visitVar_declar(self)
            else:
                return visitor.visitChildren(self)




    def var_declar(self):

        localctx = mashParser.Var_declarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_declar)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.type_()
                self.state = 86
                self.match(mashParser.IDENTIFIER)
                self.state = 87
                self.match(mashParser.T__12)
                self.state = 88
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.type_()
                self.state = 91
                self.match(mashParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.additive_expression_sempred
        self._predicates[7] = self.multiplicative_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def additive_expression_sempred(self, localctx:Additive_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def multiplicative_expression_sempred(self, localctx:Multiplicative_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




