from lang.Variable import Variable
from .ExprNode import ExprNode

class LiteralExprNode(ExprNode):
  value: Variable

  def __init__(self, value: Variable) -> None:
    self.value = value

  def get_value(self) -> Variable:
    return self.value
