from .MatrixExpr import MatrixExpr

class AddMatrix(MatrixExpr):
  lhs: MatrixExpr
  rhs: MatrixExpr

  def __init__(self, lhs: MatrixExpr, rhs: MatrixExpr) -> None:
    self.lhs = lhs
    self.rhs = rhs

  def to_string(self) -> str:
    return f'the sum of ({self.lhs.to_string()}) and ({self.rhs.to_string()})'
