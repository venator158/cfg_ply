
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'EQUAL FLOAT IDENTIFIER INT NUMBER SEMICOLON STRING STRING_TYPEdeclaration : type IDENTIFIER SEMICOLON\n                   | type IDENTIFIER EQUAL expression SEMICOLONtype : INT\n            | FLOAT\n            | STRING_TYPEexpression : NUMBER\n                  | STRING'
    
_lr_action_items = {'INT':([0,],[3,]),'FLOAT':([0,],[4,]),'STRING_TYPE':([0,],[5,]),'$end':([1,7,12,],[0,-1,-2,]),'IDENTIFIER':([2,3,4,5,],[6,-3,-4,-5,]),'SEMICOLON':([6,9,10,11,],[7,12,-6,-7,]),'EQUAL':([6,],[8,]),'NUMBER':([8,],[10,]),'STRING':([8,],[11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaration':([0,],[1,]),'type':([0,],[2,]),'expression':([8,],[9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaration","S'",1,None,None,None),
  ('declaration -> type IDENTIFIER SEMICOLON','declaration',3,'p_declaration','parser.py',6),
  ('declaration -> type IDENTIFIER EQUAL expression SEMICOLON','declaration',5,'p_declaration','parser.py',7),
  ('type -> INT','type',1,'p_type','parser.py',14),
  ('type -> FLOAT','type',1,'p_type','parser.py',15),
  ('type -> STRING_TYPE','type',1,'p_type','parser.py',16),
  ('expression -> NUMBER','expression',1,'p_expression','parser.py',20),
  ('expression -> STRING','expression',1,'p_expression','parser.py',21),
]
