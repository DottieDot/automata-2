from antlr4 import CommonTokenStream, InputStream
from antlr.MyGrammarLexer import MyGrammarLexer
from antlr.MyGrammarParser import MyGrammarParser
from MyVisitor import MyVisitor
from lang import ExprNode

def main():
  while True:
    text = InputStream(input("> "))

    lexer = MyGrammarLexer(text)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.compile_unit()

    visitor = MyVisitor()
    program: ExprNode = visitor.visitCompile_unit(tree)

    print(program.get_value().value)

main()