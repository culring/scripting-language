# Generated from my_grammar.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u0182\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\3\3\3\3\3\3\3\7\3_\n\3\f\3\16\3b\13\3\3\3\3\3\5\3")
        buf.write("f\n\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4u\n\4\3\5\3\5\3\6\3\6\3\6\5\6|\n\6\3\7\3\7\3\7")
        buf.write("\5\7\u0081\n\7\3\b\3\b\3\b\5\b\u0086\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u008d\n\t\3\n\3\n\3\n\3\n\5\n\u0093\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00a3\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00af\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\5\17\u00ba\n\17\3\20\3\20\3\20\3\21")
        buf.write("\7\21\u00c0\n\21\f\21\16\21\u00c3\13\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\7\24\u00ce\n\24\f\24\16")
        buf.write("\24\u00d1\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00d9")
        buf.write("\n\25\f\25\16\25\u00dc\13\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\7\26\u00e4\n\26\f\26\16\26\u00e7\13\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u00f0\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u00f8\n\30\3\31\3\31\7\31\u00fc")
        buf.write("\n\31\f\31\16\31\u00ff\13\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\5\32\u0107\n\32\3\33\3\33\5\33\u010b\n\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u0113\n\33\3\34\3\34\3\34")
        buf.write("\7\34\u0118\n\34\f\34\16\34\u011b\13\34\3\34\5\34\u011e")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0125\n\35\3\36\3")
        buf.write("\36\3\36\5\36\u012a\n\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\5!\u0143\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\5\"\u014f\n\"\3#\3#\3#\3#\3#\3#\5#\u0157\n#\3$\3$\3")
        buf.write("$\5$\u015c\n$\3%\3%\5%\u0160\n%\3&\3&\3&\3&\3&\5&\u0167")
        buf.write("\n&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\5(\u0171\n(\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\7*\u017d\n*\f*\16*\u0180\13*\3*\2")
        buf.write("\2+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPR\2\6\4\2\37\"$%\3\2\32\33\5\2\b")
        buf.write("\b\35\36\'\'\4\2\20\20&&\2\u0185\2W\3\2\2\2\4Z\3\2\2\2")
        buf.write("\6t\3\2\2\2\bv\3\2\2\2\nx\3\2\2\2\f}\3\2\2\2\16\u0085")
        buf.write("\3\2\2\2\20\u008c\3\2\2\2\22\u0092\3\2\2\2\24\u00a2\3")
        buf.write("\2\2\2\26\u00a4\3\2\2\2\30\u00aa\3\2\2\2\32\u00b0\3\2")
        buf.write("\2\2\34\u00b5\3\2\2\2\36\u00bb\3\2\2\2 \u00c1\3\2\2\2")
        buf.write("\"\u00c4\3\2\2\2$\u00c8\3\2\2\2&\u00cf\3\2\2\2(\u00d2")
        buf.write("\3\2\2\2*\u00dd\3\2\2\2,\u00ef\3\2\2\2.\u00f1\3\2\2\2")
        buf.write("\60\u00f9\3\2\2\2\62\u0106\3\2\2\2\64\u0112\3\2\2\2\66")
        buf.write("\u0114\3\2\2\28\u0124\3\2\2\2:\u0129\3\2\2\2<\u012b\3")
        buf.write("\2\2\2>\u0135\3\2\2\2@\u0142\3\2\2\2B\u0146\3\2\2\2D\u0150")
        buf.write("\3\2\2\2F\u015b\3\2\2\2H\u015f\3\2\2\2J\u0166\3\2\2\2")
        buf.write("L\u0168\3\2\2\2N\u0170\3\2\2\2P\u0172\3\2\2\2R\u017e\3")
        buf.write("\2\2\2TV\5F$\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2")
        buf.write("X\3\3\2\2\2YW\3\2\2\2Z`\7\24\2\2[\\\5(\25\2\\]\7\30\2")
        buf.write("\2]_\3\2\2\2^[\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a")
        buf.write("e\3\2\2\2b`\3\2\2\2cf\5(\25\2df\7\30\2\2ec\3\2\2\2ed\3")
        buf.write("\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7\25\2\2hi\b\3\1\2i\5\3\2")
        buf.write("\2\2jk\5(\25\2kl\7(\2\2lm\5(\25\2mn\7(\2\2no\5(\25\2o")
        buf.write("u\3\2\2\2pq\5(\25\2qr\7(\2\2rs\5(\25\2su\3\2\2\2tj\3\2")
        buf.write("\2\2tp\3\2\2\2u\7\3\2\2\2vw\t\2\2\2w\t\3\2\2\2x{\5\f\7")
        buf.write("\2yz\7\3\2\2z|\5\f\7\2{y\3\2\2\2{|\3\2\2\2|\13\3\2\2\2")
        buf.write("}\u0080\5\16\b\2~\177\7\4\2\2\177\u0081\5\16\b\2\u0080")
        buf.write("~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\r\3\2\2\2\u0082\u0083")
        buf.write("\7\4\2\2\u0083\u0086\5\16\b\2\u0084\u0086\5\20\t\2\u0085")
        buf.write("\u0082\3\2\2\2\u0085\u0084\3\2\2\2\u0086\17\3\2\2\2\u0087")
        buf.write("\u0088\5(\25\2\u0088\u0089\5\b\5\2\u0089\u008a\5(\25\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u008d\5(\25\2\u008c\u0087\3")
        buf.write("\2\2\2\u008c\u008b\3\2\2\2\u008d\21\3\2\2\2\u008e\u008f")
        buf.write("\7-\2\2\u008f\u0093\b\n\1\2\u0090\u0091\7.\2\2\u0091\u0093")
        buf.write("\b\n\1\2\u0092\u008e\3\2\2\2\u0092\u0090\3\2\2\2\u0093")
        buf.write("\23\3\2\2\2\u0094\u0095\7/\2\2\u0095\u00a3\b\13\1\2\u0096")
        buf.write("\u0097\7-\2\2\u0097\u00a3\b\13\1\2\u0098\u0099\5\22\n")
        buf.write("\2\u0099\u009a\b\13\1\2\u009a\u00a3\3\2\2\2\u009b\u009c")
        buf.write("\7)\2\2\u009c\u00a3\b\13\1\2\u009d\u009e\7*\2\2\u009e")
        buf.write("\u00a3\b\13\1\2\u009f\u00a0\5\4\3\2\u00a0\u00a1\b\13\1")
        buf.write("\2\u00a1\u00a3\3\2\2\2\u00a2\u0094\3\2\2\2\u00a2\u0096")
        buf.write("\3\2\2\2\u00a2\u0098\3\2\2\2\u00a2\u009b\3\2\2\2\u00a2")
        buf.write("\u009d\3\2\2\2\u00a2\u009f\3\2\2\2\u00a3\25\3\2\2\2\u00a4")
        buf.write("\u00a5\7\5\2\2\u00a5\u00a6\7\60\2\2\u00a6\u00a7\7\26\2")
        buf.write("\2\u00a7\u00a8\5&\24\2\u00a8\u00a9\7\27\2\2\u00a9\27\3")
        buf.write("\2\2\2\u00aa\u00ab\5\6\4\2\u00ab\u00ae\7\6\2\2\u00ac\u00af")
        buf.write("\7\60\2\2\u00ad\u00af\5\32\16\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\31\3\2\2\2\u00b0\u00b1\7\7\2\2\u00b1")
        buf.write("\u00b2\7\60\2\2\u00b2\u00b3\7(\2\2\u00b3\u00b4\5(\25\2")
        buf.write("\u00b4\33\3\2\2\2\u00b5\u00b6\7\60\2\2\u00b6\u00b9\7#")
        buf.write("\2\2\u00b7\u00ba\5(\25\2\u00b8\u00ba\5\6\4\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\35\3\2\2\2\u00bb\u00bc")
        buf.write("\5\34\17\2\u00bc\u00bd\7\31\2\2\u00bd\37\3\2\2\2\u00be")
        buf.write("\u00c0\5\36\20\2\u00bf\u00be\3\2\2\2\u00c0\u00c3\3\2\2")
        buf.write("\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2!\3\2")
        buf.write("\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5\7\60\2\2\u00c5\u00c6")
        buf.write("\7#\2\2\u00c6\u00c7\5\30\r\2\u00c7#\3\2\2\2\u00c8\u00c9")
        buf.write("\5\"\22\2\u00c9\u00ca\7\31\2\2\u00ca%\3\2\2\2\u00cb\u00ce")
        buf.write("\5\36\20\2\u00cc\u00ce\5$\23\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\'\3\2\2\2\u00d1\u00cf\3\2\2")
        buf.write("\2\u00d2\u00d3\5*\26\2\u00d3\u00da\b\25\1\2\u00d4\u00d5")
        buf.write("\t\3\2\2\u00d5\u00d6\5*\26\2\u00d6\u00d7\b\25\1\2\u00d7")
        buf.write("\u00d9\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9\u00dc\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db)\3\2\2")
        buf.write("\2\u00dc\u00da\3\2\2\2\u00dd\u00de\5,\27\2\u00de\u00e5")
        buf.write("\b\26\1\2\u00df\u00e0\t\4\2\2\u00e0\u00e1\5,\27\2\u00e1")
        buf.write("\u00e2\b\26\1\2\u00e2\u00e4\3\2\2\2\u00e3\u00df\3\2\2")
        buf.write("\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6+\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9")
        buf.write("\t\3\2\2\u00e9\u00ea\5,\27\2\u00ea\u00eb\b\27\1\2\u00eb")
        buf.write("\u00f0\3\2\2\2\u00ec\u00ed\5.\30\2\u00ed\u00ee\b\27\1")
        buf.write("\2\u00ee\u00f0\3\2\2\2\u00ef\u00e8\3\2\2\2\u00ef\u00ec")
        buf.write("\3\2\2\2\u00f0-\3\2\2\2\u00f1\u00f2\5\60\31\2\u00f2\u00f7")
        buf.write("\b\30\1\2\u00f3\u00f4\7\34\2\2\u00f4\u00f5\5,\27\2\u00f5")
        buf.write("\u00f6\b\30\1\2\u00f6\u00f8\3\2\2\2\u00f7\u00f3\3\2\2")
        buf.write("\2\u00f7\u00f8\3\2\2\2\u00f8/\3\2\2\2\u00f9\u00fd\5\62")
        buf.write("\32\2\u00fa\u00fc\5\64\33\2\u00fb\u00fa\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0100\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\b")
        buf.write("\31\1\2\u0101\61\3\2\2\2\u0102\u0107\7\60\2\2\u0103\u0104")
        buf.write("\5\24\13\2\u0104\u0105\b\32\1\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u0102\3\2\2\2\u0106\u0103\3\2\2\2\u0107\63\3\2\2\2\u0108")
        buf.write("\u010a\7\22\2\2\u0109\u010b\5\66\34\2\u010a\u0109\3\2")
        buf.write("\2\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0113")
        buf.write("\7\23\2\2\u010d\u010e\7\24\2\2\u010e\u010f\7-\2\2\u010f")
        buf.write("\u0113\7\25\2\2\u0110\u0111\7&\2\2\u0111\u0113\7\60\2")
        buf.write("\2\u0112\u0108\3\2\2\2\u0112\u010d\3\2\2\2\u0112\u0110")
        buf.write("\3\2\2\2\u0113\65\3\2\2\2\u0114\u0119\58\35\2\u0115\u0116")
        buf.write("\7\30\2\2\u0116\u0118\58\35\2\u0117\u0115\3\2\2\2\u0118")
        buf.write("\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2")
        buf.write("\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011e\7")
        buf.write("\30\2\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\67\3\2\2\2\u011f\u0125\5\24\13\2\u0120\u0125\7\60\2\2")
        buf.write("\u0121\u0122\7\60\2\2\u0122\u0123\7#\2\2\u0123\u0125\5")
        buf.write("(\25\2\u0124\u011f\3\2\2\2\u0124\u0120\3\2\2\2\u0124\u0121")
        buf.write("\3\2\2\2\u01259\3\2\2\2\u0126\u012a\5<\37\2\u0127\u012a")
        buf.write("\5> \2\u0128\u012a\5B\"\2\u0129\u0126\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u0128\3\2\2\2\u012a;\3\2\2\2\u012b\u012c")
        buf.write("\7\t\2\2\u012c\u012d\7\22\2\2\u012d\u012e\7\60\2\2\u012e")
        buf.write("\u012f\7\n\2\2\u012f\u0130\5(\25\2\u0130\u0131\7\23\2")
        buf.write("\2\u0131\u0132\7\26\2\2\u0132\u0133\5@!\2\u0133\u0134")
        buf.write("\7\27\2\2\u0134=\3\2\2\2\u0135\u0136\7\13\2\2\u0136\u0137")
        buf.write("\7\22\2\2\u0137\u0138\5\n\6\2\u0138\u0139\7\23\2\2\u0139")
        buf.write("\u013a\7\26\2\2\u013a\u013b\5@!\2\u013b\u013c\7\27\2\2")
        buf.write("\u013c?\3\2\2\2\u013d\u013e\7\f\2\2\u013e\u013f\7\26\2")
        buf.write("\2\u013f\u0140\5 \21\2\u0140\u0141\7\27\2\2\u0141\u0143")
        buf.write("\3\2\2\2\u0142\u013d\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\3\2\2\2\u0144\u0145\5R*\2\u0145A\3\2\2\2\u0146")
        buf.write("\u0147\7\r\2\2\u0147\u0148\7\22\2\2\u0148\u0149\5\n\6")
        buf.write("\2\u0149\u014a\7\23\2\2\u014a\u014b\7\26\2\2\u014b\u014c")
        buf.write("\5R*\2\u014c\u014e\7\27\2\2\u014d\u014f\5D#\2\u014e\u014d")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014fC\3\2\2\2\u0150\u0156")
        buf.write("\7\16\2\2\u0151\u0152\7\26\2\2\u0152\u0153\5R*\2\u0153")
        buf.write("\u0154\7\27\2\2\u0154\u0157\3\2\2\2\u0155\u0157\5B\"\2")
        buf.write("\u0156\u0151\3\2\2\2\u0156\u0155\3\2\2\2\u0157E\3\2\2")
        buf.write("\2\u0158\u015c\5H%\2\u0159\u015c\5P)\2\u015a\u015c\5\26")
        buf.write("\f\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a")
        buf.write("\3\2\2\2\u015cG\3\2\2\2\u015d\u0160\5:\36\2\u015e\u0160")
        buf.write("\5J&\2\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160I")
        buf.write("\3\2\2\2\u0161\u0167\5L\'\2\u0162\u0163\5(\25\2\u0163")
        buf.write("\u0164\7\31\2\2\u0164\u0167\3\2\2\2\u0165\u0167\5\36\20")
        buf.write("\2\u0166\u0161\3\2\2\2\u0166\u0162\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167K\3\2\2\2\u0168\u0169\7\17\2\2\u0169\u016a")
        buf.write("\5N(\2\u016a\u016b\7\31\2\2\u016bM\3\2\2\2\u016c\u0171")
        buf.write("\7\60\2\2\u016d\u016e\7\60\2\2\u016e\u016f\t\5\2\2\u016f")
        buf.write("\u0171\5N(\2\u0170\u016c\3\2\2\2\u0170\u016d\3\2\2\2\u0171")
        buf.write("O\3\2\2\2\u0172\u0173\7\21\2\2\u0173\u0174\7\60\2\2\u0174")
        buf.write("\u0175\7\22\2\2\u0175\u0176\5\66\34\2\u0176\u0177\7\23")
        buf.write("\2\2\u0177\u0178\7\26\2\2\u0178\u0179\5R*\2\u0179\u017a")
        buf.write("\7\27\2\2\u017aQ\3\2\2\2\u017b\u017d\5H%\2\u017c\u017b")
        buf.write("\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017fS\3\2\2\2\u0180\u017e\3\2\2\2%W`e")
        buf.write("t{\u0080\u0085\u008c\u0092\u00a2\u00ae\u00b9\u00c1\u00cd")
        buf.write("\u00cf\u00da\u00e5\u00ef\u00f7\u00fd\u0106\u010a\u0112")
        buf.write("\u0119\u011d\u0124\u0129\u0142\u014e\u0156\u015b\u015f")
        buf.write("\u0166\u0170\u017e")
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
                self.stmt()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.value = None
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
            localctx.value = [e.value for e in localctx.exprs]
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
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.expr()
                self.state = 105
                self.match(my_grammarParser.COLON)
                self.state = 106
                self.expr()
                self.state = 107
                self.match(my_grammarParser.COLON)
                self.state = 108
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.expr()
                self.state = 111
                self.match(my_grammarParser.COLON)
                self.state = 112
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
            self.state = 116
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
            self.state = 118
            self.and_test()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__0:
                self.state = 119
                self.match(my_grammarParser.T__0)
                self.state = 120
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
            self.state = 123
            self.not_test()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__1:
                self.state = 124
                self.match(my_grammarParser.T__1)
                self.state = 125
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
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(my_grammarParser.T__1)
                self.state = 129
                self.not_test()
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
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
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.expr()
                self.state = 134
                self.comparator()
                self.state = 135
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
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
            self.value = None
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
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NON_NEGATIVE_INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                localctx.value = int((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass
            elif token in [my_grammarParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                localctx._FLOAT = self.match(my_grammarParser.FLOAT)
                localctx.value = float((None if localctx._FLOAT is None else localctx._FLOAT.text))
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
            self.value = None
            self._STRING = None # Token
            self._NON_NEGATIVE_INTEGER = None # Token
            self._number = None # NumberContext
            self._BOOL = None # Token
            self._basic_list = None # Basic_listContext

        def STRING(self):
            return self.getToken(my_grammarParser.STRING, 0)

        def NON_NEGATIVE_INTEGER(self):
            return self.getToken(my_grammarParser.NON_NEGATIVE_INTEGER, 0)

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
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                localctx._STRING = self.match(my_grammarParser.STRING)
                localctx.value =  str((None if localctx._STRING is None else localctx._STRING.text))
                localctx.value = localctx.value[1:-1]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                localctx._NON_NEGATIVE_INTEGER = self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                localctx.value = int((None if localctx._NON_NEGATIVE_INTEGER is None else localctx._NON_NEGATIVE_INTEGER.text))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                localctx._number = self.number()
                localctx.value = localctx._number.value
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 153
                localctx._BOOL = self.match(my_grammarParser.BOOL)
                localctx.value = bool((None if localctx._BOOL is None else localctx._BOOL.text))
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(my_grammarParser.NONE)
                localctx.value = None
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 157
                localctx._basic_list = self.basic_list()
                localctx.value = localctx._basic_list.value
                pass


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
            self.state = 162
            self.match(my_grammarParser.T__2)
            self.state = 163
            self.match(my_grammarParser.NAME)
            self.state = 164
            self.match(my_grammarParser.LBRACE)
            self.state = 165
            self.parameter_set_suite()
            self.state = 166
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
            self.state = 168
            self.by_slice_list()
            self.state = 169
            self.match(my_grammarParser.T__3)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.state = 170
                self.match(my_grammarParser.NAME)
                pass
            elif token in [my_grammarParser.T__4]:
                self.state = 171
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
            self.state = 174
            self.match(my_grammarParser.T__4)
            self.state = 175
            self.match(my_grammarParser.NAME)
            self.state = 176
            self.match(my_grammarParser.COLON)
            self.state = 177
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
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(my_grammarParser.NAME)
            self.state = 180
            self.match(my_grammarParser.EQUAL)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 181
                self.expr()
                pass

            elif la_ == 2:
                self.state = 182
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
            self.state = 185
            self.assignment()
            self.state = 186
            self.match(my_grammarParser.SEMI)
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
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 188
                self.assignment_stmt()
                self.state = 193
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
            self.state = 194
            self.match(my_grammarParser.NAME)
            self.state = 195
            self.match(my_grammarParser.EQUAL)
            self.state = 196
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
            self.state = 198
            self.where_assignment()
            self.state = 199
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
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.NAME:
                self.state = 203
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 201
                    self.assignment_stmt()
                    pass

                elif la_ == 2:
                    self.state = 202
                    self.where_assignemnt_stmt()
                    pass


                self.state = 207
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
            self.value = None
            self._term = None # TermContext
            self.o = None # Token

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
            self.state = 208
            localctx._term = self.term()
            localctx.value = localctx._term.value
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS:
                self.state = 210
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211
                localctx._term = self.term()
                if localctx.o.type == my_grammarParser.PLUS:
                    localctx.value += localctx._term.value
                else:
                    localctx.value -= localctx._term.value
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)

            print(localctx.value)
                
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
            self.value = None
            self._factor = None # FactorContext
            self.op = None # Token

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
            self.state = 219
            localctx._factor = self.factor()
            localctx.value = localctx._factor.value
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0):
                self.state = 221
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__5) | (1 << my_grammarParser.STAR) | (1 << my_grammarParser.SLASH) | (1 << my_grammarParser.PERCENT))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                localctx._factor = self.factor()

                if localctx.op.type == my_grammarParser.STAR:
                    localctx.value *= localctx._factor.value
                elif localctx.op.type == my_grammarParser.SLASH:
                    localctx.value /= localctx._factor.value
                elif localctx.op.type == my_grammarParser.PERCENT:
                    localctx.value %= localctx._factor.value
                elif localctx.op.text == '//':
                    localctx.value //= localctx._factor.value
                    
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.value = None
            self.op = None # Token
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.PLUS, my_grammarParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.PLUS or _la==my_grammarParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                localctx._factor = self.factor()
                localctx.value = -localctx._factor.value if (0 if localctx.op is None else localctx.op.type() == my_grammarParser.MINUS) else localctx._factor.value
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                localctx._power = self.power()
                localctx.value = localctx._power.value
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
            self.value = None
            self._atom_expr = None # Atom_exprContext
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
            self.state = 239
            localctx._atom_expr = self.atom_expr()
            localctx.value = localctx._atom_expr.value
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.DOUBLESTAR:
                self.state = 241
                self.match(my_grammarParser.DOUBLESTAR)
                self.state = 242
                localctx._factor = self.factor()
                localctx.value **= localctx._factor.value


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
            self.value = None
            self._atom = None # AtomContext

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
            self.state = 247
            localctx._atom = self.atom()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LPAR) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.DOT))) != 0):
                self.state = 248
                self.trailer()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            localctx.value = localctx._atom.value
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
            self.value = None
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
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(my_grammarParser.NAME)
                pass
            elif token in [my_grammarParser.LSQPAR, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                localctx._simple_literal = self.simple_literal()
                localctx.value = localctx._simple_literal.value
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
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(my_grammarParser.LPAR)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                    self.state = 263
                    self.arglist()


                self.state = 266
                self.match(my_grammarParser.RPAR)
                pass
            elif token in [my_grammarParser.LSQPAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(my_grammarParser.LSQPAR)
                self.state = 268
                self.match(my_grammarParser.NON_NEGATIVE_INTEGER)
                self.state = 269
                self.match(my_grammarParser.RSQPAR)
                pass
            elif token in [my_grammarParser.DOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.match(my_grammarParser.DOT)
                self.state = 271
                self.match(my_grammarParser.NAME)
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
            self.state = 274
            self.argument()
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 275
                    self.match(my_grammarParser.COMMA)
                    self.state = 276
                    self.argument() 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.COMMA:
                self.state = 282
                self.match(my_grammarParser.COMMA)


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

        def simple_literal(self):
            return self.getTypedRuleContext(my_grammarParser.Simple_literalContext,0)


        def NAME(self):
            return self.getToken(my_grammarParser.NAME, 0)

        def EQUAL(self):
            return self.getToken(my_grammarParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(my_grammarParser.ExprContext,0)


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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.simple_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(my_grammarParser.NAME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(my_grammarParser.NAME)
                self.state = 288
                self.match(my_grammarParser.EQUAL)
                self.state = 289
                self.expr()
                pass


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
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.for_stmt()
                pass
            elif token in [my_grammarParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.while_stmt()
                pass
            elif token in [my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
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
            self.state = 297
            self.match(my_grammarParser.T__6)
            self.state = 298
            self.match(my_grammarParser.LPAR)
            self.state = 299
            self.match(my_grammarParser.NAME)
            self.state = 300
            self.match(my_grammarParser.T__7)
            self.state = 301
            self.expr()
            self.state = 302
            self.match(my_grammarParser.RPAR)
            self.state = 303
            self.match(my_grammarParser.LBRACE)
            self.state = 304
            self.loop_suite()
            self.state = 305
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
            self.state = 307
            self.match(my_grammarParser.T__8)
            self.state = 308
            self.match(my_grammarParser.LPAR)
            self.state = 309
            self.or_test()
            self.state = 310
            self.match(my_grammarParser.RPAR)
            self.state = 311
            self.match(my_grammarParser.LBRACE)
            self.state = 312
            self.loop_suite()
            self.state = 313
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
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__9:
                self.state = 315
                self.match(my_grammarParser.T__9)
                self.state = 316
                self.match(my_grammarParser.LBRACE)
                self.state = 317
                self.assignment_suite()
                self.state = 318
                self.match(my_grammarParser.RBRACE)


            self.state = 322
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
            self.state = 324
            self.match(my_grammarParser.T__10)
            self.state = 325
            self.match(my_grammarParser.LPAR)
            self.state = 326
            self.or_test()
            self.state = 327
            self.match(my_grammarParser.RPAR)
            self.state = 328
            self.match(my_grammarParser.LBRACE)
            self.state = 329
            self.suite()
            self.state = 330
            self.match(my_grammarParser.RBRACE)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==my_grammarParser.T__11:
                self.state = 331
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
            self.state = 334
            self.match(my_grammarParser.T__11)
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.LBRACE]:
                self.state = 335
                self.match(my_grammarParser.LBRACE)
                self.state = 336
                self.suite()
                self.state = 337
                self.match(my_grammarParser.RBRACE)
                pass
            elif token in [my_grammarParser.T__10]:
                self.state = 339
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
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10, my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.context_stmt()
                pass
            elif token in [my_grammarParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.funcdef_stmt()
                pass
            elif token in [my_grammarParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
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
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [my_grammarParser.T__6, my_grammarParser.T__8, my_grammarParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.compound_stmt()
                pass
            elif token in [my_grammarParser.T__12, my_grammarParser.LSQPAR, my_grammarParser.PLUS, my_grammarParser.MINUS, my_grammarParser.BOOL, my_grammarParser.NONE, my_grammarParser.NON_NEGATIVE_INTEGER, my_grammarParser.FLOAT, my_grammarParser.STRING, my_grammarParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.simple_stmt()
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
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.import_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.expr()
                self.state = 353
                self.match(my_grammarParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.assignment_stmt()
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
            self.state = 358
            self.match(my_grammarParser.T__12)
            self.state = 359
            self.dotted_name()
            self.state = 360
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
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(my_grammarParser.NAME)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.match(my_grammarParser.NAME)
                self.state = 364
                _la = self._input.LA(1)
                if not(_la==my_grammarParser.T__13 or _la==my_grammarParser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 365
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
            self.state = 368
            self.match(my_grammarParser.T__14)
            self.state = 369
            self.match(my_grammarParser.NAME)
            self.state = 370
            self.match(my_grammarParser.LPAR)
            self.state = 371
            self.arglist()
            self.state = 372
            self.match(my_grammarParser.RPAR)
            self.state = 373
            self.match(my_grammarParser.LBRACE)
            self.state = 374
            self.suite()
            self.state = 375
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
            self.state = 380
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << my_grammarParser.T__6) | (1 << my_grammarParser.T__8) | (1 << my_grammarParser.T__10) | (1 << my_grammarParser.T__12) | (1 << my_grammarParser.LSQPAR) | (1 << my_grammarParser.PLUS) | (1 << my_grammarParser.MINUS) | (1 << my_grammarParser.BOOL) | (1 << my_grammarParser.NONE) | (1 << my_grammarParser.NON_NEGATIVE_INTEGER) | (1 << my_grammarParser.FLOAT) | (1 << my_grammarParser.STRING) | (1 << my_grammarParser.NAME))) != 0):
                self.state = 377
                self.context_stmt()
                self.state = 382
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





