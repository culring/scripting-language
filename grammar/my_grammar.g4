grammar my_grammar;

@header {
from operations.and_test import AndTest
from operations.arglist import Arglist
from operations.argument import Argument
from operations.assignment import Assignment
from operations.assignment_stmt import AssignmentStmt
from operations.assignment_suite import AssignmentSuite
from operations.atom import Atom
from operations.atom_expr import AtomExpr
from operations.basic_list import BasicList
from operations.by_slice_list import BySliceList
from operations.comparator import Comparator
from operations.comparison import Comparison
from operations.compound_stmt import CompoundStmt
from operations.context_stmt import ContextStmt
from operations.expr import Expr
from operations.else_stmt import ElseStmt
from operations.factor import Factor
from operations.for_stmt import ForStmt
from operations.funcdef_stmt import FuncdefStmt
from operations.if_stmt import IfStmt
from operations.import_stmt import ImportStmt
from operations.loop_suite import LoopSuite
from operations.not_test import NotTest
from operations.number import Number
from operations.operation import Operation
from operations.or_test import OrTest
from operations.parameter_set_stmt import ParameterSetStmt
from operations.parameter_set_suite import ParameterSetSuite
from operations.power import Power
from operations.script import Script
from operations.simple_lambda import SimpleLambda
from operations.simple_literal import SimpleLiteral
from operations.simple_stmt import SimpleStmt
from operations.stmt import Stmt
from operations.suite import Suite
from operations.symbol_table import SymbolTable
from operations.term import Term
from operations.trailer import Trailer
from operations.where_assignment import WhereAssignment
from operations.where_assignment_stmt import WhereAssignmentStmt
from operations.where_expr import WhereExpr
from operations.while_stmt import WhileStmt
}

// file
script
    returns [myObj]
    : (stmts+=stmt)* {$myObj = Script(tuple([stmt.myObj for stmt in $stmts]))};

// lists
basic_list
    returns [myObj]
    @after{
$myObj = BasicList(tuple([expr.myObj for expr in $exprs]))
    }
    : LSQPAR (exprs+=expr COMMA)* (exprs+=expr | COMMA)? RSQPAR;
by_slice_list
    returns [myObj]
    : e1=expr COLON e2=expr COLON e3=expr {$myObj = BySliceList($e1.myObj, $e2.myObj, $e3.myObj)}
    | e1=expr COLON e2=expr {$myObj = BySliceList($e1.myObj, $e2.myObj)};

// logical expressions
comparator
    returns [myObj]
    : LESS {$myObj = Comparator(Comparator.Type.LESS)}
    | GREATER {$myObj = Comparator(Comparator.Type.GREATER)}
    | DOUBLEEQUAL {$myObj = Comparator(Comparator.Type.DOUBLEEQUAL)}
    | LESSEQUAL {$myObj = Comparator(Comparator.Type.LESSEQUAL)}
    | GREATEREQUAL {$myObj = Comparator(Comparator.Type.GREATEREQUAL)}
    | NOTEQUAL {$myObj = Comparator(Comparator.Type.NOTEQUAL)};
or_test
    returns [myObj]
    @after{
if $y:
    $myObj = OrTest($x.myObj, $y[0].myObj)
else:
    $myObj = OrTest($x.myObj)
    }
    : x=and_test ('or' y+=and_test)?;
and_test
    returns [myObj]
    @after{
if $y:
    $myObj = OrTest($x.myObj, $y[0].myObj)
else:
    $myObj = OrTest($x.myObj)
    }
    : x=not_test ('not' y+=not_test)?;
not_test
    returns [myObj]
    : ('not' not_test) {$myObj = NotTest.createFromNonTest($not_test.myObj)}
    | comparison {$myObj = NotTest.createFromComparison($comparison.myObj)};
comparison
    returns [myObj]
    : e1=expr c=comparator e2=expr {$myObj = Comparison.createFromTwoExprs($e1.myObj, $c.myObj, $e2.myObj)}
    | expr {$myObj = Comparison.createFromExpr($expr.myObj)};

// literal
number
    returns [myObj]
    : NON_NEGATIVE_INTEGER {$myObj = Number.createNonNegativeInteger($NON_NEGATIVE_INTEGER.text)}
    | FLOAT {$myObj = Number.createFloat($FLOAT.text)};

simple_literal
    returns [myObj]
    : STRING {$myObj = SimpleLiteral.createFromString($STRING.text)}
    | number {$myObj = SimpleLiteral.createFromNumber($number.myObj)}
    | BOOL {$myObj = SimpleLiteral.createFromBool($BOOL.text)}
    | NONE {$myObj = SimpleLiteral.createFromNone()}
    | basic_list {$myObj = SimpleLiteral.createFromBasicList($basic_list.myObj)};

// parameter set
parameter_set_stmt
    : 'parameter_set' NAME LBRACE parameter_set_suite RBRACE;
where_expr
    : by_slice_list 'where' (NAME | simple_lambda);
simple_lambda
    : 'lambda' NAME COLON expr;

// assignment
assignment
    returns [myObj]
    : NAME EQUAL expr {$myObj = Assignment.createFromExpr($NAME.text, $expr.myObj)}
    | NAME EQUAL by_slice_list {$myObj = Assignment.createFromBySliceList($NAME.text, $by_slice_list.myObj)};
assignment_stmt
    returns [myObj]
    : assignment SEMI {$myObj = AssignmentStmt($assignment.myObj)};
