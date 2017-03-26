
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PLUS MINUS MULTIPLICATION DIVISION MOD EQUALS EQUALEQUALS DIFFERENT GREATER LESS GREATEROREQUAL LESSOREQUAL AND OR LPAR RPAR LBRACKET RBRACKET LSQRTBRACKET RSQRTBRACKET COMMA SEMICOLON CTEINT CTEDOUBLE CTEBOOL ID RETURN READ VOID ELSE FUNC IF DOUBLE WRITE INT WHILE BOOL MAINprogram : more_vars more_func mainmore_vars : vars\n\t\t\t|vars : var_type vars_aux SEMICOLON more_varsvar_type : BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEvars_aux : ID arr to_var_table var_assign more_vars_auxto_var_table :var_assign : EQUALS var_cte\n\t\t\t|more_vars_aux : COMMA vars_aux\n\t\t\t|arr : LSQRTBRACKET const RSQRTBRACKET arr\n\t\t\t|var_cte : const\n\t\t\t| ID arr\n\t\t\t| func_callconst : CTEINT\n\t\t\t| CTEDOUBLE\n\t\t\t| CTEBOOLmore_func : func\n\t\t\t|func : FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_functo_proc_dir :func_type : VOID \n\t\t\t| BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEarguments : var_type ID to_args more_args\n\t\t\t|more_args : COMMA var_type ID to_args more_args\n\t\t\t|to_args :func_block : LBRACKET more_vars more_statement optional_return RBRACKEToptional_return : RETURN exp SEMICOLON\n\t\t\t|more_statement : statement more_statement\n\t\t\t|statement : read\n\t\t| write\n\t\t| cycle\n\t\t| condition\n\t\t| assignation\n\t\t| func_call SEMICOLONread : READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLONgen_read_quad :write : WRITE LPAR exp RPAR gen_write_quad SEMICOLONgen_write_quad :cycle : WHILE cycle_start LPAR expression RPAR check_type block cycle_endcycle_start :cycle_end :condition : IF LPAR expression RPAR check_type block else_posible fill_end_conditionelse_posible : ELSE gen_goto block\n\t\t\t|gen_goto :fill_end_condition :check_type :assignation : ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLONgen_assignation_quad :func_call : ID LPAR params RPAR gen_func_call_quadparams : exp more_params\n\t\t\t|more_params : COMMA exp more_params\n\t\t\t|gen_func_call_quad :block : LBRACKET more_statement RBRACKETarr_par : LSQRTBRACKET exp RSQRTBRACKET arr_par\n\t\t\t|expression : conc gen_conc_quad expression_auxexpression_aux : ao add_to_pilaOptr conc gen_conc_quad expression_aux\n\t\t\t|gen_conc_quad :conc : exp gen_comp_quad conc_auxconc_aux : comp add_to_pilaOptr exp gen_comp_quad\n\t\t\t\t|gen_comp_quad :exp : term gen_term_quad exp_auxexp_aux : pl add_to_pilaOptr term gen_term_quad exp_aux\n\t\t\t|gen_term_quad :term : factor gen_factor_quad term_auxterm_aux : dm add_to_pilaOptr factor gen_factor_quad term_aux\n\t\t\t|gen_factor_quad :factor : LPAR add_to_pilaOptr expression RPAR pop_false_bottom\n\t\t\t| var_cte to_pilaOpao : AND\n\t\t\t| ORcomp : GREATER\n\t\t\t| LESS\n\t\t\t| GREATEROREQUAL\n\t\t\t| LESSOREQUAL\n\t\t\t| EQUALEQUALS\n\t\t\t| DIFFERENTpl : PLUS\n\t\t\t| MINUSto_pilaOp :add_to_pilaOptr :pop_false_bottom :dm : MULTIPLICATION\n\t\t\t| DIVISION\n\t\t\t| MODmain : MAIN main_to_proc_dir main_blockmain_to_proc_dir :main_block : LBRACKET more_vars more_statement RBRACKET gen_end_quadgen_end_quad :'
    
