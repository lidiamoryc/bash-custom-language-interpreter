grammar mash;

program : statement* EOF;

statement : echo_function
          | var_declar
          | assignment
          | if_statement
          | while_statement
          | for_statement
          | function_declar
          | return_statement
          | increment_statement
          | decrement_statement;

increment_statement : IDENTIFIER '++' ;
decrement_statement : IDENTIFIER '--' ;

echo_function : 'echo' (expression | IDENTIFIER);

expression : '$((' arithmetic_expression '))'
           | string_expression
           | logical_expression
           | int_expression
           | IDENTIFIER
           | function_call;

string_expression : STRING;
int_expression: INTEGER;

arithmetic_expression : additive_expression;

additive_expression : multiplicative_expression
                     | additive_expression '+' multiplicative_expression
                     | additive_expression '-' multiplicative_expression;

multiplicative_expression : primary_expression
                           | multiplicative_expression '*' primary_expression
                           | multiplicative_expression '/' primary_expression;

primary_expression : INTEGER | IDENTIFIER | '(' additive_expression ')' | function_call;

logical_expression : comparison_expression
                    | logical_expression 'and' logical_expression
                    | logical_expression 'or' logical_expression
                    | 'not' logical_expression
                    | '(' logical_expression ')'
                    | 'true'
                    | 'false';

comparison_expression : arithmetic_expression ('<' | '>' | '==' | '!=') arithmetic_expression
                      | IDENTIFIER ('<' | '>' | '==' | '!=') IDENTIFIER;

var_declar : type IDENTIFIER ('=' (expression | IDENTIFIER))?;

type : 'string_var' | 'int_var';

assignment : IDENTIFIER '=' (expression | IDENTIFIER);

while_statement : 'while' '(' logical_expression ')' '{' statement* '}';

for_statement : 'for' '(' (assignment | var_declar) ';' logical_expression ';' (increment_statement | decrement_statement | assignment) ')' '{' statement* '}';

if_statement : 'if' '(' logical_expression ')' '{' statement* '}' elif_block* else_block?;

elif_block : 'elif' '(' logical_expression ')' '{' statement* '}';

else_block : 'else' '{' statement* '}';

function_declar : 'function' IDENTIFIER '(' parameters? ')' return_type? '{' statement_list '}';

parameters : parameter (',' parameter)*;
parameter : type IDENTIFIER;

return_type : '->' type;

function_call : IDENTIFIER '(' arguments? ')';

arguments : expression* (',' expression)*;

return_statement : 'return' expression ;

statement_list : statement* ;

INTEGER : DIGIT+;
IDENTIFIER : LETTER (LETTER | DIGIT)*;
STRING : '"' (LETTER | ' ')*? '"';
DIGIT : [0-9]+;
LETTER : [a-zA-Z_]+;
COMMENT : '#' .*? '\n' -> skip;
WS : [ \t\n\r]+ -> skip;
