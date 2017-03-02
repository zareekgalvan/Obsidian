
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PLUS MINUS MULTIPLICATION DIVISION MOD EQUALS EQUALEQUALS DIFFERENT GREATER LESS GREATEROREQUAL LESSOREQUAL AND OR LPAR RPAR LBRACKET RBRACKET LSQRTBRACKET RSQRTBRACKET COMMA SEMICOLON CTEINT CTEDOUBLE CTEBOOL ID FALSE READ VOID FUNC RETURN TRUE IF DOUBLE WRITE INT WHILE BOOL MAINprogram : more_vars more_func mainmore_vars : vars\n\t\t\t|vars : var_type vars_aux SEMICOLON more_varsvar_type : BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEvars_aux : ID arr var_assign more_vars_auxvar_assign : EQUALS var_cte\n\t\t\t|more_vars_aux : COMMA vars_aux\n\t\t\t|arr : LSQRTBRACKET const RSQRTBRACKET arr\n\t\t\t|var_cte : CTEINT\n\t\t\t| CTEDOUBLE\n\t\t\t| CTEBOOL\n\t\t\t| ID arr\n\t\t\t| func_callconst : CTEINT\n\t\t\t| CTEDOUBLE\n\t\t\t| CTEBOOLmore_func : func\n\t\t\t|func : func_call : main : '
    
_lr_action_items = {'CTEDOUBLE':([14,17,],[19,23,]),'RSQRTBRACKET':([19,20,21,22,],[-21,31,-22,-20,]),'SEMICOLON':([8,9,13,17,18,23,24,25,26,27,28,29,31,32,33,34,],[12,-14,-10,-26,-12,-16,-19,-17,-15,-9,-14,-8,-14,-18,-11,-13,]),'INT':([0,12,],[3,3,]),'DOUBLE':([0,12,],[4,4,]),'LSQRTBRACKET':([9,28,31,],[14,14,14,]),'CTEINT':([14,17,],[22,26,]),'EQUALS':([9,13,31,34,],[-14,17,-14,-13,]),'BOOL':([0,12,],[6,6,]),'CTEBOOL':([14,17,],[21,25,]),'COMMA':([9,13,17,18,23,24,25,26,27,28,31,32,34,],[-14,-10,-26,30,-16,-19,-17,-15,-9,-14,-14,-18,-13,]),'ID':([2,3,4,6,17,30,],[9,-6,-7,-5,28,9,]),'$end':([0,1,5,7,10,11,12,15,16,],[-3,-2,0,-24,-23,-27,-3,-1,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'func_call':([17,],[24,]),'arr':([9,28,31,],[13,32,34,]),'var_assign':([13,],[18,]),'const':([14,],[20,]),'var_type':([0,12,],[2,2,]),'vars':([0,12,],[1,1,]),'more_vars':([0,12,],[7,16,]),'vars_aux':([2,30,],[8,33,]),'more_vars_aux':([18,],[29,]),'program':([0,],[5,]),'func':([7,],[10,]),'main':([11,],[15,]),'var_cte':([17,],[27,]),'more_func':([7,],[11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> more_vars more_func main','program',3,'p_program','ObsidianParser.py',10),
  ('more_vars -> vars','more_vars',1,'p_more_vars','ObsidianParser.py',14),
  ('more_vars -> <empty>','more_vars',0,'p_more_vars','ObsidianParser.py',15),
  ('vars -> var_type vars_aux SEMICOLON more_vars','vars',4,'p_vars','ObsidianParser.py',18),
  ('var_type -> BOOL','var_type',1,'p_var_type','ObsidianParser.py',21),
  ('var_type -> INT','var_type',1,'p_var_type','ObsidianParser.py',22),
  ('var_type -> DOUBLE','var_type',1,'p_var_type','ObsidianParser.py',23),
  ('vars_aux -> ID arr var_assign more_vars_aux','vars_aux',4,'p_vars_aux','ObsidianParser.py',26),
  ('var_assign -> EQUALS var_cte','var_assign',2,'p_var_assign','ObsidianParser.py',29),
  ('var_assign -> <empty>','var_assign',0,'p_var_assign','ObsidianParser.py',30),
  ('more_vars_aux -> COMMA vars_aux','more_vars_aux',2,'p_more_vars_aux','ObsidianParser.py',33),
  ('more_vars_aux -> <empty>','more_vars_aux',0,'p_more_vars_aux','ObsidianParser.py',34),
  ('arr -> LSQRTBRACKET const RSQRTBRACKET arr','arr',4,'p_arr','ObsidianParser.py',37),
  ('arr -> <empty>','arr',0,'p_arr','ObsidianParser.py',38),
  ('var_cte -> CTEINT','var_cte',1,'p_var_cte','ObsidianParser.py',41),
  ('var_cte -> CTEDOUBLE','var_cte',1,'p_var_cte','ObsidianParser.py',42),
  ('var_cte -> CTEBOOL','var_cte',1,'p_var_cte','ObsidianParser.py',43),
  ('var_cte -> ID arr','var_cte',2,'p_var_cte','ObsidianParser.py',44),
  ('var_cte -> func_call','var_cte',1,'p_var_cte','ObsidianParser.py',45),
  ('const -> CTEINT','const',1,'p_const','ObsidianParser.py',48),
  ('const -> CTEDOUBLE','const',1,'p_const','ObsidianParser.py',49),
  ('const -> CTEBOOL','const',1,'p_const','ObsidianParser.py',50),
  ('more_func -> func','more_func',1,'p_more_func','ObsidianParser.py',53),
  ('more_func -> <empty>','more_func',0,'p_more_func','ObsidianParser.py',54),
  ('func -> <empty>','func',0,'p_func','ObsidianParser.py',57),
  ('func_call -> <empty>','func_call',0,'p_func_call','ObsidianParser.py',60),
  ('main -> <empty>','main',0,'p_main','ObsidianParser.py',63),
]
