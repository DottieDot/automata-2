# Generated from MyGrammar.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\7\3\16\n")
        buf.write("\3\f\3\16\3\21\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4%\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5\5\5\63")
        buf.write("\n\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\7\5C\n\5\f\5\16\5F\13\5\3\5\2\3\b\6\2\4\6\b\2")
        buf.write("\4\3\2\5\6\3\2\3\4\2N\2\n\3\2\2\2\4\17\3\2\2\2\6$\3\2")
        buf.write("\2\2\b:\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\16\5\6\4\2")
        buf.write("\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\5\3\2\2\2\21\17\3\2\2\2\22\23\7\13\2\2\23\24\5\4\3")
        buf.write("\2\24\25\7\f\2\2\25%\3\2\2\2\26\27\7\16\2\2\27\30\7\20")
        buf.write("\2\2\30\31\7\7\2\2\31\32\5\b\5\2\32\33\7\n\2\2\33%\3\2")
        buf.write("\2\2\34\35\7\20\2\2\35\36\7\7\2\2\36\37\5\b\5\2\37 \7")
        buf.write("\n\2\2 %\3\2\2\2!\"\5\b\5\2\"#\7\n\2\2#%\3\2\2\2$\22\3")
        buf.write("\2\2\2$\26\3\2\2\2$\34\3\2\2\2$!\3\2\2\2%\7\3\2\2\2&\'")
        buf.write("\b\5\1\2\';\7\17\2\2()\7\20\2\2)\62\7\b\2\2*/\5\b\5\2")
        buf.write("+,\7\r\2\2,.\5\b\5\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/")
        buf.write("\60\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\62*\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64;\7\t\2\2\65\66\7\b\2\2\66\67")
        buf.write("\5\b\5\2\678\7\t\2\28;\3\2\2\29;\7\20\2\2:&\3\2\2\2:(")
        buf.write("\3\2\2\2:\65\3\2\2\2:9\3\2\2\2;D\3\2\2\2<=\f\5\2\2=>\t")
        buf.write("\2\2\2>C\5\b\5\6?@\f\4\2\2@A\t\3\2\2AC\5\b\5\5B<\3\2\2")
        buf.write("\2B?\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\t\3\2\2\2")
        buf.write("FD\3\2\2\2\t\17$/\62:BD")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'('", 
                     "')'", "';'", "'{'", "'}'", "','", "'let'" ]

    symbolicNames = [ "<INVALID>", "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", 
                      "OP_ASSIGN", "LPAR", "RPAR", "EOS", "OPEN_BLOCK", 
                      "CLOSE_BLOCK", "COMMA", "LET", "INTEGER", "IDENTIFIER", 
                      "WHITESPACE" ]

    RULE_compileUnit = 0
    RULE_scope = 1
    RULE_statement = 2
    RULE_expr = 3

    ruleNames =  [ "compileUnit", "scope", "statement", "expr" ]

    EOF = Token.EOF
    OP_PLUS=1
    OP_MINUS=2
    OP_MULT=3
    OP_DIV=4
    OP_ASSIGN=5
    LPAR=6
    RPAR=7
    EOS=8
    OPEN_BLOCK=9
    CLOSE_BLOCK=10
    COMMA=11
    LET=12
    INTEGER=13
    IDENTIFIER=14
    WHITESPACE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompileUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scope(self):
            return self.getTypedRuleContext(MyGrammarParser.ScopeContext,0)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_compileUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompileUnit" ):
                listener.enterCompileUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompileUnit" ):
                listener.exitCompileUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompileUnit" ):
                return visitor.visitCompileUnit(self)
            else:
                return visitor.visitChildren(self)




    def compileUnit(self):

        localctx = MyGrammarParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return MyGrammarParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = MyGrammarParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.OPEN_BLOCK) | (1 << MyGrammarParser.LET) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
                self.state = 10
                self.statement()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def getRuleIndex(self):
            return MyGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefineVariableContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(MyGrammarParser.LET, 0)
        def IDENTIFIER(self):
            return self.getToken(MyGrammarParser.IDENTIFIER, 0)
        def OP_ASSIGN(self):
            return self.getToken(MyGrammarParser.OP_ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def EOS(self):
            return self.getToken(MyGrammarParser.EOS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineVariable" ):
                listener.enterDefineVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineVariable" ):
                listener.exitDefineVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineVariable" ):
                return visitor.visitDefineVariable(self)
            else:
                return visitor.visitChildren(self)


    class NewScopeContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPEN_BLOCK(self):
            return self.getToken(MyGrammarParser.OPEN_BLOCK, 0)
        def scope(self):
            return self.getTypedRuleContext(MyGrammarParser.ScopeContext,0)

        def CLOSE_BLOCK(self):
            return self.getToken(MyGrammarParser.CLOSE_BLOCK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewScope" ):
                listener.enterNewScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewScope" ):
                listener.exitNewScope(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewScope" ):
                return visitor.visitNewScope(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def EOS(self):
            return self.getToken(MyGrammarParser.EOS, 0)

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


    class AssignVariableContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(MyGrammarParser.IDENTIFIER, 0)
        def OP_ASSIGN(self):
            return self.getToken(MyGrammarParser.OP_ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def EOS(self):
            return self.getToken(MyGrammarParser.EOS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignVariable" ):
                listener.enterAssignVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignVariable" ):
                listener.exitAssignVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignVariable" ):
                return visitor.visitAssignVariable(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.NewScopeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.match(MyGrammarParser.OPEN_BLOCK)
                self.state = 17
                self.scope()
                self.state = 18
                self.match(MyGrammarParser.CLOSE_BLOCK)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.DefineVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(MyGrammarParser.LET)
                self.state = 21
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 22
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.AssignVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 27
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(MyGrammarParser.EOS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)

        def OP_DIV(self):
            return self.getToken(MyGrammarParser.OP_DIV, 0)
        def OP_MULT(self):
            return self.getToken(MyGrammarParser.OP_MULT, 0)
        def OP_PLUS(self):
            return self.getToken(MyGrammarParser.OP_PLUS, 0)
        def OP_MINUS(self):
            return self.getToken(MyGrammarParser.OP_MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class ReadVariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(MyGrammarParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadVariable" ):
                listener.enterReadVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadVariable" ):
                listener.exitReadVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadVariable" ):
                return visitor.visitReadVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(MyGrammarParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.ident = None # Token
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MyGrammarParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MyGrammarParser.RPAR, 0)
        def IDENTIFIER(self):
            return self.getToken(MyGrammarParser.IDENTIFIER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammarParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MyGrammarParser.COMMA)
            else:
                return self.getToken(MyGrammarParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MyGrammarParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(MyGrammarParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 37
                localctx.value = self.match(MyGrammarParser.INTEGER)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                localctx.ident = self.match(MyGrammarParser.IDENTIFIER)
                self.state = 39
                self.match(MyGrammarParser.LPAR)
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
                    self.state = 40
                    self.expr(0)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MyGrammarParser.COMMA:
                        self.state = 41
                        self.match(MyGrammarParser.COMMA)
                        self.state = 42
                        self.expr(0)
                        self.state = 47
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 50
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(MyGrammarParser.LPAR)
                self.state = 52
                self.expr(0)
                self.state = 53
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.ReadVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(MyGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_MULT or _la==MyGrammarParser.OP_DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_PLUS or _la==MyGrammarParser.OP_MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




