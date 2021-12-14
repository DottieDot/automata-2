# Generated from MyGrammar.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("N\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\16\6\16=\n\16\r\16\16\16>\3")
        buf.write("\17\3\17\7\17C\n\17\f\17\16\17F\13\17\3\20\6\20I\n\20")
        buf.write("\r\20\16\20J\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2")
        buf.write("\6\3\2\62;\5\2C\\aac|\5\2\62;C\\c|\5\2\13\f\17\17\"\"")
        buf.write("\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2")
        buf.write("\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2")
        buf.write("\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\63\3\2\2\2\27\65\3\2")
        buf.write("\2\2\31\67\3\2\2\2\33<\3\2\2\2\35@\3\2\2\2\37H\3\2\2\2")
        buf.write("!\"\7-\2\2\"\4\3\2\2\2#$\7/\2\2$\6\3\2\2\2%&\7,\2\2&\b")
        buf.write("\3\2\2\2\'(\7\61\2\2(\n\3\2\2\2)*\7?\2\2*\f\3\2\2\2+,")
        buf.write("\7*\2\2,\16\3\2\2\2-.\7+\2\2.\20\3\2\2\2/\60\7=\2\2\60")
        buf.write("\22\3\2\2\2\61\62\7}\2\2\62\24\3\2\2\2\63\64\7\177\2\2")
        buf.write("\64\26\3\2\2\2\65\66\7.\2\2\66\30\3\2\2\2\678\7n\2\28")
        buf.write("9\7g\2\29:\7v\2\2:\32\3\2\2\2;=\t\2\2\2<;\3\2\2\2=>\3")
        buf.write("\2\2\2><\3\2\2\2>?\3\2\2\2?\34\3\2\2\2@D\t\3\2\2AC\t\4")
        buf.write("\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\36\3\2\2")
        buf.write("\2FD\3\2\2\2GI\t\5\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2J")
        buf.write("K\3\2\2\2KL\3\2\2\2LM\b\20\2\2M \3\2\2\2\6\2>DJ\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class MyGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OP_PLUS = 1
    OP_MINUS = 2
    OP_MULT = 3
    OP_DIV = 4
    OP_ASSIGN = 5
    LPAR = 6
    RPAR = 7
    EOS = 8
    OPEN_BLOCK = 9
    CLOSE_BLOCK = 10
    COMMA = 11
    LET = 12
    INTEGER = 13
    IDENTIFIER = 14
    WHITESPACE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'('", "')'", "';'", "'{'", 
            "'}'", "','", "'let'" ]

    symbolicNames = [ "<INVALID>",
            "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", "OP_ASSIGN", "LPAR", 
            "RPAR", "EOS", "OPEN_BLOCK", "CLOSE_BLOCK", "COMMA", "LET", 
            "INTEGER", "IDENTIFIER", "WHITESPACE" ]

    ruleNames = [ "OP_PLUS", "OP_MINUS", "OP_MULT", "OP_DIV", "OP_ASSIGN", 
                  "LPAR", "RPAR", "EOS", "OPEN_BLOCK", "CLOSE_BLOCK", "COMMA", 
                  "LET", "INTEGER", "IDENTIFIER", "WHITESPACE" ]

    grammarFileName = "MyGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


