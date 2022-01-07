# Generated from MyGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#compile_unit.
    def visitCompile_unit(self, ctx:MyGrammarParser.Compile_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#scoped_expr.
    def visitScoped_expr(self, ctx:MyGrammarParser.Scoped_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parentheses.
    def visitParentheses(self, ctx:MyGrammarParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#comparison.
    def visitComparison(self, ctx:MyGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_call.
    def visitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#multiply_divide.
    def visitMultiply_divide(self, ctx:MyGrammarParser.Multiply_divideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#bool_literal.
    def visitBool_literal(self, ctx:MyGrammarParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#define_variable.
    def visitDefine_variable(self, ctx:MyGrammarParser.Define_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#int_literal.
    def visitInt_literal(self, ctx:MyGrammarParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_decl.
    def visitFunction_decl(self, ctx:MyGrammarParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#not.
    def visitNot(self, ctx:MyGrammarParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#conjunction.
    def visitConjunction(self, ctx:MyGrammarParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#none_literal.
    def visitNone_literal(self, ctx:MyGrammarParser.None_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#read_variable.
    def visitRead_variable(self, ctx:MyGrammarParser.Read_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assign_variable.
    def visitAssign_variable(self, ctx:MyGrammarParser.Assign_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#float_literal.
    def visitFloat_literal(self, ctx:MyGrammarParser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#if_statement.
    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#nan_literal.
    def visitNan_literal(self, ctx:MyGrammarParser.Nan_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#add_subtract.
    def visitAdd_subtract(self, ctx:MyGrammarParser.Add_subtractContext):
        return self.visitChildren(ctx)



del MyGrammarParser