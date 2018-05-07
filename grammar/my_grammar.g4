grammar my_grammar;

@header{
from .sol import *
}

// file
script
    : stmt*;

// lists
basic_list
    : LSQPAR (expr COMMA)* (expr | COMMA)? RSQPAR;
by_slice_list
    : expr COLON expr COLON expr
    | expr COLON expr;

// logical expressions
comparator
    : LESS
    | GREATER
    | DOUBLEEQUAL
    | LESSEQUAL
    | GREATEREQUAL
    | NOTEQUAL;
or_test
    : and_test ('or' and_test)?;
and_test
    : not_test ('not' not_test)?;
not_test
    : ('not' not_test)
    | comparison;
comparison
    : expr comparator expr
    | expr;

// literal
number
    : NON_NEGATIVE_INTEGER
    | FLOAT;

simple_literal
    : STRING
    | NON_NEGATIVE_INTEGER
    | number
    | BOOL
    | NONE
    | basic_list;

// parameter set
parameter_set_stmt
    : 'parameter_set' NAME LBRACE parameter_set_suite RBRACE;
where_expr
    : by_slice_list 'where' (NAME | simple_lambda);
simple_lambda
    : 'lambda' NAME COLON expr;

// assignment
assignment
    : NAME EQUAL (expr | by_slice_list);
assignment_stmt
    : assignment SEMI;
assignment_suite
    : assignment_stmt*;
where_assignment
    : NAME EQUAL where_expr;
where_assignemnt_stmt
    : where_assignment SEMI;
parameter_set_suite
    : (assignment_stmt | where_assignemnt_stmt)*;

// expression
expr
    returns[y]
    locals [x]
    @init{
Namespace.fun()
    }
    @after {
y = x
print(y)
    }
    : term {x = $term.text}((PLUS term {x += $term.text}) | (MINUS term {x -= $term.text}))*;
term
    : factor ((STAR | SLASH | PERCENT | '//') factor)*;
factor
    : (PLUS | MINUS) factor
    | power;
power
    : atom_expr (DOUBLESTAR factor)*;
atom_expr
    : atom trailer*;
atom
    : NAME
    | simple_literal;
trailer
    : LPAR arglist? RPAR
    | LSQPAR NON_NEGATIVE_INTEGER RSQPAR
    | DOT NAME;
arglist
    : argument (COMMA argument)* COMMA?;
argument
    : simple_literal
    | NAME
    | (NAME EQUAL expr);

// compound statements
compound_stmt
    : for_stmt
    | while_stmt
    | if_stmt;
for_stmt
    : 'for' LPAR NAME 'in' expr RPAR LBRACE loop_suite RBRACE;
while_stmt
    : 'while' LPAR or_test RPAR LBRACE loop_suite RBRACE;
loop_suite
    : ('init' LBRACE assignment_suite RBRACE)? suite;
if_stmt
    : 'if' LPAR or_test RPAR LBRACE suite RBRACE else_stmt?;
else_stmt
    : 'else' (LBRACE suite RBRACE | if_stmt);

// statements
stmt
    : context_stmt
    | funcdef_stmt
    | parameter_set_stmt;
context_stmt
    : compound_stmt
    | simple_stmt;
simple_stmt
    : import_stmt
    | expr SEMI
    | assignment_stmt;
import_stmt
    : 'import' dotted_name SEMI;
dotted_name
    : NAME
    | NAME ('.' | '..') dotted_name;

// functions
funcdef_stmt
    : 'def' NAME LPAR arglist RPAR LBRACE suite RBRACE;
suite
    : context_stmt*;

// simple tokens

LPAR            : '(';
RPAR            : ')';
LSQPAR          : '[';
RSQPAR          : ']';
LBRACE          : '{';
RBRACE          : '}';
COMMA           : ',';
SEMI            : ';';
PLUS            : '+';
MINUS           : '-';
DOUBLESTAR      : '**';
STAR            : '*';
SLASH           : '/';
LESS            : '<';
LESSEQUAL       : '<=';
GREATER         : '>';
GREATEREQUAL    : '>=';
EQUAL           : '=';
NOTEQUAL        : '!=';
DOUBLEEQUAL     : '==';
DOT             : '.';
PERCENT         : '%';
COLON           : ':';
BOOL            : 'True' | 'False';
NONE            : 'None';

WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '#' ~[\n]* -> skip;

// compound tokens

// numbers
fragment
NON_ZERO_DIGIT
    : [1-9];
fragment
DIGIT
    : NON_ZERO_DIGIT
    | '0';
NON_NEGATIVE_INTEGER
    : NON_ZERO_DIGIT DIGIT*
    | '0';
FLOAT
    : NON_NEGATIVE_INTEGER '.' DIGIT+;

// strings
fragment
CHAR
    : [a-zA-Z];
fragment
STRING_CHAR
    : ~["'\\]
    | '\\' STRING_CHAR
    | '\\' '"'
    | '\\' '\'';
STRING
    : '"' STRING_CHAR* '"'
    | '\'' STRING_CHAR* '\'';
NAME
    : (CHAR | '_') (NON_NEGATIVE_INTEGER | CHAR | '_')*;