
from lang.Variable import Variable, VariableTypes
from lang.Matrix import Matrix
from .ExprNode import ExprNode


class MatrixDefinitionNode(ExprNode):
  _w: ExprNode
  _h: ExprNode
  
  def __init__(self, w: ExprNode, h: ExprNode) -> None:
    super().__init__()
    self._w = w
    self._h = h

  def set_scope(self, scope: ExprNode) -> None:
    super().set_scope(scope)
    self._w.set_scope(scope)
    self._h.set_scope(scope)

  def get_value(self) -> Variable:
    w = self._w.get_value()
    h = self._h.get_value()

    if w.type != VariableTypes.INT or h.type != VariableTypes.INT:
      raise Exception('matrix size definition must conssit of integers')

    return Variable(Matrix(w.value, h.value), VariableTypes.MATRIX)
