from .ExprNode import ExprNode
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .ScopeNode import ScopeNode

class InfixExprNode(ExprNode):
  left: ExprNode
  right: ExprNode

  def __init__(self, left: ExprNode, right: ExprNode):
    super().__init__()
    self.left = left
    self.right = right

  def set_scope(self, scope: 'ScopeNode') -> None:
    super().set_scope(scope)
    self.left.set_scope(scope)
    self.right.set_scope(scope)
