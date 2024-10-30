 
import re

 
token_specs = [
    ('TYPE', r'\b(int|float|double|char|short|long|unsigned|signed)\b'),
    ('POINTER', r'\*'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('ASSIGN', r'='),
    ('SEMICOLON', r';'),
    ('INT_VALUE', r'\b[0-9]+\b'),
    ('FLOAT_VALUE', r'\b[0-9]+\.[0-9]+\b'),
    ('CHAR_VALUE', r"'.'"),
    ('STRING_VALUE', r'"[^"]*"'),
    ('WHITESPACE', r'\s+'),   
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
