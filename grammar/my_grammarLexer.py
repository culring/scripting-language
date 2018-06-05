# Generated from my_grammar.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


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
from operations.factor import Factor
from operations.for_stmt import ForStmt
from operations.funcdef_stmt import FuncdefStmt
from operations.if_stmt import IfStmt
from operations.import_stmt import ImportStmt
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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u0147\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u00f1\n(\3)\3)\3)\3")
        buf.write(")\3)\3*\6*\u00f9\n*\r*\16*\u00fa\3*\3*\3+\3+\7+\u0101")
        buf.write("\n+\f+\16+\u0104\13+\3+\3+\3,\3,\3-\3-\5-\u010c\n-\3.")
        buf.write("\3.\7.\u0110\n.\f.\16.\u0113\13.\3.\5.\u0116\n.\3/\3/")
        buf.write("\3/\6/\u011b\n/\r/\16/\u011c\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u0128\n\61\3\62\3\62\7\62\u012c")
        buf.write("\n\62\f\62\16\62\u012f\13\62\3\62\3\62\3\62\7\62\u0134")
        buf.write("\n\62\f\62\16\62\u0137\13\62\3\62\5\62\u013a\n\62\3\63")
        buf.write("\3\63\5\63\u013e\n\63\3\63\3\63\3\63\7\63\u0143\n\63\f")
        buf.write("\63\16\63\u0146\13\63\2\2\64\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2[-]._\2a\2c")
        buf.write("/e\60\3\2\7\5\2\13\f\17\17\"\"\3\2\f\f\3\2\63;\4\2C\\")
        buf.write("c|\5\2$$))^^\2\u0153\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2c\3\2\2\2\2e\3\2\2\2\3g\3\2\2\2\5j\3\2\2\2\7n\3\2\2")
        buf.write("\2\t|\3\2\2\2\13\u0082\3\2\2\2\r\u0089\3\2\2\2\17\u008c")
        buf.write("\3\2\2\2\21\u0090\3\2\2\2\23\u0093\3\2\2\2\25\u0099\3")
        buf.write("\2\2\2\27\u009e\3\2\2\2\31\u00a1\3\2\2\2\33\u00a6\3\2")
        buf.write("\2\2\35\u00ad\3\2\2\2\37\u00b0\3\2\2\2!\u00b4\3\2\2\2")
        buf.write("#\u00b6\3\2\2\2%\u00b8\3\2\2\2\'\u00ba\3\2\2\2)\u00bc")
        buf.write("\3\2\2\2+\u00be\3\2\2\2-\u00c0\3\2\2\2/\u00c2\3\2\2\2")
        buf.write("\61\u00c4\3\2\2\2\63\u00c6\3\2\2\2\65\u00c8\3\2\2\2\67")
        buf.write("\u00cb\3\2\2\29\u00cd\3\2\2\2;\u00cf\3\2\2\2=\u00d1\3")
        buf.write("\2\2\2?\u00d4\3\2\2\2A\u00d6\3\2\2\2C\u00d9\3\2\2\2E\u00db")
        buf.write("\3\2\2\2G\u00de\3\2\2\2I\u00e1\3\2\2\2K\u00e3\3\2\2\2")
        buf.write("M\u00e5\3\2\2\2O\u00f0\3\2\2\2Q\u00f2\3\2\2\2S\u00f8\3")
        buf.write("\2\2\2U\u00fe\3\2\2\2W\u0107\3\2\2\2Y\u010b\3\2\2\2[\u0115")
        buf.write("\3\2\2\2]\u0117\3\2\2\2_\u011e\3\2\2\2a\u0127\3\2\2\2")
        buf.write("c\u0139\3\2\2\2e\u013d\3\2\2\2gh\7q\2\2hi\7t\2\2i\4\3")
        buf.write("\2\2\2jk\7p\2\2kl\7q\2\2lm\7v\2\2m\6\3\2\2\2no\7r\2\2")
        buf.write("op\7c\2\2pq\7t\2\2qr\7c\2\2rs\7o\2\2st\7g\2\2tu\7v\2\2")
        buf.write("uv\7g\2\2vw\7t\2\2wx\7a\2\2xy\7u\2\2yz\7g\2\2z{\7v\2\2")
        buf.write("{\b\3\2\2\2|}\7y\2\2}~\7j\2\2~\177\7g\2\2\177\u0080\7")
        buf.write("t\2\2\u0080\u0081\7g\2\2\u0081\n\3\2\2\2\u0082\u0083\7")
        buf.write("n\2\2\u0083\u0084\7c\2\2\u0084\u0085\7o\2\2\u0085\u0086")
        buf.write("\7d\2\2\u0086\u0087\7f\2\2\u0087\u0088\7c\2\2\u0088\f")
        buf.write("\3\2\2\2\u0089\u008a\7\61\2\2\u008a\u008b\7\61\2\2\u008b")
        buf.write("\16\3\2\2\2\u008c\u008d\7h\2\2\u008d\u008e\7q\2\2\u008e")
        buf.write("\u008f\7t\2\2\u008f\20\3\2\2\2\u0090\u0091\7k\2\2\u0091")
        buf.write("\u0092\7p\2\2\u0092\22\3\2\2\2\u0093\u0094\7y\2\2\u0094")
        buf.write("\u0095\7j\2\2\u0095\u0096\7k\2\2\u0096\u0097\7n\2\2\u0097")
        buf.write("\u0098\7g\2\2\u0098\24\3\2\2\2\u0099\u009a\7k\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7k\2\2\u009c\u009d\7v\2\2\u009d")
        buf.write("\26\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7h\2\2\u00a0")
        buf.write("\30\3\2\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7n\2\2\u00a3")
        buf.write("\u00a4\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\32\3\2\2\2\u00a6")
        buf.write("\u00a7\7k\2\2\u00a7\u00a8\7o\2\2\u00a8\u00a9\7r\2\2\u00a9")
        buf.write("\u00aa\7q\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7v\2\2\u00ac")
        buf.write("\34\3\2\2\2\u00ad\u00ae\7\60\2\2\u00ae\u00af\7\60\2\2")
        buf.write("\u00af\36\3\2\2\2\u00b0\u00b1\7f\2\2\u00b1\u00b2\7g\2")
        buf.write("\2\u00b2\u00b3\7h\2\2\u00b3 \3\2\2\2\u00b4\u00b5\7*\2")
        buf.write("\2\u00b5\"\3\2\2\2\u00b6\u00b7\7+\2\2\u00b7$\3\2\2\2\u00b8")
        buf.write("\u00b9\7]\2\2\u00b9&\3\2\2\2\u00ba\u00bb\7_\2\2\u00bb")
        buf.write("(\3\2\2\2\u00bc\u00bd\7}\2\2\u00bd*\3\2\2\2\u00be\u00bf")
        buf.write("\7\177\2\2\u00bf,\3\2\2\2\u00c0\u00c1\7.\2\2\u00c1.\3")
        buf.write("\2\2\2\u00c2\u00c3\7=\2\2\u00c3\60\3\2\2\2\u00c4\u00c5")
        buf.write("\7-\2\2\u00c5\62\3\2\2\2\u00c6\u00c7\7/\2\2\u00c7\64\3")
        buf.write("\2\2\2\u00c8\u00c9\7,\2\2\u00c9\u00ca\7,\2\2\u00ca\66")
        buf.write("\3\2\2\2\u00cb\u00cc\7,\2\2\u00cc8\3\2\2\2\u00cd\u00ce")
        buf.write("\7\61\2\2\u00ce:\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0<\3\2")
        buf.write("\2\2\u00d1\u00d2\7>\2\2\u00d2\u00d3\7?\2\2\u00d3>\3\2")
        buf.write("\2\2\u00d4\u00d5\7@\2\2\u00d5@\3\2\2\2\u00d6\u00d7\7@")
        buf.write("\2\2\u00d7\u00d8\7?\2\2\u00d8B\3\2\2\2\u00d9\u00da\7?")
        buf.write("\2\2\u00daD\3\2\2\2\u00db\u00dc\7#\2\2\u00dc\u00dd\7?")
        buf.write("\2\2\u00ddF\3\2\2\2\u00de\u00df\7?\2\2\u00df\u00e0\7?")
        buf.write("\2\2\u00e0H\3\2\2\2\u00e1\u00e2\7\60\2\2\u00e2J\3\2\2")
        buf.write("\2\u00e3\u00e4\7\'\2\2\u00e4L\3\2\2\2\u00e5\u00e6\7<\2")
        buf.write("\2\u00e6N\3\2\2\2\u00e7\u00e8\7V\2\2\u00e8\u00e9\7t\2")
        buf.write("\2\u00e9\u00ea\7w\2\2\u00ea\u00f1\7g\2\2\u00eb\u00ec\7")
        buf.write("H\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7u\2\2\u00ef\u00f1\7g\2\2\u00f0\u00e7\3\2\2\2\u00f0\u00eb")
        buf.write("\3\2\2\2\u00f1P\3\2\2\2\u00f2\u00f3\7P\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7g\2\2\u00f6R\3")
        buf.write("\2\2\2\u00f7\u00f9\t\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa")
        buf.write("\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\u00fd\b*\2\2\u00fdT\3\2\2\2\u00fe")
        buf.write("\u0102\7%\2\2\u00ff\u0101\n\3\2\2\u0100\u00ff\3\2\2\2")
        buf.write("\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3")
        buf.write("\2\2\2\u0103\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105\u0106")
        buf.write("\b+\2\2\u0106V\3\2\2\2\u0107\u0108\t\4\2\2\u0108X\3\2")
        buf.write("\2\2\u0109\u010c\5W,\2\u010a\u010c\7\62\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010cZ\3\2\2\2\u010d\u0111")
        buf.write("\5W,\2\u010e\u0110\5Y-\2\u010f\u010e\3\2\2\2\u0110\u0113")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u0116\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0116\7\62\2")
        buf.write("\2\u0115\u010d\3\2\2\2\u0115\u0114\3\2\2\2\u0116\\\3\2")
        buf.write("\2\2\u0117\u0118\5[.\2\u0118\u011a\7\60\2\2\u0119\u011b")
        buf.write("\5Y-\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d^\3\2\2\2\u011e\u011f")
        buf.write("\t\5\2\2\u011f`\3\2\2\2\u0120\u0128\n\6\2\2\u0121\u0122")
        buf.write("\7^\2\2\u0122\u0128\5a\61\2\u0123\u0124\7^\2\2\u0124\u0128")
        buf.write("\7$\2\2\u0125\u0126\7^\2\2\u0126\u0128\7)\2\2\u0127\u0120")
        buf.write("\3\2\2\2\u0127\u0121\3\2\2\2\u0127\u0123\3\2\2\2\u0127")
        buf.write("\u0125\3\2\2\2\u0128b\3\2\2\2\u0129\u012d\7$\2\2\u012a")
        buf.write("\u012c\5a\61\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2")
        buf.write("\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3")
        buf.write("\2\2\2\u012f\u012d\3\2\2\2\u0130\u013a\7$\2\2\u0131\u0135")
        buf.write("\7)\2\2\u0132\u0134\5a\61\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0138\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u013a\7")
        buf.write(")\2\2\u0139\u0129\3\2\2\2\u0139\u0131\3\2\2\2\u013ad\3")
        buf.write("\2\2\2\u013b\u013e\5_\60\2\u013c\u013e\7a\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013c\3\2\2\2\u013e\u0144\3\2\2\2\u013f")
        buf.write("\u0143\5[.\2\u0140\u0143\5_\60\2\u0141\u0143\7a\2\2\u0142")
        buf.write("\u013f\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145f\3\2\2\2\u0146\u0144\3\2\2\2\21\2\u00f0\u00fa")
        buf.write("\u0102\u010b\u0111\u0115\u011c\u0127\u012d\u0135\u0139")
        buf.write("\u013d\u0142\u0144\3\b\2\2")
        return buf.getvalue()


