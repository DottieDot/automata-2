from typing import Dict, Optional

from lang.Variable import Variable, VariableTypes
from .ExprNode import ExprNode

class ScopeNode(ExprNode):
  expressions: list[ExprNode]
  variables  : Dict[str, Variable]
  has_result : bool

  def _exit_scope(self):
    self.variables  = {}

  def __init__(self, has_result: bool) -> None:
    super().__init__()
    self.expressions = []
    self.variables  = {}
    self.has_result = has_result

  def add_node(self, node: ExprNode):
    node.set_scope(self)
    self.expressions.append(node)

  def get_value(self) -> Variable:
    result = None
    for statement in self.expressions:
      result = statement.get_value()

    self._exit_scope()

    return result if self.has_result else Variable(None, VariableTypes.NONE)

  def define_variable(self, identifier: str, value: Variable):
    if identifier in self.variables:
      raise Exception(f'{identifier} already exists in current scope.')

    self.variables[identifier] = value;

  def assign_variable(self, identifier: str, value: Variable):
    if identifier in self.variables:
      self.variables[identifier] = value
    elif self.scope:
      self.scope.assign_variable(identifier, value)
    else:
      raise Exception(f'{identifier} does not exist in current scope.')

  def get_variable(self, identifier: str) -> Optional[Variable]:
    if identifier in self.variables:
      return self.variables[identifier]
    elif self.scope:
      return self.scope.get_variable(identifier)
    else:
      return None
