
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PLUS MINUS MULTIPLICATION DIVISION MOD EQUALS EQUALEQUALS DIFFERENT GREATER LESS GREATEROREQUAL LESSOREQUAL AND OR LPAR RPAR LBRACKET RBRACKET LSQRTBRACKET RSQRTBRACKET COMMA SEMICOLON CTEINT CTEDOUBLE CTEBOOL ID RETURN READ VOID ELSE FUNC IF DOUBLE WRITE INT WHILE BOOL MAINprogram : gen_goto_main more_vars more_func maingen_goto_main :more_vars : vars\n\t\t\t|vars : var_type vars_aux SEMICOLON more_varsvar_type : BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEvars_aux : ID arr to_var_table var_assign more_vars_auxto_var_table :var_assign : EQUALS var_cte\n\t\t\t|more_vars_aux : COMMA vars_aux\n\t\t\t|arr : LSQRTBRACKET const RSQRTBRACKET arr\n\t\t\t|var_cte : const\n\t\t\t| ID arr\n\t\t\t| func_callconst : CTEINT\n\t\t\t| CTEDOUBLE\n\t\t\t| CTEBOOLmore_func : func\n\t\t\t|func : FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_functo_proc_dir :func_type : VOID \n\t\t\t| BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEarguments : var_type ID to_args more_args\n\t\t\t|more_args : COMMA var_type ID to_args more_args\n\t\t\t|to_args :func_block : LBRACKET more_vars actual_quad_no more_statement gen_endproc_quad RBRACKETactual_quad_no :gen_endproc_quad :more_statement : statement more_statement\n\t\t\t|statement : read\n\t\t| write\n\t\t| return_stmt\n\t\t| cycle\n\t\t| condition\n\t\t| assignation\n\t\t| func_call SEMICOLONread : READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLONgen_read_quad :write : WRITE LPAR exp RPAR gen_write_quad SEMICOLONgen_write_quad :return_stmt : RETURN exp gen_return_quad SEMICOLONgen_return_quad :cycle : WHILE cycle_start LPAR expression RPAR check_type block cycle_endcycle_start :cycle_end :condition : IF LPAR expression RPAR check_type block else_posible fill_end_conditionelse_posible : ELSE gen_goto block\n\t\t\t|gen_goto :fill_end_condition :check_type :assignation : ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLONgen_assignation_quad :func_call : ID is_valid_func LPAR gen_era push_false_bottom params pop_false_bottom RPAR gen_go_subparams : exp check_args more_params\n\t\t\t|more_params : COMMA exp check_args more_params\n\t\t\t|check_args :is_valid_func :gen_era :gen_go_sub :block : LBRACKET more_statement RBRACKETarr_par : LSQRTBRACKET exp RSQRTBRACKET arr_par\n\t\t\t|expression : conc gen_conc_quad expression_auxexpression_aux : ao add_to_pilaOptr conc gen_conc_quad expression_aux\n\t\t\t|gen_conc_quad :conc : exp gen_comp_quad conc_auxconc_aux : comp add_to_pilaOptr exp gen_comp_quad\n\t\t\t\t|gen_comp_quad :exp : term gen_term_quad exp_auxexp_aux : pl add_to_pilaOptr term gen_term_quad exp_aux\n\t\t\t|gen_term_quad :term : factor gen_factor_quad term_auxterm_aux : dm add_to_pilaOptr factor gen_factor_quad term_aux\n\t\t\t|gen_factor_quad :factor : LPAR add_to_pilaOptr expression RPAR pop_false_bottom\n\t\t\t| var_cte to_pilaOpao : AND\n\t\t\t| ORcomp : GREATER\n\t\t\t| LESS\n\t\t\t| GREATEROREQUAL\n\t\t\t| LESSOREQUAL\n\t\t\t| EQUALEQUALS\n\t\t\t| DIFFERENTpl : PLUS\n\t\t\t| MINUSto_pilaOp :add_to_pilaOptr :push_false_bottom :pop_false_bottom :dm : MULTIPLICATION\n\t\t\t| DIVISION\n\t\t\t| MODmain : MAIN main_to_proc_dir main_blockmain_to_proc_dir :main_block : LBRACKET more_vars more_statement RBRACKET gen_end_quadgen_end_quad :'
    
