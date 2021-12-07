from antlr.MyGrammarParser import MyGrammarParser
from antlr.MyGrammarVisitor import MyGrammarVisitor
from lang.AddExprNode import AddExprNode
from lang.SubtractExprNode import SubtractExprNode
from lang.MultiplyExprNode import MultiplyExprNode
from lang.DivideExprNode import DivideExprNode
from lang.NumberExprNode import NumberExprNode

class MyVisitor(MyGrammarVisitor):
  def __init__(self) -> None:
    super().__init__()

  def visitCompileUnit(self, ctx: MyGrammarParser.CompileUnitContext):
    return self.visit(ctx.expr())

  def visitParenExpr(self, ctx: MyGrammarParser.ParenExprContext):
    return self.visit(ctx.expr())

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
  
  def visitNumberExpr(self, ctx: MyGrammarParser.NumberExprContext):
    return NumberExprNode(int(str(ctx.INTEGER())))
