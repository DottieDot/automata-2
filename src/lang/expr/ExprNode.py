from ..Node import Node

class ExprNode(Node):
  def __init__(self) -> None:
    super().__init__()

  def get_value(self) -> int:
    pass

  def execute(self):
    self.get_value()
