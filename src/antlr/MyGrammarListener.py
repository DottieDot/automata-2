# Generated from MyGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete listener for a parse tree produced by MyGrammarParser.
class MyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammarParser#compile_unit.
    def enterCompile_unit(self, ctx:MyGrammarParser.Compile_unitContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#compile_unit.
    def exitCompile_unit(self, ctx:MyGrammarParser.Compile_unitContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#scoped_expr.
    def enterScoped_expr(self, ctx:MyGrammarParser.Scoped_exprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#scoped_expr.
    def exitScoped_expr(self, ctx:MyGrammarParser.Scoped_exprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#if_statement.
    def enterIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#if_statement.
    def exitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#else_if_statement.
    def enterElse_if_statement(self, ctx:MyGrammarParser.Else_if_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#else_if_statement.
    def exitElse_if_statement(self, ctx:MyGrammarParser.Else_if_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#else_statement.
    def enterElse_statement(self, ctx:MyGrammarParser.Else_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#else_statement.
    def exitElse_statement(self, ctx:MyGrammarParser.Else_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#anonymous_function_call.
    def enterAnonymous_function_call(self, ctx:MyGrammarParser.Anonymous_function_callContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#anonymous_function_call.
    def exitAnonymous_function_call(self, ctx:MyGrammarParser.Anonymous_function_callContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#parentheses.
    def enterParentheses(self, ctx:MyGrammarParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#parentheses.
    def exitParentheses(self, ctx:MyGrammarParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#comparison.
    def enterComparison(self, ctx:MyGrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#comparison.
    def exitComparison(self, ctx:MyGrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#function_call.
    def enterFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#function_call.
    def exitFunction_call(self, ctx:MyGrammarParser.Function_callContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#multiply_divide.
    def enterMultiply_divide(self, ctx:MyGrammarParser.Multiply_divideContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#multiply_divide.
    def exitMultiply_divide(self, ctx:MyGrammarParser.Multiply_divideContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#bool_literal.
    def enterBool_literal(self, ctx:MyGrammarParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#bool_literal.
    def exitBool_literal(self, ctx:MyGrammarParser.Bool_literalContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#define_variable.
    def enterDefine_variable(self, ctx:MyGrammarParser.Define_variableContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#define_variable.
    def exitDefine_variable(self, ctx:MyGrammarParser.Define_variableContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#if_expr.
    def enterIf_expr(self, ctx:MyGrammarParser.If_exprContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#if_expr.
    def exitIf_expr(self, ctx:MyGrammarParser.If_exprContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#int_literal.
    def enterInt_literal(self, ctx:MyGrammarParser.Int_literalContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#int_literal.
    def exitInt_literal(self, ctx:MyGrammarParser.Int_literalContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#function_decl.
    def enterFunction_decl(self, ctx:MyGrammarParser.Function_declContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#function_decl.
    def exitFunction_decl(self, ctx:MyGrammarParser.Function_declContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#not.
    def enterNot(self, ctx:MyGrammarParser.NotContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#not.
    def exitNot(self, ctx:MyGrammarParser.NotContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#print_statement.
    def enterPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#print_statement.
    def exitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#conjunction.
    def enterConjunction(self, ctx:MyGrammarParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#conjunction.
    def exitConjunction(self, ctx:MyGrammarParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#none_literal.
    def enterNone_literal(self, ctx:MyGrammarParser.None_literalContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#none_literal.
    def exitNone_literal(self, ctx:MyGrammarParser.None_literalContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#read_variable.
    def enterRead_variable(self, ctx:MyGrammarParser.Read_variableContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#read_variable.
    def exitRead_variable(self, ctx:MyGrammarParser.Read_variableContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#assign_variable.
    def enterAssign_variable(self, ctx:MyGrammarParser.Assign_variableContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#assign_variable.
    def exitAssign_variable(self, ctx:MyGrammarParser.Assign_variableContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#float_literal.
    def enterFloat_literal(self, ctx:MyGrammarParser.Float_literalContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#float_literal.
    def exitFloat_literal(self, ctx:MyGrammarParser.Float_literalContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#nan_literal.
    def enterNan_literal(self, ctx:MyGrammarParser.Nan_literalContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#nan_literal.
    def exitNan_literal(self, ctx:MyGrammarParser.Nan_literalContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#while_statement.
    def enterWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#while_statement.
    def exitWhile_statement(self, ctx:MyGrammarParser.While_statementContext):
        pass


    # Enter a parse tree produced by MyGrammarParser#add_subtract.
    def enterAdd_subtract(self, ctx:MyGrammarParser.Add_subtractContext):
        pass

    # Exit a parse tree produced by MyGrammarParser#add_subtract.
    def exitAdd_subtract(self, ctx:MyGrammarParser.Add_subtractContext):
        pass



del MyGrammarParser