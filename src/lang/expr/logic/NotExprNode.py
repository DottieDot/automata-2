from lang.expr.ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from lang.ScopeNode import ScopeNode

class NotExprNode(ExprNode):
  value: ExprNode

  def __init__(self, value: ExprNode):
    super().__init__()
    self.value = value

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.value.set_scope()
  
  def get_value(self) -> int:
    return int(not self.left.get_value())
