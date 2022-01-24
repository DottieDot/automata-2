from .MatrixExpr import MatrixExpr

class Scalar(MatrixExpr):
  scalar: int

  def __init__(self, scalar: int) -> None:
    self.scalar = scalar

  def to_string(self) -> str:
    return f'scalar {self.scalar}'