_lr_action_items = {'CTEDOUBLE':([15,31,46,64,72,73,80,86,92,94,101,102,104,105,106,107,108,117,124,125,129,130,131,133,134,135,136,137,138,139,153,154,160,],[25,25,25,-99,25,25,25,25,25,25,-102,-99,-101,-103,-97,-96,-99,25,25,25,-88,-99,-89,-95,-93,-90,-91,-94,-99,-92,25,25,25,]),'LPAR':([30,36,40,46,49,52,54,55,60,64,72,73,76,80,86,92,94,101,102,104,105,106,107,108,117,124,125,129,130,131,133,134,135,136,137,138,139,153,154,160,],[-25,45,46,64,70,72,73,46,-51,-99,64,64,94,64,64,64,64,-102,-99,-101,-103,-97,-96,-99,64,64,64,-88,-99,-89,-95,-93,-90,-91,-94,-99,-92,64,64,64,]),'RETURN':([1,13,23,50,51,53,56,57,59,71,75,98,122,146,152,155,166,170,171,177,178,179,183,186,],[-2,-3,-4,-41,-39,-40,-43,-42,-44,-38,-45,-3,-39,160,-55,-48,-57,-59,-52,-46,-67,-53,-50,-54,]),'LESS':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,136,-100,-86,-85,-81,-84,-80,-83,-79,]),'READ':([1,13,23,35,44,50,51,53,56,57,59,75,98,122,151,152,155,166,170,171,177,178,179,183,186,],[-2,-3,-4,-3,49,-41,49,-40,-43,-42,-44,-45,-3,49,49,-55,-48,-57,-59,-52,-46,-67,-53,-50,-54,]),'VOID':([12,],[20,]),'RPAR':([25,27,28,33,37,38,40,43,45,46,47,63,65,66,67,68,69,78,81,82,83,84,85,87,88,89,90,91,96,99,100,103,109,110,111,113,114,118,119,123,126,127,132,140,142,147,148,149,156,159,162,163,168,169,172,175,176,181,182,184,187,],[-20,-21,-19,-15,-18,-16,-15,-14,-31,-63,-17,79,81,-85,-98,-81,-65,-34,-66,-84,-87,-80,-62,-98,112,-73,-77,115,-33,123,-61,-82,-78,-65,-69,-72,-76,144,-30,-100,-64,150,-70,-74,-69,-86,-85,-81,-68,-34,-84,-80,-73,-77,-33,-83,-79,-72,-75,-32,-71,]),'LBRACKET':([17,29,79,112,128,144,158,167,180,],[-105,35,98,-58,151,-58,151,-56,151,]),'WHILE':([1,13,23,35,44,50,51,53,56,57,59,75,98,122,151,152,155,166,170,171,177,178,179,183,186,],[-2,-3,-4,-3,60,-41,60,-40,-43,-42,-44,-45,-3,60,60,-55,-48,-57,-59,-52,-46,-67,-53,-50,-54,]),'MULTIPLICATION':([25,27,28,33,37,38,40,43,47,66,67,81,82,83,100,123,147,148,162,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-66,104,-87,-61,-100,-86,-85,104,]),'MINUS':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,100,103,123,147,148,149,162,163,175,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,106,-61,-82,-100,-86,-85,-81,-84,106,-83,]),'SEMICOLON':([8,9,14,24,25,27,28,32,33,37,38,39,40,41,43,47,48,58,66,67,68,81,82,83,84,89,90,100,103,109,113,114,115,123,132,140,141,143,147,148,149,150,157,162,163,164,168,169,173,175,176,181,182,187,],[13,-15,-9,-11,-20,-21,-19,-13,-15,-18,-16,-10,-15,-8,-14,-17,-12,75,-85,-98,-81,-66,-84,-87,-80,-73,-77,-61,-82,-78,-72,-76,-49,-100,-70,-74,155,-60,-86,-85,-81,-47,170,-84,-80,177,-73,-77,185,-83,-79,-72,-75,-71,]),'PLUS':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,100,103,123,147,148,149,162,163,175,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,107,-61,-82,-100,-86,-85,-81,-84,107,-83,]),'COMMA':([9,14,24,25,27,28,32,33,37,38,39,40,43,47,66,67,68,69,78,81,82,83,84,96,100,103,109,110,123,147,148,149,159,162,163,172,175,176,],[-15,-9,-11,-20,-21,-19,42,-15,-18,-16,-10,-15,-14,-17,-85,-98,-81,86,-34,-66,-84,-87,-80,120,-61,-82,-78,86,-100,-86,-85,-81,-34,-84,-80,120,-83,-79,]),'RSQRTBRACKET':([25,26,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,100,103,109,116,123,147,148,149,162,163,175,176,],[-20,33,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-61,-82,-78,142,-100,-86,-85,-81,-84,-80,-83,-79,]),'$end':([5,16,34,77,95,],[0,-1,-104,-107,-106,]),'DIVISION':([25,27,28,33,37,38,40,43,47,66,67,81,82,83,100,123,147,148,162,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-66,101,-87,-61,-100,-86,-85,101,]),'DIFFERENT':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,133,-100,-86,-85,-81,-84,-80,-83,-79,]),'LESSOREQUAL':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,134,-100,-86,-85,-81,-84,-80,-83,-79,]),'EQUALEQUALS':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,137,-100,-86,-85,-81,-84,-80,-83,-79,]),'CTEINT':([15,31,46,64,72,73,80,86,92,94,101,102,104,105,106,107,108,117,124,125,129,130,131,133,134,135,136,137,138,139,153,154,160,],[28,28,28,-99,28,28,28,28,28,28,-102,-99,-101,-103,-97,-96,-99,28,28,28,-88,-99,-89,-95,-93,-90,-91,-94,-99,-92,28,28,28,]),'EQUALS':([9,14,24,33,43,55,74,93,142,156,],[-15,-9,31,-15,-14,-98,-69,117,-69,-68,]),'ELSE':([152,178,],[167,-67,]),'WRITE':([1,13,23,35,44,50,51,53,56,57,59,75,98,122,151,152,155,166,170,171,177,178,179,183,186,],[-2,-3,-4,-3,54,-41,54,-40,-43,-42,-44,-45,-3,54,54,-55,-48,-57,-59,-52,-46,-67,-53,-50,-54,]),'FUNC':([0,1,7,13,23,97,174,],[-3,-2,12,-3,-4,12,-35,]),'ID':([1,2,3,4,6,13,18,19,20,21,22,23,31,35,42,44,46,50,51,53,56,57,59,62,64,70,72,73,75,80,86,92,94,98,101,102,104,105,106,107,108,117,122,124,125,129,130,131,133,134,135,136,137,138,139,145,151,152,153,154,155,160,166,170,171,177,178,179,183,186,],[-2,9,-6,-7,-5,-3,30,-29,-26,-28,-27,-4,40,-3,9,55,40,-41,55,-40,-43,-42,-44,78,-99,87,40,40,-45,40,40,40,40,-3,-102,-99,-101,-103,-97,-96,-99,40,55,40,40,-88,-99,-89,-95,-93,-90,-91,-94,-99,-92,159,55,-55,40,40,-48,40,-57,-59,-52,-46,-67,-53,-50,-54,]),'IF':([1,13,23,35,44,50,51,53,56,57,59,75,98,122,151,152,155,166,170,171,177,178,179,183,186,],[-2,-3,-4,-3,52,-41,52,-40,-43,-42,-44,-45,-3,52,52,-55,-48,-57,-59,-52,-46,-67,-53,-50,-54,]),'AND':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,89,90,100,103,109,113,114,123,140,147,148,149,162,163,168,169,175,176,181,182,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-73,-77,-61,-82,-78,129,-76,-100,-74,-86,-85,-81,-84,-80,-73,-77,-83,-79,129,-75,]),'GREATER':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,135,-100,-86,-85,-81,-84,-80,-83,-79,]),'INT':([0,12,13,35,45,98,120,],[3,21,3,3,3,3,3,]),'DOUBLE':([0,12,13,35,45,98,120,],[4,19,4,4,4,4,4,]),'LSQRTBRACKET':([9,33,40,55,74,87,111,142,],[15,15,15,-98,92,-98,92,92,]),'BOOL':([0,12,13,35,45,98,120,],[6,22,6,6,6,6,6,]),'GREATEROREQUAL':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,90,100,103,109,114,123,147,148,149,162,163,175,176,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-77,-61,-82,-78,139,-100,-86,-85,-81,-84,-80,-83,-79,]),'CTEBOOL':([15,31,46,64,72,73,80,86,92,94,101,102,104,105,106,107,108,117,124,125,129,130,131,133,134,135,136,137,138,139,153,154,160,],[27,27,27,-99,27,27,27,27,27,27,-102,-99,-101,-103,-97,-96,-99,27,27,27,-88,-99,-89,-95,-93,-90,-91,-94,-99,-92,27,27,27,]),'RBRACKET':([1,13,23,35,44,50,51,53,56,57,59,61,71,75,98,122,146,151,152,155,161,165,166,170,171,177,178,179,183,185,186,],[-2,-3,-4,-3,-39,-41,-39,-40,-43,-42,-44,77,-38,-45,-3,-39,-37,-39,-55,-48,174,178,-57,-59,-52,-46,-67,-53,-50,-36,-54,]),'MAIN':([0,1,7,10,11,13,23,97,121,174,],[-3,-2,-23,-22,17,-3,-4,-23,-24,-35,]),'OR':([25,27,28,33,37,38,40,43,47,66,67,68,81,82,83,84,89,90,100,103,109,113,114,123,140,147,148,149,162,163,168,169,175,176,181,182,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-81,-66,-84,-87,-80,-73,-77,-61,-82,-78,131,-76,-100,-74,-86,-85,-81,-84,-80,-73,-77,-83,-79,131,-75,]),'MOD':([25,27,28,33,37,38,40,43,47,66,67,81,82,83,100,123,147,148,162,],[-20,-21,-19,-15,-18,-16,-15,-14,-17,-85,-98,-66,105,-87,-61,-100,-86,-85,105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'more_args':([96,172,],[119,184,]),'else_posible':([152,],[166,]),'arr':([9,33,40,],[14,43,47,]),'optional_return':([146,],[161,]),'check_type':([112,144,],[128,158,]),'var_type':([0,13,35,45,98,120,],[2,2,2,62,2,145,]),'main_block':([29,],[34,]),'to_pilaOp':([55,67,87,],[74,83,111,]),'expression_aux':([113,181,],[132,187,]),'var_cte':([31,46,72,73,80,86,92,94,117,124,125,153,154,160,],[39,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'vars_aux':([2,42,],[8,48,]),'arr_par':([74,111,142,],[93,127,156,]),'conc':([72,80,94,117,153,],[89,89,89,89,168,]),'conc_aux':([114,],[140,]),'gen_read_quad':([150,],[164,]),'more_vars':([0,13,35,98,],[7,23,44,122,]),'term_aux':([82,162,],[103,175,]),'cycle_start':([60,],[76,]),'gen_func_call_quad':([81,],[100,]),'const':([15,31,46,72,73,80,86,92,94,117,124,125,153,154,160,],[26,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'vars':([0,13,35,98,],[1,1,1,1,]),'cycle_end':([171,],[183,]),'gen_end_quad':([77,],[95,]),'gen_term_quad':([68,149,],[84,163,]),'more_func':([7,97,],[11,121,]),'write':([44,51,122,151,],[50,50,50,50,]),'read':([44,51,122,151,],[53,53,53,53,]),'program':([0,],[5,]),'params':([46,],[65,]),'arguments':([45,],[63,]),'statement':([44,51,122,151,],[51,51,51,51,]),'factor':([46,72,73,80,86,92,94,117,124,125,153,154,160,],[66,66,66,66,66,66,66,66,148,66,66,66,66,]),'main_to_proc_dir':([17,],[29,]),'gen_goto':([167,],[180,]),'var_assign':([24,],[32,]),'to_proc_dir':([30,],[36,]),'add_to_pilaOptr':([64,102,108,130,138,],[80,124,125,153,154,]),'gen_conc_quad':([89,168,],[113,181,]),'dm':([82,162,],[102,102,]),'to_args':([78,159,],[96,172,]),'func_type':([12,],[18,]),'comp':([114,],[138,]),'gen_comp_quad':([90,169,],[114,182,]),'gen_factor_quad':([66,148,],[82,162,]),'fill_end_condition':([166,],[179,]),'gen_write_quad':([115,],[141,]),'ao':([113,181,],[130,130,]),'func':([7,97,],[10,10,]),'condition':([44,51,122,151,],[56,56,56,56,]),'cycle':([44,51,122,151,],[57,57,57,57,]),'func_call':([31,44,46,51,72,73,80,86,92,94,117,122,124,125,151,153,154,160,],[37,58,37,58,37,37,37,37,37,37,37,58,37,37,58,37,37,37,]),'term':([46,72,73,80,86,92,94,117,125,153,154,160,],[68,68,68,68,68,68,68,68,149,68,68,68,]),'main':([11,],[16,]),'assignation':([44,51,122,151,],[59,59,59,59,]),'func_block':([79,],[97,]),'pop_false_bottom':([123,],[147,]),'more_statement':([44,51,122,151,],[61,71,146,165,]),'to_var_table':([14,],[24,]),'gen_assignation_quad':([143,],[157,]),'more_vars_aux':([32,],[41,]),'more_params':([69,110,],[85,126,]),'pl':([84,163,],[108,108,]),'exp':([46,72,73,80,86,92,94,117,153,154,160,],[69,90,91,90,110,116,90,90,90,169,173,]),'expression':([72,80,94,117,],[88,99,118,143,]),'exp_aux':([84,163,],[109,176,]),'block':([128,158,180,],[152,171,186,]),}

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
  ('vars_aux -> ID arr to_var_table var_assign more_vars_aux','vars_aux',5,'p_vars_aux','ObsidianParser.py',28),
  ('to_var_table -> <empty>','to_var_table',0,'p_to_var_table','ObsidianParser.py',32),
  ('var_assign -> EQUALS var_cte','var_assign',2,'p_var_assign','ObsidianParser.py',36),
  ('var_assign -> <empty>','var_assign',0,'p_var_assign','ObsidianParser.py',37),
  ('more_vars_aux -> COMMA vars_aux','more_vars_aux',2,'p_more_vars_aux','ObsidianParser.py',41),
  ('more_vars_aux -> <empty>','more_vars_aux',0,'p_more_vars_aux','ObsidianParser.py',42),
  ('arr -> LSQRTBRACKET const RSQRTBRACKET arr','arr',4,'p_arr','ObsidianParser.py',45),
  ('arr -> <empty>','arr',0,'p_arr','ObsidianParser.py',46),
  ('var_cte -> const','var_cte',1,'p_var_cte','ObsidianParser.py',50),
  ('var_cte -> ID arr','var_cte',2,'p_var_cte','ObsidianParser.py',51),
  ('var_cte -> func_call','var_cte',1,'p_var_cte','ObsidianParser.py',52),
  ('const -> CTEINT','const',1,'p_const','ObsidianParser.py',56),
  ('const -> CTEDOUBLE','const',1,'p_const','ObsidianParser.py',57),
  ('const -> CTEBOOL','const',1,'p_const','ObsidianParser.py',58),
  ('more_func -> func','more_func',1,'p_more_func','ObsidianParser.py',62),
  ('more_func -> <empty>','more_func',0,'p_more_func','ObsidianParser.py',63),
  ('func -> FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_func','func',9,'p_func','ObsidianParser.py',66),
  ('to_proc_dir -> <empty>','to_proc_dir',0,'p_to_proc_dir','ObsidianParser.py',69),
  ('func_type -> VOID','func_type',1,'p_func_type','ObsidianParser.py',73),
  ('func_type -> BOOL','func_type',1,'p_func_type','ObsidianParser.py',74),
  ('func_type -> INT','func_type',1,'p_func_type','ObsidianParser.py',75),
  ('func_type -> DOUBLE','func_type',1,'p_func_type','ObsidianParser.py',76),
  ('arguments -> var_type ID to_args more_args','arguments',4,'p_arguments','ObsidianParser.py',80),
  ('arguments -> <empty>','arguments',0,'p_arguments','ObsidianParser.py',81),
  ('more_args -> COMMA var_type ID to_args more_args','more_args',5,'p_more_args','ObsidianParser.py',85),
  ('more_args -> <empty>','more_args',0,'p_more_args','ObsidianParser.py',86),
  ('to_args -> <empty>','to_args',0,'p_to_args','ObsidianParser.py',89),
  ('func_block -> LBRACKET more_vars more_statement optional_return RBRACKET','func_block',5,'p_func_block','ObsidianParser.py',96),
  ('optional_return -> RETURN exp SEMICOLON','optional_return',3,'p_optional_return','ObsidianParser.py',99),
  ('optional_return -> <empty>','optional_return',0,'p_optional_return','ObsidianParser.py',100),
  ('more_statement -> statement more_statement','more_statement',2,'p_more_statement','ObsidianParser.py',103),
  ('more_statement -> <empty>','more_statement',0,'p_more_statement','ObsidianParser.py',104),
  ('statement -> read','statement',1,'p_statement','ObsidianParser.py',107),
  ('statement -> write','statement',1,'p_statement','ObsidianParser.py',108),
  ('statement -> cycle','statement',1,'p_statement','ObsidianParser.py',109),
  ('statement -> condition','statement',1,'p_statement','ObsidianParser.py',110),
  ('statement -> assignation','statement',1,'p_statement','ObsidianParser.py',111),
  ('statement -> func_call SEMICOLON','statement',2,'p_statement','ObsidianParser.py',112),
  ('read -> READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLON','read',8,'p_read','ObsidianParser.py',115),
  ('gen_read_quad -> <empty>','gen_read_quad',0,'p_gen_read_quad','ObsidianParser.py',118),
  ('write -> WRITE LPAR exp RPAR gen_write_quad SEMICOLON','write',6,'p_write','ObsidianParser.py',123),
  ('gen_write_quad -> <empty>','gen_write_quad',0,'p_gen_write_quad','ObsidianParser.py',126),
  ('cycle -> WHILE cycle_start LPAR expression RPAR check_type block cycle_end','cycle',8,'p_cycle','ObsidianParser.py',131),
  ('cycle_start -> <empty>','cycle_start',0,'p_cycle_start','ObsidianParser.py',134),
  ('cycle_end -> <empty>','cycle_end',0,'p_cycle_end','ObsidianParser.py',138),
  ('condition -> IF LPAR expression RPAR check_type block else_posible fill_end_condition','condition',8,'p_condition','ObsidianParser.py',142),
  ('else_posible -> ELSE gen_goto block','else_posible',3,'p_else_posible','ObsidianParser.py',145),
  ('else_posible -> <empty>','else_posible',0,'p_else_posible','ObsidianParser.py',146),
  ('gen_goto -> <empty>','gen_goto',0,'p_gen_goto','ObsidianParser.py',149),
  ('fill_end_condition -> <empty>','fill_end_condition',0,'p_fill_end_condition','ObsidianParser.py',153),
  ('check_type -> <empty>','check_type',0,'p_check_type','ObsidianParser.py',157),
  ('assignation -> ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLON','assignation',7,'p_assignation','ObsidianParser.py',161),
  ('gen_assignation_quad -> <empty>','gen_assignation_quad',0,'p_gen_assignation_quad','ObsidianParser.py',164),
  ('func_call -> ID LPAR params RPAR gen_func_call_quad','func_call',5,'p_func_call','ObsidianParser.py',169),
  ('params -> exp more_params','params',2,'p_params','ObsidianParser.py',172),
  ('params -> <empty>','params',0,'p_params','ObsidianParser.py',173),
  ('more_params -> COMMA exp more_params','more_params',3,'p_more_params','ObsidianParser.py',176),
  ('more_params -> <empty>','more_params',0,'p_more_params','ObsidianParser.py',177),
  ('gen_func_call_quad -> <empty>','gen_func_call_quad',0,'p_gen_func_call_quad','ObsidianParser.py',180),
  ('block -> LBRACKET more_statement RBRACKET','block',3,'p_block','ObsidianParser.py',184),
  ('arr_par -> LSQRTBRACKET exp RSQRTBRACKET arr_par','arr_par',4,'p_arr_par','ObsidianParser.py',187),
  ('arr_par -> <empty>','arr_par',0,'p_arr_par','ObsidianParser.py',188),
  ('expression -> conc gen_conc_quad expression_aux','expression',3,'p_expression','ObsidianParser.py',191),
  ('expression_aux -> ao add_to_pilaOptr conc gen_conc_quad expression_aux','expression_aux',5,'p_expression_aux','ObsidianParser.py',195),
  ('expression_aux -> <empty>','expression_aux',0,'p_expression_aux','ObsidianParser.py',196),
  ('gen_conc_quad -> <empty>','gen_conc_quad',0,'p_gen_conc_quad','ObsidianParser.py',198),
  ('conc -> exp gen_comp_quad conc_aux','conc',3,'p_conc','ObsidianParser.py',203),
  ('conc_aux -> comp add_to_pilaOptr exp gen_comp_quad','conc_aux',4,'p_conc_aux','ObsidianParser.py',207),
  ('conc_aux -> <empty>','conc_aux',0,'p_conc_aux','ObsidianParser.py',208),
  ('gen_comp_quad -> <empty>','gen_comp_quad',0,'p_gen_comp_quad','ObsidianParser.py',211),
  ('exp -> term gen_term_quad exp_aux','exp',3,'p_exp','ObsidianParser.py',216),
  ('exp_aux -> pl add_to_pilaOptr term gen_term_quad exp_aux','exp_aux',5,'p_exp_aux','ObsidianParser.py',220),
  ('exp_aux -> <empty>','exp_aux',0,'p_exp_aux','ObsidianParser.py',221),
  ('gen_term_quad -> <empty>','gen_term_quad',0,'p_gen_term_quad','ObsidianParser.py',224),
  ('term -> factor gen_factor_quad term_aux','term',3,'p_term','ObsidianParser.py',229),
  ('term_aux -> dm add_to_pilaOptr factor gen_factor_quad term_aux','term_aux',5,'p_term_aux','ObsidianParser.py',233),
  ('term_aux -> <empty>','term_aux',0,'p_term_aux','ObsidianParser.py',234),
  ('gen_factor_quad -> <empty>','gen_factor_quad',0,'p_gen_factor_quad','ObsidianParser.py',237),
  ('factor -> LPAR add_to_pilaOptr expression RPAR pop_false_bottom','factor',5,'p_factor','ObsidianParser.py',242),
  ('factor -> var_cte to_pilaOp','factor',2,'p_factor','ObsidianParser.py',243),
  ('ao -> AND','ao',1,'p_ao','ObsidianParser.py',250),
  ('ao -> OR','ao',1,'p_ao','ObsidianParser.py',251),
  ('comp -> GREATER','comp',1,'p_comp','ObsidianParser.py',255),
  ('comp -> LESS','comp',1,'p_comp','ObsidianParser.py',256),
  ('comp -> GREATEROREQUAL','comp',1,'p_comp','ObsidianParser.py',257),
  ('comp -> LESSOREQUAL','comp',1,'p_comp','ObsidianParser.py',258),
  ('comp -> EQUALEQUALS','comp',1,'p_comp','ObsidianParser.py',259),
  ('comp -> DIFFERENT','comp',1,'p_comp','ObsidianParser.py',260),
  ('pl -> PLUS','pl',1,'p_pl','ObsidianParser.py',264),
  ('pl -> MINUS','pl',1,'p_pl','ObsidianParser.py',265),
  ('to_pilaOp -> <empty>','to_pilaOp',0,'p_to_pilaOp','ObsidianParser.py',269),
  ('add_to_pilaOptr -> <empty>','add_to_pilaOptr',0,'p_add_to_pilaOptr','ObsidianParser.py',276),
  ('pop_false_bottom -> <empty>','pop_false_bottom',0,'p_pop_false_bottom','ObsidianParser.py',280),
  ('dm -> MULTIPLICATION','dm',1,'p_dm','ObsidianParser.py',284),
  ('dm -> DIVISION','dm',1,'p_dm','ObsidianParser.py',285),
  ('dm -> MOD','dm',1,'p_dm','ObsidianParser.py',286),
  ('main -> MAIN main_to_proc_dir main_block','main',3,'p_main','ObsidianParser.py',290),
  ('main_to_proc_dir -> <empty>','main_to_proc_dir',0,'p_main_to_proc_dir','ObsidianParser.py',293),
  ('main_block -> LBRACKET more_vars more_statement RBRACKET gen_end_quad','main_block',5,'p_main_block','ObsidianParser.py',299),
  ('gen_end_quad -> <empty>','gen_end_quad',0,'p_gen_end_quad','ObsidianParser.py',301),
]
