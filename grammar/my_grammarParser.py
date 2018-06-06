# Generated from my_grammar.g4 by ANTLR 4.7.1
# encoding: utf-8
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

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u01ac\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f\2\16\2W\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\7\3_\n\3\f\3\16\3b\13\3\3\3\3\3\5")
        buf.write("\3f\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4v\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5\u0084\n\5\3\6\3\6\3\6\5\6\u0089\n\6")
        buf.write("\3\7\3\7\3\7\5\7\u008e\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u0098\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00a2\n\t\3\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b6")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00c2")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00d3\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\21\7\21\u00da\n\21\f\21\16\21\u00dd\13\21\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\7\24\u00e8")
        buf.write("\n\24\f\24\16\24\u00eb\13\24\3\25\3\25\3\25\7\25\u00f0")
        buf.write("\n\25\f\25\16\25\u00f3\13\25\3\26\3\26\3\26\7\26\u00f8")
        buf.write("\n\26\f\26\16\26\u00fb\13\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0104\n\27\3\30\3\30\3\30\3\30\3\30\5")
        buf.write("\30\u010b\n\30\3\30\3\30\3\31\3\31\7\31\u0111\n\31\f\31")
        buf.write("\16\31\u0114\13\31\3\32\3\32\3\32\3\32\3\32\5\32\u011b")
        buf.write("\n\32\3\33\3\33\5\33\u011f\n\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u012a\n\33\3\34\3\34\3\34")
        buf.write("\7\34\u012f\n\34\f\34\16\34\u0132\13\34\3\34\5\34\u0135")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0140\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \5 \u015a\n \3 \7 \u015d\n \f \16 \u0160")
        buf.write("\13 \3!\3!\3!\3!\3!\3!\3!\3!\5!\u016a\n!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u0178\n\"\3#\3#\3")
        buf.write("#\3#\3#\5#\u017f\n#\3$\3$\3$\3$\3$\3$\5$\u0187\n$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\5%\u0191\n%\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u019b\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\7)")
        buf.write("\u01a7\n)\f)\16)\u01aa\13)\3)\2\2*\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP\2")
        buf.write("\5\3\2\32\33\5\2\b\b\35\36\'\'\4\2\20\20&&\2\u01b3\2U")
        buf.write("\3\2\2\2\4Z\3\2\2\2\6u\3\2\2\2\b\u0083\3\2\2\2\n\u0085")
        buf.write("\3\2\2\2\f\u008a\3\2\2\2\16\u0097\3\2\2\2\20\u00a1\3\2")
        buf.write("\2\2\22\u00a7\3\2\2\2\24\u00b5\3\2\2\2\26\u00b7\3\2\2")
        buf.write("\2\30\u00bd\3\2\2\2\32\u00c3\3\2\2\2\34\u00d2\3\2\2\2")
        buf.write("\36\u00d4\3\2\2\2 \u00db\3\2\2\2\"\u00de\3\2\2\2$\u00e2")
        buf.write("\3\2\2\2&\u00e9\3\2\2\2(\u00ec\3\2\2\2*\u00f4\3\2\2\2")
        buf.write(",\u0103\3\2\2\2.\u0105\3\2\2\2\60\u010e\3\2\2\2\62\u011a")
        buf.write("\3\2\2\2\64\u0129\3\2\2\2\66\u012b\3\2\2\28\u013f\3\2")
        buf.write("\2\2:\u0141\3\2\2\2<\u014c\3\2\2\2>\u0159\3\2\2\2@\u0161")
        buf.write("\3\2\2\2B\u0177\3\2\2\2D\u017e\3\2\2\2F\u0186\3\2\2\2")
        buf.write("H\u0190\3\2\2\2J\u0192\3\2\2\2L\u019a\3\2\2\2N\u019c\3")
        buf.write("\2\2\2P\u01a8\3\2\2\2RT\5D#\2SR\3\2\2\2TW\3\2\2\2US\3")
        buf.write("\2\2\2UV\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\b\2\1\2Y\3\3\2")
        buf.write("\2\2Z`\7\24\2\2[\\\5(\25\2\\]\7\30\2\2]_\3\2\2\2^[\3\2")
        buf.write("\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ae\3\2\2\2b`\3\2\2\2")
        buf.write("cf\5(\25\2df\7\30\2\2ec\3\2\2\2ed\3\2\2\2ef\3\2\2\2fg")
        buf.write("\3\2\2\2gh\7\25\2\2h\5\3\2\2\2ij\5(\25\2jk\7(\2\2kl\5")
        buf.write("(\25\2lm\7(\2\2mn\5(\25\2no\b\4\1\2ov\3\2\2\2pq\5(\25")
        buf.write("\2qr\7(\2\2rs\5(\25\2st\b\4\1\2tv\3\2\2\2ui\3\2\2\2up")
        buf.write("\3\2\2\2v\7\3\2\2\2wx\7\37\2\2x\u0084\b\5\1\2yz\7!\2\2")
        buf.write("z\u0084\b\5\1\2{|\7%\2\2|\u0084\b\5\1\2}~\7 \2\2~\u0084")
        buf.write("\b\5\1\2\177\u0080\7\"\2\2\u0080\u0084\b\5\1\2\u0081\u0082")
        buf.write("\7$\2\2\u0082\u0084\b\5\1\2\u0083w\3\2\2\2\u0083y\3\2")
        buf.write("\2\2\u0083{\3\2\2\2\u0083}\3\2\2\2\u0083\177\3\2\2\2\u0083")
        buf.write("\u0081\3\2\2\2\u0084\t\3\2\2\2\u0085\u0088\5\f\7\2\u0086")
        buf.write("\u0087\7\3\2\2\u0087\u0089\5\f\7\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\13\3\2\2\2\u008a\u008d\5\16")
        buf.write("\b\2\u008b\u008c\7\4\2\2\u008c\u008e\5\16\b\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\r\3\2\2\2\u008f\u0090")
        buf.write("\7\4\2\2\u0090\u0091\5\16\b\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0093\b\b\1\2\u0093\u0098\3\2\2\2\u0094\u0095\5\20\t")
        buf.write("\2\u0095\u0096\b\b\1\2\u0096\u0098\3\2\2\2\u0097\u008f")
        buf.write("\3\2\2\2\u0097\u0094\3\2\2\2\u0098\17\3\2\2\2\u0099\u009a")
        buf.write("\5(\25\2\u009a\u009b\5\b\5\2\u009b\u009c\5(\25\2\u009c")
        buf.write("\u009d\b\t\1\2\u009d\u00a2\3\2\2\2\u009e\u009f\5(\25\2")
        buf.write("\u009f\u00a0\b\t\1\2\u00a0\u00a2\3\2\2\2\u00a1\u0099\3")
        buf.write("\2\2\2\u00a1\u009e\3\2\2\2\u00a2\21\3\2\2\2\u00a3\u00a4")
        buf.write("\7-\2\2\u00a4\u00a8\b\n\1\2\u00a5\u00a6\7.\2\2\u00a6\u00a8")
        buf.write("\b\n\1\2\u00a7\u00a3\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8")
        buf.write("\23\3\2\2\2\u00a9\u00aa\7/\2\2\u00aa\u00b6\b\13\1\2\u00ab")
        buf.write("\u00ac\5\22\n\2\u00ac\u00ad\b\13\1\2\u00ad\u00b6\3\2\2")
        buf.write("\2\u00ae\u00af\7)\2\2\u00af\u00b6\b\13\1\2\u00b0\u00b1")
        buf.write("\7*\2\2\u00b1\u00b6\b\13\1\2\u00b2\u00b3\5\4\3\2\u00b3")
        buf.write("\u00b4\b\13\1\2\u00b4\u00b6\3\2\2\2\u00b5\u00a9\3\2\2")
        buf.write("\2\u00b5\u00ab\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b0")
        buf.write("\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b6\25\3\2\2\2\u00b7\u00b8")
        buf.write("\7\5\2\2\u00b8\u00b9\7\60\2\2\u00b9\u00ba\7\26\2\2\u00ba")
        buf.write("\u00bb\5&\24\2\u00bb\u00bc\7\27\2\2\u00bc\27\3\2\2\2\u00bd")
        buf.write("\u00be\5\6\4\2\u00be\u00c1\7\6\2\2\u00bf\u00c2\7\60\2")
        buf.write("\2\u00c0\u00c2\5\32\16\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\31\3\2\2\2\u00c3\u00c4\7\7\2\2\u00c4\u00c5")
        buf.write("\7\60\2\2\u00c5\u00c6\7(\2\2\u00c6\u00c7\5(\25\2\u00c7")
        buf.write("\33\3\2\2\2\u00c8\u00c9\7\60\2\2\u00c9\u00ca\7#\2\2\u00ca")
        buf.write("\u00cb\5(\25\2\u00cb\u00cc\b\17\1\2\u00cc\u00d3\3\2\2")
        buf.write("\2\u00cd\u00ce\7\60\2\2\u00ce\u00cf\7#\2\2\u00cf\u00d0")
        buf.write("\5\6\4\2\u00d0\u00d1\b\17\1\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00c8\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d3\35\3\2\2\2\u00d4")
        buf.write("\u00d5\5\34\17\2\u00d5\u00d6\7\31\2\2\u00d6\u00d7\b\20")
        buf.write("\1\2\u00d7\37\3\2\2\2\u00d8\u00da\5\36\20\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc!\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\7\60\2\2\u00df\u00e0\7#\2\2\u00e0\u00e1\5\30\r")
        buf.write("\2\u00e1#\3\2\2\2\u00e2\u00e3\5\"\22\2\u00e3\u00e4\7\31")
        buf.write("\2\2\u00e4%\3\2\2\2\u00e5\u00e8\5\36\20\2\u00e6\u00e8")
        buf.write("\5$\23\2\u00e7\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8")
        buf.write("\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\'\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00f1\5*\26")
        buf.write("\2\u00ed\u00ee\t\2\2\2\u00ee\u00f0\5*\26\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2)\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f9\5,\27\2\u00f5\u00f6\t\3\2\2\u00f6\u00f8\5,\27\2")
        buf.write("\u00f7\u00f5\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa+\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fd\t\2\2\2\u00fd\u00fe\5,\27\2\u00fe")
        buf.write("\u00ff\b\27\1\2\u00ff\u0104\3\2\2\2\u0100\u0101\5.\30")
        buf.write("\2\u0101\u0102\b\27\1\2\u0102\u0104\3\2\2\2\u0103\u00fc")
        buf.write("\3\2\2\2\u0103\u0100\3\2\2\2\u0104-\3\2\2\2\u0105\u010a")
        buf.write("\5\60\31\2\u0106\u0107\7\34\2\2\u0107\u0108\5,\27\2\u0108")
        buf.write("\u0109\b\30\1\2\u0109\u010b\3\2\2\2\u010a\u0106\3\2\2")
        buf.write("\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d")
        buf.write("\b\30\1\2\u010d/\3\2\2\2\u010e\u0112\5\62\32\2\u010f\u0111")
        buf.write("\5\64\33\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\61\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0115\u0116\7\60\2\2\u0116\u011b\b\32\1")
        buf.write("\2\u0117\u0118\5\24\13\2\u0118\u0119\b\32\1\2\u0119\u011b")
        buf.write("\3\2\2\2\u011a\u0115\3\2\2\2\u011a\u0117\3\2\2\2\u011b")
        buf.write("\63\3\2\2\2\u011c\u011e\7\22\2\2\u011d\u011f\5\66\34\2")
        buf.write("\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\3")
        buf.write("\2\2\2\u0120\u0121\7\23\2\2\u0121\u012a\b\33\1\2\u0122")
        buf.write("\u0123\7\24\2\2\u0123\u0124\7-\2\2\u0124\u0125\7\25\2")
        buf.write("\2\u0125\u012a\b\33\1\2\u0126\u0127\7&\2\2\u0127\u0128")
        buf.write("\7\60\2\2\u0128\u012a\b\33\1\2\u0129\u011c\3\2\2\2\u0129")
        buf.write("\u0122\3\2\2\2\u0129\u0126\3\2\2\2\u012a\65\3\2\2\2\u012b")
        buf.write("\u0130\5(\25\2\u012c\u012d\7\30\2\2\u012d\u012f\5(\25")
        buf.write("\2\u012e\u012c\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0134\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0133\u0135\7\30\2\2\u0134\u0133\3\2\2")
        buf.write("\2\u0134\u0135\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0137")
        buf.write("\b\34\1\2\u0137\67\3\2\2\2\u0138\u0139\5:\36\2\u0139\u013a")
        buf.write("\b\35\1\2\u013a\u0140\3\2\2\2\u013b\u0140\5<\37\2\u013c")
        buf.write("\u013d\5@!\2\u013d\u013e\b\35\1\2\u013e\u0140\3\2\2\2")
        buf.write("\u013f\u0138\3\2\2\2\u013f\u013b\3\2\2\2\u013f\u013c\3")
        buf.write("\2\2\2\u01409\3\2\2\2\u0141\u0142\7\t\2\2\u0142\u0143")
        buf.write("\7\22\2\2\u0143\u0144\7\60\2\2\u0144\u0145\7\n\2\2\u0145")
        buf.write("\u0146\5(\25\2\u0146\u0147\7\23\2\2\u0147\u0148\7\26\2")
        buf.write("\2\u0148\u0149\5> \2\u0149\u014a\7\27\2\2\u014a\u014b")
        buf.write("\b\36\1\2\u014b;\3\2\2\2\u014c\u014d\7\13\2\2\u014d\u014e")
        buf.write("\7\22\2\2\u014e\u014f\5\n\6\2\u014f\u0150\7\23\2\2\u0150")
        buf.write("\u0151\7\26\2\2\u0151\u0152\5> \2\u0152\u0153\7\27\2\2")
        buf.write("\u0153=\3\2\2\2\u0154\u0155\7\f\2\2\u0155\u0156\7\26\2")
        buf.write("\2\u0156\u0157\5 \21\2\u0157\u0158\7\27\2\2\u0158\u015a")
        buf.write("\3\2\2\2\u0159\u0154\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015e\3\2\2\2\u015b\u015d\5F$\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f?\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7\r\2")
        buf.write("\2\u0162\u0163\7\22\2\2\u0163\u0164\5\n\6\2\u0164\u0165")
        buf.write("\7\23\2\2\u0165\u0166\7\26\2\2\u0166\u0167\5P)\2\u0167")
        buf.write("\u0169\7\27\2\2\u0168\u016a\5B\"\2\u0169\u0168\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b")
        buf.write("!\1\2\u016cA\3\2\2\2\u016d\u016e\7\16\2\2\u016e\u016f")
        buf.write("\7\26\2\2\u016f\u0170\5P)\2\u0170\u0171\7\27\2\2\u0171")
        buf.write("\u0172\b\"\1\2\u0172\u0178\3\2\2\2\u0173\u0174\7\16\2")
        buf.write("\2\u0174\u0175\5@!\2\u0175\u0176\b\"\1\2\u0176\u0178\3")
        buf.write("\2\2\2\u0177\u016d\3\2\2\2\u0177\u0173\3\2\2\2\u0178C")
        buf.write("\3\2\2\2\u0179\u017a\5F$\2\u017a\u017b\b#\1\2\u017b\u017f")
        buf.write("\3\2\2\2\u017c\u017f\5N(\2\u017d\u017f\5\26\f\2\u017e")
        buf.write("\u0179\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2")
        buf.write("\u017fE\3\2\2\2\u0180\u0181\58\35\2\u0181\u0182\b$\1\2")
        buf.write("\u0182\u0187\3\2\2\2\u0183\u0184\5H%\2\u0184\u0185\b$")
        buf.write("\1\2\u0185\u0187\3\2\2\2\u0186\u0180\3\2\2\2\u0186\u0183")
        buf.write("\3\2\2\2\u0187G\3\2\2\2\u0188\u0191\5J&\2\u0189\u018a")
        buf.write("\5(\25\2\u018a\u018b\7\31\2\2\u018b\u018c\b%\1\2\u018c")
        buf.write("\u0191\3\2\2\2\u018d\u018e\5\36\20\2\u018e\u018f\b%\1")
        buf.write("\2\u018f\u0191\3\2\2\2\u0190\u0188\3\2\2\2\u0190\u0189")
        buf.write("\3\2\2\2\u0190\u018d\3\2\2\2\u0191I\3\2\2\2\u0192\u0193")
        buf.write("\7\17\2\2\u0193\u0194\5L\'\2\u0194\u0195\7\31\2\2\u0195")
        buf.write("K\3\2\2\2\u0196\u019b\7\60\2\2\u0197\u0198\7\60\2\2\u0198")
        buf.write("\u0199\t\4\2\2\u0199\u019b\5L\'\2\u019a\u0196\3\2\2\2")
        buf.write("\u019a\u0197\3\2\2\2\u019bM\3\2\2\2\u019c\u019d\7\21\2")
        buf.write("\2\u019d\u019e\7\60\2\2\u019e\u019f\7\22\2\2\u019f\u01a0")
        buf.write("\5\66\34\2\u01a0\u01a1\7\23\2\2\u01a1\u01a2\7\26\2\2\u01a2")
        buf.write("\u01a3\5P)\2\u01a3\u01a4\7\27\2\2\u01a4O\3\2\2\2\u01a5")
        buf.write("\u01a7\5F$\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9Q\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2&U`eu\u0083\u0088\u008d\u0097\u00a1\u00a7")
        buf.write("\u00b5\u00c1\u00d2\u00db\u00e7\u00e9\u00f1\u00f9\u0103")
        buf.write("\u010a\u0112\u011a\u011e\u0129\u0130\u0134\u013f\u0159")
        buf.write("\u015e\u0169\u0177\u017e\u0186\u0190\u019a\u01a8")
        return buf.getvalue()


