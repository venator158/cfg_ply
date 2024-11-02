
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA IDENTIFIER LBRACE LPAREN NUMBER RBRACE RETURN RPAREN SEMICOLON TYPEfunction_declaration : TYPE IDENTIFIER parameter_list SEMICOLONparameter_list : LPAREN parameter_declarations RPAREN\n                      | LPAREN RPARENparameter_declarations : parameter_declaration\n                              | parameter_declaration COMMA parameter_declarationsparameter_declaration : TYPE IDENTIFIER'
    
_lr_action_items = {'TYPE':([0,5,12,],[2,10,10,]),'$end':([1,6,],[0,-1,]),'IDENTIFIER':([2,10,],[3,13,]),'LPAREN':([3,],[5,]),'SEMICOLON':([4,8,11,],[6,-3,-2,]),'RPAREN':([5,7,9,13,14,],[8,11,-4,-6,-5,]),'COMMA':([9,13,],[12,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function_declaration':([0,],[1,]),'parameter_list':([3,],[4,]),'parameter_declarations':([5,12,],[7,14,]),'parameter_declaration':([5,12,],[9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function_declaration","S'",1,None,None,None),
  ('function_declaration -> TYPE IDENTIFIER parameter_list SEMICOLON','function_declaration',4,'p_function_declaration','fndef_parser.py',9),
  ('parameter_list -> LPAREN parameter_declarations RPAREN','parameter_list',3,'p_parameter_list','fndef_parser.py',13),
  ('parameter_list -> LPAREN RPAREN','parameter_list',2,'p_parameter_list','fndef_parser.py',14),
  ('parameter_declarations -> parameter_declaration','parameter_declarations',1,'p_parameter_declarations','fndef_parser.py',18),
  ('parameter_declarations -> parameter_declaration COMMA parameter_declarations','parameter_declarations',3,'p_parameter_declarations','fndef_parser.py',19),
  ('parameter_declaration -> TYPE IDENTIFIER','parameter_declaration',2,'p_parameter_declaration','fndef_parser.py',23),
]
