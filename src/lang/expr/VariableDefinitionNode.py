from lang.Variable import Variable
from .ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class VariableDefinitionNode(ExprNode):
  identifier: str
  value: ExprNode

  def __init__(self, identifier: str, value: ExprNode) -> None:
    super().__init__()
    self.identifier = identifier
    self.value = value

  def get_value(self) -> Variable:
    self.scope.define_variable(self.identifier, self.value.get_value())

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.value.set_scope(scope)
