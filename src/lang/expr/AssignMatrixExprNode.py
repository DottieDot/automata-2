from copy import deepcopy
from lang.Variable import Variable, VariableTypes
from lang.Matrix import Matrix
from .ExprNode import ExprNode

class AssignMatrixExprNode(ExprNode):
  identifier: str
  x: ExprNode
  y: ExprNode
  value: ExprNode

  def __init__(self, identifier: str, x: ExprNode, y: ExprNode, value: ExprNode) -> None:
    super().__init__()
    self.identifier = identifier
    self.x = x
    self.y = y
    self.value = value

  def set_scope(self, scope: ExprNode) -> None:
    super().set_scope(scope)
    self.x.set_scope(scope)
    self.y.set_scope(scope)
    self.value.set_scope(scope)

  def get_value(self) -> Variable:
    var = deepcopy(self.scope.get_variable(self.identifier))
    x = self.x.get_value()
    y = self.y.get_value()

    if var.type != VariableTypes.MATRIX:
      raise Exception(f'{self.identifier} is not a matrix')
    if x.type != VariableTypes.INT or y.type != VariableTypes.INT:
      raise Exception(f'matrix position must be an integer')

    value = self.value.get_value()
    var.value.set(x.value, y.value, value)
    self.scope.assign_variable(self.identifier, var)

    return value
