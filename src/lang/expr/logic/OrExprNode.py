from lang.Variable import Variable, VariableTypes
from .BooleanExprNode import BooleanExprNode
from ..ExprNode import ExprNode

class OrExprNode(BooleanExprNode):
  def __init__(self, left: ExprNode, right: ExprNode):
    super().__init__(left, right)
  
  def get_value(self) -> Variable:
    return Variable(
      self.left.get_value().is_truthy() or self.right.get_value().is_truthy(), 
      VariableTypes.BOOL
    )
