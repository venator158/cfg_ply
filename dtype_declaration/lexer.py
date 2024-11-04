import ply.lex as lex

# List of token names
tokens = (
    'INT', 'FLOAT', 'STRING_TYPE',  # Data types
    'IDENTIFIER', 'EQUAL', 'NUMBER', 'STRING', 'SEMICOLON'
)

# Reserved words for data types
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING_TYPE'
}

# Regular expressions for tokens
t_EQUAL = r'='
t_SEMICOLON = r';'

# Identifier token, checking against reserved words
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Number token (handling integers and floats)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# String token
def t_STRING(t):
    r'\".*?\"'
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track line numbers for error reporting
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
