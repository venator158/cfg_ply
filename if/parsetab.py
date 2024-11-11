
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON ELIF ELSE EQUALS EQUALS_EQUALS GREATER GREATER_EQUALS IDENTIFIER IF LESSER LESSER_EQUALS LPAREN MINUS_MINUS NEWLINE NUMBER PLUS_PLUS PRINT RPARENprogram : statement_liststatement_list : statement\n                      | statement NEWLINE statement_liststatement : assignment\n                 | print_statement\n                 | increment\n                 | decrement\n                 | standalone_statement\n                 | if_statement\n                 | elif_block\n                 | else_blockif_statement : IF expression COLON NEWLINE statement_list\n                    | IF expression COLON NEWLINE statement_list NEWLINE if_statement\n                    | IF expression COLON NEWLINE statement_list NEWLINE ELIF expression COLON NEWLINE statement_list\n                    | IF expression COLON NEWLINE statement_list NEWLINE ELSE COLON NEWLINE statement_list\n                    | IF expression COLON NEWLINE statement_list NEWLINE elif_block NEWLINE else_blockelif_block : ELIF expression COLON NEWLINE statement_list\n                  | ELIF expression COLON NEWLINE statement_list NEWLINE elif_blockelse_block : ELSE COLON NEWLINE statement_listexpression : IDENTIFIER\n                  | NUMBER\n                  | IDENTIFIER EQUALS_EQUALS NUMBER\n                  | IDENTIFIER GREATER NUMBER\n                  | IDENTIFIER LESSER NUMBER\n                  | IDENTIFIER GREATER_EQUALS NUMBER\n                  | IDENTIFIER LESSER_EQUALS NUMBERassignment : IDENTIFIER EQUALS NUMBERprint_statement : PRINT LPAREN IDENTIFIER RPARENincrement : IDENTIFIER PLUS_PLUSdecrement : IDENTIFIER MINUS_MINUSstandalone_statement : IDENTIFIER'
    
