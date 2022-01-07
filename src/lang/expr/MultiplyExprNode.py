from lang.Variable import Variable
from .ExprNode import ExprNode
from .InfixExprNode import InfixExprNode

class MultiplyExprNode(InfixExprNode):
  def __init__(self, left: ExprNode, right: ExprNode) -> None:
    super().__init__(left, right)

  def get_value(self) -> Variable:
    return self.left.get_value().multiply(self.right.get_value())
