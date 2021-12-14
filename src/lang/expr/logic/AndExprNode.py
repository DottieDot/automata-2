from .BooleanExprNode import BooleanExprNode
from ..ExprNode import ExprNode

class AndExprNode(BooleanExprNode):
  def __init__(self, left: ExprNode, right: ExprNode):
    super().__init__(left, right)
  
  def get_value(self) -> int:
    return int(self.left.get_value() and self.right.get_value())
