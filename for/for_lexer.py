import ply.lex as lex

 
tokens = (
    'FOR', 'IN', 'COLON', 'IDENTIFIER', 'NUMBER', 'LPAREN', 'RPAREN',
    'PLUS', 'EQUALS', 'COMMA'
)

 
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

 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
     
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t

 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

 
t_ignore = ' \t'

 
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

 
lexer = lex.lex()
