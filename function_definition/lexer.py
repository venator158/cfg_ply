import ply.lex as lex

# List of token names
tokens = (
    'DEF', 'LPAREN', 'RPAREN', 'COLON', 'COMMA', 'EQUAL',
    'IDENTIFIER', 'NUMBER', 'STRING', 'PLUS', 'MINUS'
)

# Reserved words
reserved = {
    'def': 'DEF'
}

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'-'

# Identifier token, checking against reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Number token
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String token
def t_STRING(t):
    r'\".*?\"'
    return t

# Ignore spaces and tabs (only leading indentation affects Python parsing)
t_ignore = ' \t'

# Track line numbers for better error reporting
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
