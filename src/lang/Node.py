from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class Node:
  scope: Optional['ScopeNode'] = None

  def __init__(self) -> None:
    pass

  def set_scope(self, scope: 'ScopeNode') -> None:
    self.scope = scope

  def execute(self) -> None:
    pass
