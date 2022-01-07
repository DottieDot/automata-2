grammar MyGrammar;
compile_unit
  : scoped_expr  
  ;

scoped_expr
  : (expr EOS)* final_expr=expr?
  ;

expr
  : INTEGER                                         # int_literal
  | FLOAT                                           # float_literal
  | (TRUE|FALSE)                                    # bool_literal
  | NONE                                            # none_literal
  | NAN                                             # nan_literal
  | FUNCTION ident=IDENTIFIER? LPAR (IDENTIFIER(COMMA IDENTIFIER)*)? RPAR OPEN_BLOCK scoped_expr CLOSE_BLOCK # function_decl
  | ident=IDENTIFIER LPAR (expr(COMMA expr)*)? RPAR # function_call
  | LET IDENTIFIER OP_ASSIGN expr                   # define_variable
  | IDENTIFIER OP_ASSIGN expr                       # assign_variable
  | IF expr OPEN_BLOCK scoped_expr CLOSE_BLOCK      # if_statement
  | LPAR expr RPAR                                  # parentheses
  | NOT expr                                        # not
  | left=expr op=(OP_DIV|OP_MULT)       right=expr  # multiply_divide
  | left=expr op=(OP_PLUS|OP_MINUS)     right=expr  # add_subtract
  | left=expr op=(GT|GE|LT|LE|EQ|NEQ)   right=expr  # comparison
  | left=expr op=(AND|OR)               right=expr  # conjunction
  | IDENTIFIER                                      # read_variable
  ;

AND: '&&';
OR : '||';
GE : '>=';
LE : '<=';
EQ : '==';
NEQ: '!=';
GT : '>' ;
LT : '<' ;
NOT: '!' ;

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

LET  : 'let';
IF   : 'if';
WHILE: 'while';
FOR  : 'for';

FUNCTION: 'fn';

TRUE: 'true';
FALSE: 'false';
NONE: 'None';
NAN: 'NaN';
INTEGER: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
IDENTIFIER: [A-Za-z_][A-Za-z0-9]*;

WHITESPACE: [ \r\n\t]+ -> skip;
