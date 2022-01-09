from lang.expr import ScopeNode
from .Variable import Variable, VariableTypes

class Function:
  _scope: ScopeNode
  _parameter_names: list[str]
  _body: ScopeNode
  _captured_variables: dict[str, Variable]
  
  def __init__(self, parameter_names: list[str], body: ScopeNode, captured_variables: dict[str, Variable]) -> None:
    self._parameter_names = parameter_names
    self._body = body
    self._captured_variables = captured_variables
    self._scope = ScopeNode(True)
    
    self._body.set_scope(self._scope)

  def call(self, params: list[Variable]) -> Variable:
    if len(params) != len(self._parameter_names):
      raise f'expected {len(self._parameter_names)} paremeters, got {len(params)}'

    param_dict = {}
    for i in range(len(params)):
      param_dict[self._parameter_names[i]] = params[i]

    # Truly awful code
    self._scope._enter_scope()
    self._scope._variables().update(self._captured_variables | param_dict | { 'self': Variable(self, VariableTypes.FUNCTION) })
    result = self._body.get_value()
    self._scope._exit_scope()

    return result
