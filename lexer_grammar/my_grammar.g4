grammar my_grammar;

NAME            : [a-zA-Z] [a-zA-Z0-9_]*;
NUMBER          : NON_NEGATIVE_INTEGER | FLOAT;
STRING          : '"' (~('"') | ('\\' '"'))* '"';
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
DOUBLEEQUAL     : '==';
DOT             : '.';
PERCENT         : '%';
COLON           : ':';

WS              : [ \t\r\n]+ -> skip ;
COMMENT         : '#' ~[\n]* -> skip;

fragment
NON_ZERO_DIGIT: [1-9];
fragment
DIGIT: NON_ZERO_DIGIT | '0';
fragment
NON_NEGATIVE_INTEGER: (NON_ZERO_DIGIT DIGIT*) | '0';
fragment
FLOAT: NON_NEGATIVE_INTEGER '.' DIGIT+;