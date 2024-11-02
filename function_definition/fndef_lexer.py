import ply.lex as lex

 
tokens = (
    'TYPE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON', 
    'LBRACE', 'RBRACE', 'ASSIGN', 'RETURN', 'NUMBER'
)

 
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_SEMICOLON = r';'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_ASSIGN    = r'='

 
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

 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')   
    return t

 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   
    return t

 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 
t_ignore = ' \t'

 
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

 
lexer = lex.lex()
