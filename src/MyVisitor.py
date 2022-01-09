from antlr.MyGrammarParser import MyGrammarParser
from antlr.MyGrammarVisitor import MyGrammarVisitor
from lang import *


class MyVisitor(MyGrammarVisitor):
  def __init__(self) -> None:
    super().__init__()

  # Visit a parse tree produced by MyGrammarParser#compile_unit.
  def visitCompile_unit(self, ctx: MyGrammarParser.Compile_unitContext):
    return self.visit(ctx.scoped_expr())

  # Visit a parse tree produced by MyGrammarParser#scoped_expr.
  def visitScoped_expr(self, ctx: MyGrammarParser.Scoped_exprContext):
    scope = ScopeNode(ctx.final_expr)
    for statement in ctx.expr():
      scope.add_node(self.visit(statement))
    return scope

  # Visit a parse tree produced by MyGrammarParser#int_literal.
  def visitInt_literal(self, ctx: MyGrammarParser.Int_literalContext):
    return LiteralExprNode(Variable(int(str(ctx.INTEGER())), VariableTypes.INT))

  # Visit a parse tree produced by MyGrammarParser#float_literal.
  def visitFloat_literal(self, ctx: MyGrammarParser.Float_literalContext):
    return LiteralExprNode(Variable(float(str(ctx.FLOAT())), VariableTypes.FLOAT))

  # Visit a parse tree produced by MyGrammarParser#bool_literal.
  def visitBool_literal(self, ctx: MyGrammarParser.Bool_literalContext):
    return LiteralExprNode(Variable(not ctx.FALSE(), VariableTypes.BOOL))

  # Visit a parse tree produced by MyGrammarParser#none_literal.
  def visitNone_literal(self, ctx: MyGrammarParser.None_literalContext):
    return LiteralExprNode(Variable(None, VariableTypes.NONE))

  # Visit a parse tree produced by MyGrammarParser#nan_literal.
  def visitNan_literal(self, ctx: MyGrammarParser.Nan_literalContext):
    return LiteralExprNode(Variable(None, VariableTypes.NAN))

  # Visit a parse tree produced by MyGrammarParser#function_decl.
  def visitFunction_decl(self, ctx: MyGrammarParser.Function_declContext):
    params = ctx.IDENTIFIER()
    if ctx.ident: params.pop(0)
    fn = FunctionExprNode([str(ident) for ident in params], self.visit(ctx.scoped_expr()))
    if ctx.ident:
      return VariableDefinitionNode(ctx.ident.text, fn)
    else:
      return fn

  # Visit a parse tree produced by MyGrammarParser#parentheses.
  def visitParentheses(self, ctx: MyGrammarParser.ParenthesesContext):
    return self.visit(ctx.expr())

  # Visit a parse tree produced by MyGrammarParser#not.
  def visitNot(self, ctx: MyGrammarParser.NotContext):
    return NotExprNode(self.visit(ctx.expr()))

  # Visit a parse tree produced by MyGrammarParser#comparison.
  def visitComparison(self, ctx: MyGrammarParser.ComparisonContext):
    if ctx.GT():
      return GtExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.GE():
      return GeExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.LT():
      return LtExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.LE():
      return LeExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.EQ():
      return EqExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.NEQ():
      return NeqExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )

  # Visit a parse tree produced by MyGrammarParser#conjunction.
  def visitConjunction(self, ctx: MyGrammarParser.ConjunctionContext):
    if ctx.AND():
      return AndExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.OR:
      return OrExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )

  # Visit a parse tree produced by MyGrammarParser#read_variable.
  def visitRead_variable(self, ctx: MyGrammarParser.Read_variableContext):
    return ReadVariableExprNode(
        str(ctx.IDENTIFIER())
    )

  # Visit a parse tree produced by MyGrammarParser#function_call.
  def visitFunction_call(self, ctx: MyGrammarParser.Function_callContext):
    params: list[ExprNode] = []
    for param in ctx.expr():
      params.append(self.visit(param))

    return FunctionCallNode(ctx.ident.text, params)

  # Visit a parse tree produced by MyGrammarParser#multiply_divide.
  def visitMultiply_divide(self, ctx: MyGrammarParser.Multiply_divideContext):
    if ctx.OP_MULT():
      return MultiplyExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.OP_DIV():
      return DivideExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )

  # Visit a parse tree produced by MyGrammarParser#add_subtract.
  def visitAdd_subtract(self, ctx: MyGrammarParser.Add_subtractContext):
    if ctx.OP_PLUS():
      return AddExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )
    elif ctx.OP_MINUS():
      return SubtractExprNode(
          self.visit(ctx.left),
          self.visit(ctx.right)
      )

  # Visit a parse tree produced by MyGrammarParser#define_variable.
  def visitDefine_variable(self, ctx:MyGrammarParser.Define_variableContext):
    return VariableDefinitionNode(
      str(ctx.IDENTIFIER()),
      self.visit(ctx.expr())
    )

  # Visit a parse tree produced by MyGrammarParser#assign_variable.
  def visitAssign_variable(self, ctx:MyGrammarParser.Assign_variableContext):
    return VariableAssignmentNode(
      str(ctx.IDENTIFIER()),
      self.visit(ctx.expr())
    )

  # Visit a parse tree produced by MyGrammarParser#if_statement.
  def visitIf_statement(self, ctx:MyGrammarParser.If_statementContext):
    return IfNode(
      self.visit(ctx.expr()),
      self.visit(ctx.scoped_expr())
    )

  # Visit a parse tree produced by MyGrammarParser#else_if_statement.
  def visitElseIf_statement(self, ctx:MyGrammarParser.Else_if_statementContext):
    return IfNode(
      self.visit(ctx.expr()),
      self.visit(ctx.scoped_expr())
    )

  # Visit a parse tree produced by MyGrammarParser#else_statement.
  def visitElse_statement(self, ctx:MyGrammarParser.Else_statementContext):
    return self.visit(ctx.scoped_expr())

  # Visit a parse tree produced by MyGrammarParser#If_expr
  def visitIf_expr(self, ctx:MyGrammarParser.If_exprContext):
    if_statement = self.visit(ctx.if_statement())
    last_statement = if_statement
    for statement in ctx.else_if_statement():
      node = self.visit(statement)
      last_statement.set_next(node)
      last_statement = node
    if ctx.else_statement():
      last_statement.set_next(self.visit(ctx.else_statement()))
    return if_statement

  # Visit a parse tree produced by MyGrammarParser#anonymous_function_call.
  def visitAnonymous_function_call(self, ctx:MyGrammarParser.Anonymous_function_callContext):
    return AnonymousFunctionCallNode(self.visit(ctx.fn_expr), [self.visit(expr) for expr in ctx.expr()[1:]])

  # Visit a parse tree produced by MyGrammarParser#print_statement.
  def visitPrint_statement(self, ctx:MyGrammarParser.Print_statementContext):
    return PrintExprNode(self.visit(ctx.expr()))
