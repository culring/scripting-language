from antlr4 import *
from grammar.my_grammarLexer import my_grammarLexer
import unittest
import os
import sys

from grammar.my_grammarParser import my_grammarParser


def getValueToNameDict(lexer):
    tokensNames = {}
    for attr in my_grammarLexer.__dict__.items():
        if attr[0].isupper() and type(attr[1]) is int:
            tokensNames[attr[1]] = attr[0]
    return tokensNames


class LexerTest(unittest.TestCase):
    def getAllSymbolicNames(self, data):
        filename = 'in0.txt'
        with open(filename, 'w') as file:
            file.write(data)
        stream = FileStream(filename)
        lexer = my_grammarLexer(stream)
        tokens = lexer.getAllTokens()
        os.remove(filename)
        tokensNames = getValueToNameDict(my_grammarLexer)
        return [tokensNames[token.type] for token in tokens]

    def test_isTokenizedCorrectly1(self):
        data = '''
            while(i <= 3){
                a = 2;
            }
        '''
        expected = [
            'T__8', 'LPAR', 'NAME', 'LESSEQUAL', 'NON_NEGATIVE_INTEGER',
            'RPAR', 'LBRACE', 'NAME', 'EQUAL', 'NON_NEGATIVE_INTEGER',
            'SEMI', 'RBRACE'
        ]
        symbolicNames = self.getAllSymbolicNames(data)
        self.assertEqual(symbolicNames, expected)

    def test_isTokenizedCorrectly2(self):
        data = '''
            a = a+3**3;
        '''
        expected = [
            'NAME', 'EQUAL', 'NAME', 'PLUS', 'NON_NEGATIVE_INTEGER',
            'DOUBLESTAR', 'NON_NEGATIVE_INTEGER', 'SEMI'
        ]
        symbolicNames = self.getAllSymbolicNames(data)
        self.assertEqual(symbolicNames, expected)

    def test_isTokenizedCorrectly3(self):
        data = '''
            if(a == True){
                log("a is True");
            }
        '''
        expected = [
            'T__10', 'LPAR', 'NAME', 'DOUBLEEQUAL', 'BOOL',
            'RPAR', 'LBRACE', 'NAME', 'LPAR','STRING',
            'RPAR', 'SEMI', 'RBRACE'
        ]
        symbolicNames = self.getAllSymbolicNames(data)
        self.assertEqual(symbolicNames, expected)


def main():
    inputStream = FileStream("operations.txt")
    lexer = my_grammarLexer(inputStream)
    stream = CommonTokenStream(lexer)
    parser = my_grammarParser(stream)
    parser.script()

    # if len(sys.argv) <= 1:
    #     unittest.main()
    # else:
    #     stream = FileStream(sys.argv[1])
    #     lexer = my_grammarLexer(stream)
    #     tokens = lexer.getAllTokens()
    #     tokensNames = getValueToNameDict(my_grammarLexer)
    #     tokensValues = [(tokensNames[token.type], token.text) for token in tokens]
    #     columnWidth = max([max(len(e1), len(e2)) for e1, e2 in tokensValues]) + 2
    #     for values in tokensValues:
    #         output = ''.join(word.ljust(columnWidth) for word in values)
    #         print(output)


if __name__ == '__main__':
    main()