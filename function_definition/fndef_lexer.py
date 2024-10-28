import ply.lex as lex

# List of token names
tokens = (
    'TYPE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 
    'LBRACE', 'RBRACE', 'ASSIGN', 'RETURN', 'NUMBER'
)

# Regular expressions for simple tokens
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_SEMICOLON = r';'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_ASSIGN    = r'='

# Define reserved words
reserved = {    
    'void': 'TYPE',
    'int': 'TYPE',
    'float': 'TYPE',
    'double': 'TYPE',
    'char': 'TYPE',
    'short': 'TYPE',
    'long': 'TYPE',
    'unsigned': 'TYPE',
    'signed': 'TYPE',
    'return': 'RETURN'
}

# Regular expression rules for identifiers and types
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Number token (for simple numeric expressions)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the string to an integer
    return t

# Rule for tracking line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignoring spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
