from lang.Variable import Variable
from .ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class AnonymousFunctionCallNode(ExprNode):
  expr: ExprNode
  params: list[ExprNode]

  def __init__(self, expr: ExprNode, params: list[ExprNode]) -> None:
    super().__init__()
    self.expr = expr
    self.params = params

  def get_value(self) -> Variable:
    return self.expr.get_value().call([p.get_value() for p in self.params])

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.expr.set_scope(scope)
    for param in self.params:
      param.set_scope(scope)
