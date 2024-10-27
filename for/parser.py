import ply.yacc as yacc
from lexer import tokens  # Importing tokens and lexer

# Grammar rules
def p_for_loop(p):
    '''for_loop : FOR IDENTIFIER IN func_call COLON'''
    print(f"Parsed a for loop with iterator '{p[2]}' and iterable '{p[4]}'.")

def p_func_call_one_arg(p):
    '''func_call : IDENTIFIER LPAREN expression RPAREN'''
    p[0] = f"{p[1]}({p[3]})"

def p_func_call_two_args(p):
    '''func_call : IDENTIFIER LPAREN expression COMMA expression RPAREN'''
    p[0] = f"{p[1]}({p[3]}, {p[5]})"

def p_func_call_three_args(p):
    '''func_call : IDENTIFIER LPAREN expression COMMA expression COMMA expression RPAREN'''
    p[0] = f"{p[1]}({p[3]}, {p[5]}, {p[7]})"

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = p[1]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_statement_assignment(p):
    '''statement : IDENTIFIER EQUALS expression'''
    print(f"Parsed assignment: {p[1]} = {p[3]}")

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF: Possibly missing ':' at the end of the 'for' loop")

# Build the parser
parser = yacc.yacc()

# Function to process input code
def process_code(input_code):
    # Parse the input
    print("\nParsing result:")
    try:
        parser.parse(input_code)
    except SyntaxError as e:
        print(e)

# Main loop to input code interactively
if __name__ == "__main__":
    while True:
        print("\nEnter your Python code to parse (or type 'exit' to quit):")
        line = input()
        if line.lower() == "exit":
            break
        process_code(line)
