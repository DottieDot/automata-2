from .MatrixExpr import MatrixExpr

class ReadMatrixField(MatrixExpr):
  x: int
  y: int
  expr: MatrixExpr

  def __init__(self, x: int, y: int, expr: MatrixExpr) -> None:
    self.x = x
    self.y = y
    self.expr = expr

  def to_string(self) -> str:
    return f'retrieve position ({self.x}, {self.y}) of ({self.expr.to_string()})'