_lr_action_items = {'IDENTIFIER':([0,14,15,17,21,37,39,45,52,60,62,],[12,23,23,12,29,12,12,12,23,12,12,]),'PRINT':([0,17,37,39,45,60,62,],[13,13,13,13,13,13,13,]),'IF':([0,17,37,39,45,49,60,62,],[14,14,14,14,14,14,14,14,]),'ELIF':([0,17,37,39,45,49,50,60,62,],[15,15,15,15,15,52,15,15,15,]),'ELSE':([0,17,37,39,45,49,58,60,62,],[16,16,16,16,16,53,16,16,16,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,19,20,27,28,38,46,47,48,51,55,61,63,64,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-31,-29,-30,-3,-27,-28,-19,-12,-17,-13,-18,-16,-15,-14,]),'NEWLINE':([3,4,5,6,7,8,9,10,11,12,19,20,26,27,28,30,36,38,46,47,48,51,54,55,57,59,61,63,64,],[17,-4,-5,-6,-7,-8,-9,-10,-11,-31,-29,-30,37,-3,-27,39,45,-28,-19,49,50,-13,58,-18,60,62,-16,-15,50,]),'EQUALS':([12,],[18,]),'PLUS_PLUS':([12,],[19,]),'MINUS_MINUS':([12,],[20,]),'LPAREN':([13,],[21,]),'NUMBER':([14,15,18,31,32,33,34,35,52,],[24,24,28,40,41,42,43,44,24,]),'COLON':([16,22,23,24,25,40,41,42,43,44,53,56,],[26,30,-20,-21,36,-22,-23,-24,-25,-26,57,59,]),'EQUALS_EQUALS':([23,],[31,]),'GREATER':([23,],[32,]),'LESSER':([23,],[33,]),'GREATER_EQUALS':([23,],[34,]),'LESSER_EQUALS':([23,],[35,]),'RPAREN':([29,],[38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,17,37,39,45,60,62,],[2,27,46,47,48,63,64,]),'statement':([0,17,37,39,45,60,62,],[3,3,3,3,3,3,3,]),'assignment':([0,17,37,39,45,60,62,],[4,4,4,4,4,4,4,]),'print_statement':([0,17,37,39,45,60,62,],[5,5,5,5,5,5,5,]),'increment':([0,17,37,39,45,60,62,],[6,6,6,6,6,6,6,]),'decrement':([0,17,37,39,45,60,62,],[7,7,7,7,7,7,7,]),'standalone_statement':([0,17,37,39,45,60,62,],[8,8,8,8,8,8,8,]),'if_statement':([0,17,37,39,45,49,60,62,],[9,9,9,9,9,51,9,9,]),'elif_block':([0,17,37,39,45,49,50,60,62,],[10,10,10,10,10,54,55,10,10,]),'else_block':([0,17,37,39,45,58,60,62,],[11,11,11,11,11,61,11,11,]),'expression':([14,15,52,],[22,25,56,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','if_parser.py',5),
  ('statement_list -> statement','statement_list',1,'p_statement_list','if_parser.py',9),
  ('statement_list -> statement NEWLINE statement_list','statement_list',3,'p_statement_list','if_parser.py',10),
  ('statement -> assignment','statement',1,'p_statement','if_parser.py',14),
  ('statement -> print_statement','statement',1,'p_statement','if_parser.py',15),
  ('statement -> increment','statement',1,'p_statement','if_parser.py',16),
  ('statement -> decrement','statement',1,'p_statement','if_parser.py',17),
  ('statement -> standalone_statement','statement',1,'p_statement','if_parser.py',18),
  ('statement -> if_statement','statement',1,'p_statement','if_parser.py',19),
  ('statement -> elif_block','statement',1,'p_statement','if_parser.py',20),
  ('statement -> else_block','statement',1,'p_statement','if_parser.py',21),
  ('if_statement -> IF expression COLON NEWLINE statement_list','if_statement',5,'p_if_statement','if_parser.py',25),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE if_statement','if_statement',7,'p_if_statement','if_parser.py',26),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE ELIF expression COLON NEWLINE statement_list','if_statement',11,'p_if_statement','if_parser.py',27),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE ELSE COLON NEWLINE statement_list','if_statement',10,'p_if_statement','if_parser.py',28),
  ('if_statement -> IF expression COLON NEWLINE statement_list NEWLINE elif_block NEWLINE else_block','if_statement',9,'p_if_statement','if_parser.py',29),
  ('elif_block -> ELIF expression COLON NEWLINE statement_list','elif_block',5,'p_elif_block','if_parser.py',44),
  ('elif_block -> ELIF expression COLON NEWLINE statement_list NEWLINE elif_block','elif_block',7,'p_elif_block','if_parser.py',45),
  ('else_block -> ELSE COLON NEWLINE statement_list','else_block',4,'p_else_block','if_parser.py',53),
  ('expression -> IDENTIFIER','expression',1,'p_expression','if_parser.py',58),
  ('expression -> NUMBER','expression',1,'p_expression','if_parser.py',59),
  ('expression -> IDENTIFIER EQUALS_EQUALS NUMBER','expression',3,'p_expression','if_parser.py',60),
  ('expression -> IDENTIFIER GREATER NUMBER','expression',3,'p_expression','if_parser.py',61),
  ('expression -> IDENTIFIER LESSER NUMBER','expression',3,'p_expression','if_parser.py',62),
  ('expression -> IDENTIFIER GREATER_EQUALS NUMBER','expression',3,'p_expression','if_parser.py',63),
  ('expression -> IDENTIFIER LESSER_EQUALS NUMBER','expression',3,'p_expression','if_parser.py',64),
  ('assignment -> IDENTIFIER EQUALS NUMBER','assignment',3,'p_assignment','if_parser.py',71),
  ('print_statement -> PRINT LPAREN IDENTIFIER RPAREN','print_statement',4,'p_print_statement','if_parser.py',75),
  ('increment -> IDENTIFIER PLUS_PLUS','increment',2,'p_increment','if_parser.py',79),
  ('decrement -> IDENTIFIER MINUS_MINUS','decrement',2,'p_decrement','if_parser.py',83),
  ('standalone_statement -> IDENTIFIER','standalone_statement',1,'p_standalone_statement','if_parser.py',87),
]
