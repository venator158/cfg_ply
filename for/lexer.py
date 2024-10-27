import ply.lex as lex

# List of token names
tokens = (
    'FOR', 'IN', 'COLON', 'IDENTIFIER', 'NUMBER', 'LPAREN', 'RPAREN',
    'PLUS', 'EQUALS', 'COMMA'
)

# Regular expression rules for simple tokens
t_COLON = r':'
t_PLUS  = r'\+'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

reserved = {
    'for': 'FOR',
    'in': 'IN'
}

# Rule to match identifiers and reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

# Rule to match numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