class my_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    LPAR = 16
    RPAR = 17
    LSQPAR = 18
    RSQPAR = 19
    LBRACE = 20
    RBRACE = 21
    COMMA = 22
    SEMI = 23
    PLUS = 24
    MINUS = 25
    DOUBLESTAR = 26
    STAR = 27
    SLASH = 28
    LESS = 29
    LESSEQUAL = 30
    GREATER = 31
    GREATEREQUAL = 32
    EQUAL = 33
    NOTEQUAL = 34
    DOUBLEEQUAL = 35
    DOT = 36
    PERCENT = 37
    COLON = 38
    BOOL = 39
    NONE = 40
    WS = 41
    COMMENT = 42
    NON_NEGATIVE_INTEGER = 43
    FLOAT = 44
    STRING = 45
    NAME = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'or'", "'not'", "'parameter_set'", "'where'", "'lambda'", "'//'", 
            "'for'", "'in'", "'while'", "'init'", "'if'", "'else'", "'import'", 
            "'..'", "'def'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
            "';'", "'+'", "'-'", "'**'", "'*'", "'/'", "'<'", "'<='", "'>'", 
            "'>='", "'='", "'!='", "'=='", "'.'", "'%'", "':'", "'None'" ]

    symbolicNames = [ "<INVALID>",
            "LPAR", "RPAR", "LSQPAR", "RSQPAR", "LBRACE", "RBRACE", "COMMA", 
            "SEMI", "PLUS", "MINUS", "DOUBLESTAR", "STAR", "SLASH", "LESS", 
            "LESSEQUAL", "GREATER", "GREATEREQUAL", "EQUAL", "NOTEQUAL", 
            "DOUBLEEQUAL", "DOT", "PERCENT", "COLON", "BOOL", "NONE", "WS", 
            "COMMENT", "NON_NEGATIVE_INTEGER", "FLOAT", "STRING", "NAME" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "LPAR", "RPAR", "LSQPAR", "RSQPAR", "LBRACE", 
                  "RBRACE", "COMMA", "SEMI", "PLUS", "MINUS", "DOUBLESTAR", 
                  "STAR", "SLASH", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
                  "EQUAL", "NOTEQUAL", "DOUBLEEQUAL", "DOT", "PERCENT", 
                  "COLON", "BOOL", "NONE", "WS", "COMMENT", "NON_ZERO_DIGIT", 
                  "DIGIT", "NON_NEGATIVE_INTEGER", "FLOAT", "CHAR", "STRING_CHAR", 
                  "STRING", "NAME" ]

    grammarFileName = "my_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


