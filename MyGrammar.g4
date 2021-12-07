grammar MyGrammar;

compileUnit
  : expr EOF    
  ;

expr
  : value=INTEGER                              # numberExpr
  | LPAR expr RPAR                             # parenExpr
  | left=expr op=(OP_DIV|OP_MULT)   right=expr # infixExpr
  | left=expr op=(OP_PLUS|OP_MINUS) right=expr # infixExpr
  ;

INTEGER: [0-9]+;

OP_PLUS : '+';
OP_MINUS: '-';
OP_MULT : '*';
OP_DIV  : '/';

LPAR: '(';
RPAR: ')';

WHITESPACE: [ \r\n\t]+ -> skip;
