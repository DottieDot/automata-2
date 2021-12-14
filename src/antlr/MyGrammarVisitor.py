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


    # Visit a parse tree produced by MyGrammarParser#scope.
    def visitScope(self, ctx:MyGrammarParser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#newScope.
    def visitNewScope(self, ctx:MyGrammarParser.NewScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#ifStatement.
    def visitIfStatement(self, ctx:MyGrammarParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#whileStatement.
    def visitWhileStatement(self, ctx:MyGrammarParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#defineVariable.
    def visitDefineVariable(self, ctx:MyGrammarParser.DefineVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assignVariable.
    def visitAssignVariable(self, ctx:MyGrammarParser.AssignVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expression.
    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#not.
    def visitNot(self, ctx:MyGrammarParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#infixExpr.
    def visitInfixExpr(self, ctx:MyGrammarParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#comparison.
    def visitComparison(self, ctx:MyGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#conjunction.
    def visitConjunction(self, ctx:MyGrammarParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#readVariable.
    def visitReadVariable(self, ctx:MyGrammarParser.ReadVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#numberExpr.
    def visitNumberExpr(self, ctx:MyGrammarParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#functionCall.
    def visitFunctionCall(self, ctx:MyGrammarParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parenExpr.
    def visitParenExpr(self, ctx:MyGrammarParser.ParenExprContext):
        return self.visitChildren(ctx)



del MyGrammarParser