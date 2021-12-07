# Generated from MyGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#compileUnit.
    def visitCompileUnit(self, ctx:MyGrammarParser.CompileUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#infixExpr.
    def visitInfixExpr(self, ctx:MyGrammarParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#numberExpr.
    def visitNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parenExpr.
    def visitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        return self.visitChildren(ctx)



del MyGrammarParser