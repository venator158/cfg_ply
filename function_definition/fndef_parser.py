import tkinter as tk
import io
import sys
import ply.yacc as yacc
from fndef_lexer import tokens  # Assuming fndec_lex contains the necessary tokens

# Define the parsing functions here
def p_function_declaration(p):
    '''function_declaration : TYPE IDENTIFIER parameter_list SEMICOLON'''
    print("Valid function declaration:", p[1], p[2], p[3])

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

def p_error(p):
    print("Syntax error at '%s'" % p.value if p else "Syntax error at EOF")

parser = yacc.yacc()

class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Declaration Validator")
        self.root.geometry("600x400")

        self.input_label = tk.Label(root, text="Enter a function declaration:")
        self.input_label.pack(pady=10)
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()

        self.validate_button = tk.Button(root, text="Validate", command=self.validate_declaration)
        self.validate_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=50, state='disabled')
        self.output_text.pack()

    def validate_declaration(self):
        input_string = self.input_text.get("1.0", tk.END).strip()

        if not input_string.endswith(";"):
            self.display_result("Error: Function declaration must end with a semicolon.", "red")
            return

        old_stdout = sys.stdout
        sys.stdout = result_capture = io.StringIO()

        try:
            parser.parse(input_string)
            result = result_capture.getvalue().strip()
            self.display_result("Parsing succeeded. The function declaration is valid.", "green")
        except Exception as e:
            self.display_result(f"Parsing failed: {str(e)}", "red")
        finally:
            sys.stdout = old_stdout

    def display_result(self, message, color):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()