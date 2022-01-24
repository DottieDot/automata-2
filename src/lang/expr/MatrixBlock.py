from .ExprNode import ExprNode
from ..Variable import Variable, VariableTypes
from lang.dummy_matrix import MatrixExpr

class MatrixBlock(ExprNode):
  _matrix_block: MatrixExpr

  def __init__(self, matrix_block: MatrixExpr) -> None:
    super().__init__()
    self._matrix_block = matrix_block

  def get_value(self) -> Variable:
    return Variable(self._matrix_block.to_string(), VariableTypes.STRING)
