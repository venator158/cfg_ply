import ply.yacc as yacc
from for_lexer import tokens, tokenize

def p_program(p):
    '''program : statement_list'''
    print("Parsed program successfully.")

def p_statement_list(p):
    '''statement_list : statement
                      | statement NEWLINE statement_list'''
    pass

def p_statement(p):
    '''statement : assignment
                 | for_loop
                 | print_statement
                 | increment
                 | decrement
                 | standalone_statement'''
    pass    

def p_for_loop(p):
    '''for_loop : FOR IDENTIFIER IN func_call COLON NEWLINE statement_list'''
    print(f"Parsed a for loop with iterator '{p[2]}' and iterable '{p[4]}'.")
    p[0] = f"for {p[2]} in {p[4]}:\n{p[6]}"

def p_func_call(p):
    '''func_call : IDENTIFIER LPAREN NUMBER RPAREN
                 | IDENTIFIER LPAREN NUMBER COMMA NUMBER RPAREN
                 | IDENTIFIER LPAREN NUMBER COMMA NUMBER COMMA NUMBER RPAREN'''
    if p[1] == "range":
        if len(p) == 5:  # range(NUMBER)
            p[0] = f"{p[1]}({p[3]})"
        elif len(p) == 7:  # range(NUMBER, NUMBER)
            p[0] = f"{p[1]}({p[3]}, {p[5]})"
        elif len(p) == 9:  # range(NUMBER, NUMBER, NUMBER)
            p[0] = f"{p[1]}({p[3]}, {p[5]}, {p[7]})"
    else:
        args = ', '.join(p[3:-1])  
        p[0] = f"{p[1]}({args})" 

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS NUMBER'''
    print(f"Parsed assignment: {p[1]} = {p[3]}")

def p_print_statement(p):
    '''print_statement : PRINT LPAREN IDENTIFIER RPAREN'''
    print(f"Parsed print statement with identifier: {p[3]}")

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
    print("\nEnter your code to parse. Finish with a blank line and press ctrl+c to exit")
    input_lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        input_lines.append(line)
    input_code = "\n".join(input_lines)

    print("\nParsing result:")
    tokens = tokenize(input_code)
    for token in tokens:
        print(token)
    try:
        parser.parse(input_code)
    except SyntaxError as e:
        print(e)

if __name__ == "__main__":
    while True:
        process_code()


'''
S -> SL

SL -> STMT NEWLINE SL
   | STMT

STMT -> FOR_LOOP
     | ASSIGNMENT
     | PRINT_STMT
     | INCREMENT
     | DECREMENT
     | STANDALONE_STMT

FOR_LOOP -> 'for' IDENTIFIER 'in' FUNC_CALL ':' NEWLINE SL

ASSIGNMENT -> IDENTIFIER '=' NUMBER

PRINT_STMT -> 'print' '(' IDENTIFIER ')'

INCREMENT -> IDENTIFIER '++'

DECREMENT -> IDENTIFIER '--'

STANDALONE_STMT -> IDENTIFIER

FUNC_CALL -> IDENTIFIER '(' NUMBER ')'
          | IDENTIFIER '(' NUMBER ',' NUMBER ')'
          | IDENTIFIER '(' NUMBER ',' NUMBER ',' NUMBER ')'

'''