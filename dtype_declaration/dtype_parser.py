import tkinter as tk
from tkinter import messagebox
import re

def parse(tokens):
    try:
        idx = 0
        
        # Check for identifier (variable name)
        if idx < len(tokens) and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', tokens[idx]):
            idx += 1
        else:
            return "Error: Expected a valid identifier (variable name) at the beginning."

        # Check for assignment operator
        if idx < len(tokens) and tokens[idx] == '=':
            idx += 1
        else:
            return "Error: Expected '=' after identifier."

        # Check for value (can be an integer, float, string, etc.)
        if idx < len(tokens) and re.match(r'^\d+(\.\d+)?|\'[^\']*\'|"[^"]*"$', tokens[idx]):
            idx += 1
        else:
            return "Error: Expected a value after '='."

        # Check for optional semicolon (not required in Python but can be included)
        if idx < len(tokens) and tokens[idx] == ';':
            idx += 1

        return "Parsed successfully: Valid declaration."
    
    except IndexError:
        return "Error: Incomplete declaration."
    
    return "Error: Invalid declaration syntax."

class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Variable Declaration Parser")
        self.root.geometry("600x400")

        self.input_label = tk.Label(root, text="Enter Python Variable Declaration:")
        self.input_label.pack(pady=10)
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()

        self.parse_button = tk.Button(root, text="Parse", command=self.parse_declaration)
        self.parse_button.pack(pady=10)

        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=50, state='disabled')
        self.output_text.pack()

    def parse_declaration(self):
        input_code = self.input_text.get("1.0", tk.END).strip()
        # Tokenize the input code
        tokens = re.split(r'\s+', input_code)  # Split by whitespace
        
        result = parse(tokens)

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()