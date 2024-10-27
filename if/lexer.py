import ply.lex as lex

# List of token names
tokens = (
    'IF',
    'ELIF',
    'ELSE',
    'COLON',
    'EQUALS',
    'GREATER',
    'LESSER',
    'GREATER_EQUALS',
    'LESSER_EQUALS',
    'IDENTIFIER',
    'NUMBER',
    'NEWLINE'
)

# Regular expression rules for simple tokens
t_COLON = r':'
t_EQUALS = r'='
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATER_EQUALS = r'>='
t_LESSER_EQUALS = r'<='

# Reserved words
reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE'
}

# A rule for identifiers (variable names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check if it's a reserved word
    return t

# A rule for numbers (both integer and float)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# A rule to track newlines and handle indentation
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with an example input
if __name__ == "__main__":
    # Example input for testing
    input_code = '''
    if x > 5:
        x = 10
    elif x < 3:
        x = 1
    else:
        x = 0
    '''
    
    lexer.input(input_code)
    
    # Tokenize the input
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
