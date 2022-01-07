from lang.Variable import Variable
from .BooleanExprNode import BooleanExprNode
from ..ExprNode import ExprNode

class GtExprNode(BooleanExprNode):
  def __init__(self, left: ExprNode, right: ExprNode):
    super().__init__(left, right)
  
  def get_value(self) -> Variable:
    return self.left.get_value().greater_than(self.right.get_value())
