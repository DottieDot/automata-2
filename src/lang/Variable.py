from typing import Any
from enum import Enum
from typing_extensions import Self

class VariableTypes(Enum):
  NONE = 0
  INT = 1
  FLOAT = 2
  BOOL = 3
  NAN = 4
  FUNCTION = 5


class Variable:
  value: Any
  type: VariableTypes

  def _is_numeric(self) -> bool:
    match self.type:
      case VariableTypes.INT:
        return True
      case VariableTypes.FLOAT:
        return True
      case _:
        return False

  def __init__(self, value: Any, type: VariableTypes) -> None:
    self.value = value
    self.type = type

  def is_truthy(self) -> bool:
    return not not self.value

  def add(self, rvalue: Self) -> Self:
    if self._is_numeric() and rvalue._is_numeric():
      return Variable(
          self.value + rvalue.value,
          VariableTypes.FLOAT if (
              self.type == VariableTypes.INT and rvalue.type == VariableTypes.INT) else VariableTypes.INT
      )
    else:
      return Variable(
          None,
          VariableTypes.NAN
      )

  def subtract(self, rvalue: Self) -> Self:
    if self._is_numeric() and rvalue._is_numeric():
      return Variable(
          self.value - rvalue.value,
          VariableTypes.FLOAT if (
              self.type == VariableTypes.INT and rvalue.type == VariableTypes.INT) else VariableTypes.INT
      )
    else:
      return Variable(
          None,
          VariableTypes.NAN
      )

  def multiply(self, rvalue: Self) -> Self:
    if self._is_numeric() and rvalue._is_numeric():
      return Variable(
          self.value * rvalue.value,
          VariableTypes.FLOAT if (
              self.type == VariableTypes.INT and rvalue.type == VariableTypes.INT) else VariableTypes.INT
      )
    else:
      return Variable(
          None,
          VariableTypes.NAN
      )

  def divide(self, rvalue: Self) -> Self:
    if self._is_numeric() and rvalue._is_numeric():
      return Variable(
          self.value / rvalue.value,
          VariableTypes.FLOAT
      )
    else:
      return Variable(
          None,
          VariableTypes.NAN
      )

  def equals(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value == rvalue.value,
        VariableTypes.BOOL
    )

  def not_equals(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value != rvalue.value,
        VariableTypes.BOOL
    )

  def greater_than(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value > rvalue.value,
        VariableTypes.BOOL
    )

  def lower_than(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value < rvalue.value,
        VariableTypes.BOOL
    )

  def greater_or_equal(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value >= rvalue.value,
        VariableTypes.BOOL
    )

  def lower_or_equal(self, rvalue: Self) -> Self:
    return Variable(
        self.type == rvalue.type and self.value <= rvalue.value,
        VariableTypes.BOOL
    )

  def call(self, params: list[Self]) -> Self:
    if self.type != VariableTypes.FUNCTION:
      raise f"{self.type} is not a callable type"
    
    return self.value.call(params)
