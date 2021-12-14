from .ExprNode import ExprNode
from .InfixExprNode import InfixExprNode

class AddExprNode(InfixExprNode):
  def __init__(self, left: ExprNode, right: ExprNode) -> None:
    super().__init__(left, right)

  def get_value(self) -> int:
    return self.left.get_value() + self.right.get_value()
