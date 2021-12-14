from .ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from ..ScopeNode import ScopeNode

class FunctionCallNode(ExprNode):
  params: list[ExprNode]

  def __init__(self, params: list[ExprNode]) -> None:
    super().__init__()
    self.params = params

  def get_value(self) -> int:
    for param in self.params:
      print(param.get_value())
    return 0

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    for param in self.params:
      param.set_scope(scope)
