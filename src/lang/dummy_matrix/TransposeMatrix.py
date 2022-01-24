from .MatrixExpr import MatrixExpr

class TransposeMatrix(MatrixExpr):
  expr: MatrixExpr

  def __init__(self, expr: MatrixExpr) -> None:
    self.expr = expr

  def to_string(self) -> str:
    return f'transpose matrix of ({self.expr.to_string()})'
