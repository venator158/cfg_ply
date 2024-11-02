from parser import parser

# Example function declarations
test_code = [
    "def my_function(arg1, arg2):",                    # Valid
    "def my_function(arg1, arg2=default):",            # Valid with default
    "def another_function():",                         # Valid with no parameters
    "def bad_function(, arg2):",                       # Invalid syntax
    "def another_bad_function(arg1 arg2):",            # Invalid syntax
    "def func_with_default(param=default, another):"   # Invalid: default not at end
]

for code in test_code:
    print(f"Testing: {code}")
    parser.parse(code)
    print()