assignment_suite
    returns [myObj]
    @after{
$myObj = AssignmentSuite(tuple([stmt.myObj for stmt in $s]))
    }
    : (s+=assignment_stmt)*;
where_assignment
    : NAME EQUAL where_expr;
where_assignemnt_stmt
    : where_assignment SEMI;
parameter_set_suite
    : (assignment_stmt | where_assignemnt_stmt)*;

// expression
expr
    returns [myObj]
    @after {
$myObj = Expr($t.myObj, tuple(zip([operator.text for operator in $operators], [operand.myObj for operand in $operands])))
    }
    : t=term (operators+=(PLUS | MINUS) operands+=term )*;
term
    returns [myObj]
    @after {
$myObj = Term($f.myObj, tuple(zip([operator.text for operator in $operators], [operand.myObj for operand in $operands])))
    }
    : f=factor (operators+=(STAR | SLASH | PERCENT | '//') operands+=factor)*;
factor
    returns [myObj]
    : sign=(PLUS | MINUS) factor {$myObj = Factor.createFromFactor($sign.text, $factor.myObj)}
    | power {$myObj = Factor.createFromPower($power.myObj)};
power
    returns [myObj]
    locals [x]
    : a=atom_expr (DOUBLESTAR factor {$x = $factor.myObj})?
{if $x:
    $myObj = Power($a.myObj, $x)
else:
    $myObj = Power($a.myObj)};
atom_expr
    returns [myObj]
    @after{
$myObj = AtomExpr($a.myObj, tuple([trailer.myObj for trailer in $trailers]))
    }
    : a=atom (trailers+=trailer)*;
atom
    returns [myObj]
    : NAME {$myObj = Atom.createFromName($NAME.text)}
    | simple_literal {$myObj = Atom.createFromSimpleLiteral($simple_literal.myObj)};
trailer
    returns [myObj]
    : LPAR arglist? RPAR {$myObj = Trailer.createFromArglist($arglist.myObj)}
    | LSQPAR NON_NEGATIVE_INTEGER RSQPAR {$myObj = Trailer.createFromAccess($NON_NEGATIVE_INTEGER.text)}
    | DOT NAME {$myObj = Trailer.createFromDotName($NAME.text)};
arglist
    returns [myObj]
    : arg=expr (COMMA args+=expr)* COMMA? {$myObj = Arglist(tuple([$arg.myObj] + [argument.myObj for argument in $args]))};
//argument
//    returns [myObj]
//    : simple_literal {$myObj = Argument.createFromSimpleLiteral($simple_literal.myObj)}
//    | NAME {$myObj = Argument.createFromName($NAME.text)};

// compound statements
compound_stmt
    returns [myObj]
    : for_stmt {$myObj = CompoundStmt.createFromForStmt($for_stmt.myObj)}
    | while_stmt
    | if_stmt {$myObj = CompoundStmt.createFromIfStmt($if_stmt.myObj)};
for_stmt
    returns [myObj]
    : 'for' LPAR NAME 'in' expr RPAR LBRACE loop_suite RBRACE {$myObj = ForStmt($NAME.text, $expr.myObj, $loop_suite.myObj)};
while_stmt
    : 'while' LPAR or_test RPAR LBRACE loop_suite RBRACE;
loop_suite
    returns [myObj]
    @after{
if $az:
    $myObj = LoopSuite(contextStmts=tuple([c.myObj for c in $ctxs]), assignmentSuite=$az[0].myObj)
else:
    $myObj = LoopSuite(contextStmts=tuple([c.myObj for c in $ctxs]))
    }
    : ('init' LBRACE az+=assignment_suite RBRACE)? (ctxs+=context_stmt)*;
if_stmt
    returns [myObj]
    : 'if' LPAR or_test RPAR LBRACE suite RBRACE (e+=else_stmt)?
    {$myObj = IfStmt($or_test.myObj, $suite.myObj, $e[0].myObj if $e else None)};
else_stmt
    returns [myObj]
    : 'else' LBRACE suite RBRACE {$myObj = ElseStmt.createFromSuite($suite.myObj)}
    | 'else' if_stmt {$myObj = ElseStmt.createFromIfStmt($if_stmt.myObj)};

// statements
stmt
    returns [myObj]
    : context_stmt {$myObj = ContextStmt.createFromSimpleStmt($context_stmt.myObj)}
    | funcdef_stmt
    | parameter_set_stmt;
context_stmt
    returns [myObj]
    : compound_stmt {$myObj = ContextStmt.createFromCompoundStmt($compound_stmt.myObj)}
    | simple_stmt {$myObj = ContextStmt.createFromSimpleStmt($simple_stmt.myObj)};
simple_stmt
    returns [myObj]
    : import_stmt
    | expr SEMI {$myObj = SimpleStmt.createFromExpr($expr.myObj)}
    | a=assignment_stmt {$myObj = AssignmentStmt($a.myObj)};
import_stmt
    : 'import' dotted_name SEMI;
dotted_name
    : NAME
    | NAME ('.' | '..') dotted_name;

// functions
funcdef_stmt
    : 'def' NAME LPAR arglist RPAR LBRACE suite RBRACE;
suite
    returns [myObj]
    @after{
$myObj = Suite(tuple([c.myObj for c in $ctxs]))
    }
    : (ctxs+=context_stmt)*;

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