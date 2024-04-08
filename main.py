# from antlr4 import *

#
# class PrintStatementVisitor(ParseTreeVisitor):
#     def visitStatement(self, ctx:PrintStatementParser.StatementContext):
#         print(ctx.getText())
#
# def main():
#     input_stream = InputStream("echo Hello")
#     lexer = PrintStatementLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = PrintStatementParser(token_stream)
#     tree = parser.program()
#
#     visitor = PrintStatementVisitor()
#     visitor.visit(tree)
#
# if __name__ == '__main__':
#     main()