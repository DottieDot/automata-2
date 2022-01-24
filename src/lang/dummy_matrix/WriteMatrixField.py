from .MatrixExpr import MatrixExpr

class WriteMatrixField(MatrixExpr):
  x: int
  y: int
  ident: str
  value: MatrixExpr

  def __init__(self, x: int, y: int, ident: str, value: int) -> None:
    self.x = x
    self.y = y
    self.ident = ident
    self.value = value

  def to_string(self) -> str:
    return f'set position ({self.x}, {self.y}) of {self.ident} to {self.value}'
