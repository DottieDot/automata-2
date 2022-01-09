from lang.Variable import Variable, VariableTypes
from lang.Function import Function
from .ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class PrintExprNode(ExprNode):
  expr: ExprNode

  def __init__(self, expr: ExprNode) -> None:
    super().__init__()
    self.expr = expr

  def get_value(self) -> Variable:
    value = self.expr.get_value()
    print(value.value)
    return value

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.expr.set_scope(scope)
