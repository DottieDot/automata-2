from typing import Dict, Optional
from .Node import Node

class ScopeNode(Node):
  statements: list[Node]
  variables : Dict[str, int]

  def __init__(self) -> None:
    super().__init__()
    self.statements = []
    self.variables  = {}

  def add_node(self, node: Node):
    node.set_scope(self)
    self.statements.append(node)

  def execute(self):
    for statement in self.statements:
      statement.execute()

  def define_variable(self, identifier: str, value: int):
    if identifier in self.variables:
      raise Exception(f'{identifier} already exists in current scope.')

    self.variables[identifier] = value;

  def assign_variable(self, identifier: str, value: int):
    if identifier in self.variables:
      self.variables[identifier] = value
    elif self.scope:
      self.scope.assign_variable(identifier, value)
    else:
      raise Exception(f'{identifier} does not exist in current scope.')

  def get_variable(self, identifier: str) -> Optional[int]:
    if identifier in self.variables:
      return self.variables[identifier]
    elif self.scope:
      return self.scope.get_variable(identifier)
    else:
      return None
