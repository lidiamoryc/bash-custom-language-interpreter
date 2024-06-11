from antlr4 import *
from gen.mashLexer import mashLexer
from gen.mashParser import mashParser
from mashVisitorCustom import mashVisitorCustom
from antlr4.InputStream import InputStream
from antlr4.FileStream import FileStream
from antlr4.error.ErrorListener import ErrorListener  # Import ErrorListener


class CustomSyntaxError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise CustomSyntaxError(f"Line {line}:{column} {msg}")


def main():
    input_stream = FileStream("test3.mash")
    lexer = mashLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = mashParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        tree = parser.program()
    except CustomSyntaxError as e:
        print(f"Syntax Error: {e.message}")
        exit(1)

    visitor = mashVisitorCustom()
    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"Runtime Error: {e}")


if __name__ == '__main__':
    main()
