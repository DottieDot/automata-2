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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\7\3\16")
        buf.write("\n\3\f\3\16\3\21\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5?\13\5\5")
        buf.write("\5A\n\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5I\n\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5W\n\5\f\5\16\5Z")
        buf.write("\13\5\3\5\2\3\b\6\2\4\6\b\2\6\3\2\16\17\3\2\f\r\3\2\5")
        buf.write("\n\3\2\3\4\2g\2\n\3\2\2\2\4\17\3\2\2\2\6\60\3\2\2\2\b")
        buf.write("H\3\2\2\2\n\13\5\4\3\2\13\3\3\2\2\2\f\16\5\6\4\2\r\f\3")
        buf.write("\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\5\3")
        buf.write("\2\2\2\21\17\3\2\2\2\22\23\7\24\2\2\23\24\5\4\3\2\24\25")
        buf.write("\7\25\2\2\25\61\3\2\2\2\26\27\7\30\2\2\27\30\7\21\2\2")
        buf.write("\30\31\5\b\5\2\31\32\7\22\2\2\32\33\5\6\4\2\33\61\3\2")
        buf.write("\2\2\34\35\7\31\2\2\35\36\7\21\2\2\36\37\5\b\5\2\37 \7")
        buf.write("\22\2\2 !\5\6\4\2!\61\3\2\2\2\"#\7\27\2\2#$\7\34\2\2$")
        buf.write("%\7\20\2\2%&\5\b\5\2&\'\7\23\2\2\'\61\3\2\2\2()\7\34\2")
        buf.write("\2)*\7\20\2\2*+\5\b\5\2+,\7\23\2\2,\61\3\2\2\2-.\5\b\5")
        buf.write("\2./\7\23\2\2/\61\3\2\2\2\60\22\3\2\2\2\60\26\3\2\2\2")
        buf.write("\60\34\3\2\2\2\60\"\3\2\2\2\60(\3\2\2\2\60-\3\2\2\2\61")
        buf.write("\7\3\2\2\2\62\63\b\5\1\2\63I\7\33\2\2\64\65\7\13\2\2\65")
        buf.write("I\5\b\5\n\66\67\7\34\2\2\67@\7\21\2\28=\5\b\5\29:\7\26")
        buf.write("\2\2:<\5\b\5\2;9\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2")
        buf.write(">A\3\2\2\2?=\3\2\2\2@8\3\2\2\2@A\3\2\2\2AB\3\2\2\2BI\7")
        buf.write("\22\2\2CD\7\21\2\2DE\5\b\5\2EF\7\22\2\2FI\3\2\2\2GI\7")
        buf.write("\34\2\2H\62\3\2\2\2H\64\3\2\2\2H\66\3\2\2\2HC\3\2\2\2")
        buf.write("HG\3\2\2\2IX\3\2\2\2JK\f\7\2\2KL\t\2\2\2LW\5\b\5\bMN\f")
        buf.write("\6\2\2NO\t\3\2\2OW\5\b\5\7PQ\f\5\2\2QR\t\4\2\2RW\5\b\5")
        buf.write("\6ST\f\4\2\2TU\t\5\2\2UW\5\b\5\5VJ\3\2\2\2VM\3\2\2\2V")
        buf.write("P\3\2\2\2VS\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\t\3")
        buf.write("\2\2\2ZX\3\2\2\2\t\17\60=@HVX")
        return buf.getvalue()


class MyGrammarParser ( Parser ):

    grammarFileName = "MyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&&'", "'||'", "'>='", "'<='", "'=='", 
                     "'!='", "'>'", "'<'", "'!'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'('", "')'", "';'", "'{'", "'}'", "','", "'let'", 
                     "'if'", "'while'", "'for'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "GE", "LE", "EQ", "NEQ", 
                      "GT", "LT", "NOT", "OP_PLUS", "OP_MINUS", "OP_MULT", 
                      "OP_DIV", "OP_ASSIGN", "LPAR", "RPAR", "EOS", "OPEN_BLOCK", 
                      "CLOSE_BLOCK", "COMMA", "LET", "IF", "WHILE", "FOR", 
                      "INTEGER", "IDENTIFIER", "WHITESPACE" ]

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
    WHILE=23
    FOR=24
    INTEGER=25
    IDENTIFIER=26
    WHITESPACE=27

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.NOT) | (1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.OPEN_BLOCK) | (1 << MyGrammarParser.LET) | (1 << MyGrammarParser.IF) | (1 << MyGrammarParser.WHILE) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
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



    class WhileStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MyGrammarParser.WHILE, 0)
        def LPAR(self):
            return self.getToken(MyGrammarParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(MyGrammarParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(MyGrammarParser.RPAR, 0)
        def statement(self):
            return self.getTypedRuleContext(MyGrammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)


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
            self.state = 46
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
                localctx = MyGrammarParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(MyGrammarParser.WHILE)
                self.state = 27
                self.match(MyGrammarParser.LPAR)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(MyGrammarParser.RPAR)
                self.state = 30
                self.statement()
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.DefineVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(MyGrammarParser.LET)
                self.state = 33
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 34
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.AssignVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.match(MyGrammarParser.IDENTIFIER)
                self.state = 39
                self.match(MyGrammarParser.OP_ASSIGN)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(MyGrammarParser.EOS)
                pass

            elif la_ == 6:
                localctx = MyGrammarParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.expr(0)
                self.state = 44
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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MyGrammarParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 49
                localctx.value = self.match(MyGrammarParser.INTEGER)
                pass

            elif la_ == 2:
                localctx = MyGrammarParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.match(MyGrammarParser.NOT)
                self.state = 51
                self.expr(8)
                pass

            elif la_ == 3:
                localctx = MyGrammarParser.FunctionCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                localctx.ident = self.match(MyGrammarParser.IDENTIFIER)
                self.state = 53
                self.match(MyGrammarParser.LPAR)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.NOT) | (1 << MyGrammarParser.LPAR) | (1 << MyGrammarParser.INTEGER) | (1 << MyGrammarParser.IDENTIFIER))) != 0):
                    self.state = 54
                    self.expr(0)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==MyGrammarParser.COMMA:
                        self.state = 55
                        self.match(MyGrammarParser.COMMA)
                        self.state = 56
                        self.expr(0)
                        self.state = 61
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 64
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 4:
                localctx = MyGrammarParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(MyGrammarParser.LPAR)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(MyGrammarParser.RPAR)
                pass

            elif la_ == 5:
                localctx = MyGrammarParser.ReadVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(MyGrammarParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 84
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_MULT or _la==MyGrammarParser.OP_DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammarParser.InfixExprContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.OP_PLUS or _la==MyGrammarParser.OP_MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = MyGrammarParser.ComparisonContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MyGrammarParser.GE) | (1 << MyGrammarParser.LE) | (1 << MyGrammarParser.EQ) | (1 << MyGrammarParser.NEQ) | (1 << MyGrammarParser.GT) | (1 << MyGrammarParser.LT))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = MyGrammarParser.ConjunctionContext(self, MyGrammarParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammarParser.AND or _la==MyGrammarParser.OR):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 88
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
         




