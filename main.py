from antlr4 import *
from gen.mashLexer import mashLexer  # Import your visitor class
from antlr4.InputStream import InputStream
from mashVisitorCustom import mashParser
from mashVisitorCustom import mashVisitorCustom


def main():
    # Input string to parse
    # input_str = 'echo $(((10/2)+7+2*3))'
    # input_str = 'echo $(((10/2)+7+2*3))  \n echo "hej"'
    # # Create an ANTLR input stream from the input string
    # input_stream = InputStream(input_str)
    input_stream = FileStream("test.mash")
    # Create a lexer and parser
    lexer = mashLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = mashParser(token_stream)

    parser.removeErrorListeners()
    # parser.addErrorListener(MyErrorListener())

    try:
        tree = parser.program()
    except SyntaxError as e:
        print(e)
        exit(1)

    visitor = mashVisitorCustom()
    visitor.visit(tree)
    # parser = mashParser(token_stream)
    #
    # # Parse the input to generate the parse tree
    # parse_tree = parser.program()
    #
    # # Create an instance of YourVisitorClass
    # visitor = mashVisitorCustom()
    #
    # # Visit the parse tree with the visitor
    # visitor_result = visitor.visit(parse_tree)

    # # Output the result (if any)
    # print("Visitor result:", visitor_result)


if __name__ == '__main__':
    main()
