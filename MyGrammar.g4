grammar MyGrammar;

compileUnit
  : scope  
  ;

scope
  : (statement)*
  ;

statement
  : OPEN_BLOCK scope CLOSE_BLOCK       # newScope
  | LET IDENTIFIER OP_ASSIGN expr EOS  # defineVariable
  | IDENTIFIER OP_ASSIGN expr EOS      # assignVariable
  | expr EOS                           # expression
  ;

expr
  : value=INTEGER                                   # numberExpr
  | ident=IDENTIFIER LPAR (expr(COMMA expr)*)? RPAR # functionCall
  | LPAR expr RPAR                                  # parenExpr
  | left=expr op=(OP_DIV|OP_MULT)   right=expr      # infixExpr
  | left=expr op=(OP_PLUS|OP_MINUS) right=expr      # infixExpr
  | IDENTIFIER                                      # readVariable
  ;

OP_PLUS  : '+';
OP_MINUS : '-';
OP_MULT  : '*';
OP_DIV   : '/';
OP_ASSIGN: '=';

LPAR       : '(';
RPAR       : ')';
EOS        : ';'; // End of statement
OPEN_BLOCK : '{';
CLOSE_BLOCK: '}';
COMMA      : ',';

LET: 'let';

INTEGER: [0-9]+;
IDENTIFIER: [A-Za-z_][A-Za-z0-9]*;

WHITESPACE: [ \r\n\t]+ -> skip;
