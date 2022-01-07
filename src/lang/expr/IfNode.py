from lang.Variable import Variable, VariableTypes
from .ExprNode import ExprNode

class IfNode(ExprNode):
  condition: ExprNode
  body: ExprNode

  def __init__(self, condition: ExprNode, body: ExprNode) -> None:
    super().__init__()
    self.condition = condition
    self.body = body

  def set_scope(self, scope: ExprNode) -> None:
    super().set_scope(scope)
    self.condition.set_scope(scope)
    self.body.set_scope(scope)

  def get_value(self) -> None:
    if self.condition.get_value().is_truthy():
      return self.body.get_value()
    else:
      return Variable(None, VariableTypes.NONE)
