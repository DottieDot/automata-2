from .MatrixExpr import MatrixExpr

class Identifier(MatrixExpr):
  ident: str

  def __init__(self, ident: str) -> None:
    self.ident = ident

  def to_string(self) -> str:
    return f'matrix {self.ident}'
