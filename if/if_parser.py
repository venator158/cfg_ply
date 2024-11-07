import ply.yacc as yacc
import ply.lex as lexer
from if_lexer import tokens, tokenize

def p_program(p):
    '''program : statement_list'''
    print("Parsed program successfully.")

def p_statement_list(p):
    '''statement_list : statement
                      | statement NEWLINE statement_list'''
    pass

def p_statement(p):
    '''statement : assignment
                 | if_statement'''
    pass

def p_if_statement(p):
    '''if_statement : IF expression COLON NEWLINE INDENT ignored_block DEDENT
                    | IF expression COLON NEWLINE INDENT ignored_block DEDENT elif_blocks
                    | IF expression COLON NEWLINE INDENT ignored_block DEDENT elif_blocks else_block
                    | IF expression COLON NEWLINE INDENT ignored_block DEDENT else_block'''
    print("Parsed 'if' statement.")

def p_elif_blocks(p):
    '''elif_blocks : ELIF expression COLON NEWLINE INDENT ignored_block DEDENT
                   | ELIF expression COLON NEWLINE INDENT ignored_block DEDENT elif_blocks'''
    print("Parsed 'elif' block.")

def p_else_block(p):
    '''else_block : ELSE COLON NEWLINE INDENT ignored_block DEDENT'''
    print("Parsed 'else' block.")

# Define an ignored block that will match any content without processing it
def p_ignored_block(p):
    '''ignored_block : statement_list
                     | empty'''
    pass

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | IDENTIFIER EQUALS_EQUALS NUMBER
                  | IDENTIFIER GREATER NUMBER
                  | IDENTIFIER LESSER NUMBER
                  | IDENTIFIER GREATER_EQUALS NUMBER
                  | IDENTIFIER LESSER_EQUALS NUMBER'''
    pass

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS NUMBER'''
    print(f"Parsed assignment: {p[1]} = {p[3]}")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def parse_code(input_code):
    tokens = tokenize(input_code)
    try:
        parser.parse(input_code, lexer=lexer)
    except Exception as e:
        print("Parsing failed:", e)

if __name__ == "__main__":
    print("\nEnter code to parse. Finish with a blank line.")
    input_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            input_lines.append(line)
        except EOFError:
            break
    input_code = "\n".join(input_lines)
    print("\nParsing result:")
    parse_code(input_code)
