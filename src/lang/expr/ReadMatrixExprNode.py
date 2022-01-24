from lang.Variable import Variable, VariableTypes
from lang.Matrix import Matrix
from .ExprNode import ExprNode

class ReadmatrixExprNode(ExprNode):
  matrix: ExprNode
  x: ExprNode
  y: ExprNode

  def __init__(self, matrix: ExprNode, x: ExprNode, y: ExprNode) -> None:
    super().__init__()
    self.matrix = matrix
    self.x = x
    self.y = y

  def set_scope(self, scope: ExprNode) -> None:
    super().set_scope(scope)
    self.matrix.set_scope(scope)
    self.x.set_scope(scope)
    self.y.set_scope(scope)

  def get_value(self) -> Variable:
    var = self.matrix.get_value()
    x = self.x.get_value()
    y = self.y.get_value()

    if x.type != VariableTypes.INT or y.type != VariableTypes.INT:
      raise Exception(f'matrix position must be an integer')

    return var.value.read(x.value, y.value)
