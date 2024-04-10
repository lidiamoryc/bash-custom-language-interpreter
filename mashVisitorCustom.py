import warnings

from antlr4 import *

from gen.mashParser import mashParser
from gen.mashVisitor import mashVisitor

class mashVisitorCustom(mashVisitor):
    def __int__(self):
        self.variables = {}


    def visitProgram(self, ctx: mashParser.ProgramContext):
        # Initialize a list to store the result of visiting each statement
        program_result = []

        # Iterate over each statement in the program
        for statement_ctx in ctx.getChildren():
            # Visit the statement and append the result to the program result list
            statement_result = self.visit(statement_ctx)
            program_result.append(statement_result)

        # Return the list of results for each statement in the program
        return program_result

    def visitEcho_statement(self, ctx: mashParser.Echo_statementContext):
        # Get the value to be echoed by visiting the child context
        echoed_value = self.visit(ctx.sentence())

        # Print the echoed value if it's a string
        if isinstance(echoed_value, str):
            print(echoed_value)
        else:
            # If echoed_value is not a string, print an error message
            print("Error: Echo statement should echo a string value.")

        # Return None as there's no specific return value for echo statements
        return None

    def visitPrint_string_statement(self, ctx: mashParser.Print_string_statementContext):
        # Get the string value from the context
        string_value = ctx.string_value().getText()

        # Remove the surrounding double quotes
        string_value = string_value[2:-1]

        # Print the string value
        print(string_value)

        # Return None as there's no specific return value for print statements
        return None

