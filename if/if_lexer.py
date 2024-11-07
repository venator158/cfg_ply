import ply.lex as lex

tokens = (
    'IF', 'ELIF', 'ELSE', 'IDENTIFIER', 'NUMBER',
    'EQUALS', 'EQUALS_EQUALS', 'GREATER', 'LESSER',
    'GREATER_EQUALS', 'LESSER_EQUALS', 'COLON', 'NEWLINE', 'INDENT', 'DEDENT'
)

reserved = {
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
}

t_EQUALS = r'='
t_EQUALS_EQUALS = r'=='
t_GREATER = r'>'
t_LESSER = r'<'
t_GREATER_EQUALS = r'>='
t_LESSER_EQUALS = r'<='
t_COLON = r':'

t_ignore = ' \t'

indent_stack = [0]

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.value = '\n'
    return t

def t_indent_dedent(t):
    r'\n[ ]*'
    count = len(t.value) - 1  # Get indentation level
    if count > indent_stack[-1]:
        indent_stack.append(count)
        t.type = 'INDENT'
    elif count < indent_stack[-1]:
        while indent_stack and indent_stack[-1] > count:
            indent_stack.pop()
            t.type = 'DEDENT'
            yield t
    t.value = count
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(input_code):
    lexer.input(input_code)
    return list(lexer)
