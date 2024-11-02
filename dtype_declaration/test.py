from parser import parser

# Example declarations
test_code = [
    "int x;",
    "float y = 3.14;",
    "string name = \"Alice\";",
    "int invalid_var = ;",  # Invalid syntax
    "float num = 42.0;", 
]

for code in test_code:
    print(f"Testing: {code}")
    result = parser.parse(code)
    print()
