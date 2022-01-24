grammar MyGrammar;
compile_unit
  : scoped_expr EOF
  ;

scoped_expr
  : (expr EOS)* final_expr=expr?
  ;

if_statement: IF expr OPEN_BLOCK scoped_expr CLOSE_BLOCK;
else_if_statement: ELSE IF expr OPEN_BLOCK scoped_expr CLOSE_BLOCK;
else_statement: ELSE OPEN_BLOCK scoped_expr CLOSE_BLOCK;

matrix_statements: (matrix_expr EOS)*;

matrix_expr
  : IDENTIFIER                                                # read_dummy_matrix
  | matrix_expr '^-1'                                         # inverse_dummy_matrix
  | matrix_expr '^T'                                          # transpose_dummy_matrix
  | lhs=matrix_expr OP_PLUS rhs=matrix_expr                   # add_dummy_matrix
  | lhs=matrix_expr OP_MULT rhs=matrix_expr                   # mult_dummy_matrix
  | ((lhs=INTEGER OP_MULT rhs=matrix_expr) | (lhs=IDENTIFIER matrix_expr rhs=INTEGER)) # mult_dummy_matrix_int
  | IDENTIFIER LBR x=INTEGER COMMA y=INTEGER RBR              # read_dummy_matrix_field
  | LET IDENTIFIER = MATRIX LBR w=INTEGER COMMA h=INTEGER RBR # define_dummy_matrix
  ;

expr
  // Put dummy matrix stuff in a seperate block to avoid breaking the grammar
  : MATRIX OPEN_BLOCK matrix_statements CLOSE_BLOCK # matrix_block

  | INTEGER                                         # int_literal
  | FLOAT                                           # float_literal
  | (TRUE|FALSE)                                    # bool_literal
  | NONE                                            # none_literal
  | NAN                                             # nan_literal
  | LPAR expr RPAR                                  # parentheses
  | MATRIX LBR w=expr COMMA h=expr RBR              # matrix_defintion
  | NOT expr                                        # not
  | fn_expr=expr LPAR (expr(COMMA expr)*)? RPAR     # anonymous_function_call
  | left=expr op=(OP_DIV|OP_MULT)       right=expr  # multiply_divide
  | left=expr op=(OP_PLUS|OP_MINUS)     right=expr  # add_subtract
  | left=expr op=(GT|GE|LT|LE|EQ|NEQ)   right=expr  # comparison
  | left=expr op=(AND|OR)               right=expr  # conjunction
  | if_statement (else_if_statement)* (else_statement)?  # if_expr
  | WHILE expr OPEN_BLOCK scoped_expr CLOSE_BLOCK   # while_statement
  | REPEAT OPEN_BLOCK scoped_expr CLOSE_BLOCK UNTIL expr # repeat_until
  | LET IDENTIFIER OP_ASSIGN expr                   # define_variable
  | IDENTIFIER OP_ASSIGN expr                       # assign_variable
  | IDENTIFIER LBR x=expr COMMA y=expr RBR OP_ASSIGN value=expr # assign_matrix_field
  | FUNCTION ident=IDENTIFIER? LPAR (IDENTIFIER(COMMA IDENTIFIER)*)? RPAR OPEN_BLOCK scoped_expr CLOSE_BLOCK # function_decl
  | ident=IDENTIFIER LPAR (expr(COMMA expr)*)? RPAR # function_call
  | PRINT expr                                      # print_statement
  | IDENTIFIER                                      # read_variable
  | IDENTIFIER LBR x=expr COMMA y=expr RBR    # read_matrix_field
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
LBR        : '[';
RBR        : ']';
EOS        : ';'; // End of statement
OPEN_BLOCK : '{';
CLOSE_BLOCK: '}';
COMMA      : ',';

PRINT: '$';

LET  : 'let';
IF   : 'if';
ELSE : 'else';
WHILE: 'while';
FOR  : 'for';
REPEAT: 'repeat';
UNTIL: 'until';
MATRIX: 'matrix';

FUNCTION: 'fn';

TRUE: 'true';
FALSE: 'false';
NONE: 'None';
NAN: 'NaN';
INTEGER: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
IDENTIFIER: [A-Za-z_][A-Za-z0-9_]*;

WHITESPACE: [ \r\n\t]+ -> skip;
