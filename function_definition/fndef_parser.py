import tkinter as tk
import ply.yacc as yacc
from fndef_lexer import tokens

# Global variable to hold function context
function_context = {}

# Grammar rules for parsing

# Start symbol for function declaration and definition
def p_function_declaration(p):
    '''function_declaration : TYPE IDENTIFIER parameter_list SEMICOLON
                            | function_definition'''
    if len(p) == 5:  # Function declaration
        print("Valid function declaration:", p[1], p[2], p[3])
    elif len(p) == 2:  # Function definition
        print("Valid function definition:", p[1])

def p_function_definition(p):
    '''function_definition : TYPE IDENTIFIER parameter_list LBRACE statement_list RBRACE'''
    expected_type = p[1]
    function_context[p[2]] = expected_type  # Store the return type in context
    print("Function Defined:", p[0])

def p_parameter_list(p):
    '''parameter_list : LPAREN parameter_declarations RPAREN
                      | LPAREN RPAREN'''
    p[0] = p[2] if len(p) == 4 else []  # Set to parameter declarations or empty

def p_parameter_declarations(p):
    '''parameter_declarations : parameter_declaration
                              | parameter_declaration COMMA parameter_declarations'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]  # Build parameter list

def p_parameter_declaration(p):
    'parameter_declaration : TYPE IDENTIFIER'
    p[0] = (p[1], p[2])  # Return type and identifier

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]  # Build list of statements

def p_statement(p):
    '''statement : RETURN expression SEMICOLON
                 | RETURN SEMICOLON
                 | IDENTIFIER ASSIGN expression SEMICOLON
                 | empty'''
    
    if p[1] == 'return':
        expected_type = function_context.get(p[-1], None)  # Get the expected return type
        if expected_type == 'void' and len(p) == 4:  # Check for return with value
            raise SyntaxError("Void function cannot return a value.")
        elif expected_type != 'void' and len(p) == 3:  # If not void, need an expression
            raise SyntaxError("Expected return value for non-void function.")
        
        # If there are expressions, validate that they end with a semicolon
        if len(p) > 1 and not p[-1].endswith(';'):
            raise SyntaxError("Statement must end with a semicolon.")

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER'''
    p[0] = p[1]  # Return the identifier or number

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Function to validate the function declaration
def validate_declaration():
    input_string = text_box.get("1.0", tk.END).strip()  # Get text from text box

    # Basic validation check
    if not (input_string.endswith(";") or input_string.endswith("}")):
        result_label.config(text="Error: Function declaration must end with a semicolon or brace.", fg="red")
        return

    # Temporarily redirect stdout to capture `print` output from parsing
    import io
    import sys
    old_stdout = sys.stdout
    sys.stdout = result_capture = io.StringIO()

    # Attempt parsing
    try:
        parser.parse(input_string)
        result = result_capture.getvalue().strip()
        result_label.config(text="Parsing succeeded. The function declaration is valid.", fg="green")
    except Exception as e:
        result_label.config(text=f"Parsing failed: {str(e)}", fg="red")
    finally:
        # Restore original stdout
        sys.stdout = old_stdout

# GUI setup
root = tk.Tk()
root.title("Function Declaration and Definition Validator")

# Input field
tk.Label(root, text="Enter a function declaration or definition:").pack(pady=5)
text_box = tk.Text(root, width=60, height=10)  # Use a Text widget for multi-line input
text_box.pack(pady=5)

# Validate button
validate_button = tk.Button(root, text="Validate", command=validate_declaration)
validate_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
