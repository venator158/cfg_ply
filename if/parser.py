import ply.yacc as yacc
from if_lexer import tokens

def p_program(p):
    '''program : statement_list'''
    print("Parsed program successfully.")

def p_statement_list(p):
    '''statement_list : statement
                      | statement NEWLINE statement_list'''
    pass

def p_statement(p):
    '''statement : assignment
                 | print_statement
                 | increment
                 | decrement
                 | standalone_statement
                 | if_statement
                 | elif_block
                 | else_block'''
    pass

def p_if_statement(p):
    '''if_statement : IF expression COLON NEWLINE statement_list
                    | IF expression COLON NEWLINE statement_list NEWLINE if_statement
                    | IF expression COLON NEWLINE statement_list NEWLINE ELIF expression COLON NEWLINE statement_list
                    | IF expression COLON NEWLINE statement_list NEWLINE ELSE COLON NEWLINE statement_list
                    | IF expression COLON NEWLINE statement_list NEWLINE elif_block NEWLINE else_block'''
    if len(p) == 6:
        p[0] = f"if {p[2]}:\n{p[5]}"
        #print(f"Parsed 'if' statement with condition '{p[2]}'.")
    elif len(p) == 12:
        p[0] = f"if {p[2]}:\n{p[5]}\n elif {p[8]}:\n{p[11]}"
        #print(f"Parsed 'if' statement with condition '{p[2]}' and 'elif' statement with condition '{p[8]}")
    elif len(p) == 11:
        p[0] = f"if {p[2]}:\n{p[5]}\n else:\n{p[10]}"
        #print(f"Parsed 'if-else' statement with condition '{p[2]}'")
    else:
        p[0] = f"if {p[2]}:\n{p[5]}\n {p[7]}\n{p[9]}"
        #print(f"Parsed  'if-elif-else' statement with condition '{p[2]}'")

def p_elif_block(p):
    '''elif_block : ELIF expression COLON NEWLINE statement_list
                  | ELIF expression COLON NEWLINE statement_list NEWLINE elif_block'''
    if len(p) == 6:
        p[0] = f"elif {p[2]}:\n{p[5]}"
    else:
        p[0] = f"elif {p[2]}:\n{p[5]} {p[7]}"
    print(f"Parsed 'elif' statement with condition '{p[2]}'.")

def p_else_block(p):
    '''else_block : ELSE COLON NEWLINE statement_list'''
    p[0] = f"else:\n{p[4]}"
    print("Parsed 'else' statement.")

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | IDENTIFIER EQUALS_EQUALS NUMBER
                  | IDENTIFIER GREATER NUMBER
                  | IDENTIFIER LESSER NUMBER
                  | IDENTIFIER GREATER_EQUALS NUMBER
                  | IDENTIFIER LESSER_EQUALS NUMBER'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS NUMBER'''
    print(f"Parsed assignment: {p[1]} = {p[3]}")

def p_print_statement(p):
    '''print_statement : PRINT IDENTIFIER'''
    print(f"Parsed print statement with identifier: {p[2]}")

def p_increment(p):
    '''increment : IDENTIFIER PLUS_PLUS'''
    print(f"Parsed increment: {p[1]}++")

def p_decrement(p):
    '''decrement : IDENTIFIER MINUS_MINUS'''
    print(f"Parsed decrement: {p[1]}--")

def p_standalone_statement(p):
    '''standalone_statement : IDENTIFIER'''
    print(f"Parsed standalone statement: {p[1]}")

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def process_code():
    print("\nEnter your Python code to parse. Finish with a blank line and press ctrl+c to exit")
    input_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        input_lines.append(line)
    input_code = "\n".join(input_lines)
    
    print("\nParsing result:")
    try:
        parser.parse(input_code)
    except SyntaxError as e:
        print(e)

if __name__ == "__main__":
    while True:
        process_code()
