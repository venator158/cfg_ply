from parser import parser
from lexer import *

# Example function definitions
test_code = [
    "def my_function(arg1, arg2):\n    x = 10\n    y = x + 5",
    "def my_function():\n    name = \"John\"\n    age = 30",
    "def add(a, b=0):\n    return a + b",
    "def incorrect_function(arg1,):\n    x = +",  # Invalid function with syntax error
]

for code in test_code:
    print(f"Testing:\n{code}")
    result = parser.parse(code)
    print("\n--- TOKENIZING ---")
    tokens = tokenize_input(code)
    for tok in tokens:
        print(f"Token(type={tok.type}, value={tok.value})")
    print("\n--- VALIDITY CHECK ---")
    print()
