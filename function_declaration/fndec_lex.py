import ply.lex as lex

 
tokens = (
    'TYPE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COMMA', 'SEMICOLON'
)

 
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_COMMA     = r','
t_SEMICOLON = r';'

 
reserved = {    
    'void': 'TYPE',
    'int': 'TYPE',
    'float': 'TYPE',
    'double': 'TYPE',
    'char': 'TYPE',
    'short': 'TYPE',
    'long': 'TYPE',
    'unsigned': 'TYPE',
    'signed': 'TYPE'
}

 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')   
    return t

 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 
t_ignore = ' \t'

 
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

 
lexer = lex.lex()
