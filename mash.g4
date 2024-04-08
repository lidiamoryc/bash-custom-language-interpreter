grammar mash;
program :	(var_declar | operation | loop | function | logical_operation)*;

var_declar :	type identifier '=' value;
type    : 'string_var'
        | 'array_var'
        | 'int_var'
        | 'bool_var'
        ;

value   : string_value
        | int_value
        | array_value
        | bool_value
        ;

string_value : '"' .*? '"';
array_value  : '(' value (',' value)* ')';
int_value    : INTEGER;
bool_value   : 'true'
             | 'false'
             ;

operation   : arithmetic_operation
            | echo_statement
            ;

arithmetic_operation : '$((' expression '))';

expression  : value (sign value)*;

sign    : '+'
        | '-'
        | '*'
        ;

logical_operation : 'if' condition 'then' operation 'else' operation 'fi';

condition   : '[' bool_value ('==' | '!=') bool_value ']'
            | '[' (value | identifier) logic_operator (value | identifier) ']'
            ;

logic_operator  : '=='
                | '!='
                | '<'
                | '>'
                | '&&'
                | '||'
                ;

loop    : for_loop
        | while_loop
        ;

for_loop :  'for' identifier 'in' array_value 'do' operation 'done';

while_loop :    'while' condition 'do' operation 'done';

function    : function_definition
            | function_call
            ;

function_definition :   identifier '(' ')' '{' operation '}';

function_call : identifier arguments;

arguments : value (value)*;

echo_statement :    'echo' sentence;

sentence :  value (value)*;

INTEGER : DIGIT+;

identifier : LETTER (LETTER | DIGIT)*;

DIGIT : [0-9]+;
LETTER : [a-zA-Z_]+;
COMMENT : '#' .*? '\n' -> skip;
WS : [ \t\n\r]+ -> skip;

string_var      : 'string_var';
array_var       : 'array_var';
int_var         : 'int_var';
bool_var        : 'bool_var';
