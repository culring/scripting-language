from antlr4 import *
from my_grammarLexer import my_grammarLexer
import unittest
import os
import sys


class LexerTest(unittest.TestCase):
    def getAllSymbolicNames(self, data):
        filename = 'in0.txt'
        with open(filename, 'w') as file:
            file.write(data)
        stream = FileStream(filename)
        lexer = my_grammarLexer(stream)
        tokens = lexer.getAllTokens()
        os.remove(filename)
        return [value[0] for value in [(lexer.symbolicNames[token.type], token.text) for token in tokens]]

    def test_isTokenizedCorrectly1(self):
        data = '''
            while(i <= 3){
                a = 2;
            }
        '''
        expected = [
            'NAME', 'LPAR', 'NAME', 'LESSEQUAL', 'NUMBER', 'RPAR',
            'LBRACE', 'NAME', 'EQUAL', 'NUMBER', 'SEMI', 'RBRACE'
        ]
        symbolicNames = self.getAllSymbolicNames(data)
        self.assertEqual(symbolicNames, expected)

    def test_isTokenizedCorrectly2(self):
        data = '''
            a = a+3**3;
        '''
        expected = [
            'NAME', 'EQUAL', 'NAME', 'PLUS', 'NUMBER', 'DOUBLESTAR',
            'NUMBER', 'SEMI'
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
            'NAME', 'LPAR', 'NAME', 'DOUBLEEQUAL', 'NAME',
            'RPAR', 'LBRACE', 'NAME', 'LPAR', 'STRING', 'RPAR',
            'SEMI', 'RBRACE'
        ]
        symbolicNames = self.getAllSymbolicNames(data)
        self.assertEqual(symbolicNames, expected)


def main():
    stream = FileStream(sys.argv[1])
    lexer = my_grammarLexer(stream)
    tokens = lexer.getAllTokens()
    tokensValues = [(lexer.symbolicNames[token.type], token.text) for token in tokens]
    columnWidth = max([max(len(e1), len(e2)) for e1, e2 in tokensValues]) + 2
    for values in tokensValues:
        output = ''.join(word.ljust(columnWidth) for word in values)
        print(output)


if __name__ == '__main__':
    main()
    # unittest.main()