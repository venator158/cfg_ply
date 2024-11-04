import ply.lex as lex

tokens = (
    'FOR', 'IN', 'COLON', 'IDENTIFIER', 'NUMBER', 'LPAREN', 'RPAREN',
    'PLUS_PLUS', 'MINUS_MINUS', 'EQUALS', 'COMMA', 'NEWLINE', 'PRINT'
)

t_COLON = r':'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'
t_ignore = ' \t'

reserved = {
    'for': 'FOR',
    'in': 'IN',
    'print': 'PRINT'
}

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
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
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

input_lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    input_lines.append(line)
input_code = "\n".join(input_lines)

lexer.input(input_code)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)