import tkinter as tk
import ply.yacc as yacc
from fndef_lexer import tokens

 
function_context = {}

 

 
def p_function_declaration(p):
    '''function_declaration : TYPE IDENTIFIER parameter_list SEMICOLON
                            | function_definition'''
    if len(p) == 5:   
        print("Valid function declaration:", p[1], p[2], p[3])
    elif len(p) == 2:   
        print("Valid function definition:", p[1])

def p_function_definition(p):
    '''function_definition : TYPE IDENTIFIER parameter_list LBRACE statement_list RBRACE'''
    expected_type = p[1]
    function_context[p[2]] = expected_type   
    print("Function Defined:", p[0])

def p_parameter_list(p):
    '''parameter_list : LPAREN parameter_declarations RPAREN
                      | LPAREN RPAREN'''
    p[0] = p[2] if len(p) == 4 else []   

def p_parameter_declarations(p):
    '''parameter_declarations : parameter_declaration
                              | parameter_declaration COMMA parameter_declarations'''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]   

def p_parameter_declaration(p):
    'parameter_declaration : TYPE IDENTIFIER'
    p[0] = (p[1], p[2])   

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]   

def p_statement(p):
    '''statement : RETURN expression SEMICOLON
                 | RETURN SEMICOLON
                 | IDENTIFIER ASSIGN expression SEMICOLON
                 | empty'''
    
    if p[1] == 'return':
        expected_type = function_context.get(p[-1], None)   
        if expected_type == 'void' and len(p) == 4:   
            raise SyntaxError("Void function cannot return a value.")
        elif expected_type != 'void' and len(p) == 3:   
            raise SyntaxError("Expected return value for non-void function.")
        
         
        if len(p) > 1 and not p[-1].endswith(';'):
            raise SyntaxError("Statement must end with a semicolon.")

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER'''
    p[0] = p[1]   

def p_empty(p):
    'empty :'
    pass

 
def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

 
parser = yacc.yacc()

 
def validate_declaration():
    input_string = text_box.get("1.0", tk.END).strip()   

     
    if not (input_string.endswith(";") or input_string.endswith("}")):
        result_label.config(text="Error: Function declaration must end with a semicolon or brace.", fg="red")
        return

     
    import io
    import sys
    old_stdout = sys.stdout
    sys.stdout = result_capture = io.StringIO()

     
    try:
        parser.parse(input_string)
        result = result_capture.getvalue().strip()
        result_label.config(text="Parsing succeeded. The function declaration is valid.", fg="green")
    except Exception as e:
        result_label.config(text=f"Parsing failed: {str(e)}", fg="red")
    finally:
         
        sys.stdout = old_stdout

 
root = tk.Tk()
root.title("Function Declaration and Definition Validator")

 
tk.Label(root, text="Enter a function declaration or definition:").pack(pady=5)
text_box = tk.Text(root, width=60, height=10)   
text_box.pack(pady=5)

 
validate_button = tk.Button(root, text="Validate", command=validate_declaration)
validate_button.pack(pady=5)

 
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

 
root.mainloop()
