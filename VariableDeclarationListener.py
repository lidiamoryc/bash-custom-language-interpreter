from antlr4 import *
from gen.VariableLangLexer import VariableLangLexer
from gen.VariableLangParser import VariableLangParser
from gen.VariableLangListener import VariableLangListener

class VariableDeclarationListener(VariableLangListener):
    def __init__(self):
        self.variables = {}
        self.errors = []

    def enterVarDeclaration(self, ctx:VariableLangParser.VarDeclarationContext):
        identifier = ctx.IDENTIFIER().getText()
        if identifier in self.variables:
            raise Exception(f"Zmienna '{identifier}' została już zadeklarowana")
        self.variables[identifier] = None  # Zarejestruj zmienną bez wartości


