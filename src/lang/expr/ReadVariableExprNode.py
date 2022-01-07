from lang.Variable import Variable
from .ExprNode import ExprNode

class ReadVariableExprNode(ExprNode):
  identifier: str

  def __init__(self, identifier: str) -> None:
    super().__init__()
    self.identifier = identifier

  def get_value(self) -> Variable:
    return self.scope.get_variable(self.identifier)
