 
import tkinter as tk
from tkinter import messagebox
from dtype_lexer import lexer

 
def parse(tokens):
    try:
         
        idx = 0
        
         
        if tokens[idx][0] == 'TYPE':
            idx += 1
        else:
            return "Error: Expected data type at the beginning."

         
        if idx < len(tokens) and tokens[idx][0] == 'POINTER':
            idx += 1

         
        if idx < len(tokens) and tokens[idx][0] == 'IDENTIFIER':
            idx += 1
        else:
            return "Error: Expected an identifier after type."

         
        if idx < len(tokens) and tokens[idx][0] == 'ASSIGN':
            idx += 1
            if idx < len(tokens) and tokens[idx][0] in {'INT_VALUE', 'FLOAT_VALUE', 'CHAR_VALUE', 'STRING_VALUE'}:
                idx += 1
            else:
                return "Error: Expected a value after '='."

         
        if idx < len(tokens) and tokens[idx][0] == 'SEMICOLON':
            return "Parsed successfully: Valid declaration."
        else:
            return "Error: Expected ';' at the end of declaration."

    except IndexError:
        return "Error: Incomplete declaration."
    return "Error: Invalid declaration syntax."

 
class ParserGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C Data Type Declaration Parser")
        self.root.geometry("600x400")

         
        self.input_label = tk.Label(root, text="Enter C Data Type Declaration:")
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
        tokens = lexer(input_code)
        
         
        result = parse(tokens)
        
         
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state='disabled')

 
if __name__ == "__main__":
    root = tk.Tk()
    app = ParserGUI(root)
    root.mainloop()
