from typing import Any
import unittest
from antlr4 import CommonTokenStream, InputStream
from antlr.MyGrammarLexer import MyGrammarLexer
from antlr.MyGrammarParser import MyGrammarParser
from MyVisitor import MyVisitor
from lang.Variable import VariableTypes

def run_code(code: str) -> Any:
  lexer = MyGrammarLexer(InputStream(code))
  stream = CommonTokenStream(lexer)
  parser = MyGrammarParser(stream)
  tree = parser.compile_unit()

  visitor = MyVisitor()
  return visitor.visitCompile_unit(tree).get_value().value

class MyTests(unittest.TestCase):
  def test_sum(self):
    result = run_code("2 + 2")
    self.assertEqual(4, result)

  def test_sum_and_multiply(self):
    result = run_code("2 * 4 + 2 * 4")
    self.assertEqual(16, result)

  def test_boolean_expression(self):
    result = run_code("10 > 5")
    self.assertEqual(True, result)

  def test_non_numeric_arithmetics(self):
    result = run_code("true + true")
    self.assertEqual(None, result)

  def test_partially_non_numeric_arithmetics(self):
    result = run_code("1 + true")
    self.assertEqual(None, result)

  def test_if(self):
    result = run_code("if true { 1 }")
    self.assertEqual(1, result)

  def test_if_else_if(self):
    result = run_code("if false { None } else if true { 1 }")
    self.assertEqual(1, result)

  def test_if_else(self):
    result = run_code("if false { None } else { 1 }")
    self.assertEqual(1, result)

  def test_function(self):
    result = run_code("fn(a) { a * 2 }(4)")
    self.assertEqual(8, result)

  def test_call_other_function(self):
    result = run_code("fn a(a) { a / 2 }; fn b(b) { a(b) * 2 }; b(4)")
    self.assertEqual(4, result)

  def test_function_as_paramater(self):
    result = run_code("fn a(cb) { cb() / 2 }; a(fn() { 10 })")
    self.assertEqual(5, result)

  def test_while(self):
    result = run_code("let n = 0; while n < 10 { n = n + 1 }")
    self.assertEqual(10, result)

  def test_function_returns_function_that_captures_variable(self):
    result = run_code("fn a(a) { fn() { a * 2 } }; a(2)()")
    self.assertEqual(4, result)

  def test_recursive_function(self):
    result = run_code("fn factorial(n) { if n > 0 { self(n - 1) * n } else { 1 } }; factorial(5)")
    self.assertEqual(120, result)

  def test_recursive_anonymous_function(self):
    result = run_code("fn(n){ if n > 0 { self(n - 1) * n } else { 1 } }(5)")
    self.assertEqual(120, result)

  def test_repeat_until(self):
    result = run_code("let a = 0; repeat { a = a + 1 } until a >= 10")
    self.assertEqual(10, result)

  def test_repeat_until_runs_once(self):
    result = run_code("repeat { 5 } until true")
    self.assertEqual(5, result)

  def test_define_matrix(self):
    result = run_code("matrix[2,2+2]")
    self.assertEqual(2, result._width)
    self.assertEqual(4, result._height)

  def test_write_matrix(self):
    result = run_code("let m = matrix[1,1]; m[0,0] = 20")
    self.assertEqual(20, result)

  def test_read_matrix(self):
    result = run_code("let m = matrix[1,1]; m[0,0] = 20; m[0,0]")
    self.assertEqual(20, result)

  def test_complex_matrix(self):
    result = run_code("let m = matrix[4,4]; let x = 0; while x < 4 { let y = 0; while y < 4 { m[x, y] = x * y; y = y + 1; }; x = x + 1; }; m")

    raw = [[item.value for item in col] for col in result._matrix]

    self.assertListEqual([
      [0, 0, 0, 0],
      [0, 1, 2, 3],
      [0, 2, 4, 6],
      [0, 3, 6, 9],
    ], raw)

  def test_matrix_in_expr(self):
    result = run_code("let m = matrix[1,1]; m[0,0] = 10; 2 * m[0,0]")
    self.assertEqual(20, result)

if __name__ == '__main__':
  unittest.main()