_lr_action_items = {'CTEDOUBLE':([16,32,52,67,69,75,76,83,85,94,96,101,104,105,107,108,109,110,111,119,129,130,132,133,134,136,137,138,139,140,141,142,158,159,168,],[26,26,26,-72,-106,26,26,-107,26,26,26,26,-110,-106,-109,-111,-104,-103,-106,26,26,26,-95,-106,-96,-102,-100,-97,-98,-101,-106,-99,26,26,26,]),'LPAR':([31,37,41,48,50,52,55,57,58,63,67,69,75,76,79,83,85,94,96,101,104,105,107,108,109,110,111,119,129,130,132,133,134,136,137,138,139,140,141,142,158,159,168,],[-26,46,-71,67,68,69,75,76,-71,-55,-72,-106,69,69,96,-107,69,69,69,69,-110,-106,-109,-111,-104,-103,-106,69,69,69,-95,-106,-96,-102,-100,-97,-98,-101,-106,-99,69,69,69,]),'RETURN':([3,14,24,36,45,51,53,54,56,59,60,62,78,100,113,124,149,156,157,160,173,177,178,183,186,187,191,195,],[-3,-4,-5,-4,52,-43,-42,52,-41,-45,-44,-46,-47,-4,-52,-37,52,52,-59,-50,-61,-63,-56,-48,-74,-57,-54,-58,]),'LESS':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,139,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'READ':([3,14,24,36,45,51,53,54,56,59,60,62,78,100,113,124,149,156,157,160,173,177,178,183,186,187,191,195,],[-3,-4,-5,-4,50,-43,-42,50,-41,-45,-44,-46,-47,-4,-52,-37,50,50,-59,-50,-61,-63,-56,-48,-74,-57,-54,-58,]),'VOID':([13,],[21,]),'RPAR':([26,28,29,34,38,39,41,44,46,47,66,67,70,71,72,81,83,84,86,87,88,90,91,92,93,98,101,102,103,106,112,115,116,120,121,125,126,127,128,135,143,145,150,151,153,154,155,161,164,166,167,170,171,175,176,179,181,182,184,185,189,190,192,194,196,197,],[-21,-22,-20,-16,-19,-17,-16,-15,-32,-18,82,-72,-92,-105,-88,-35,-107,-105,-91,-94,-87,114,-80,-84,117,-34,-67,-76,128,-89,-85,-79,-83,147,-31,-108,-70,152,-108,-77,-81,-76,166,-69,-93,-92,-88,-75,-35,-73,-66,-91,-87,-80,-84,-34,-65,-70,-90,-86,-79,-82,-33,-69,-78,-68,]),'LBRACKET':([18,30,82,114,131,147,163,174,188,],[-113,36,100,-62,156,-62,156,-60,156,]),'WHILE':([3,14,24,36,45,51,53,54,56,59,60,62,78,100,113,124,149,156,157,160,173,177,178,183,186,187,191,195,],[-3,-4,-5,-4,63,-43,-42,63,-41,-45,-44,-46,-47,-4,-52,-37,63,63,-59,-50,-61,-63,-56,-48,-74,-57,-54,-58,]),'MULTIPLICATION':([26,28,29,34,38,39,41,44,47,70,71,86,87,128,153,154,166,170,181,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,107,-94,-108,-93,-92,-73,107,-65,]),'MINUS':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,106,128,153,154,155,166,170,171,181,184,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,109,-89,-108,-93,-92,-88,-73,-91,109,-65,-90,]),'RSQRTBRACKET':([26,27,28,29,34,38,39,41,44,47,70,71,72,86,87,88,106,112,118,128,153,154,155,166,170,171,181,184,185,],[-21,34,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-89,-85,145,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'SEMICOLON':([9,10,15,25,26,28,29,33,34,38,39,40,41,42,44,47,49,61,70,71,72,73,86,87,88,89,91,92,106,112,115,116,117,128,135,143,144,146,152,153,154,155,162,166,169,170,171,175,176,181,184,185,189,190,196,],[14,-16,-10,-12,-21,-22,-20,-14,-16,-19,-17,-11,-16,-9,-15,-18,-13,78,-92,-105,-88,-53,-91,-94,-87,113,-80,-84,-89,-85,-79,-83,-51,-108,-77,-81,160,-64,-49,-93,-92,-88,177,-73,183,-91,-87,-80,-84,-65,-90,-86,-79,-82,-78,]),'COMMA':([10,15,25,26,28,29,33,34,38,39,40,41,44,47,70,71,72,81,86,87,88,98,106,112,126,128,151,153,154,155,164,166,170,171,179,181,182,184,185,194,],[-16,-10,-12,-21,-22,-20,43,-16,-19,-17,-11,-16,-15,-18,-92,-105,-88,-35,-91,-94,-87,122,-89,-85,-70,-108,168,-93,-92,-88,-35,-73,-91,-87,122,-65,-70,-90,-86,168,]),'PLUS':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,106,128,153,154,155,166,170,171,181,184,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,110,-89,-108,-93,-92,-88,-73,-91,110,-65,-90,]),'$end':([2,17,35,80,97,],[0,-1,-112,-115,-114,]),'DIVISION':([26,28,29,34,38,39,41,44,47,70,71,86,87,128,153,154,166,170,181,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,104,-94,-108,-93,-92,-73,104,-65,]),'DIFFERENT':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,136,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'LESSOREQUAL':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,137,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'EQUALEQUALS':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,140,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'CTEINT':([16,32,52,67,69,75,76,83,85,94,96,101,104,105,107,108,109,110,111,119,129,130,132,133,134,136,137,138,139,140,141,142,158,159,168,],[29,29,29,-72,-106,29,29,-107,29,29,29,29,-110,-106,-109,-111,-104,-103,-106,29,29,29,-95,-106,-96,-102,-100,-97,-98,-101,-106,-99,29,29,29,]),'EQUALS':([10,15,25,34,44,58,77,95,145,161,],[-16,-10,32,-16,-15,-105,-76,119,-76,-75,]),'ELSE':([157,186,],[174,-74,]),'WRITE':([3,14,24,36,45,51,53,54,56,59,60,62,78,100,113,124,149,156,157,160,173,177,178,183,186,187,191,195,],[-3,-4,-5,-4,57,-43,-42,57,-41,-45,-44,-46,-47,-4,-52,-37,57,57,-59,-50,-61,-63,-56,-48,-74,-57,-54,-58,]),'FUNC':([0,1,3,8,14,24,99,193,],[-2,-4,-3,13,-4,-5,13,-36,]),'ID':([3,4,5,6,7,14,19,20,21,22,23,24,32,36,43,45,51,52,53,54,56,59,60,62,65,67,68,69,75,76,78,83,85,94,96,100,101,104,105,107,108,109,110,111,113,119,124,129,130,132,133,134,136,137,138,139,140,141,142,148,149,156,157,158,159,160,168,173,177,178,183,186,187,191,195,],[-3,10,-7,-8,-6,-4,31,-30,-27,-29,-28,-5,41,-4,10,58,-43,41,-42,58,-41,-45,-44,-46,81,-72,84,-106,41,41,-47,-107,41,41,41,-4,41,-110,-106,-109,-111,-104,-103,-106,-52,41,-37,41,41,-95,-106,-96,-102,-100,-97,-98,-101,-106,-99,164,58,58,-59,41,41,-50,41,-61,-63,-56,-48,-74,-57,-54,-58,]),'IF':([3,14,24,36,45,51,53,54,56,59,60,62,78,100,113,124,149,156,157,160,173,177,178,183,186,187,191,195,],[-3,-4,-5,-4,55,-43,-42,55,-41,-45,-44,-46,-47,-4,-52,-37,55,55,-59,-50,-61,-63,-56,-48,-74,-57,-54,-58,]),'AND':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,91,92,106,112,115,116,128,143,153,154,155,166,170,171,175,176,181,184,185,189,190,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-80,-84,-89,-85,132,-83,-108,-81,-93,-92,-88,-73,-91,-87,-80,-84,-65,-90,-86,132,-82,]),'GREATER':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,138,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'INT':([0,1,13,14,36,46,100,122,],[-2,5,22,5,5,5,5,5,]),'DOUBLE':([0,1,13,14,36,46,100,122,],[-2,6,20,6,6,6,6,6,]),'LSQRTBRACKET':([10,34,41,58,77,84,102,145,],[16,16,16,-105,94,-105,94,94,]),'BOOL':([0,1,13,14,36,46,100,122,],[-2,7,23,7,7,7,7,7,]),'GREATEROREQUAL':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,92,106,112,116,128,153,154,155,166,170,171,181,184,185,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-84,-89,-85,142,-108,-93,-92,-88,-73,-91,-87,-65,-90,-86,]),'CTEBOOL':([16,32,52,67,69,75,76,83,85,94,96,101,104,105,107,108,109,110,111,119,129,130,132,133,134,136,137,138,139,140,141,142,158,159,168,],[28,28,28,-72,-106,28,28,-107,28,28,28,28,-110,-106,-109,-111,-104,-103,-106,28,28,28,-95,-106,-96,-102,-100,-97,-98,-101,-106,-99,28,28,28,]),'RBRACKET':([3,14,24,36,45,51,53,54,56,59,60,62,64,74,78,100,113,124,149,156,157,160,165,172,173,177,178,180,183,186,187,191,195,],[-3,-4,-5,-4,-40,-43,-42,-40,-41,-45,-44,-46,80,-39,-47,-4,-52,-37,-40,-40,-59,-50,-38,186,-61,-63,-56,193,-48,-74,-57,-54,-58,]),'MAIN':([0,1,3,8,11,12,14,24,99,123,193,],[-2,-4,-3,-24,-23,18,-4,-5,-24,-25,-36,]),'OR':([26,28,29,34,38,39,41,44,47,70,71,72,86,87,88,91,92,106,112,115,116,128,143,153,154,155,166,170,171,175,176,181,184,185,189,190,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,-88,-91,-94,-87,-80,-84,-89,-85,134,-83,-108,-81,-93,-92,-88,-73,-91,-87,-80,-84,-65,-90,-86,134,-82,]),'MOD':([26,28,29,34,38,39,41,44,47,70,71,86,87,128,153,154,166,170,181,],[-21,-22,-20,-16,-19,-17,-16,-15,-18,-92,-105,108,-94,-108,-93,-92,-73,108,-65,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'more_args':([98,179,],[121,192,]),'else_posible':([157,],[173,]),'arr':([10,34,41,],[15,44,47,]),'gen_read_quad':([152,],[169,]),'check_type':([114,147,],[131,163,]),'var_type':([1,14,36,46,100,122,],[4,4,4,65,4,148,]),'main_block':([30,],[35,]),'to_pilaOp':([58,71,84,],[77,87,102,]),'ao':([115,189,],[133,133,]),'var_cte':([32,52,75,76,85,94,96,101,119,129,130,158,159,168,],[40,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'vars_aux':([4,43,],[9,49,]),'arr_par':([77,102,145,],[95,127,161,]),'conc':([75,85,96,119,158,],[91,91,91,91,175,]),'return_stmt':([45,54,149,156,],[51,51,51,51,]),'conc_aux':([116,],[143,]),'is_valid_func':([41,58,],[48,48,]),'more_func':([8,99,],[12,123,]),'gen_era':([67,],[83,]),'term_aux':([86,170,],[106,184,]),'cycle_start':([63,],[79,]),'const':([16,32,52,75,76,85,94,96,101,119,129,130,158,159,168,],[27,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'vars':([1,14,36,100,],[3,3,3,3,]),'gen_return_quad':([73,],[89,]),'cycle_end':([178,],[191,]),'gen_end_quad':([80,],[97,]),'gen_term_quad':([72,155,],[88,171,]),'more_vars':([1,14,36,100,],[8,24,45,124,]),'write':([45,54,149,156,],[53,53,53,53,]),'gen_goto_main':([0,],[1,]),'program':([0,],[2,]),'params':([101,],[125,]),'arguments':([46,],[66,]),'statement':([45,54,149,156,],[54,54,54,54,]),'factor':([52,75,76,85,94,96,101,119,129,130,158,159,168,],[70,70,70,70,70,70,70,70,154,70,70,70,70,]),'main_to_proc_dir':([18,],[30,]),'actual_quad_no':([124,],[149,]),'var_assign':([25,],[33,]),'to_proc_dir':([31,],[37,]),'add_to_pilaOptr':([69,105,111,133,141,],[85,129,130,158,159,]),'gen_conc_quad':([91,175,],[115,189,]),'dm':([86,170,],[105,105,]),'to_args':([81,164,],[98,179,]),'func_type':([13,],[19,]),'comp':([116,],[141,]),'gen_comp_quad':([92,176,],[116,190,]),'gen_factor_quad':([70,154,],[86,170,]),'check_args':([126,182,],[151,194,]),'fill_end_condition':([173,],[187,]),'gen_write_quad':([117,],[144,]),'gen_goto':([174,],[188,]),'func':([8,99,],[11,11,]),'more_params':([151,194,],[167,197,]),'push_false_bottom':([83,],[101,]),'condition':([45,54,149,156,],[59,59,59,59,]),'cycle':([45,54,149,156,],[60,60,60,60,]),'func_call':([32,45,52,54,75,76,85,94,96,101,119,129,130,149,156,158,159,168,],[38,61,38,61,38,38,38,38,38,38,38,38,38,61,61,38,38,38,]),'term':([52,75,76,85,94,96,101,119,130,158,159,168,],[72,72,72,72,72,72,72,72,155,72,72,72,]),'main':([12,],[17,]),'assignation':([45,54,149,156,],[62,62,62,62,]),'func_block':([82,],[99,]),'read':([45,54,149,156,],[56,56,56,56,]),'pop_false_bottom':([125,128,],[150,153,]),'gen_endproc_quad':([165,],[180,]),'gen_go_sub':([166,],[181,]),'more_statement':([45,54,149,156,],[64,74,165,172,]),'to_var_table':([15,],[25,]),'gen_assignation_quad':([146,],[162,]),'more_vars_aux':([33,],[42,]),'expression_aux':([115,189,],[135,196,]),'pl':([88,171,],[111,111,]),'exp':([52,75,76,85,94,96,101,119,158,159,168,],[73,92,93,92,118,92,126,92,92,176,182,]),'expression':([75,85,96,119,],[90,103,120,146,]),'exp_aux':([88,171,],[112,185,]),'block':([131,163,188,],[157,178,195,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> gen_goto_main more_vars more_func main','program',4,'p_program','ObsidianParser.py',13),
  ('gen_goto_main -> <empty>','gen_goto_main',0,'p_gen_goto_main','ObsidianParser.py',17),
  ('more_vars -> vars','more_vars',1,'p_more_vars','ObsidianParser.py',22),
  ('more_vars -> <empty>','more_vars',0,'p_more_vars','ObsidianParser.py',23),
  ('vars -> var_type vars_aux SEMICOLON more_vars','vars',4,'p_vars','ObsidianParser.py',26),
  ('var_type -> BOOL','var_type',1,'p_var_type','ObsidianParser.py',29),
  ('var_type -> INT','var_type',1,'p_var_type','ObsidianParser.py',30),
  ('var_type -> DOUBLE','var_type',1,'p_var_type','ObsidianParser.py',31),
  ('vars_aux -> ID arr to_var_table var_assign more_vars_aux','vars_aux',5,'p_vars_aux','ObsidianParser.py',36),
  ('to_var_table -> <empty>','to_var_table',0,'p_to_var_table','ObsidianParser.py',40),
  ('var_assign -> EQUALS var_cte','var_assign',2,'p_var_assign','ObsidianParser.py',44),
  ('var_assign -> <empty>','var_assign',0,'p_var_assign','ObsidianParser.py',45),
  ('more_vars_aux -> COMMA vars_aux','more_vars_aux',2,'p_more_vars_aux','ObsidianParser.py',49),
  ('more_vars_aux -> <empty>','more_vars_aux',0,'p_more_vars_aux','ObsidianParser.py',50),
  ('arr -> LSQRTBRACKET const RSQRTBRACKET arr','arr',4,'p_arr','ObsidianParser.py',53),
  ('arr -> <empty>','arr',0,'p_arr','ObsidianParser.py',54),
  ('var_cte -> const','var_cte',1,'p_var_cte','ObsidianParser.py',58),
  ('var_cte -> ID arr','var_cte',2,'p_var_cte','ObsidianParser.py',59),
  ('var_cte -> func_call','var_cte',1,'p_var_cte','ObsidianParser.py',60),
  ('const -> CTEINT','const',1,'p_const','ObsidianParser.py',64),
  ('const -> CTEDOUBLE','const',1,'p_const','ObsidianParser.py',65),
  ('const -> CTEBOOL','const',1,'p_const','ObsidianParser.py',66),
  ('more_func -> func','more_func',1,'p_more_func','ObsidianParser.py',70),
  ('more_func -> <empty>','more_func',0,'p_more_func','ObsidianParser.py',71),
  ('func -> FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_func','func',9,'p_func','ObsidianParser.py',74),
  ('to_proc_dir -> <empty>','to_proc_dir',0,'p_to_proc_dir','ObsidianParser.py',77),
  ('func_type -> VOID','func_type',1,'p_func_type','ObsidianParser.py',81),
  ('func_type -> BOOL','func_type',1,'p_func_type','ObsidianParser.py',82),
  ('func_type -> INT','func_type',1,'p_func_type','ObsidianParser.py',83),
  ('func_type -> DOUBLE','func_type',1,'p_func_type','ObsidianParser.py',84),
  ('arguments -> var_type ID to_args more_args','arguments',4,'p_arguments','ObsidianParser.py',88),
  ('arguments -> <empty>','arguments',0,'p_arguments','ObsidianParser.py',89),
  ('more_args -> COMMA var_type ID to_args more_args','more_args',5,'p_more_args','ObsidianParser.py',93),
  ('more_args -> <empty>','more_args',0,'p_more_args','ObsidianParser.py',94),
  ('to_args -> <empty>','to_args',0,'p_to_args','ObsidianParser.py',97),
  ('func_block -> LBRACKET more_vars actual_quad_no more_statement gen_endproc_quad RBRACKET','func_block',6,'p_func_block','ObsidianParser.py',104),
  ('actual_quad_no -> <empty>','actual_quad_no',0,'p_actual_quad_no','ObsidianParser.py',107),
  ('gen_endproc_quad -> <empty>','gen_endproc_quad',0,'p_gen_endproc_quad','ObsidianParser.py',112),
  ('more_statement -> statement more_statement','more_statement',2,'p_more_statement','ObsidianParser.py',117),
  ('more_statement -> <empty>','more_statement',0,'p_more_statement','ObsidianParser.py',118),
  ('statement -> read','statement',1,'p_statement','ObsidianParser.py',121),
  ('statement -> write','statement',1,'p_statement','ObsidianParser.py',122),
  ('statement -> return_stmt','statement',1,'p_statement','ObsidianParser.py',123),
  ('statement -> cycle','statement',1,'p_statement','ObsidianParser.py',124),
  ('statement -> condition','statement',1,'p_statement','ObsidianParser.py',125),
  ('statement -> assignation','statement',1,'p_statement','ObsidianParser.py',126),
  ('statement -> func_call SEMICOLON','statement',2,'p_statement','ObsidianParser.py',127),
  ('read -> READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLON','read',8,'p_read','ObsidianParser.py',130),
  ('gen_read_quad -> <empty>','gen_read_quad',0,'p_gen_read_quad','ObsidianParser.py',133),
  ('write -> WRITE LPAR exp RPAR gen_write_quad SEMICOLON','write',6,'p_write','ObsidianParser.py',138),
  ('gen_write_quad -> <empty>','gen_write_quad',0,'p_gen_write_quad','ObsidianParser.py',141),
  ('return_stmt -> RETURN exp gen_return_quad SEMICOLON','return_stmt',4,'p_return_stmt','ObsidianParser.py',146),
  ('gen_return_quad -> <empty>','gen_return_quad',0,'p_gen_return_quad','ObsidianParser.py',149),
  ('cycle -> WHILE cycle_start LPAR expression RPAR check_type block cycle_end','cycle',8,'p_cycle','ObsidianParser.py',155),
  ('cycle_start -> <empty>','cycle_start',0,'p_cycle_start','ObsidianParser.py',158),
  ('cycle_end -> <empty>','cycle_end',0,'p_cycle_end','ObsidianParser.py',162),
  ('condition -> IF LPAR expression RPAR check_type block else_posible fill_end_condition','condition',8,'p_condition','ObsidianParser.py',166),
  ('else_posible -> ELSE gen_goto block','else_posible',3,'p_else_posible','ObsidianParser.py',169),
  ('else_posible -> <empty>','else_posible',0,'p_else_posible','ObsidianParser.py',170),
  ('gen_goto -> <empty>','gen_goto',0,'p_gen_goto','ObsidianParser.py',173),
  ('fill_end_condition -> <empty>','fill_end_condition',0,'p_fill_end_condition','ObsidianParser.py',177),
  ('check_type -> <empty>','check_type',0,'p_check_type','ObsidianParser.py',181),
  ('assignation -> ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLON','assignation',7,'p_assignation','ObsidianParser.py',185),
  ('gen_assignation_quad -> <empty>','gen_assignation_quad',0,'p_gen_assignation_quad','ObsidianParser.py',188),
  ('func_call -> ID is_valid_func LPAR gen_era push_false_bottom params pop_false_bottom RPAR gen_go_sub','func_call',9,'p_func_call','ObsidianParser.py',193),
  ('params -> exp check_args more_params','params',3,'p_params','ObsidianParser.py',197),
  ('params -> <empty>','params',0,'p_params','ObsidianParser.py',198),
  ('more_params -> COMMA exp check_args more_params','more_params',4,'p_more_params','ObsidianParser.py',201),
  ('more_params -> <empty>','more_params',0,'p_more_params','ObsidianParser.py',202),
  ('check_args -> <empty>','check_args',0,'p_check_args','ObsidianParser.py',205),
  ('is_valid_func -> <empty>','is_valid_func',0,'p_is_valid_func','ObsidianParser.py',209),
  ('gen_era -> <empty>','gen_era',0,'p_gen_era','ObsidianParser.py',213),
  ('gen_go_sub -> <empty>','gen_go_sub',0,'p_gen_go_sub','ObsidianParser.py',217),
  ('block -> LBRACKET more_statement RBRACKET','block',3,'p_block','ObsidianParser.py',221),
  ('arr_par -> LSQRTBRACKET exp RSQRTBRACKET arr_par','arr_par',4,'p_arr_par','ObsidianParser.py',224),
  ('arr_par -> <empty>','arr_par',0,'p_arr_par','ObsidianParser.py',225),
  ('expression -> conc gen_conc_quad expression_aux','expression',3,'p_expression','ObsidianParser.py',228),
  ('expression_aux -> ao add_to_pilaOptr conc gen_conc_quad expression_aux','expression_aux',5,'p_expression_aux','ObsidianParser.py',232),
  ('expression_aux -> <empty>','expression_aux',0,'p_expression_aux','ObsidianParser.py',233),
  ('gen_conc_quad -> <empty>','gen_conc_quad',0,'p_gen_conc_quad','ObsidianParser.py',235),
  ('conc -> exp gen_comp_quad conc_aux','conc',3,'p_conc','ObsidianParser.py',240),
  ('conc_aux -> comp add_to_pilaOptr exp gen_comp_quad','conc_aux',4,'p_conc_aux','ObsidianParser.py',244),
  ('conc_aux -> <empty>','conc_aux',0,'p_conc_aux','ObsidianParser.py',245),
  ('gen_comp_quad -> <empty>','gen_comp_quad',0,'p_gen_comp_quad','ObsidianParser.py',248),
  ('exp -> term gen_term_quad exp_aux','exp',3,'p_exp','ObsidianParser.py',253),
  ('exp_aux -> pl add_to_pilaOptr term gen_term_quad exp_aux','exp_aux',5,'p_exp_aux','ObsidianParser.py',257),
  ('exp_aux -> <empty>','exp_aux',0,'p_exp_aux','ObsidianParser.py',258),
  ('gen_term_quad -> <empty>','gen_term_quad',0,'p_gen_term_quad','ObsidianParser.py',261),
  ('term -> factor gen_factor_quad term_aux','term',3,'p_term','ObsidianParser.py',266),
  ('term_aux -> dm add_to_pilaOptr factor gen_factor_quad term_aux','term_aux',5,'p_term_aux','ObsidianParser.py',270),
  ('term_aux -> <empty>','term_aux',0,'p_term_aux','ObsidianParser.py',271),
  ('gen_factor_quad -> <empty>','gen_factor_quad',0,'p_gen_factor_quad','ObsidianParser.py',274),
  ('factor -> LPAR add_to_pilaOptr expression RPAR pop_false_bottom','factor',5,'p_factor','ObsidianParser.py',279),
  ('factor -> var_cte to_pilaOp','factor',2,'p_factor','ObsidianParser.py',280),
  ('ao -> AND','ao',1,'p_ao','ObsidianParser.py',287),
  ('ao -> OR','ao',1,'p_ao','ObsidianParser.py',288),
  ('comp -> GREATER','comp',1,'p_comp','ObsidianParser.py',292),
  ('comp -> LESS','comp',1,'p_comp','ObsidianParser.py',293),
  ('comp -> GREATEROREQUAL','comp',1,'p_comp','ObsidianParser.py',294),
  ('comp -> LESSOREQUAL','comp',1,'p_comp','ObsidianParser.py',295),
  ('comp -> EQUALEQUALS','comp',1,'p_comp','ObsidianParser.py',296),
  ('comp -> DIFFERENT','comp',1,'p_comp','ObsidianParser.py',297),
  ('pl -> PLUS','pl',1,'p_pl','ObsidianParser.py',301),
  ('pl -> MINUS','pl',1,'p_pl','ObsidianParser.py',302),
  ('to_pilaOp -> <empty>','to_pilaOp',0,'p_to_pilaOp','ObsidianParser.py',306),
  ('add_to_pilaOptr -> <empty>','add_to_pilaOptr',0,'p_add_to_pilaOptr','ObsidianParser.py',316),
  ('push_false_bottom -> <empty>','push_false_bottom',0,'p_push_false_bottom','ObsidianParser.py',320),
  ('pop_false_bottom -> <empty>','pop_false_bottom',0,'p_pop_false_bottom','ObsidianParser.py',324),
  ('dm -> MULTIPLICATION','dm',1,'p_dm','ObsidianParser.py',328),
  ('dm -> DIVISION','dm',1,'p_dm','ObsidianParser.py',329),
  ('dm -> MOD','dm',1,'p_dm','ObsidianParser.py',330),
  ('main -> MAIN main_to_proc_dir main_block','main',3,'p_main','ObsidianParser.py',334),
  ('main_to_proc_dir -> <empty>','main_to_proc_dir',0,'p_main_to_proc_dir','ObsidianParser.py',337),
  ('main_block -> LBRACKET more_vars more_statement RBRACKET gen_end_quad','main_block',5,'p_main_block','ObsidianParser.py',344),
  ('gen_end_quad -> <empty>','gen_end_quad',0,'p_gen_end_quad','ObsidianParser.py',346),
]
