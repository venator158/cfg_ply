import ply.lex as lex

# List of token names
tokens = (
    'DEF', 'LPAREN', 'RPAREN', 'COLON', 'COMMA', 'EQUAL', 'IDENTIFIER'
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

# Identifier token, checking against reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers for better error reporting
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)
    
def tokenize_input(input_string):
    lexer.input(input_string)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list 

# Build the lexer
lexer = lex.lex()

