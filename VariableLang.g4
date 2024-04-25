grammar VariableLang;

// Reguły parsera
program : statement* EOF;

statement
    : varDeclaration
    | assignment
    ;

varDeclaration : 'int_var' IDENTIFIER ';' ;
assignment : IDENTIFIER '=' expr ';' ;

expr
    : expr '+' expr  // Przerobić na zaimplementowane działania
    | expr '-' expr
    | IDENTIFIER
    | INT
    ;

// Reguły leksera
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ; // Ignoruj białe znaki
