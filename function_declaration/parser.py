import ply.yacc as yacc
from lexer import tokens

# Parsing rules
def p_function_declaration(p):
    '''function_declaration : DEF IDENTIFIER LPAREN parameter_list RPAREN COLON'''
    print(f"Function '{p[2]}' declaration is syntactically correct.")

def p_parameter_list(p):
    '''parameter_list : parameters
                      | empty'''
    pass

def p_parameters(p):
    '''parameters : parameter
                  | parameter COMMA parameters'''
    pass

def p_parameter(p):
    '''parameter : IDENTIFIER
                 | IDENTIFIER EQUAL IDENTIFIER'''
    pass

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
