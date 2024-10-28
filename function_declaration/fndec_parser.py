import tkinter as tk
from tkinter import messagebox
import ply.yacc as yacc
from fndec_lex import tokens

# Grammar rules for parsing

# Start symbol
def p_function_declaration(p):
    'function_declaration : TYPE IDENTIFIER parameter_list SEMICOLON'
    print("Valid function declaration:", p[1], p[2], p[3])

def p_parameter_list(p):
    '''parameter_list : LPAREN parameter_declarations RPAREN
                      | LPAREN RPAREN'''
    if len(p) == 4:
        p[0] = p[2]  # Non-empty parameter list
    else:
        p[0] = []  # Empty parameter list

def p_parameter_declarations(p):
    '''parameter_declarations : parameter_declaration
                              | parameter_declaration COMMA parameter_declarations'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_parameter_declaration(p):
    'parameter_declaration : TYPE IDENTIFIER'
    p[0] = (p[1], p[2])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Function to validate the function declaration
def validate_declaration():
    input_string = entry.get().strip()
    
    # Basic validation check
    if not input_string.endswith(";"):
        result_label.config(text="Error: Function declaration must end with a semicolon.", fg="red")
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
root.title("Function Declaration Validator")

# Input field
tk.Label(root, text="Enter a function declaration:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Validate button
validate_button = tk.Button(root, text="Validate", command=validate_declaration)
validate_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
