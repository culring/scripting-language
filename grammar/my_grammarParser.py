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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u018a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3a\n\3\f\3\16\3d\13\3\3\3")
        buf.write("\3\3\5\3h\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4v\n\4\3\5\3\5\3\6\3\6\3\6\5\6}\n\6\3\7\3\7")
        buf.write("\3\7\5\7\u0082\n\7\3\b\3\b\3\b\5\b\u0087\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u008e\n\t\3\n\3\n\3\n\3\n\5\n\u0094\n\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00a0\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00ac\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00bb\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\7\21\u00c2\n\21\f\21\16\21\u00c5\13\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\7\24\u00d0\n")
        buf.write("\24\f\24\16\24\u00d3\13\24\3\25\3\25\3\25\7\25\u00d8\n")
        buf.write("\25\f\25\16\25\u00db\13\25\3\26\3\26\3\26\7\26\u00e0\n")
        buf.write("\26\f\26\16\26\u00e3\13\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u00ec\n\27\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u00f3\n\30\3\30\3\30\3\31\3\31\7\31\u00f9\n\31\f\31\16")
        buf.write("\31\u00fc\13\31\3\32\3\32\3\32\3\32\3\32\5\32\u0103\n")
        buf.write("\32\3\33\3\33\5\33\u0107\n\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0112\n\33\3\34\3\34\3\34\7")
        buf.write("\34\u0117\n\34\f\34\16\34\u011a\13\34\3\34\5\34\u011d")
        buf.write("\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u0126\n")
        buf.write("\35\3\36\3\36\3\36\5\36\u012b\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\5!\u0144\n!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\5\"\u0150\n\"\3#\3#\3#\3#\3#\3#\5#\u0158")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u015f\n$\3%\3%\3%\3%\5%\u0165\n")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u016f\n&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\5(\u0179\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\7*\u0185\n*\f*\16*\u0188\13*\3*\2\2+\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPR\2\6\4\2\37\"$%\3\2\32\33\5\2\b\b\35\36\'\'\4\2")
        buf.write("\20\20&&\2\u018b\2W\3\2\2\2\4\\\3\2\2\2\6u\3\2\2\2\bw")
        buf.write("\3\2\2\2\ny\3\2\2\2\f~\3\2\2\2\16\u0086\3\2\2\2\20\u008d")
        buf.write("\3\2\2\2\22\u0093\3\2\2\2\24\u009f\3\2\2\2\26\u00a1\3")
        buf.write("\2\2\2\30\u00a7\3\2\2\2\32\u00ad\3\2\2\2\34\u00ba\3\2")
        buf.write("\2\2\36\u00bc\3\2\2\2 \u00c3\3\2\2\2\"\u00c6\3\2\2\2$")
        buf.write("\u00ca\3\2\2\2&\u00d1\3\2\2\2(\u00d4\3\2\2\2*\u00dc\3")
        buf.write("\2\2\2,\u00eb\3\2\2\2.\u00ed\3\2\2\2\60\u00f6\3\2\2\2")
        buf.write("\62\u0102\3\2\2\2\64\u0111\3\2\2\2\66\u0113\3\2\2\28\u0125")
        buf.write("\3\2\2\2:\u012a\3\2\2\2<\u012c\3\2\2\2>\u0136\3\2\2\2")
        buf.write("@\u0143\3\2\2\2B\u0147\3\2\2\2D\u0151\3\2\2\2F\u015e\3")
        buf.write("\2\2\2H\u0164\3\2\2\2J\u016e\3\2\2\2L\u0170\3\2\2\2N\u0178")
        buf.write("\3\2\2\2P\u017a\3\2\2\2R\u0186\3\2\2\2TV\5F$\2UT\3\2\2")
        buf.write("\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z")
        buf.write("[\b\2\1\2[\3\3\2\2\2\\b\7\24\2\2]^\5(\25\2^_\7\30\2\2")
        buf.write("_a\3\2\2\2`]\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2cg\3")
        buf.write("\2\2\2db\3\2\2\2eh\5(\25\2fh\7\30\2\2ge\3\2\2\2gf\3\2")
        buf.write("\2\2gh\3\2\2\2hi\3\2\2\2ij\7\25\2\2j\5\3\2\2\2kl\5(\25")
        buf.write("\2lm\7(\2\2mn\5(\25\2no\7(\2\2op\5(\25\2pv\3\2\2\2qr\5")
        buf.write("(\25\2rs\7(\2\2st\5(\25\2tv\3\2\2\2uk\3\2\2\2uq\3\2\2")
        buf.write("\2v\7\3\2\2\2wx\t\2\2\2x\t\3\2\2\2y|\5\f\7\2z{\7\3\2\2")
        buf.write("{}\5\f\7\2|z\3\2\2\2|}\3\2\2\2}\13\3\2\2\2~\u0081\5\16")
        buf.write("\b\2\177\u0080\7\4\2\2\u0080\u0082\5\16\b\2\u0081\177")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\r\3\2\2\2\u0083\u0084")
        buf.write("\7\4\2\2\u0084\u0087\5\16\b\2\u0085\u0087\5\20\t\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0085\3\2\2\2\u0087\17\3\2\2\2\u0088")
        buf.write("\u0089\5(\25\2\u0089\u008a\5\b\5\2\u008a\u008b\5(\25\2")
        buf.write("\u008b\u008e\3\2\2\2\u008c\u008e\5(\25\2\u008d\u0088\3")
        buf.write("\2\2\2\u008d\u008c\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090")
        buf.write("\7-\2\2\u0090\u0094\b\n\1\2\u0091\u0092\7.\2\2\u0092\u0094")
        buf.write("\b\n\1\2\u0093\u008f\3\2\2\2\u0093\u0091\3\2\2\2\u0094")
        buf.write("\23\3\2\2\2\u0095\u0096\7/\2\2\u0096\u00a0\b\13\1\2\u0097")
        buf.write("\u0098\5\22\n\2\u0098\u0099\b\13\1\2\u0099\u00a0\3\2\2")
        buf.write("\2\u009a\u009b\7)\2\2\u009b\u00a0\b\13\1\2\u009c\u009d")
        buf.write("\7*\2\2\u009d\u00a0\b\13\1\2\u009e\u00a0\5\4\3\2\u009f")
        buf.write("\u0095\3\2\2\2\u009f\u0097\3\2\2\2\u009f\u009a\3\2\2\2")
        buf.write("\u009f\u009c\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\25\3\2")
        buf.write("\2\2\u00a1\u00a2\7\5\2\2\u00a2\u00a3\7\60\2\2\u00a3\u00a4")
        buf.write("\7\26\2\2\u00a4\u00a5\5&\24\2\u00a5\u00a6\7\27\2\2\u00a6")
        buf.write("\27\3\2\2\2\u00a7\u00a8\5\6\4\2\u00a8\u00ab\7\6\2\2\u00a9")
        buf.write("\u00ac\7\60\2\2\u00aa\u00ac\5\32\16\2\u00ab\u00a9\3\2")
        buf.write("\2\2\u00ab\u00aa\3\2\2\2\u00ac\31\3\2\2\2\u00ad\u00ae")
        buf.write("\7\7\2\2\u00ae\u00af\7\60\2\2\u00af\u00b0\7(\2\2\u00b0")
        buf.write("\u00b1\5(\25\2\u00b1\33\3\2\2\2\u00b2\u00b3\7\60\2\2\u00b3")
        buf.write("\u00b4\7#\2\2\u00b4\u00b5\5(\25\2\u00b5\u00b6\b\17\1\2")
        buf.write("\u00b6\u00bb\3\2\2\2\u00b7\u00b8\7\60\2\2\u00b8\u00b9")
        buf.write("\7#\2\2\u00b9\u00bb\5\6\4\2\u00ba\u00b2\3\2\2\2\u00ba")
        buf.write("\u00b7\3\2\2\2\u00bb\35\3\2\2\2\u00bc\u00bd\5\34\17\2")
        buf.write("\u00bd\u00be\7\31\2\2\u00be\u00bf\b\20\1\2\u00bf\37\3")
        buf.write("\2\2\2\u00c0\u00c2\5\36\20\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4!\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\7\60\2")
        buf.write("\2\u00c7\u00c8\7#\2\2\u00c8\u00c9\5\30\r\2\u00c9#\3\2")
        buf.write("\2\2\u00ca\u00cb\5\"\22\2\u00cb\u00cc\7\31\2\2\u00cc%")
        buf.write("\3\2\2\2\u00cd\u00d0\5\36\20\2\u00ce\u00d0\5$\23\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2")
        buf.write("\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\'\3\2\2")
        buf.write("\2\u00d3\u00d1\3\2\2\2\u00d4\u00d9\5*\26\2\u00d5\u00d6")
        buf.write("\t\3\2\2\u00d6\u00d8\5*\26\2\u00d7\u00d5\3\2\2\2\u00d8")
        buf.write("\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2")
        buf.write("\u00da)\3\2\2\2\u00db\u00d9\3\2\2\2\u00dc\u00e1\5,\27")
        buf.write("\2\u00dd\u00de\t\4\2\2\u00de\u00e0\5,\27\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2+\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4")
        buf.write("\u00e5\t\3\2\2\u00e5\u00e6\5,\27\2\u00e6\u00e7\b\27\1")
        buf.write("\2\u00e7\u00ec\3\2\2\2\u00e8\u00e9\5.\30\2\u00e9\u00ea")
        buf.write("\b\27\1\2\u00ea\u00ec\3\2\2\2\u00eb\u00e4\3\2\2\2\u00eb")
        buf.write("\u00e8\3\2\2\2\u00ec-\3\2\2\2\u00ed\u00f2\5\60\31\2\u00ee")
        buf.write("\u00ef\7\34\2\2\u00ef\u00f0\5,\27\2\u00f0\u00f1\b\30\1")
        buf.write("\2\u00f1\u00f3\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\b\30\1\2\u00f5")
        buf.write("/\3\2\2\2\u00f6\u00fa\5\62\32\2\u00f7\u00f9\5\64\33\2")
        buf.write("\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\61\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\7\60\2\2\u00fe\u0103\b\32\1\2\u00ff")
        buf.write("\u0100\5\24\13\2\u0100\u0101\b\32\1\2\u0101\u0103\3\2")
        buf.write("\2\2\u0102\u00fd\3\2\2\2\u0102\u00ff\3\2\2\2\u0103\63")
        buf.write("\3\2\2\2\u0104\u0106\7\22\2\2\u0105\u0107\5\66\34\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\7\23\2\2\u0109\u0112\b\33\1\2\u010a\u010b")
        buf.write("\7\24\2\2\u010b\u010c\7-\2\2\u010c\u010d\7\25\2\2\u010d")
        buf.write("\u0112\b\33\1\2\u010e\u010f\7&\2\2\u010f\u0110\7\60\2")
        buf.write("\2\u0110\u0112\b\33\1\2\u0111\u0104\3\2\2\2\u0111\u010a")
        buf.write("\3\2\2\2\u0111\u010e\3\2\2\2\u0112\65\3\2\2\2\u0113\u0118")
        buf.write("\58\35\2\u0114\u0115\7\30\2\2\u0115\u0117\58\35\2\u0116")
        buf.write("\u0114\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3")
        buf.write("\2\2\2\u011b\u011d\7\30\2\2\u011c\u011b\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\b\34\1")
        buf.write("\2\u011f\67\3\2\2\2\u0120\u0121\5\24\13\2\u0121\u0122")
        buf.write("\b\35\1\2\u0122\u0126\3\2\2\2\u0123\u0124\7\60\2\2\u0124")
        buf.write("\u0126\b\35\1\2\u0125\u0120\3\2\2\2\u0125\u0123\3\2\2")
        buf.write("\2\u01269\3\2\2\2\u0127\u012b\5<\37\2\u0128\u012b\5> ")
        buf.write("\2\u0129\u012b\5B\"\2\u012a\u0127\3\2\2\2\u012a\u0128")
        buf.write("\3\2\2\2\u012a\u0129\3\2\2\2\u012b;\3\2\2\2\u012c\u012d")
        buf.write("\7\t\2\2\u012d\u012e\7\22\2\2\u012e\u012f\7\60\2\2\u012f")
        buf.write("\u0130\7\n\2\2\u0130\u0131\5(\25\2\u0131\u0132\7\23\2")
        buf.write("\2\u0132\u0133\7\26\2\2\u0133\u0134\5@!\2\u0134\u0135")
        buf.write("\7\27\2\2\u0135=\3\2\2\2\u0136\u0137\7\13\2\2\u0137\u0138")
        buf.write("\7\22\2\2\u0138\u0139\5\n\6\2\u0139\u013a\7\23\2\2\u013a")
        buf.write("\u013b\7\26\2\2\u013b\u013c\5@!\2\u013c\u013d\7\27\2\2")
        buf.write("\u013d?\3\2\2\2\u013e\u013f\7\f\2\2\u013f\u0140\7\26\2")
        buf.write("\2\u0140\u0141\5 \21\2\u0141\u0142\7\27\2\2\u0142\u0144")
        buf.write("\3\2\2\2\u0143\u013e\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0146\5R*\2\u0146A\3\2\2\2\u0147")
        buf.write("\u0148\7\r\2\2\u0148\u0149\7\22\2\2\u0149\u014a\5\n\6")
        buf.write("\2\u014a\u014b\7\23\2\2\u014b\u014c\7\26\2\2\u014c\u014d")
        buf.write("\5R*\2\u014d\u014f\7\27\2\2\u014e\u0150\5D#\2\u014f\u014e")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150C\3\2\2\2\u0151\u0157")
        buf.write("\7\16\2\2\u0152\u0153\7\26\2\2\u0153\u0154\5R*\2\u0154")
        buf.write("\u0155\7\27\2\2\u0155\u0158\3\2\2\2\u0156\u0158\5B\"\2")
        buf.write("\u0157\u0152\3\2\2\2\u0157\u0156\3\2\2\2\u0158E\3\2\2")
        buf.write("\2\u0159\u015a\5H%\2\u015a\u015b\b$\1\2\u015b\u015f\3")
        buf.write("\2\2\2\u015c\u015f\5P)\2\u015d\u015f\5\26\f\2\u015e\u0159")
        buf.write("\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("G\3\2\2\2\u0160\u0165\5:\36\2\u0161\u0162\5J&\2\u0162")
        buf.write("\u0163\b%\1\2\u0163\u0165\3\2\2\2\u0164\u0160\3\2\2\2")
        buf.write("\u0164\u0161\3\2\2\2\u0165I\3\2\2\2\u0166\u016f\5L\'\2")
        buf.write("\u0167\u0168\5(\25\2\u0168\u0169\7\31\2\2\u0169\u016a")
        buf.write("\b&\1\2\u016a\u016f\3\2\2\2\u016b\u016c\5\36\20\2\u016c")
        buf.write("\u016d\b&\1\2\u016d\u016f\3\2\2\2\u016e\u0166\3\2\2\2")
        buf.write("\u016e\u0167\3\2\2\2\u016e\u016b\3\2\2\2\u016fK\3\2\2")
        buf.write("\2\u0170\u0171\7\17\2\2\u0171\u0172\5N(\2\u0172\u0173")
        buf.write("\7\31\2\2\u0173M\3\2\2\2\u0174\u0179\7\60\2\2\u0175\u0176")
        buf.write("\7\60\2\2\u0176\u0177\t\5\2\2\u0177\u0179\5N(\2\u0178")
        buf.write("\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0179O\3\2\2\2\u017a")
        buf.write("\u017b\7\21\2\2\u017b\u017c\7\60\2\2\u017c\u017d\7\22")
        buf.write("\2\2\u017d\u017e\5\66\34\2\u017e\u017f\7\23\2\2\u017f")
        buf.write("\u0180\7\26\2\2\u0180\u0181\5R*\2\u0181\u0182\7\27\2\2")
        buf.write("\u0182Q\3\2\2\2\u0183\u0185\5H%\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3")
        buf.write("\2\2\2\u0187S\3\2\2\2\u0188\u0186\3\2\2\2%Wbgu|\u0081")
        buf.write("\u0086\u008d\u0093\u009f\u00ab\u00ba\u00c3\u00cf\u00d1")
        buf.write("\u00d9\u00e1\u00eb\u00f2\u00fa\u0102\u0106\u0111\u0118")
        buf.write("\u011c\u0125\u012a\u0143\u014f\u0157\u015e\u0164\u016e")
        buf.write("\u0178\u0186")
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
    RULE_argument = 27
    RULE_compound_stmt = 28
    RULE_for_stmt = 29
    RULE_while_stmt = 30
    RULE_loop_suite = 31
    RULE_if_stmt = 32
    RULE_else_stmt = 33
    RULE_stmt = 34
    RULE_context_stmt = 35
    RULE_simple_stmt = 36
    RULE_import_stmt = 37
    RULE_dotted_name = 38
    RULE_funcdef_stmt = 39
    RULE_suite = 40

    ruleNames =  [ "script", "basic_list", "by_slice_list", "comparator", 
                   "or_test", "and_test", "not_test", "comparison", "number", 
                   "simple_literal", "parameter_set_stmt", "where_expr", 
                   "simple_lambda", "assignment", "assignment_stmt", "assignment_suite", 
                   "where_assignment", "where_assignemnt_stmt", "parameter_set_suite", 
                   "expr", "term", "factor", "power", "atom_expr", "atom", 
                   "trailer", "arglist", "argument", "compound_stmt", "for_stmt", 
                   "while_stmt", "loop_suite", "if_stmt", "else_stmt", "stmt", 
                   "context_stmt", "simple_stmt", "import_stmt", "dotted_name", 
                   "funcdef_stmt", "suite" ]

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
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__2) | (1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.T__14) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 82
                localctx._stmt = self.stmt()
                localctx.stmts.append(localctx._stmt)
                self.state = 87
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
            self.state = 90
            self.match(my_grammarParser.LSQPAR)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    localctx._expr = self.expr()
                    localctx.exprs.append(localctx._expr)
                    self.state = 92
                    self.match(my_grammarParser.COMMA) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.state = 99
                localctx._expr = self.expr()
                localctx.exprs.append(localctx._expr)
                pass
            elif token in [my_grammarParser.COMMA]:
                self.state = 100
                self.match(my_grammarParser.COMMA)
                pass
            elif token in [my_grammarParser.RSQPAR]:
                pass
            else:
                pass
            self.state = 103
            self.match(my_grammarParser.RSQPAR)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(my_grammarParser.COLON)
            else:
                return self.getToken(my_grammarParser.COLON, i)

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
                self.state = 105
                self.expr()
                self.state = 106
                self.match(my_grammarParser.COLON)
                self.state = 107
                self.expr()
                self.state = 108
                self.match(my_grammarParser.COLON)
                self.state = 109
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.expr()
                self.state = 112
                self.match(my_grammarParser.COLON)
                self.state = 113
                self.expr()
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LESS) | (1 << my_grammarParser.LESSEQUAL) | (1 << my_grammarParser.GREATER) | (1 << my_grammarParser.GREATEREQUAL) | (1 << my_grammarParser.NOTEQUAL) | (1 << my_grammarParser.DOUBLEEQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            self.state = 119
            self.and_test()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__0:
                self.state = 120
                self.match(my_grammarParser.T__0)
                self.state = 121
                self.and_test()


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
            self.state = 124
            self.not_test()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__1:
                self.state = 125
                self.match(my_grammarParser.T__1)
                self.state = 126
                self.not_test()


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
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(my_grammarParser.T__1)
                self.state = 130
                self.not_test()
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.comparison()
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
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.expr()
                self.state = 135
                self.comparator()
                self.state = 136
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.expr()
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
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NON_NEGATIVE_INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                localctx.myObj = Number.createNonNegativeInteger((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass
            elif token in [my_grammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                localctx._STRING = self.match(my_grammarParser.STRING)
                localctx.myObj = SimpleLiteral.createFromString((None if localctx._STRING is None else localctx._STRING.text))
                pass
            elif token in [my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                localctx._number = self.number()
                localctx.myObj = SimpleLiteral.createFromNumber(localctx._number.myObj)
                pass
            elif token in [my_grammarParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                localctx._BOOL = self.match(my_grammarParser.BOOL)
                localctx.myObj = SimpleLiteral.createFromBool((None if localctx._BOOL is None else localctx._BOOL.text))
                pass
            elif token in [my_grammarParser.NONE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(my_grammarParser.NONE)
                localctx.myObj = SimpleLiteral.createFromNone()
                pass
            elif token in [my_grammarParser.LSQPAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.basic_list()
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
            self.state = 159
            self.match(my_grammarParser.T__2)
            self.state = 160
            self.match(my_grammarParser.NAME)
            self.state = 161
            self.match(my_grammarParser.LBRACE)
            self.state = 162
            self.parameter_set_suite()
            self.state = 163
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
            self.state = 165
            self.by_slice_list()
            self.state = 166
            self.match(my_grammarParser.T__3)
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.state = 167
                self.match(my_grammarParser.NAME)
                pass
            elif token in [my_grammarParser.T__4]:
                self.state = 168
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
            self.state = 171
            self.match(my_grammarParser.T__4)
            self.state = 172
            self.match(my_grammarParser.NAME)
            self.state = 173
            self.match(my_grammarParser.COLON)
            self.state = 174
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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                localctx._NAME = self.match(my_grammarParser.NAME)
                self.state = 177
                self.match(my_grammarParser.EQUAL)
                self.state = 178
                localctx._expr = self.expr()
                localctx.myObj = Assignment.createFromExpr((None if localctx._NAME is None else localctx._NAME.text), localctx._expr.myObj)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(my_grammarParser.NAME)
                self.state = 182
                self.match(my_grammarParser.EQUAL)
                self.state = 183
                self.by_slice_list()
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
            self.state = 186
            localctx._assignment = self.assignment()
            self.state = 187
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
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 190
                self.assignment_stmt()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 196
            self.match(my_grammarParser.NAME)
            self.state = 197
            self.match(my_grammarParser.EQUAL)
            self.state = 198
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
            self.state = 200
            self.where_assignment()
            self.state = 201
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
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 203
                    self.assignment_stmt()
                    pass

                elif la_ == 2:
                    self.state = 204
                    self.where_assignemnt_stmt()
                    pass


                self.state = 209
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
            self._tset380 = None # Token
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
            self.state = 210
            localctx.t = self.term()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS:
                self.state = 211
                localctx._tset380 = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx._tset380 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.operators.append(localctx._tset380)
                self.state = 212
                localctx._term = self.term()
                localctx.operands.append(localctx._term)
                self.state = 217
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
            self._tset416 = None # Token
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
            self.state = 218
            localctx.f = self.factor()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0):
                self.state = 219
                localctx._tset416 = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0)):
                    localctx._tset416 = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                localctx.operators.append(localctx._tset416)
                self.state = 220
                localctx._factor = self.factor()
                localctx.operands.append(localctx._factor)
                self.state = 225
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
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.PLUS, my_grammarParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 227
                localctx._factor = self.factor()
                localctx.myObj = Factor.createFromFactor((None if localctx.sign is None else localctx.sign.text), localctx._factor.myObj)
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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
            self.state = 235
            localctx.a = self.atom_expr()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.DOUBLESTAR:
                self.state = 236
                self.match(my_grammarParser.DOUBLESTAR)
                self.state = 237
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
            self.state = 244
            localctx.a = self.atom()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LPAR) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.DOT))) != 0):
                self.state = 245
                localctx._trailer = self.trailer()
                localctx.trailers.append(localctx._trailer)
                self.state = 250
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
            self.state = 256
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                localctx._NAME = self.match(my_grammarParser.NAME)
                localctx.myObj = Atom.createFromName((None if localctx._NAME is None else localctx._NAME.text))
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(my_grammarParser.LPAR)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                    self.state = 259
                    localctx._arglist = self.arglist()


                self.state = 262
                self.match(my_grammarParser.RPAR)
                localctx.myObj = Trailer.createFromArglist(localctx._arglist.myObj)
                pass
            elif token in [my_grammarParser.LSQPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(my_grammarParser.LSQPAR)
                self.state = 265
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                self.state = 266
                self.match(my_grammarParser.RSQPAR)
                localctx.myObj = Trailer.createFromAccess((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass
            elif token in [my_grammarParser.DOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(my_grammarParser.DOT)
                self.state = 269
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
            self.arg = None # ArgumentContext
            self._argument = None # ArgumentContext
            self.args = list() # of ArgumentContexts

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(my_grammarParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(my_grammarParser.ArgumentContext,i)


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
            self.state = 273
            localctx.arg = self.argument()
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 274
                    self.match(my_grammarParser.COMMA)
                    self.state = 275
                    localctx._argument = self.argument()
                    localctx.args.append(localctx._argument) 
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.COMMA:
                self.state = 281
                self.match(my_grammarParser.COMMA)


            localctx.myObj = Arglist(tuple([localctx.arg.myObj] + [argument.myObj for argument in localctx.args]))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.myObj = None
            self._simple_literal = None # Simple_literalContext
            self._NAME = None # Token

        def simple_literal(self):
            return self.getTypedRuleContext(my_grammarParser.Simple_literalContext,0)


        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def getRuleIndex(self):
            return my_grammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = my_grammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_argument)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                localctx._simple_literal = self.simple_literal()
                localctx.myObj = Argument.createFromSimpleLiteral(localctx._simple_literal.myObj)
                pass
            elif token in [my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                localctx._NAME = self.match(my_grammarParser.NAME)
                localctx.myObj = Argument.createFromName((None if localctx._NAME is None else localctx._NAME.text))
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

    class Compound_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 56, self.RULE_compound_stmt)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.for_stmt()
                pass
            elif token in [my_grammarParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.while_stmt()
                pass
            elif token in [my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.if_stmt()
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
        self.enterRule(localctx, 58, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(my_grammarParser.T__6)
            self.state = 299
            self.match(my_grammarParser.LPAR)
            self.state = 300
            self.match(my_grammarParser.NAME)
            self.state = 301
            self.match(my_grammarParser.T__7)
            self.state = 302
            self.expr()
            self.state = 303
            self.match(my_grammarParser.RPAR)
            self.state = 304
            self.match(my_grammarParser.LBRACE)
            self.state = 305
            self.loop_suite()
            self.state = 306
            self.match(my_grammarParser.RBRACE)
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
        self.enterRule(localctx, 60, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(my_grammarParser.T__8)
            self.state = 309
            self.match(my_grammarParser.LPAR)
            self.state = 310
            self.or_test()
            self.state = 311
            self.match(my_grammarParser.RPAR)
            self.state = 312
            self.match(my_grammarParser.LBRACE)
            self.state = 313
            self.loop_suite()
            self.state = 314
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

        def suite(self):
            return self.getTypedRuleContext(my_grammarParser.SuiteContext,0)


        def LBRACE(self):
            return self.getToken(my_grammarParser.LBRACE, 0)

        def assignment_suite(self):
            return self.getTypedRuleContext(my_grammarParser.Assignment_suiteContext,0)


        def RBRACE(self):
            return self.getToken(my_grammarParser.RBRACE, 0)

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
        self.enterRule(localctx, 62, self.RULE_loop_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__9:
                self.state = 316
                self.match(my_grammarParser.T__9)
                self.state = 317
                self.match(my_grammarParser.LBRACE)
                self.state = 318
                self.assignment_suite()
                self.state = 319
                self.match(my_grammarParser.RBRACE)


            self.state = 323
            self.suite()
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
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(my_grammarParser.T__10)
            self.state = 326
            self.match(my_grammarParser.LPAR)
            self.state = 327
            self.or_test()
            self.state = 328
            self.match(my_grammarParser.RPAR)
            self.state = 329
            self.match(my_grammarParser.LBRACE)
            self.state = 330
            self.suite()
            self.state = 331
            self.match(my_grammarParser.RBRACE)
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__11:
                self.state = 332
                self.else_stmt()


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
        self.enterRule(localctx, 66, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(my_grammarParser.T__11)
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LBRACE]:
                self.state = 336
                self.match(my_grammarParser.LBRACE)
                self.state = 337
                self.suite()
                self.state = 338
                self.match(my_grammarParser.RBRACE)
                pass
            elif token in [my_grammarParser.T__10]:
                self.state = 340
                self.if_stmt()
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
        self.enterRule(localctx, 68, self.RULE_stmt)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10, my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                localctx._context_stmt = self.context_stmt()
                localctx.myObj = ContextStmt.createFromSimpleStmt(localctx._context_stmt.myObj)
                pass
            elif token in [my_grammarParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.funcdef_stmt()
                pass
            elif token in [my_grammarParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
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
        self.enterRule(localctx, 70, self.RULE_context_stmt)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.compound_stmt()
                pass
            elif token in [my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                localctx._simple_stmt = self.simple_stmt()
                localctx.myObj = SimpleStmt.createFromExpr(localctx._simple_stmt.myObj)
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
        self.enterRule(localctx, 72, self.RULE_simple_stmt)
        try:
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.import_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                localctx._expr = self.expr()
                self.state = 358
                self.match(my_grammarParser.SEMI)
                localctx.myObj = SimpleStmt.createFromExpr(localctx._expr.myObj)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361
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
        self.enterRule(localctx, 74, self.RULE_import_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(my_grammarParser.T__12)
            self.state = 367
            self.dotted_name()
            self.state = 368
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
        self.enterRule(localctx, 76, self.RULE_dotted_name)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(my_grammarParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.match(my_grammarParser.NAME)
                self.state = 372
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.T__13 or _la==my_grammarParser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 373
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
        self.enterRule(localctx, 78, self.RULE_funcdef_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(my_grammarParser.T__14)
            self.state = 377
            self.match(my_grammarParser.NAME)
            self.state = 378
            self.match(my_grammarParser.LPAR)
            self.state = 379
            self.arglist()
            self.state = 380
            self.match(my_grammarParser.RPAR)
            self.state = 381
            self.match(my_grammarParser.LBRACE)
            self.state = 382
            self.suite()
            self.state = 383
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
        self.enterRule(localctx, 80, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 385
                self.context_stmt()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





