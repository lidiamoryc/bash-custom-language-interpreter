from antlr4 import *
from gen.mashLexer import mashLexer  # Import your visitor class
from antlr4.InputStream import InputStream
from mashVisitorCustom import mashParser
from mashVisitorCustom import mashVisitorCustom

def main():
    # Input string to parse
    input_str = 'print "Dzien dobry polsko z tej strony alex "'

    """
     MAMY ECHO ALE JA ZROBIŁAM SOBIE TEGO PRINTA POMOCNICZO, ŻEBY ZOBACZYC CO MAMY NIE TAK
     I TEN PRINT ŚREDNIO DZIAŁA, ALE PRZYNAJMNIEJ DZIAŁA, NATOMIAST ECHO NIE DZIAŁA, PRZEZ JAKIŚ BŁĄD W GRAMATYCE
    PRZY PRINCIE MAM OSTRZEŻENIE: 
    line 1:5 extraneous input ' ' expecting '"'
    """

    # Create an ANTLR input stream from the input string
    input_stream = InputStream(input_str)

    # Create a lexer and parser
    lexer = mashLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = mashParser(token_stream)

    # Parse the input to generate the parse tree
    parse_tree = parser.program()

    # Create an instance of YourVisitorClass
    visitor = mashVisitorCustom()

    # Visit the parse tree with the visitor
    visitor_result = visitor.visit(parse_tree)

    # # Output the result (if any)
    # print("Visitor result:", visitor_result)

if __name__ == '__main__':
    main()