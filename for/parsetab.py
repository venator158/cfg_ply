
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA EQUALS FOR IDENTIFIER IN LPAREN NUMBER PLUS RPARENfor_loop : FOR IDENTIFIER IN func_call COLONfunc_call : IDENTIFIER LPAREN expression RPARENfunc_call : IDENTIFIER LPAREN expression COMMA expression RPARENfunc_call : IDENTIFIER LPAREN expression COMMA expression COMMA expression RPARENexpression : IDENTIFIERexpression : NUMBERstatement : IDENTIFIER EQUALS expression'
    
_lr_action_items = {'FOR':([0,],[2,]),'$end':([1,8,],[0,-1,]),'IDENTIFIER':([2,4,7,13,15,],[3,5,9,9,9,]),'IN':([3,],[4,]),'LPAREN':([5,],[7,]),'COLON':([6,12,16,18,],[8,-2,-3,-4,]),'NUMBER':([7,13,15,],[11,11,11,]),'RPAREN':([9,10,11,14,17,],[-5,12,-6,16,18,]),'COMMA':([9,10,11,14,],[-5,13,-6,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'for_loop':([0,],[1,]),'func_call':([4,],[6,]),'expression':([7,13,15,],[10,14,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> for_loop","S'",1,None,None,None),
  ('for_loop -> FOR IDENTIFIER IN func_call COLON','for_loop',5,'p_for_loop','parser.py',6),
  ('func_call -> IDENTIFIER LPAREN expression RPAREN','func_call',4,'p_func_call_one_arg','parser.py',10),
  ('func_call -> IDENTIFIER LPAREN expression COMMA expression RPAREN','func_call',6,'p_func_call_two_args','parser.py',14),
  ('func_call -> IDENTIFIER LPAREN expression COMMA expression COMMA expression RPAREN','func_call',8,'p_func_call_three_args','parser.py',18),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',22),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',26),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_assignment','parser.py',30),
]
