from antlr4 import CommonTokenStream, InputStream
from antlr.MyGrammarLexer import MyGrammarLexer
from antlr.MyGrammarParser import MyGrammarParser
from MyVisitor import MyVisitor

def main():
  while True:
    text = InputStream(input("> "))

    lexer = MyGrammarLexer(text)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.compileUnit()

    visitor = MyVisitor()
    program = visitor.visitCompileUnit(tree)

    value = program.get_value()
    print(f'= {value}')

main()