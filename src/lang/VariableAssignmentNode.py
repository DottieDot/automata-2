from .Node import Node
from .expr.ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class VariableAssignmentNode(Node):
  identifier: str
  value: ExprNode

  def __init__(self, identifier: str, value: ExprNode) -> None:
    super().__init__()
    self.identifier = identifier
    self.value = value

  def execute(self):
    self.scope.assign_variable(self.identifier, self.value.get_value())
  
  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.value.set_scope(scope)
