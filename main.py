from gen.VariableLangLexer import VariableLangLexer  # Lexer dla języka
from gen.VariableLangParser import VariableLangParser  # Parser dla języka
from gen.VariableLangListener import VariableLangListener  # Listener bazowy generowany przez ANTLR
from gen.VariableLangVisitor import VariableLangVisitor
from antlr4 import *

from VariableDeclarationListener import VariableDeclarationListener  # Klasa listenera dla deklaracji zmiennych
from VariableOperationVisitor import VariableOperationVisitor

def main():
    input_stream = InputStream('int_var x; x = 5; int_var y; y = x + 3;')
    # int_var x; x = 5; y = x + 3;
    # int_var a; a = 10; int_var a; a = 20;'
    lexer = VariableLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VariableLangParser(stream)
    tree = parser.program()

    # Pierwszy przebieg: deklaracje
    declarationListener = VariableDeclarationListener()
    walker = ParseTreeWalker()
    try:
        walker.walk(declarationListener, tree)
        # Sprawdźmy, czy nie wystąpiły błędy podczas deklaracji
        if declarationListener.errors:
            print("Errors found during declaration:")
            for error in declarationListener.errors:
                print(error)
    except Exception as e:
        print(f"Error during declaration phase: {str(e)}")

    # Drugi przebieg: wykonanie
    if not declarationListener.errors:  # Wykonuj tylko, jeśli nie ma błędów deklaracji
        operationVisitor = VariableOperationVisitor(declarationListener.variables)
        try:
            operationVisitor.visit(tree)
            print(operationVisitor.variables)
        except Exception as e:
            print(f"Runtime error: {str(e)}")

if __name__ == '__main__':
    main()
