from antlr.MyGrammarParser import MyGrammarParser
from antlr.MyGrammarVisitor import MyGrammarVisitor
from lang import *

class MyVisitor(MyGrammarVisitor):
  def __init__(self) -> None:
    super().__init__()

  def visitCompileUnit(self, ctx: MyGrammarParser.CompileUnitContext):
    return self.visit(ctx.scope())

  def visitParenExpr(self, ctx: MyGrammarParser.ParenExprContext):
    return self.visit(ctx.expr())

  def visitScope(self, ctx: MyGrammarParser.ScopeContext):
    scope = ScopeNode()
    for statement in ctx.statement():
      scope.add_node(self.visit(statement))
    return scope

  def visitNewScope(self, ctx: MyGrammarParser.NewScopeContext):
    return self.visit(ctx.scope())

  def visitDefineVariable(self, ctx: MyGrammarParser.DefineVariableContext):
    return VariableDefinitionNode(
      str(ctx.IDENTIFIER()),
      self.visit(ctx.expr())
    )
  
  def visitAssignVariable(self, ctx: MyGrammarParser.AssignVariableContext):
    return VariableAssignmentNode(
      str(ctx.IDENTIFIER()),
      self.visit(ctx.expr())
    )
  
  def visitReadVariable(self, ctx: MyGrammarParser.ReadVariableContext):
    return ReadVariableExprNode(
      str(ctx.IDENTIFIER())
    )

  def visitExpression(self, ctx: MyGrammarParser.ExpressionContext):
    return self.visit(ctx.expr())

  def visitIfStatement(self, ctx: MyGrammarParser.IfStatementContext):
    return IfNode(
      self.visit(ctx.expr()),
      self.visit(ctx.statement())
    )

  def visitNot(self, ctx: MyGrammarParser.NotContext):
    return NotExprNode(
      self.visit(ctx.expr())
    )

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

  def visitInfixExpr(self, ctx: MyGrammarParser.InfixExprContext):
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
    elif ctx.OP_MULT():
      return MultiplyExprNode(
        self.visit(ctx.left), 
        self.visit(ctx.right)
      )
    elif ctx.OP_DIV():
      return DivideExprNode(
        self.visit(ctx.left), 
        self.visit(ctx.right)
      )

  def visitFunctionCall(self, ctx:MyGrammarParser.FunctionCallContext):
    params: list[ExprNode] = []
    for param in ctx.expr():
      params.append(self.visit(param))

    return FunctionCallNode(params)
  
  def visitNumberExpr(self, ctx: MyGrammarParser.NumberExprContext):
    return NumberExprNode(int(str(ctx.INTEGER())))
