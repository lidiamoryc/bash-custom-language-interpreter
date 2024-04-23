import warnings

from antlr4 import *

from gen.mashParser import mashParser
from gen.mashVisitor import mashVisitor

class mashVisitorCustom(mashVisitor):
    def __int__(self):
        self.variables = {}

    def visitProgram(self, ctx: mashParser.ProgramContext):
        # Initialize a list to store the result of visiting each statement
        # program_result = []
        #
        # # Iterate over each statement in the program
        # for statement_ctx in ctx.getChildren():
        #     # Visit the statement and append the result to the program result list
        #     statement_result = self.visit(statement_ctx)
        #     program_result.append(statement_result)
        #
        # # Return the list of results for each statement in the program
        # return program_result
        result = []
        for statement in ctx.statement():
            result.append(self.visit(statement))
        return result

    def visitStatement(self, ctx: mashParser.StatementContext):
        # self.visitEcho_function(ctx.echo_function)
        return self.visitChildren(ctx)

    def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
        # echoed_value = self.visit(ctx.expression())
        # print(echoed_value)
        # expression = ctx.expression()
        result = self.visit(ctx.expression())

        if isinstance(result, str):
            print(result.strip('"'))  # Strip quotes if it's a string
        elif isinstance(result, int):
            print(result)
        return result

    def visitExpression(self, ctx: mashParser.ExpressionContext):
        if ctx.arithmetic_expression():
            return self.visit(ctx.arithmetic_expression())
        elif ctx.string_expression():
            return self.visit(ctx.string_expression())
        return None

    def visitArithmetic_expression(self, ctx: mashParser.Arithmetic_expressionContext):
        return self.visit(ctx.additive_expression())

    def visitAdditive_expression(self, ctx: mashParser.Additive_expressionContext):
        # If there's a single child, return its evaluation
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        # Visit left and right expressions with the operator
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        # Handle addition and subtraction
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right

    def visitMultiplicative_expression(self, ctx: mashParser.Multiplicative_expressionContext):
        # If there's a single child, return its evaluation
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        # Visit left and right expressions with the operator
        left = self.visit(ctx.getChild(0))
        operator = ctx.getChild(1).getText()
        right = self.visit(ctx.getChild(2))

        # Handle multiplication and division
        if operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise ValueError("Division by zero!")
            return left / right

    def visitPrimary_expression(self, ctx: mashParser.Primary_expressionContext):
        # # If there's an INTEGER, convert to integer
        # if ctx.INTEGER():
        #     return int(ctx.INTEGER().getText())
        # # Otherwise, recursively evaluate nested expressions
        # return self.visit(ctx.getChild(0))
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.getChildCount() == 3:  # Handles brackets (e.g., (expression))
            return self.visit(ctx.getChild(1))  # Visit the inner expression

        return None

    # def visitNumeric_expression(self, ctx: mashParser.Numeric_expressionContext):
    #     if ctx.INTEGER():
    #         return int(ctx.INTEGER().getText())
    #
    #     left = self.visit(ctx.getChild(0))
    #     operator = ctx.getChild(1).getText()
    #     right = self.visit(ctx.getChild(2))
    #
    #     # Handle different arithmetic operations
    #     if operator == '+':
    #         return left + right
    #     elif operator == '-':
    #         return left - right
    #     elif operator == '*':
    #         return left * right
    #     elif operator == '/':
    #         if right == 0:
    #             raise ValueError("Division by zero!")
    #         return left / right






    #     print(type(ctx))
    #     # if len(ctx.INTEGER()) == 1:
    #     #     return int(ctx.INTEGER()[0].getText())
    #     # else:
    #
    #
    #         #(ctx.getChildCount() == 3):  # $((
    #         # num1 = int(ctx.getChild(1).getText())
    #         # num2 = int(ctx.getChild(3).getText())
    #
    #     if ctx.getChild(1) and ctx.getChild(1).getText() == '+':
    #         left = self.visit(ctx.getChild(0))  # Odwiedź lewe poddrzewo
    #         right = self.visit(ctx.getChild(2))  # Odwiedź prawe poddrzewo
    #         return left + right  # Zwróć sumę lewego i prawego poddrzewa
    #
    # # Sprawdzamy, czy kontekst reprezentuje odejmowanie
    #     elif ctx.getChild(1) and ctx.getChild(1).getText() == '-':
    #         left = self.visit(ctx.getChild(0))  # Odwiedź lewe poddrzewo
    #         right = self.visit(ctx.getChild(2))  # Odwiedź prawe poddrzewo
    #         return left - right  # Zwróć różnicę lewego i prawego poddrzewa
    #
    # # Sprawdzamy, czy kontekst reprezentuje mnożenie
    #     elif ctx.getChild(1) and ctx.getChild(1).getText() == '*':
    #         left = self.visit(ctx.getChild(0))  # Odwiedź lewe poddrzewo
    #         right = self.visit(ctx.getChild(2))  # Odwiedź prawe poddrzewo
    #         return left * right  # Zwróć iloczyn lewego i prawego poddrzewa
    #
    # # Sprawdzamy, czy kontekst reprezentuje dzielenie
    #     elif ctx.getChild(1) and ctx.getChild(1).getText() == '/':
    #         left = self.visit(ctx.getChild(0))  # Odwiedź lewe poddrzewo
    #         right = self.visit(ctx.getChild(2))  # Odwiedź prawe poddrzewo
    #         if right != 0:
    #             return left / right  # Zwróć wynik dzielenia lewego przez prawe poddrzewo
    #         else:
    #             raise ValueError("Dzielenie przez zero!")
    #
    #     else:
    #     # Jeśli to nie jest operacja arytmetyczna, zwróć wartość
    #         return self.visit(ctx.getChild(0))

            # sum = 0
            # print(len(ctx.INTEGER()))
            # kind_of_operation = None
            # for i in range(1, 2 * len(ctx.INTEGER())):
            #     if (i % 2 == 1):
            #         num = int(ctx.getChild(i).getText())
            #         if kind_of_operation == '+':
            #             sum += num
            #         elif kind_of_operation == '-':
            #             sum -= num
            #         elif kind_of_operation == '*':
            #             sum *= num
            #         else:
            #             if sum != 0:
            #                 sum /= num # dla 0 warunki
            #
            #     else:
            #         kind_of_operation == ctx.getChild(i).getText()
            #
            #
            # return str(sum)



            # ctx.INTEGER().pop(1)
            # num1 = ctx.INTEGER()[0]
            # num2 = int(ctx.INTEGER()[1])

        #return None

    def visitString_expression(self, ctx: mashParser.String_expressionContext):
        return ctx.STRING().getText()

    #     # def visitEcho_statement(self, ctx: mashParser.Echo_statementContext):
    #     #     # Get the value to be echoed by visiting the child context
    #     #     echoed_value = self.visit(ctx.sentence())
    #     #
    #     #     print(echoed_value)
    #     # Print the echoed value if it's a string
    #     # if isinstance(echoed_value, str):
    #     #     print(echoed_value)
    #     # else:
    #     # If echoed_value is not a string, print an error message
    #     # print("Error: Echo statement should echo a string value.")
    #
    #     # Return None as there's no specific return value for echo statements
    #     return None
    #
    # # def visitPrint_string_statement(self, ctx: mashParser.Print_string_statementContext):
    # #     # Get the string value from the context
    # #     string_value = ctx.string_value().getText()
    # #
    # #     # Print the string value
    # #     print(string_value[2:-1])
    # #
    # #     # Return None as there's no specific return value for print statements
    # #     return None

