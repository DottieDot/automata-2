from lang.Variable import Variable, VariableTypes
from lang.expr.ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from ..ScopeNode import ScopeNode

class NotExprNode(ExprNode):
  value: ExprNode

  def __init__(self, value: ExprNode):
    super().__init__()
    self.value = value

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.value.set_scope(scope)
  
  def get_value(self) -> Variable:
    return Variable(not self.value.get_value().is_truthy(), VariableTypes.BOOL)
