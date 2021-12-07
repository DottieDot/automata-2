from .ExprNode import ExprNode

class NumberExprNode(ExprNode):
  value: int

  def __init__(self, value: int) -> None:
    self.value = value

  def get_value(self) -> int:
    return self.value
