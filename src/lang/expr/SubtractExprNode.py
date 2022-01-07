from lang.Variable import Variable
from .ExprNode import ExprNode
from .InfixExprNode import InfixExprNode

class SubtractExprNode(InfixExprNode):
  def __init__(self, left: ExprNode, right: ExprNode) -> None:
    super().__init__(left, right)

  def get_value(self) -> Variable:
    return self.left.get_value().subtract(self.right.get_value())
