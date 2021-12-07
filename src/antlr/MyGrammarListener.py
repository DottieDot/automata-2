# Generated from MyGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#compileUnit.
    def enterCompileUnit(self, ctx:MyGrammarParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#compileUnit.
    def exitCompileUnit(self, ctx:MyGrammarParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#infixExpr.
    def enterInfixExpr(self, ctx:MyGrammarParser.InfixExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#infixExpr.
    def exitInfixExpr(self, ctx:MyGrammarParser.InfixExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#numberExpr.
    def enterNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#numberExpr.
    def exitNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#parenExpr.
    def enterParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#parenExpr.
    def exitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        pass



del MyGrammarParser