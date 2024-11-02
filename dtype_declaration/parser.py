import ply.yacc as yacc
from lexer import tokens

# Parsing rules
def p_declaration(p):
    '''declaration : type IDENTIFIER SEMICOLON
                   | type IDENTIFIER EQUAL expression SEMICOLON'''
    if len(p) == 4:
        print(f"Declared variable '{p[2]}' of type '{p[1]}' with no initial value.")
    else:
        print(f"Declared variable '{p[2]}' of type '{p[1]}' with initial value '{p[4]}'.")

def p_type(p):
    '''type : INT
            | FLOAT
            | STRING_TYPE'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                  | STRING'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
