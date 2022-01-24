from .MatrixExpr import MatrixExpr

class MultiplyMatrix(MatrixExpr):
  lhs: MatrixExpr
  rhs: MatrixExpr

  def __init__(self, lhs: MatrixExpr, rhs: MatrixExpr) -> None:
    self.lhs = lhs
    self.rhs = rhs

  def to_string(self) -> str:
    return f'the result of multiplying ({self.lhs.to_string()}) with ({self.rhs.to_string()})'
