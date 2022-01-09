from lang.Variable import Variable, VariableTypes
from lang.Function import Function
from .ExprNode import ExprNode

class FunctionExprNode(ExprNode):
  _params: list[str]
  _body: ExprNode

  def __init__(self, params: list[str], body: ExprNode) -> None:
    super().__init__()
    self._params = params
    self._body = body

  def get_value(self) -> Variable:
    function = Function(self._params, self._body, self.scope.flatten())
    return Variable(function, VariableTypes.FUNCTION)
