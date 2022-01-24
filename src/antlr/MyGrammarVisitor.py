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


    # Visit a parse tree produced by MyGrammarParser#if_statement.
    def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#else_if_statement.
    def visitElse_if_statement(self, ctx:MyGrammarParser.Else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#else_statement.
    def visitElse_statement(self, ctx:MyGrammarParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#read_dummy_matrix.
    def visitRead_dummy_matrix(self, ctx:MyGrammarParser.Read_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#read_dummy_matrix_field.
    def visitRead_dummy_matrix_field(self, ctx:MyGrammarParser.Read_dummy_matrix_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#write_dummy_matrix_field.
    def visitWrite_dummy_matrix_field(self, ctx:MyGrammarParser.Write_dummy_matrix_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#define_dummy_matrix.
    def visitDefine_dummy_matrix(self, ctx:MyGrammarParser.Define_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#transpose_dummy_matrix.
    def visitTranspose_dummy_matrix(self, ctx:MyGrammarParser.Transpose_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#inverse_dummy_matrix.
    def visitInverse_dummy_matrix(self, ctx:MyGrammarParser.Inverse_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#mult_dummy_matrix.
    def visitMult_dummy_matrix(self, ctx:MyGrammarParser.Mult_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#dummy_scalar.
    def visitDummy_scalar(self, ctx:MyGrammarParser.Dummy_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#dummy_matrix_parenthesis.
    def visitDummy_matrix_parenthesis(self, ctx:MyGrammarParser.Dummy_matrix_parenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#add_dummy_matrix.
    def visitAdd_dummy_matrix(self, ctx:MyGrammarParser.Add_dummy_matrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#anonymous_function_call.
    def visitAnonymous_function_call(self, ctx:MyGrammarParser.Anonymous_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_call.
    def visitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#matrix_block.
    def visitMatrix_block(self, ctx:MyGrammarParser.Matrix_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#bool_literal.
    def visitBool_literal(self, ctx:MyGrammarParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#int_literal.
    def visitInt_literal(self, ctx:MyGrammarParser.Int_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#function_decl.
    def visitFunction_decl(self, ctx:MyGrammarParser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#read_matrix_field.
    def visitRead_matrix_field(self, ctx:MyGrammarParser.Read_matrix_fieldContext):
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


    # Visit a parse tree produced by MyGrammarParser#float_literal.
    def visitFloat_literal(self, ctx:MyGrammarParser.Float_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#while_statement.
    def visitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#add_subtract.
    def visitAdd_subtract(self, ctx:MyGrammarParser.Add_subtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assign_matrix_field.
    def visitAssign_matrix_field(self, ctx:MyGrammarParser.Assign_matrix_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#parentheses.
    def visitParentheses(self, ctx:MyGrammarParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#comparison.
    def visitComparison(self, ctx:MyGrammarParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#matrix_defintion.
    def visitMatrix_defintion(self, ctx:MyGrammarParser.Matrix_defintionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#repeat_until.
    def visitRepeat_until(self, ctx:MyGrammarParser.Repeat_untilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#multiply_divide.
    def visitMultiply_divide(self, ctx:MyGrammarParser.Multiply_divideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#define_variable.
    def visitDefine_variable(self, ctx:MyGrammarParser.Define_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#if_expr.
    def visitIf_expr(self, ctx:MyGrammarParser.If_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#print_statement.
    def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#read_variable.
    def visitRead_variable(self, ctx:MyGrammarParser.Read_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assign_variable.
    def visitAssign_variable(self, ctx:MyGrammarParser.Assign_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#nan_literal.
    def visitNan_literal(self, ctx:MyGrammarParser.Nan_literalContext):
        return self.visitChildren(ctx)



del MyGrammarParser