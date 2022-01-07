from typing import TYPE_CHECKING
from ..Variable import Variable

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class ExprNode:
  def __init__(self) -> None:
    super().__init__()

  def set_scope(self, scope: 'ScopeNode') -> None:
    self.scope = scope

  def get_value(self) -> Variable:
    pass
