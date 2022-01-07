from lang.expr import ScopeNode
from ..Variable import Variable, VariableTypes

class Function(ScopeNode):
  parameter_names: list[str]
  body: ScopeNode
  
  def __init__(self, parameter_names: list[str], body: ScopeNode) -> None:
    self.parameter_names = parameter_names
    self.body = body

  def call(self, params: list[Variable]) -> Variable:
    if len(params) != len(self.parameter_names):
      raise f'expected {len(self.parameter_names)} paremeters, got {len(params)}'
    
    for i in range(len(params)):
      self.define_variable(self.parameter_names[i], params[i])

    self.body.get_value()
    
    self._exit_scope()

  def set_scope(self, scope: ScopeNode):
    super().set_scope(scope)
    self.body.set_scope(scope)

  def get_value(self) -> Variable:
    Variable(self, VariableTypes.FUNCTION)
