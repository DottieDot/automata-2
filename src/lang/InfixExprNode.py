from .ExprNode import ExprNode

class InfixExprNode(ExprNode):
  left: ExprNode
  right: ExprNode

  def __init__(self, left: ExprNode, right: ExprNode):
    super().__init__()
    self.left = left
    self.right = right
