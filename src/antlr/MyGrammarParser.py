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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\7\3\16\n")
        buf.write("\3\f\3\16\3\21\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4+\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5\66\n\5\f\5\16\59\13\5\5\5;\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\5\5C\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5Q\n\5\f\5\16\5T\13\5\3\5\2\3\b\6\2\4\6\b")
        buf.write("\2\6\3\2\16\17\3\2\f\r\3\2\5\n\3\2\3\4\2`\2\n\3\2\2\2")
        buf.write("\4\17\3\2\2\2\6*\3\2\2\2\bB\3\2\2\2\n\13\5\4\3\2\13\3")
        buf.write("\3\2\2\2\f\16\5\6\4\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3")
        buf.write("\2\2\2\17\20\3\2\2\2\20\5\3\2\2\2\21\17\3\2\2\2\22\23")
        buf.write("\7\24\2\2\23\24\5\4\3\2\24\25\7\25\2\2\25+\3\2\2\2\26")
        buf.write("\27\7\30\2\2\27\30\7\21\2\2\30\31\5\b\5\2\31\32\7\22\2")
        buf.write("\2\32\33\5\6\4\2\33+\3\2\2\2\34\35\7\27\2\2\35\36\7\32")
        buf.write("\2\2\36\37\7\20\2\2\37 \5\b\5\2 !\7\23\2\2!+\3\2\2\2\"")
        buf.write("#\7\32\2\2#$\7\20\2\2$%\5\b\5\2%&\7\23\2\2&+\3\2\2\2\'")
        buf.write("(\5\b\5\2()\7\23\2\2)+\3\2\2\2*\22\3\2\2\2*\26\3\2\2\2")
        buf.write("*\34\3\2\2\2*\"\3\2\2\2*\'\3\2\2\2+\7\3\2\2\2,-\b\5\1")
        buf.write("\2-C\7\31\2\2./\7\13\2\2/C\5\b\5\n\60\61\7\32\2\2\61:")
        buf.write("\7\21\2\2\62\67\5\b\5\2\63\64\7\26\2\2\64\66\5\b\5\2\65")
        buf.write("\63\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28;\3")
        buf.write("\2\2\29\67\3\2\2\2:\62\3\2\2\2:;\3\2\2\2;<\3\2\2\2<C\7")
        buf.write("\22\2\2=>\7\21\2\2>?\5\b\5\2?@\7\22\2\2@C\3\2\2\2AC\7")
        buf.write("\32\2\2B,\3\2\2\2B.\3\2\2\2B\60\3\2\2\2B=\3\2\2\2BA\3")
        buf.write("\2\2\2CR\3\2\2\2DE\f\7\2\2EF\t\2\2\2FQ\5\b\5\bGH\f\6\2")
        buf.write("\2HI\t\3\2\2IQ\5\b\5\7JK\f\5\2\2KL\t\4\2\2LQ\5\b\5\6M")
        buf.write("N\f\4\2\2NO\t\5\2\2OQ\5\b\5\5PD\3\2\2\2PG\3\2\2\2PJ\3")
        buf.write("\2\2\2PM\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\t\3\2")
        buf.write("\2\2TR\3\2\2\2\t\17*\67:BPR")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&&'", "'||'", "'>='", "'<='", "'=='", 
                     "'!='", "'>'", "'<'", "'!'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'('", "')'", "';'", "'{'", "'}'", "','", "'let'", 
                     "'if'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "GE", "LE", "EQ", "NEQ", 
                      "GT", "LT", "NOT", "OP_PLUS", "OP_MINUS", "OP_MULT", 
                      "OP_DIV", "OP_ASSIGN", "LPAR", "RPAR", "EOS", "OPEN_BLOCK", 
                      "CLOSE_BLOCK", "COMMA", "LET", "IF", "INTEGER", "IDENTIFIER", 
                      "WHITESPACE" ]

    RULE_compileUnit = 0
    RULE_scope = 1
    RULE_statement = 2
    RULE_expr = 3

    ruleNames =  [ "compileUnit", "scope", "statement", "expr" ]

    EOF = Token.EOF
    AND=1
    OR=2
    GE=3
    LE=4
    EQ=5
    NEQ=6
    GT=7
    LT=8
    NOT=9
    OP_PLUS=10
    OP_MINUS=11
    OP_MULT=12
    OP_DIV=13
    OP_ASSIGN=14
    LPAR=15
    RPAR=16
    EOS=17
    OPEN_BLOCK=18
    CLOSE_BLOCK=19
    COMMA=20
    LET=21
    IF=22
    INTEGER=23
    IDENTIFIER=24
    WHITESPACE=25

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.NOT) | (1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.OPEN_BLOCK) | (1 << MyGrammarParser.LET) | (1 << MyGrammarParser.IF) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
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


    class IfStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MyGrammarParser.IF, 0)
        def LPAR(self):
            return self.getToken(MyGrammarParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(MyGrammarParser.RPAR, 0)
        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 40
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
                localctx = MyGrammarParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(MyGrammarParser.IF)
                self.state = 21
                self.match(MyGrammarParser.LPAR)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(MyGrammarParser.RPAR)
                self.state = 24
                self.statement()
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.DefineVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(MyGrammarParser.LET)
                self.state = 27
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 28
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.AssignVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 33
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 37
                self.expr(0)
                self.state = 38
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


    class NotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MyGrammarParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


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


    class ComparisonContext(ExprContext):

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

        def GT(self):
            return self.getToken(MyGrammarParser.GT, 0)
        def GE(self):
            return self.getToken(MyGrammarParser.GE, 0)
        def LT(self):
            return self.getToken(MyGrammarParser.LT, 0)
        def LE(self):
            return self.getToken(MyGrammarParser.LE, 0)
        def EQ(self):
            return self.getToken(MyGrammarParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MyGrammarParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(ExprContext):

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

        def AND(self):
            return self.getToken(MyGrammarParser.AND, 0)
        def OR(self):
            return self.getToken(MyGrammarParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                localctx.value = self.match(MyGrammarParser.INTEGER)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(MyGrammarParser.NOT)
                self.state = 45
                self.expr(8)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                localctx.ident = self.match(MyGrammarParser.IDENTIFIER)
                self.state = 47
                self.match(MyGrammarParser.LPAR)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.NOT) | (1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
                    self.state = 48
                    self.expr(0)
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MyGrammarParser.COMMA:
                        self.state = 49
                        self.match(MyGrammarParser.COMMA)
                        self.state = 50
                        self.expr(0)
                        self.state = 55
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 58
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(MyGrammarParser.LPAR)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.ReadVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.match(MyGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_MULT or _la==MyGrammarParser.OP_DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_PLUS or _la==MyGrammarParser.OP_MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.ComparisonContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.GE) | (1 << MyGrammarParser.LE) | (1 << MyGrammarParser.EQ) | (1 << MyGrammarParser.NEQ) | (1 << MyGrammarParser.GT) | (1 << MyGrammarParser.LT))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.ConjunctionContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.AND or _la==MyGrammarParser.OR):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 82
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




