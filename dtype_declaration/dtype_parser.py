# dtype_parser.py
import tkinter as tk
from tkinter import messagebox
from dtype_lexer import lexer

# CFG rules for parsing (simplified)
def parse(tokens):
    try:
        # Expecting a sequence: Type (Optional Pointer) Identifier (Optional Assignment) ;
        idx = 0
        
        # Check for TYPE
        if tokens[idx][0] == 'TYPE':
            idx += 1
        else:
            return "Error: Expected data type at the beginning."

        # Optional POINTER
        if idx < len(tokens) and tokens[idx][0] == 'POINTER':
            idx += 1

        # Check for IDENTIFIER
        if idx < len(tokens) and tokens[idx][0] == 'IDENTIFIER':
            idx += 1
        else:
            return "Error: Expected an identifier after type."

        # Optional ASSIGN and VALUE
        if idx < len(tokens) and tokens[idx][0] == 'ASSIGN':
            idx += 1
            if idx < len(tokens) and tokens[idx][0] in {'INT_VALUE', 'FLOAT_VALUE', 'CHAR_VALUE', 'STRING_VALUE'}:
                idx += 1
            else:
                return "Error: Expected a value after '='."

        # Check for SEMICOLON
        if idx < len(tokens) and tokens[idx][0] == 'SEMICOLON':
            return "Parsed successfully: Valid declaration."
        else:
            return "Error: Expected ';' at the end of declaration."

    except IndexError:
        return "Error: Incomplete declaration."
    return "Error: Invalid declaration syntax."

# GUI setup
class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C Data Type Declaration Parser")
        self.root.geometry("600x400")

        # Input text area
        self.input_label = tk.Label(root, text="Enter C Data Type Declaration:")
        self.input_label.pack(pady=10)
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()

        # Parse button
        self.parse_button = tk.Button(root, text="Parse", command=self.parse_declaration)
        self.parse_button.pack(pady=10)

        # Output label
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=50, state='disabled')
        self.output_text.pack()

    def parse_declaration(self):
        # Get input code and tokenize it
        input_code = self.input_text.get("1.0", tk.END).strip()
        tokens = lexer(input_code)
        
        # Parse tokens
        result = parse(tokens)
        
        # Display result
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')

# Run the parser GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()
