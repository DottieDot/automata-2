from .Variable import Variable, VariableTypes

class Matrix:
  _matrix: list[list[Variable]]
  _width: int
  _height: int

  def __init__(self, width: int, height: int) -> None:
    self._width = width
    self._height = height
    self._matrix = [[Variable(None, VariableTypes.NONE) for _ in range(height)] for _ in range(width)]

  def read(self, x: int, y: int) -> Variable:
    if x >= self._width  or y >= self._height:
      raise Exception('matrix position out of range')

    return self._matrix[x][y]

  def set(self, x: int, y: int, value: Variable):
    if x >= self._width  or y >= self._height:
      raise Exception('matrix position out of range')
    
    self._matrix[x][y] = value
