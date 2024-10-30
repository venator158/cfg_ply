import ply.yacc as yacc
from if_lexer import tokens  # Import tokens and lexer from lexer.py

# Grammar rules

def p_program(p):
    '''program : statement_list'''
    print("Parsed program.")

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | statement'''
    pass

# Rule for standalone if statement
def p_if_statement(p):
    '''statement : IF expression COLON
                 | IF expression COLON NEWLINE'''
    print(f"Parsed 'if' statement with condition: {p[2]}")

# Rule for standalone elif
def p_elif_statement(p):
    '''statement : ELIF expression COLON
                 | ELIF expression COLON NEWLINE'''
    print(f"Parsed 'elif' statement with condition: {p[2]}")

# Rule for standalone else
def p_else_statement(p):
    '''statement : ELSE COLON
                 | ELSE COLON NEWLINE'''
    print("Parsed 'else' statement")

def p_expression_comparison(p):
    '''expression : expression GREATER expression
                  | expression LESSER expression
                  | expression GREATER_EQUALS expression
                  | expression LESSER_EQUALS expression
                  | IDENTIFIER
                  | NUMBER'''
    if len(p) == 4:  # Handling comparison expressions
        p[0] = f"({p[1]} {p[2]} {p[3]})"  # Store the comparison expression
    else:
        p[0] = p[1]  # Handling identifiers or numbers

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF: Possibly missing ':' or invalid statement.")

# Build the parser
parser = yacc.yacc(debug=True)  # Enable debug to provide more information

# Function to process input code
def process_code(input_code):
    try:
        print("\nParsing result:")
        parser.parse(input_code)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    while True:
        print("\nType 'exit' to quit.")
        user_input = input("Do you want to enter code? (y/n): ").lower()
        if user_input == "n" or user_input == "exit":
            break
        elif user_input == "y":
            # Accept user input code here
            input_code = input("Enter your code: ")
            process_code(input_code)
