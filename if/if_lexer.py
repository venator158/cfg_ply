import ply.lex as lex

tokens = (
    'IF', 'ELIF', 'ELSE',
    'PRINT', 'LPAREN', 'RPAREN',
    'IDENTIFIER', 'NUMBER',
    'EQUALS', 'COLON', 'NEWLINE',
    'GREATER', 'LESSER', 'GREATER_EQUALS', 'LESSER_EQUALS', 'EQUALS_EQUALS',
    'PLUS_PLUS', 'MINUS_MINUS'
)

t_EQUALS = r'='
t_EQUALS_EQUALS = r'=='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATER_EQUALS = r'>='
t_LESSER_EQUALS = r'<='
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'
t_ignore = ' \t'

def t_IF(t):
    r'if'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(input_code):
    lexer.input(input_code)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok: 
            break
        tokens_list.append(tok)
    return tokens_list