#######################

# def __init__(self):
#     self.symbol_table = {}  # To store variables and their values
#
# # Visit a parse tree produced by mashParser#program.
# def visitProgram(self, ctx: mashParser.ProgramContext):
#     # Visit each statement in the program
#     for statement in ctx.statement():
#         self.visit(statement)
#
# # Visit a parse tree produced by mashParser#statement.
# def visitStatement(self, ctx: mashParser.StatementContext):
#     if ctx.echo_function():
#         return self.visit(ctx.echo_function())
#     elif ctx.var_declar():
#         return self.visit(ctx.var_declar())
#
# # Visit a parse tree produced by mashParser#echo_function.
# def visitEcho_function(self, ctx: mashParser.Echo_functionContext):
#     expression = ctx.expression()
#     result = self.visit(expression)
#     if isinstance(result, str):
#         print(result.strip('"'))  # Strip quotes if it's a string
#     elif isinstance(result, int):
#         print(result)
#     return result
#
# # Visit a parse tree produced by mashParser#expression.
# def visitExpression(self, ctx: mashParser.ExpressionContext):
#     if ctx.numeric_expression():
#         return self.visit(ctx.numeric_expression())
#     elif ctx.string_expression():
#         return self.visit(ctx.string_expression())
#     return None
#
# # Visit a parse tree produced by mashParser#numeric_expression.
# def visitNumeric_expression(self, ctx: mashParser.Numeric_expressionContext):
#     if ctx.INTEGER():
#         return int(ctx.INTEGER().getText())
#     elif ctx.getChildCount() == 3:  # $((
#         num1 = int(ctx.getChild(1).getText())
#         num2 = int(ctx.getChild(2).getText())
#         return num1 + num2
#     return None
#
# # Visit a parse tree produced by mashParser#string_expression.
# def visitString_expression(self, ctx: mashParser.String_expressionContext):
#     return ctx.STRING().getText()
#
# # Visit a parse tree produced by mashParser#var_declar.
# def visitVar_declar(self, ctx: mashParser.Var_declarContext):
#     var_type = ctx.type().getText()
#     identifier = ctx.IDENTIFIER().getText()
#
#     if ctx.expression():
#         expression_result = self.visit(ctx.expression())
#         self.symbol_table[identifier] = expression_result
#     else:
#         self.symbol_table[identifier] = None
#     return identifier
