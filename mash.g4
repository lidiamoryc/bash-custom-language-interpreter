grammar mash;

program : statement* EOF;

statement : echo_function | var_declar;

echo_function : 'echo' expression;

expression : '$((' arithmetic_expression '))'| string_expression | logical_expression;

string_expression : STRING;

//numeric_expression : INTEGER | '$((' INTEGER '+' INTEGER '))';

arithmetic_expression : additive_expression;

// Additive expression (addition and subtraction) has lower precedence
additive_expression : multiplicative_expression
                     | additive_expression '+' multiplicative_expression
                     | additive_expression '-' multiplicative_expression;

// Multiplicative expression (multiplication and division) has higher precedence
multiplicative_expression : primary_expression
                           | multiplicative_expression '*' primary_expression
                           | multiplicative_expression '/' primary_expression;

// Primary expression includes integers and nested expressions
primary_expression : INTEGER
                    | '(' additive_expression ')';

logical_expression : comparison_expression
                    | logical_expression 'and' logical_expression
                    | logical_expression 'or' logical_expression
                    | 'not' logical_expression
                    | '(' logical_expression ')'
                    | 'true'
                    | 'false';

comparison_expression : arithmetic_expression ('<' | '>' | '==' | '!=') arithmetic_expression;

//arithmetic_operation : '$((' numeric_expression '))';

//numeric_expression  : INTEGER
//                    | '(' numeric_expression ')'
//                    | numeric_expression '+' numeric_expression
//                    | numeric_expression '-' numeric_expression
//                    | numeric_expression '*' numeric_expression
//                    | numeric_expression '/' numeric_expression
//                    ;

type    : 'string_var'
        | 'int_var'
        | 'bool_var'
        ;



var_declar :	type IDENTIFIER '=' expression | type IDENTIFIER;





INTEGER : DIGIT+;

IDENTIFIER : LETTER (LETTER | DIGIT)*;

STRING : '"' (LETTER | ' ')*? '"';
DIGIT : [0-9]+;
LETTER : [a-zA-Z_]+;
COMMENT : '#' .*? '\n' -> skip;
WS : [ \t\n\r]+ -> skip;
