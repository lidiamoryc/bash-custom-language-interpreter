from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4 import ParserRuleContext
from antlr4.tree.Tree import ParseTree, TerminalNodeImpl

from gen.mashLexer import mashLexer
from gen.mashParser import mashParser
from gen.mashListener import mashListener

import sys

class CustomListener(mashListener):
    def enterVar_declar(self, ctx):
        print("Variable declaration:", ctx.getText())


def main():
    input_code = "int_var x=5"  # Your input code here

    lexer = mashLexer(InputStream(input_code))
    tokens = CommonTokenStream(lexer)
    parser = mashParser(tokens)
    tree = parser.program()

    listener = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()