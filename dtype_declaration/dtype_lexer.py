import re

token_specs = [
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  # Variable names
    ('ASSIGN', r'='),                              # Assignment operator
    ('INT_VALUE', r'\b[0-9]+\b'),                 # Integer values
    ('FLOAT_VALUE', r'\b[0-9]+\.[0-9]+\b'),       # Float values
    ('CHAR_VALUE', r"'.'"),                        # Character values
    ('STRING_VALUE', r'"[^"]*"'),                  # String values
    ('SEMICOLON', r';'),                           # Semicolon (not typically used in Python)
    ('WHITESPACE', r'\s+'),                        # Whitespace
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)
compiled_re = re.compile(token_regex)

def lexer(input_code):
    tokens = []
    for match in compiled_re.finditer(input_code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':   
            tokens.append((token_type, token_value))
    return tokens