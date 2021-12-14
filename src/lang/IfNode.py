from .Node import Node
from .expr import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class IfNode(Node):
  condition: ExprNode
  body: Node

  def __init__(self, condition: ExprNode, body: Node) -> None:
    super().__init__()
    self.condition = condition
    self.body = body

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.condition.set_scope(scope)
    self.body.set_scope(scope)

  def execute(self) -> None:
    if self.condition.get_value():
      self.body.execute()
