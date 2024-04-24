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





//program :	(var_declar |array_declaration| operation | loop | function | logical_operation | print_string_statement)*;
//
//var_declar :	type identifier '=' value;
//array_declaration: array_var type identifier '=' array_value; // ZMIENIONE nw, czy dobrze
//// ale dziala lepiej niz wczensiej wiec
////mysle ze w porzadku jest
//
//type    : 'string_var' //| 'array_var'
//        | 'int_var'
//        | 'bool_var'
//        ;
//
//value   : string_value
//        | int_value //        | array_value
//        | bool_value
//        ;
//
////string_value : '"' *? '"';
//string_value: '"' (LETTER | DIGIT |' ')* '"';
// //ZMIENIONE i działa, I guess
//array_value  : '(' value (',' value)* ')';
//
//int_value    : INTEGER;
//bool_value   : 'true'
//             | 'false'
//             ;
//
//operation   : arithmetic_operation
//            | echo_statement
//            ;
//
//arithmetic_operation : '$((' expression '))';
//
//expression  : value (sign value)*;
//
//sign    : '+'
//        | '-'
//        | '*'
//        ;
//
//logical_operation : 'if' condition 'then' operation 'else' operation 'fi';
//
//condition   : '[' bool_value ('==' | '!=') bool_value ']'
//            | '[' (value | identifier) logic_operator (value | identifier) ']'
//            ;
//
//logic_operator  : '=='
//                | '!='
//                | '<'
//                | '>'
//                | '&&'
//                | '||'
//                ;
//
//loop    : for_loop
//        | while_loop
//        ;
//
//for_loop :  'for' identifier 'in' array_value 'do' operation 'done';
//
//while_loop :    'while' condition 'do' operation 'done';
//
//function    : function_definition
//            | function_call
//            ;
//
//function_definition :   identifier '(' ')' '{' operation? '}'; // POPRAWIONE na operation? - mozliwosc pustej funckji
//
//function_call : identifier arguments;
//
//arguments : value (value)*;
//
//echo_statement :    'echo' sentence;
//
//sentence :  value (value)*;
//
//INTEGER : DIGIT+;
//
//identifier : LETTER (LETTER | DIGIT)*;
//
//DIGIT : [0-9]+;
//LETTER : [a-zA-Z_]+;
//COMMENT : '#' .*? '\n' -> skip;
//WS : [ \t\n\r]+ -> skip;
//WS_not_skip : [ ];
//
//string_var      : 'string_var';
//array_var       : 'array_var';
//int_var         : 'int_var';
//bool_var        : 'bool_var';
//
//print_string_statement: 'print' string_value;//value (value)*;