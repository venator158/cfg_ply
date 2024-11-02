import ply.yacc as yacc
from lexer import tokens

# Parsing rules
def p_function_definition(p):
    '''function_definition : DEF IDENTIFIER LPAREN parameter_list RPAREN COLON statement_block'''
    print(f"Function '{p[2]}' definition is syntactically correct.")

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
                 | IDENTIFIER EQUAL expression'''
    pass

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | STRING
                  | expression PLUS expression
                  | expression MINUS expression'''
    pass

def p_statement_block(p):
    '''statement_block : statement
                       | statement statement_block'''
    pass

def p_statement(p):
    '''statement : expression
                 | IDENTIFIER EQUAL expression'''
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
