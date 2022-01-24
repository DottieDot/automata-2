from .MatrixExpr import MatrixExpr

class DefineMatrix(MatrixExpr):
  w: int
  h: int
  ident: str

  def __init__(self, ident: str, w: int, h: int) -> None:
    self.w = w
    self.h = h
    self.ident = ident

  def to_string(self) -> str:
    return f'a matrix of {self.w}x{self.h} named {self.ident}'
