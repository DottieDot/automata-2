from typing import TYPE_CHECKING, Optional
from ..Variable import Variable

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class ExprNode:
  scope: Optional['ScopeNode']

  def __init__(self) -> None:
    self.scope = None

  def set_scope(self, scope: 'ScopeNode') -> None:
    self.scope = scope

  def get_value(self) -> Variable:
    raise 'get_value is not implemented'