class my_grammarParser ( Parser ):

    grammarFileName = "my_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'or'", "'not'", "'parameter_set'", "'where'", 
                     "'lambda'", "'//'", "'for'", "'in'", "'while'", "'init'", 
                     "'if'", "'else'", "'import'", "'..'", "'def'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "';'", "'+'", 
                     "'-'", "'**'", "'*'", "'/'", "'<'", "'<='", "'>'", 
                     "'>='", "'='", "'!='", "'=='", "'.'", "'%'", "':'", 
                     "<INVALID>", "'None'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LPAR", "RPAR", "LSQPAR", "RSQPAR", "LBRACE", "RBRACE", 
                      "COMMA", "SEMI", "PLUS", "MINUS", "DOUBLESTAR", "STAR", 
                      "SLASH", "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", 
                      "EQUAL", "NOTEQUAL", "DOUBLEEQUAL", "DOT", "PERCENT", 
                      "COLON", "BOOL", "NONE", "WS", "COMMENT", "NON_NEGATIVE_INTEGER", 
                      "FLOAT", "STRING", "NAME" ]

    RULE_script = 0
    RULE_basic_list = 1
    RULE_by_slice_list = 2
    RULE_comparator = 3
    RULE_or_test = 4
    RULE_and_test = 5
    RULE_not_test = 6
    RULE_comparison = 7
    RULE_number = 8
    RULE_simple_literal = 9
    RULE_parameter_set_stmt = 10
    RULE_where_expr = 11
    RULE_simple_lambda = 12
    RULE_assignment = 13
    RULE_assignment_stmt = 14
    RULE_assignment_suite = 15
    RULE_where_assignment = 16
    RULE_where_assignemnt_stmt = 17
    RULE_parameter_set_suite = 18
    RULE_expr = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_power = 22
    RULE_atom_expr = 23
    RULE_atom = 24
    RULE_trailer = 25
    RULE_arglist = 26
    RULE_compound_stmt = 27
    RULE_for_stmt = 28
    RULE_while_stmt = 29
    RULE_loop_suite = 30
    RULE_if_stmt = 31
    RULE_else_stmt = 32
    RULE_stmt = 33
    RULE_context_stmt = 34
    RULE_simple_stmt = 35
    RULE_import_stmt = 36
    RULE_dotted_name = 37
    RULE_funcdef_stmt = 38
    RULE_suite = 39

    ruleNames =  [ "script", "basic_list", "by_slice_list", "comparator", 
                   "or_test", "and_test", "not_test", "comparison", "number", 
                   "simple_literal", "parameter_set_stmt", "where_expr", 
                   "simple_lambda", "assignment", "assignment_stmt", "assignment_suite", 
                   "where_assignment", "where_assignemnt_stmt", "parameter_set_suite", 
                   "expr", "term", "factor", "power", "atom_expr", "atom", 
                   "trailer", "arglist", "compound_stmt", "for_stmt", "while_stmt", 
                   "loop_suite", "if_stmt", "else_stmt", "stmt", "context_stmt", 
                   "simple_stmt", "import_stmt", "dotted_name", "funcdef_stmt", 
                   "suite" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    LPAR=16
    RPAR=17
    LSQPAR=18
    RSQPAR=19
    LBRACE=20
    RBRACE=21
    COMMA=22
    SEMI=23
    PLUS=24
    MINUS=25
    DOUBLESTAR=26
    STAR=27
    SLASH=28
    LESS=29
    LESSEQUAL=30
    GREATER=31
    GREATEREQUAL=32
    EQUAL=33
    NOTEQUAL=34
    DOUBLEEQUAL=35
    DOT=36
    PERCENT=37
    COLON=38
    BOOL=39
    NONE=40
    WS=41
    COMMENT=42
    NON_NEGATIVE_INTEGER=43
    FLOAT=44
    STRING=45
    NAME=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._stmt = None # StmtContext
            self.stmts = list() # of StmtContexts

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.StmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.StmtContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = my_grammarParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__2) | (1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.T__14) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 80
                localctx._stmt = self.stmt()
                localctx.stmts.append(localctx._stmt)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            localctx.myObj = Script(tuple([stmt.myObj for stmt in localctx.stmts]))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Basic_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts

        def LSQPAR(self):
            return self.getToken(my_grammarParser.LSQPAR, 0)

        def RSQPAR(self):
            return self.getToken(my_grammarParser.RSQPAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.COMMA)
            else:
                return self.getToken(my_grammarParser.COMMA, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ExprContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_basic_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_list" ):
                listener.enterBasic_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_list" ):
                listener.exitBasic_list(self)




    def basic_list(self):

        localctx = my_grammarParser.Basic_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_basic_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(my_grammarParser.LSQPAR)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    localctx._expr = self.expr()
                    localctx.exprs.append(localctx._expr)
                    self.state = 90
                    self.match(my_grammarParser.COMMA) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.state = 97
                localctx._expr = self.expr()
                localctx.exprs.append(localctx._expr)
                pass
            elif token in [my_grammarParser.COMMA]:
                self.state = 98
                self.match(my_grammarParser.COMMA)
                pass
            elif token in [my_grammarParser.RSQPAR]:
                pass
            else:
                pass
            self.state = 101
            self.match(my_grammarParser.RSQPAR)
            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = BasicList(tuple([expr.myObj for expr in localctx.exprs]))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class By_slice_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.e1 = None # ExprContext
            self.e2 = None # ExprContext
            self.e3 = None # ExprContext

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.COLON)
            else:
                return self.getToken(my_grammarParser.COLON, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ExprContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_by_slice_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBy_slice_list" ):
                listener.enterBy_slice_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBy_slice_list" ):
                listener.exitBy_slice_list(self)




    def by_slice_list(self):

        localctx = my_grammarParser.By_slice_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_by_slice_list)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                localctx.e1 = self.expr()
                self.state = 104
                self.match(my_grammarParser.COLON)
                self.state = 105
                localctx.e2 = self.expr()
                self.state = 106
                self.match(my_grammarParser.COLON)
                self.state = 107
                localctx.e3 = self.expr()
                localctx.myObj = BySliceList(localctx.e1.myObj, localctx.e2.myObj, localctx.e3.myObj)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                localctx.e1 = self.expr()
                self.state = 111
                self.match(my_grammarParser.COLON)
                self.state = 112
                localctx.e2 = self.expr()
                localctx.myObj = BySliceList(localctx.e1.myObj, localctx.e2.myObj)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None

        def LESS(self):
            return self.getToken(my_grammarParser.LESS, 0)

        def GREATER(self):
            return self.getToken(my_grammarParser.GREATER, 0)

        def DOUBLEEQUAL(self):
            return self.getToken(my_grammarParser.DOUBLEEQUAL, 0)

        def LESSEQUAL(self):
            return self.getToken(my_grammarParser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(my_grammarParser.GREATEREQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(my_grammarParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)




    def comparator(self):

        localctx = my_grammarParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comparator)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LESS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(my_grammarParser.LESS)
                localctx.myObj = Comparator(Comparator.Type.LESS)
                pass
            elif token in [my_grammarParser.GREATER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(my_grammarParser.GREATER)
                localctx.myObj = Comparator(Comparator.Type.GREATER)
                pass
            elif token in [my_grammarParser.DOUBLEEQUAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.match(my_grammarParser.DOUBLEEQUAL)
                localctx.myObj = Comparator(Comparator.Type.DOUBLEEQUAL)
                pass
            elif token in [my_grammarParser.LESSEQUAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(my_grammarParser.LESSEQUAL)
                localctx.myObj = Comparator(Comparator.Type.LESSEQUAL)
                pass
            elif token in [my_grammarParser.GREATEREQUAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 125
                self.match(my_grammarParser.GREATEREQUAL)
                localctx.myObj = Comparator(Comparator.Type.GREATEREQUAL)
                pass
            elif token in [my_grammarParser.NOTEQUAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.match(my_grammarParser.NOTEQUAL)
                localctx.myObj = Comparator(Comparator.Type.NOTEQUAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.x = None # And_testContext
            self._and_test = None # And_testContext
            self.y = list() # of And_testContexts

        def and_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.And_testContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.And_testContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_or_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_test" ):
                listener.enterOr_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_test" ):
                listener.exitOr_test(self)




    def or_test(self):

        localctx = my_grammarParser.Or_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_or_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            localctx.x = self.and_test()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__0:
                self.state = 132
                self.match(my_grammarParser.T__0)
                self.state = 133
                localctx._and_test = self.and_test()
                localctx.y.append(localctx._and_test)


            self._ctx.stop = self._input.LT(-1)

            if localctx.y:
                localctx.myObj = OrTest(localctx.x.myObj, localctx.y[0].myObj)
            else:
                localctx.myObj = OrTest(localctx.x.myObj)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.x = None # Not_testContext
            self._not_test = None # Not_testContext
            self.y = list() # of Not_testContexts

        def not_test(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Not_testContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Not_testContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_and_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_test" ):
                listener.enterAnd_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_test" ):
                listener.exitAnd_test(self)




    def and_test(self):

        localctx = my_grammarParser.And_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_and_test)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx.x = self.not_test()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__1:
                self.state = 137
                self.match(my_grammarParser.T__1)
                self.state = 138
                localctx._not_test = self.not_test()
                localctx.y.append(localctx._not_test)


            self._ctx.stop = self._input.LT(-1)

            if localctx.y:
                localctx.myObj = OrTest(localctx.x.myObj, localctx.y[0].myObj)
            else:
                localctx.myObj = OrTest(localctx.x.myObj)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Not_testContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._not_test = None # Not_testContext
            self._comparison = None # ComparisonContext

        def not_test(self):
            return self.getTypedRuleContext(my_grammarParser.Not_testContext,0)


        def comparison(self):
            return self.getTypedRuleContext(my_grammarParser.ComparisonContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_not_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_test" ):
                listener.enterNot_test(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_test" ):
                listener.exitNot_test(self)




    def not_test(self):

        localctx = my_grammarParser.Not_testContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_not_test)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(my_grammarParser.T__1)
                self.state = 142
                localctx._not_test = self.not_test()
                localctx.myObj = NotTest.createFromNonTest(localctx._not_test.myObj)
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                localctx._comparison = self.comparison()
                localctx.myObj = NotTest.createFromComparison(localctx._comparison.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.e1 = None # ExprContext
            self.c = None # ComparatorContext
            self.e2 = None # ExprContext
            self._expr = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ExprContext,i)


        def comparator(self):
            return self.getTypedRuleContext(my_grammarParser.ComparatorContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = my_grammarParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparison)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                localctx.e1 = self.expr()
                self.state = 152
                localctx.c = self.comparator()
                self.state = 153
                localctx.e2 = self.expr()
                localctx.myObj = Comparison.createFromTwoExprs(localctx.e1.myObj, localctx.c.myObj, localctx.e2.myObj)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                localctx._expr = self.expr()
                localctx.myObj = Comparison.createFromExpr(localctx._expr.myObj)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._NON_NEGATIVE_INTEGER = None # Token
            self._FLOAT = None # Token

        def NON_NEGATIVE_INTEGER(self):
            return self.getToken(my_grammarParser.NON_NEGATIVE_INTEGER, 0)

        def FLOAT(self):
            return self.getToken(my_grammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = my_grammarParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NON_NEGATIVE_INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                localctx.myObj = Number.createNonNegativeInteger((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass
            elif token in [my_grammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                localctx._FLOAT = self.match(my_grammarParser.FLOAT)
                localctx.myObj = Number.createFloat((None if localctx._FLOAT is None else localctx._FLOAT.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._STRING = None # Token
            self._number = None # NumberContext
            self._BOOL = None # Token
            self._basic_list = None # Basic_listContext

        def STRING(self):
            return self.getToken(my_grammarParser.STRING, 0)

        def number(self):
            return self.getTypedRuleContext(my_grammarParser.NumberContext,0)


        def BOOL(self):
            return self.getToken(my_grammarParser.BOOL, 0)

        def NONE(self):
            return self.getToken(my_grammarParser.NONE, 0)

        def basic_list(self):
            return self.getTypedRuleContext(my_grammarParser.Basic_listContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_simple_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_literal" ):
                listener.enterSimple_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_literal" ):
                listener.exitSimple_literal(self)




    def simple_literal(self):

        localctx = my_grammarParser.Simple_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_simple_literal)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                localctx._STRING = self.match(my_grammarParser.STRING)
                localctx.myObj = SimpleLiteral.createFromString((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                localctx._number = self.number()
                localctx.myObj = SimpleLiteral.createFromNumber(localctx._number.myObj)
                pass
            elif token in [my_grammarParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                localctx._BOOL = self.match(my_grammarParser.BOOL)
                localctx.myObj = SimpleLiteral.createFromBool((None if localctx._BOOL is None else localctx._BOOL.text))
                pass
            elif token in [my_grammarParser.NONE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(my_grammarParser.NONE)
                localctx.myObj = SimpleLiteral.createFromNone()
                pass
            elif token in [my_grammarParser.LSQPAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                localctx._basic_list = self.basic_list()
                localctx.myObj = SimpleLiteral.createFromBasicList(localctx._basic_list.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_set_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def parameter_set_suite(self):
            return self.getTypedRuleContext(my_grammarParser.Parameter_set_suiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_parameter_set_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_set_stmt" ):
                listener.enterParameter_set_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_set_stmt" ):
                listener.exitParameter_set_stmt(self)




    def parameter_set_stmt(self):

        localctx = my_grammarParser.Parameter_set_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_set_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(my_grammarParser.T__2)
            self.state = 182
            self.match(my_grammarParser.NAME)
            self.state = 183
            self.match(my_grammarParser.LBRACE)
            self.state = 184
            self.parameter_set_suite()
            self.state = 185
            self.match(my_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def by_slice_list(self):
            return self.getTypedRuleContext(my_grammarParser.By_slice_listContext,0)


        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def simple_lambda(self):
            return self.getTypedRuleContext(my_grammarParser.Simple_lambdaContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_where_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_expr" ):
                listener.enterWhere_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_expr" ):
                listener.exitWhere_expr(self)




    def where_expr(self):

        localctx = my_grammarParser.Where_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_where_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.by_slice_list()
            self.state = 188
            self.match(my_grammarParser.T__3)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.state = 189
                self.match(my_grammarParser.NAME)
                pass
            elif token in [my_grammarParser.T__4]:
                self.state = 190
                self.simple_lambda()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_lambdaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def COLON(self):
            return self.getToken(my_grammarParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(my_grammarParser.ExprContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_simple_lambda

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_lambda" ):
                listener.enterSimple_lambda(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_lambda" ):
                listener.exitSimple_lambda(self)




    def simple_lambda(self):

        localctx = my_grammarParser.Simple_lambdaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_simple_lambda)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(my_grammarParser.T__4)
            self.state = 194
            self.match(my_grammarParser.NAME)
            self.state = 195
            self.match(my_grammarParser.COLON)
            self.state = 196
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._NAME = None # Token
            self._expr = None # ExprContext
            self._by_slice_list = None # By_slice_listContext

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def EQUAL(self):
            return self.getToken(my_grammarParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(my_grammarParser.ExprContext,0)


        def by_slice_list(self):
            return self.getTypedRuleContext(my_grammarParser.By_slice_listContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = my_grammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                localctx._NAME = self.match(my_grammarParser.NAME)
                self.state = 199
                self.match(my_grammarParser.EQUAL)
                self.state = 200
                localctx._expr = self.expr()
                localctx.myObj = Assignment.createFromExpr((None if localctx._NAME is None else localctx._NAME.text), localctx._expr.myObj)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                localctx._NAME = self.match(my_grammarParser.NAME)
                self.state = 204
                self.match(my_grammarParser.EQUAL)
                self.state = 205
                localctx._by_slice_list = self.by_slice_list()
                localctx.myObj = Assignment.createFromBySliceList((None if localctx._NAME is None else localctx._NAME.text), localctx._by_slice_list.myObj)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._assignment = None # AssignmentContext

        def assignment(self):
            return self.getTypedRuleContext(my_grammarParser.AssignmentContext,0)


        def SEMI(self):
            return self.getToken(my_grammarParser.SEMI, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_assignment_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_stmt" ):
                listener.enterAssignment_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_stmt" ):
                listener.exitAssignment_stmt(self)




    def assignment_stmt(self):

        localctx = my_grammarParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            localctx._assignment = self.assignment()
            self.state = 211
            self.match(my_grammarParser.SEMI)
            localctx.myObj = AssignmentStmt(localctx._assignment.myObj)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_suiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._assignment_stmt = None # Assignment_stmtContext
            self.s = list() # of Assignment_stmtContexts

        def assignment_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Assignment_stmtContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_assignment_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_suite" ):
                listener.enterAssignment_suite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_suite" ):
                listener.exitAssignment_suite(self)




    def assignment_suite(self):

        localctx = my_grammarParser.Assignment_suiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 214
                localctx._assignment_stmt = self.assignment_stmt()
                localctx.s.append(localctx._assignment_stmt)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = AssignmentSuite(tuple([stmt.myObj for stmt in localctx.s]))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def EQUAL(self):
            return self.getToken(my_grammarParser.EQUAL, 0)

        def where_expr(self):
            return self.getTypedRuleContext(my_grammarParser.Where_exprContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_where_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_assignment" ):
                listener.enterWhere_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_assignment" ):
                listener.exitWhere_assignment(self)




    def where_assignment(self):

        localctx = my_grammarParser.Where_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_where_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(my_grammarParser.NAME)
            self.state = 221
            self.match(my_grammarParser.EQUAL)
            self.state = 222
            self.where_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_assignemnt_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def where_assignment(self):
            return self.getTypedRuleContext(my_grammarParser.Where_assignmentContext,0)


        def SEMI(self):
            return self.getToken(my_grammarParser.SEMI, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_where_assignemnt_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_assignemnt_stmt" ):
                listener.enterWhere_assignemnt_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_assignemnt_stmt" ):
                listener.exitWhere_assignemnt_stmt(self)




    def where_assignemnt_stmt(self):

        localctx = my_grammarParser.Where_assignemnt_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_where_assignemnt_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.where_assignment()
            self.state = 225
            self.match(my_grammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_set_suiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Assignment_stmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Assignment_stmtContext,i)


        def where_assignemnt_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Where_assignemnt_stmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Where_assignemnt_stmtContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_parameter_set_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_set_suite" ):
                listener.enterParameter_set_suite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_set_suite" ):
                listener.exitParameter_set_suite(self)




    def parameter_set_suite(self):

        localctx = my_grammarParser.Parameter_set_suiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter_set_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 227
                    self.assignment_stmt()
                    pass

                elif la_ == 2:
                    self.state = 228
                    self.where_assignemnt_stmt()
                    pass


                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.t = None # TermContext
            self._PLUS = None # Token
            self.operators = list() # of Tokens
            self._MINUS = None # Token
            self._tset484 = None # Token
            self._term = None # TermContext
            self.operands = list() # of TermContexts

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.PLUS)
            else:
                return self.getToken(my_grammarParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.MINUS)
            else:
                return self.getToken(my_grammarParser.MINUS, i)

        def getRuleIndex(self):
            return my_grammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = my_grammarParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            localctx.t = self.term()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS:
                self.state = 235
                localctx._tset484 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx._tset484 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.operators.append(localctx._tset484)
                self.state = 236
                localctx._term = self.term()
                localctx.operands.append(localctx._term)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = Expr(localctx.t.myObj, tuple(zip([operator.text for operator in localctx.operators], [operand.myObj for operand in localctx.operands])))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.f = None # FactorContext
            self._STAR = None # Token
            self.operators = list() # of Tokens
            self._SLASH = None # Token
            self._PERCENT = None # Token
            self.s6 = None # Token
            self._tset520 = None # Token
            self._factor = None # FactorContext
            self.operands = list() # of FactorContexts

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.FactorContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.FactorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.STAR)
            else:
                return self.getToken(my_grammarParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.SLASH)
            else:
                return self.getToken(my_grammarParser.SLASH, i)

        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.PERCENT)
            else:
                return self.getToken(my_grammarParser.PERCENT, i)

        def getRuleIndex(self):
            return my_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = my_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            localctx.f = self.factor()
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0):
                self.state = 243
                localctx._tset520 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0)):
                    localctx._tset520 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.operators.append(localctx._tset520)
                self.state = 244
                localctx._factor = self.factor()
                localctx.operands.append(localctx._factor)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = Term(localctx.f.myObj, tuple(zip([operator.text for operator in localctx.operators], [operand.myObj for operand in localctx.operands])))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.sign = None # Token
            self._factor = None # FactorContext
            self._power = None # PowerContext

        def factor(self):
            return self.getTypedRuleContext(my_grammarParser.FactorContext,0)


        def PLUS(self):
            return self.getToken(my_grammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(my_grammarParser.MINUS, 0)

        def power(self):
            return self.getTypedRuleContext(my_grammarParser.PowerContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = my_grammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.PLUS, my_grammarParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 251
                localctx._factor = self.factor()
                localctx.myObj = Factor.createFromFactor((None if localctx.sign is None else localctx.sign.text), localctx._factor.myObj)
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                localctx._power = self.power()
                localctx.myObj = Factor.createFromPower(localctx._power.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PowerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.x = None
            self.a = None # Atom_exprContext
            self._factor = None # FactorContext

        def atom_expr(self):
            return self.getTypedRuleContext(my_grammarParser.Atom_exprContext,0)


        def DOUBLESTAR(self):
            return self.getToken(my_grammarParser.DOUBLESTAR, 0)

        def factor(self):
            return self.getTypedRuleContext(my_grammarParser.FactorContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)




    def power(self):

        localctx = my_grammarParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_power)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            localctx.a = self.atom_expr()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.DOUBLESTAR:
                self.state = 260
                self.match(my_grammarParser.DOUBLESTAR)
                self.state = 261
                localctx._factor = self.factor()
                localctx.x = localctx._factor.myObj


            if localctx.x:
                localctx.myObj = Power(localctx.a.myObj, localctx.x)
            else:
                localctx.myObj = Power(localctx.a.myObj)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atom_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.a = None # AtomContext
            self._trailer = None # TrailerContext
            self.trailers = list() # of TrailerContexts

        def atom(self):
            return self.getTypedRuleContext(my_grammarParser.AtomContext,0)


        def trailer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.TrailerContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.TrailerContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_atom_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_expr" ):
                listener.enterAtom_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_expr" ):
                listener.exitAtom_expr(self)




    def atom_expr(self):

        localctx = my_grammarParser.Atom_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atom_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            localctx.a = self.atom()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LPAR) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.DOT))) != 0):
                self.state = 269
                localctx._trailer = self.trailer()
                localctx.trailers.append(localctx._trailer)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = AtomExpr(localctx.a.myObj, tuple([trailer.myObj for trailer in localctx.trailers]))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._NAME = None # Token
            self._simple_literal = None # Simple_literalContext

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def simple_literal(self):
            return self.getTypedRuleContext(my_grammarParser.Simple_literalContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = my_grammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_atom)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                localctx._NAME = self.match(my_grammarParser.NAME)
                localctx.myObj = Atom.createFromName((None if localctx._NAME is None else localctx._NAME.text))
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                localctx._simple_literal = self.simple_literal()
                localctx.myObj = Atom.createFromSimpleLiteral(localctx._simple_literal.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrailerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._arglist = None # ArglistContext
            self._NON_NEGATIVE_INTEGER = None # Token
            self._NAME = None # Token

        def LPAR(self):
            return self.getToken(my_grammarParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(my_grammarParser.RPAR, 0)

        def arglist(self):
            return self.getTypedRuleContext(my_grammarParser.ArglistContext,0)


        def LSQPAR(self):
            return self.getToken(my_grammarParser.LSQPAR, 0)

        def NON_NEGATIVE_INTEGER(self):
            return self.getToken(my_grammarParser.NON_NEGATIVE_INTEGER, 0)

        def RSQPAR(self):
            return self.getToken(my_grammarParser.RSQPAR, 0)

        def DOT(self):
            return self.getToken(my_grammarParser.DOT, 0)

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_trailer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailer" ):
                listener.enterTrailer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailer" ):
                listener.exitTrailer(self)




    def trailer(self):

        localctx = my_grammarParser.TrailerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_trailer)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(my_grammarParser.LPAR)
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                    self.state = 283
                    localctx._arglist = self.arglist()


                self.state = 286
                self.match(my_grammarParser.RPAR)
                localctx.myObj = Trailer.createFromArglist(localctx._arglist.myObj)
                pass
            elif token in [my_grammarParser.LSQPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(my_grammarParser.LSQPAR)
                self.state = 289
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                self.state = 290
                self.match(my_grammarParser.RSQPAR)
                localctx.myObj = Trailer.createFromAccess((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass
            elif token in [my_grammarParser.DOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.match(my_grammarParser.DOT)
                self.state = 293
                localctx._NAME = self.match(my_grammarParser.NAME)
                localctx.myObj = Trailer.createFromDotName((None if localctx._NAME is None else localctx._NAME.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self.arg = None # ExprContext
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.COMMA)
            else:
                return self.getToken(my_grammarParser.COMMA, i)

        def getRuleIndex(self):
            return my_grammarParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)




    def arglist(self):

        localctx = my_grammarParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            localctx.arg = self.expr()
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 298
                    self.match(my_grammarParser.COMMA)
                    self.state = 299
                    localctx._expr = self.expr()
                    localctx.args.append(localctx._expr) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.COMMA:
                self.state = 305
                self.match(my_grammarParser.COMMA)


            localctx.myObj = Arglist(tuple([localctx.arg.myObj] + [argument.myObj for argument in localctx.args]))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._for_stmt = None # For_stmtContext
            self._if_stmt = None # If_stmtContext

        def for_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.While_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.If_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_compound_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_stmt" ):
                listener.enterCompound_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_stmt" ):
                listener.exitCompound_stmt(self)




    def compound_stmt(self):

        localctx = my_grammarParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_compound_stmt)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                localctx._for_stmt = self.for_stmt()
                localctx.myObj = CompoundStmt.createFromForStmt(localctx._for_stmt.myObj)
                pass
            elif token in [my_grammarParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.while_stmt()
                pass
            elif token in [my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 314
                localctx._if_stmt = self.if_stmt()
                localctx.myObj = CompoundStmt.createFromIfStmt(localctx._if_stmt.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._NAME = None # Token
            self._expr = None # ExprContext
            self._loop_suite = None # Loop_suiteContext

        def LPAR(self):
            return self.getToken(my_grammarParser.LPAR, 0)

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(my_grammarParser.ExprContext,0)


        def RPAR(self):
            return self.getToken(my_grammarParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def loop_suite(self):
            return self.getTypedRuleContext(my_grammarParser.Loop_suiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)




    def for_stmt(self):

        localctx = my_grammarParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(my_grammarParser.T__6)
            self.state = 320
            self.match(my_grammarParser.LPAR)
            self.state = 321
            localctx._NAME = self.match(my_grammarParser.NAME)
            self.state = 322
            self.match(my_grammarParser.T__7)
            self.state = 323
            localctx._expr = self.expr()
            self.state = 324
            self.match(my_grammarParser.RPAR)
            self.state = 325
            self.match(my_grammarParser.LBRACE)
            self.state = 326
            localctx._loop_suite = self.loop_suite()
            self.state = 327
            self.match(my_grammarParser.RBRACE)
            localctx.myObj = ForStmt((None if localctx._NAME is None else localctx._NAME.text), localctx._expr.myObj, localctx._loop_suite.myObj)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(my_grammarParser.LPAR, 0)

        def or_test(self):
            return self.getTypedRuleContext(my_grammarParser.Or_testContext,0)


        def RPAR(self):
            return self.getToken(my_grammarParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def loop_suite(self):
            return self.getTypedRuleContext(my_grammarParser.Loop_suiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = my_grammarParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(my_grammarParser.T__8)
            self.state = 331
            self.match(my_grammarParser.LPAR)
            self.state = 332
            self.or_test()
            self.state = 333
            self.match(my_grammarParser.RPAR)
            self.state = 334
            self.match(my_grammarParser.LBRACE)
            self.state = 335
            self.loop_suite()
            self.state = 336
            self.match(my_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Loop_suiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._assignment_suite = None # Assignment_suiteContext
            self.az = list() # of Assignment_suiteContexts
            self._context_stmt = None # Context_stmtContext
            self.ctxs = list() # of Context_stmtContexts

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def assignment_suite(self):
            return self.getTypedRuleContext(my_grammarParser.Assignment_suiteContext,0)


        def context_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Context_stmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Context_stmtContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_loop_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_suite" ):
                listener.enterLoop_suite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_suite" ):
                listener.exitLoop_suite(self)




    def loop_suite(self):

        localctx = my_grammarParser.Loop_suiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_loop_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__9:
                self.state = 338
                self.match(my_grammarParser.T__9)
                self.state = 339
                self.match(my_grammarParser.LBRACE)
                self.state = 340
                localctx._assignment_suite = self.assignment_suite()
                localctx.az.append(localctx._assignment_suite)
                self.state = 341
                self.match(my_grammarParser.RBRACE)


            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 345
                localctx._context_stmt = self.context_stmt()
                localctx.ctxs.append(localctx._context_stmt)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            if localctx.az:
                localctx.myObj = LoopSuite(contextStmts=tuple([c.myObj for c in localctx.ctxs]), assignmentSuite=localctx.az[0].myObj)
            else:
                localctx.myObj = LoopSuite(contextStmts=tuple([c.myObj for c in localctx.ctxs]))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._or_test = None # Or_testContext
            self._suite = None # SuiteContext
            self._else_stmt = None # Else_stmtContext
            self.e = list() # of Else_stmtContexts

        def LPAR(self):
            return self.getToken(my_grammarParser.LPAR, 0)

        def or_test(self):
            return self.getTypedRuleContext(my_grammarParser.Or_testContext,0)


        def RPAR(self):
            return self.getToken(my_grammarParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def suite(self):
            return self.getTypedRuleContext(my_grammarParser.SuiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def else_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = my_grammarParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(my_grammarParser.T__10)
            self.state = 352
            self.match(my_grammarParser.LPAR)
            self.state = 353
            localctx._or_test = self.or_test()
            self.state = 354
            self.match(my_grammarParser.RPAR)
            self.state = 355
            self.match(my_grammarParser.LBRACE)
            self.state = 356
            localctx._suite = self.suite()
            self.state = 357
            self.match(my_grammarParser.RBRACE)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__11:
                self.state = 358
                localctx._else_stmt = self.else_stmt()
                localctx.e.append(localctx._else_stmt)


            localctx.myObj = IfStmt(localctx._or_test.myObj, localctx._suite.myObj, localctx.e[0].myObj if localctx.e else None)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._suite = None # SuiteContext
            self._if_stmt = None # If_stmtContext

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def suite(self):
            return self.getTypedRuleContext(my_grammarParser.SuiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.If_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_else_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)




    def else_stmt(self):

        localctx = my_grammarParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_else_stmt)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(my_grammarParser.T__11)
                self.state = 364
                self.match(my_grammarParser.LBRACE)
                self.state = 365
                localctx._suite = self.suite()
                self.state = 366
                self.match(my_grammarParser.RBRACE)
                localctx.myObj = ElseStmt.createFromSuite(localctx._suite.myObj)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.match(my_grammarParser.T__11)
                self.state = 370
                localctx._if_stmt = self.if_stmt()
                localctx.myObj = ElseStmt.createFromIfStmt(localctx._if_stmt.myObj)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._context_stmt = None # Context_stmtContext

        def context_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Context_stmtContext,0)


        def funcdef_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Funcdef_stmtContext,0)


        def parameter_set_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Parameter_set_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = my_grammarParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10, my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                localctx._context_stmt = self.context_stmt()
                localctx.myObj = ContextStmt.createFromSimpleStmt(localctx._context_stmt.myObj)
                pass
            elif token in [my_grammarParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.funcdef_stmt()
                pass
            elif token in [my_grammarParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.parameter_set_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Context_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._compound_stmt = None # Compound_stmtContext
            self._simple_stmt = None # Simple_stmtContext

        def compound_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Compound_stmtContext,0)


        def simple_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Simple_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_context_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext_stmt" ):
                listener.enterContext_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext_stmt" ):
                listener.exitContext_stmt(self)




    def context_stmt(self):

        localctx = my_grammarParser.Context_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_context_stmt)
        try:
            self.state = 388
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                localctx._compound_stmt = self.compound_stmt()
                localctx.myObj = ContextStmt.createFromCompoundStmt(localctx._compound_stmt.myObj)
                pass
            elif token in [my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                localctx._simple_stmt = self.simple_stmt()
                localctx.myObj = ContextStmt.createFromSimpleStmt(localctx._simple_stmt.myObj)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._expr = None # ExprContext
            self.a = None # Assignment_stmtContext

        def import_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Import_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(my_grammarParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(my_grammarParser.SEMI, 0)

        def assignment_stmt(self):
            return self.getTypedRuleContext(my_grammarParser.Assignment_stmtContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_simple_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_stmt" ):
                listener.enterSimple_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_stmt" ):
                listener.exitSimple_stmt(self)




    def simple_stmt(self):

        localctx = my_grammarParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_simple_stmt)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.import_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                localctx._expr = self.expr()
                self.state = 392
                self.match(my_grammarParser.SEMI)
                localctx.myObj = SimpleStmt.createFromExpr(localctx._expr.myObj)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                localctx.a = self.assignment_stmt()
                localctx.myObj = AssignmentStmt(localctx.a.myObj)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dotted_name(self):
            return self.getTypedRuleContext(my_grammarParser.Dotted_nameContext,0)


        def SEMI(self):
            return self.getToken(my_grammarParser.SEMI, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_import_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmt" ):
                listener.enterImport_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmt" ):
                listener.exitImport_stmt(self)




    def import_stmt(self):

        localctx = my_grammarParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_import_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(my_grammarParser.T__12)
            self.state = 401
            self.dotted_name()
            self.state = 402
            self.match(my_grammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dotted_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def dotted_name(self):
            return self.getTypedRuleContext(my_grammarParser.Dotted_nameContext,0)


        def getRuleIndex(self):
            return my_grammarParser.RULE_dotted_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotted_name" ):
                listener.enterDotted_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotted_name" ):
                listener.exitDotted_name(self)




    def dotted_name(self):

        localctx = my_grammarParser.Dotted_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_dotted_name)
        self._la = 0 # Token type
        try:
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(my_grammarParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(my_grammarParser.NAME)
                self.state = 406
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.T__13 or _la==my_grammarParser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 407
                self.dotted_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Funcdef_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def LPAR(self):
            return self.getToken(my_grammarParser.LPAR, 0)

        def arglist(self):
            return self.getTypedRuleContext(my_grammarParser.ArglistContext,0)


        def RPAR(self):
            return self.getToken(my_grammarParser.RPAR, 0)

        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def suite(self):
            return self.getTypedRuleContext(my_grammarParser.SuiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_funcdef_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdef_stmt" ):
                listener.enterFuncdef_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdef_stmt" ):
                listener.exitFuncdef_stmt(self)




    def funcdef_stmt(self):

        localctx = my_grammarParser.Funcdef_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_funcdef_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(my_grammarParser.T__14)
            self.state = 411
            self.match(my_grammarParser.NAME)
            self.state = 412
            self.match(my_grammarParser.LPAR)
            self.state = 413
            self.arglist()
            self.state = 414
            self.match(my_grammarParser.RPAR)
            self.state = 415
            self.match(my_grammarParser.LBRACE)
            self.state = 416
            self.suite()
            self.state = 417
            self.match(my_grammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SuiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._context_stmt = None # Context_stmtContext
            self.ctxs = list() # of Context_stmtContexts

        def context_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.Context_stmtContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.Context_stmtContext,i)


        def getRuleIndex(self):
            return my_grammarParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)




    def suite(self):

        localctx = my_grammarParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 419
                localctx._context_stmt = self.context_stmt()
                localctx.ctxs.append(localctx._context_stmt)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            localctx.myObj = Suite(tuple([c.myObj for c in localctx.ctxs]))
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





