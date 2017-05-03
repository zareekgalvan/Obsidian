
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PLUS MINUS MULTIPLICATION DIVISION MOD EQUALS EQUALEQUALS DIFFERENT GREATER LESS GREATEROREQUAL LESSOREQUAL AND OR LPAR RPAR LBRACKET RBRACKET LSQRTBRACKET RSQRTBRACKET COMMA SEMICOLON CTEINT CTEDOUBLE CTEBOOL ID RETURN READ VOID ELSE FUNC IF DOUBLE WRITE INT WHILE BOOL MAINprogram : gen_goto_main more_vars more_func maingen_goto_main :more_vars : vars\n\t\t\t|vars : var_type vars_aux SEMICOLON more_varsvar_type : BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEvars_aux : ID to_var_table arr var_assign more_vars_auxto_var_table :var_assign : EQUALS var_cte\n\t\t\t|more_vars_aux : COMMA vars_aux\n\t\t\t|arr : LSQRTBRACKET const register_space RSQRTBRACKET\n\t\t\t|register_space :var_cte : const to_pilaOp\n\t\t\t| ID to_pilaOp arr_par\n\t\t\t| func_call to_pilaOpconst : CTEINT\n\t\t\t| CTEDOUBLE\n\t\t\t| CTEBOOLmore_func : func\n\t\t\t|func : FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_functo_proc_dir :func_type : VOID \n\t\t\t| BOOL\n\t\t\t| INT\n\t\t\t| DOUBLEarguments : var_type ID to_args more_args\n\t\t\t|more_args : COMMA var_type ID to_args more_args\n\t\t\t|to_args :func_block : LBRACKET more_vars actual_quad_no more_statement gen_endproc_quad RBRACKETactual_quad_no :gen_endproc_quad :more_statement : statement more_statement\n\t\t\t|statement : read\n\t\t| write\n\t\t| return_stmt\n\t\t| cycle\n\t\t| condition\n\t\t| assignation\n\t\t| func_call SEMICOLONread : READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLONgen_read_quad :write : WRITE LPAR exp RPAR gen_write_quad SEMICOLONgen_write_quad :return_stmt : RETURN exp gen_return_quad SEMICOLONgen_return_quad :cycle : WHILE cycle_start LPAR expression RPAR check_type block cycle_endcycle_start :cycle_end :condition : IF LPAR expression RPAR check_type block else_posible fill_end_conditionelse_posible : ELSE gen_goto block\n\t\t\t|gen_goto :fill_end_condition :check_type :assignation : ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLONgen_assignation_quad :func_call : ID is_valid_func LPAR gen_era push_false_bottom params pop_false_bottom RPAR gen_go_subparams : exp check_args more_params\n\t\t\t|more_params : COMMA exp check_args more_params\n\t\t\t|check_args :is_valid_func :gen_era :gen_go_sub :block : LBRACKET more_statement RBRACKETarr_par : LSQRTBRACKET exp RSQRTBRACKET \n\t\t\t|expression : conc gen_conc_quad expression_auxexpression_aux : ao add_to_pilaOptr conc gen_conc_quad expression_aux\n\t\t\t|gen_conc_quad :conc : exp gen_comp_quad conc_auxconc_aux : comp add_to_pilaOptr exp gen_comp_quad\n\t\t\t\t|gen_comp_quad :exp : term gen_term_quad exp_auxexp_aux : pl add_to_pilaOptr term gen_term_quad exp_aux\n\t\t\t|gen_term_quad :term : factor gen_factor_quad term_auxterm_aux : dm add_to_pilaOptr factor gen_factor_quad term_aux\n\t\t\t|gen_factor_quad :factor : LPAR add_to_pilaOptr expression RPAR pop_false_bottom\n\t\t\t| var_cteao : AND\n\t\t\t| ORcomp : GREATER\n\t\t\t| LESS\n\t\t\t| GREATEROREQUAL\n\t\t\t| LESSOREQUAL\n\t\t\t| EQUALEQUALS\n\t\t\t| DIFFERENTpl : PLUS\n\t\t\t| MINUSto_pilaOp :add_to_pilaOptr :push_false_bottom :pop_false_bottom :dm : MULTIPLICATION\n\t\t\t| DIVISION\n\t\t\t| MODmain : MAIN main_to_proc_dir main_blockmain_to_proc_dir :main_block : LBRACKET more_vars more_statement RBRACKET gen_end_quadgen_end_quad :'
    
_lr_action_items = {'CTEDOUBLE':([25,28,54,69,71,73,79,80,88,90,99,105,108,109,111,112,113,114,115,122,132,133,135,136,137,139,140,141,142,143,144,145,160,161,169,],[30,30,30,30,-73,-107,30,30,-108,30,30,30,-111,-107,-110,-112,-105,-104,-107,30,30,30,-96,-107,-97,-103,-101,-98,-99,-102,-107,-100,30,30,30,]),'LPAR':([27,36,40,49,52,54,57,59,60,65,69,71,73,79,80,83,88,90,99,105,108,109,111,112,113,114,115,122,132,133,135,136,137,139,140,141,142,143,144,145,160,161,169,],[-27,45,-72,71,72,73,79,80,-72,-56,73,-73,-107,73,73,99,-108,73,73,73,-111,-107,-110,-112,-105,-104,-107,73,73,73,-96,-107,-97,-103,-101,-98,-99,-102,-107,-100,73,73,73,]),'RETURN':([3,14,23,35,44,53,55,56,58,61,62,64,82,103,117,127,151,158,159,162,174,178,179,184,187,188,192,196,],[-3,-4,-5,-4,54,-44,-43,54,-42,-46,-45,-47,-48,-4,-53,-38,54,54,-60,-51,-62,-64,-57,-49,-75,-58,-55,-59,]),'LESS':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,142,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'READ':([3,14,23,35,44,53,55,56,58,61,62,64,82,103,117,127,151,158,159,162,174,178,179,184,187,188,192,196,],[-3,-4,-5,-4,52,-44,-43,52,-42,-46,-45,-47,-48,-4,-53,-38,52,52,-60,-51,-62,-64,-57,-49,-75,-58,-55,-59,]),'VOID':([13,],[20,]),'RPAR':([30,32,33,37,38,40,45,46,47,48,68,70,71,74,75,76,85,88,89,91,92,94,95,96,97,101,104,105,106,107,110,116,119,120,123,124,128,129,130,131,138,146,152,153,155,156,157,165,167,168,171,172,176,177,180,182,183,185,186,190,191,193,195,197,198,],[-22,-23,-21,-106,-106,-106,-33,-20,-18,-77,86,-19,-73,-93,-95,-89,-36,-108,-106,-92,-88,118,-81,-85,121,-35,-76,-68,-77,131,-90,-86,-80,-84,149,-32,-109,-71,154,-109,-78,-82,167,-70,-94,-93,-89,-36,-74,-67,-92,-88,-81,-85,-35,-66,-71,-91,-87,-80,-83,-34,-70,-79,-69,]),'LBRACKET':([17,26,86,118,134,149,164,175,189,],[-114,35,103,-63,158,-63,158,-61,158,]),'WHILE':([3,14,23,35,44,53,55,56,58,61,62,64,82,103,117,127,151,158,159,162,174,178,179,184,187,188,192,196,],[-3,-4,-5,-4,65,-44,-43,65,-42,-46,-45,-47,-48,-4,-53,-38,65,65,-60,-51,-62,-64,-57,-49,-75,-58,-55,-59,]),'MULTIPLICATION':([30,32,33,37,38,40,46,47,48,70,74,75,91,104,131,155,156,167,171,182,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,111,-76,-109,-94,-93,-74,111,-66,]),'MINUS':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,104,110,131,155,156,157,167,171,172,182,185,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,113,-76,-90,-109,-94,-93,-89,-74,-92,113,-66,-91,]),'RSQRTBRACKET':([30,31,32,33,37,38,40,43,46,47,48,70,74,75,76,87,91,92,104,110,116,131,155,156,157,167,171,172,182,185,186,],[-22,-17,-23,-21,-106,-106,-106,51,-20,-18,-77,-19,-93,-95,-89,104,-92,-88,-76,-90,-86,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'SEMICOLON':([9,10,15,24,29,30,32,33,37,38,39,40,41,46,47,48,50,51,63,70,74,75,76,77,91,92,93,95,96,104,110,116,119,120,121,131,138,146,147,148,154,155,156,157,163,167,170,171,172,176,177,182,185,186,190,191,197,],[14,-10,-16,-12,-14,-22,-23,-21,-106,-106,-11,-106,-9,-20,-18,-77,-13,-15,82,-19,-93,-95,-89,-54,-92,-88,117,-81,-85,-76,-90,-86,-80,-84,-52,-109,-78,-82,162,-65,-50,-94,-93,-89,178,-74,184,-92,-88,-81,-85,-66,-91,-87,-80,-83,-79,]),'COMMA':([10,15,24,29,30,32,33,37,38,39,40,46,47,48,51,70,74,75,76,85,91,92,101,104,110,116,129,131,153,155,156,157,165,167,171,172,180,182,183,185,186,195,],[-10,-16,-12,42,-22,-23,-21,-106,-106,-11,-106,-20,-18,-77,-15,-19,-93,-95,-89,-36,-92,-88,125,-76,-90,-86,-71,-109,169,-94,-93,-89,-36,-74,-92,-88,125,-66,-71,-91,-87,169,]),'PLUS':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,104,110,131,155,156,157,167,171,172,182,185,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,114,-76,-90,-109,-94,-93,-89,-74,-92,114,-66,-91,]),'$end':([2,16,34,84,100,],[0,-1,-113,-116,-115,]),'DIVISION':([30,32,33,37,38,40,46,47,48,70,74,75,91,104,131,155,156,167,171,182,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,108,-76,-109,-94,-93,-74,108,-66,]),'DIFFERENT':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,139,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'LESSOREQUAL':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,140,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'EQUALEQUALS':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,143,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'CTEINT':([25,28,54,69,71,73,79,80,88,90,99,105,108,109,111,112,113,114,115,122,132,133,135,136,137,139,140,141,142,143,144,145,160,161,169,],[33,33,33,33,-73,-107,33,33,-108,33,33,33,-111,-107,-110,-112,-105,-104,-107,33,33,33,-96,-107,-97,-103,-101,-98,-99,-102,-107,-100,33,33,33,]),'EQUALS':([10,15,24,51,60,81,98,104,],[-10,-16,28,-15,-106,-77,122,-76,]),'ELSE':([159,187,],[175,-75,]),'WRITE':([3,14,23,35,44,53,55,56,58,61,62,64,82,103,117,127,151,158,159,162,174,178,179,184,187,188,192,196,],[-3,-4,-5,-4,59,-44,-43,59,-42,-46,-45,-47,-48,-4,-53,-38,59,59,-60,-51,-62,-64,-57,-49,-75,-58,-55,-59,]),'FUNC':([0,1,3,8,14,23,102,194,],[-2,-4,-3,13,-4,-5,13,-37,]),'ID':([3,4,5,6,7,14,18,19,20,21,22,23,28,35,42,44,53,54,55,56,58,61,62,64,67,69,71,72,73,79,80,82,88,90,99,103,105,108,109,111,112,113,114,115,117,122,127,132,133,135,136,137,139,140,141,142,143,144,145,150,151,158,159,160,161,162,169,174,178,179,184,187,188,192,196,],[-3,10,-7,-8,-6,-4,27,-31,-28,-30,-29,-5,40,-4,10,60,-44,40,-43,60,-42,-46,-45,-47,85,40,-73,89,-107,40,40,-48,-108,40,40,-4,40,-111,-107,-110,-112,-105,-104,-107,-53,40,-38,40,40,-96,-107,-97,-103,-101,-98,-99,-102,-107,-100,165,60,60,-60,40,40,-51,40,-62,-64,-57,-49,-75,-58,-55,-59,]),'IF':([3,14,23,35,44,53,55,56,58,61,62,64,82,103,117,127,151,158,159,162,174,178,179,184,187,188,192,196,],[-3,-4,-5,-4,57,-44,-43,57,-42,-46,-45,-47,-48,-4,-53,-38,57,57,-60,-51,-62,-64,-57,-49,-75,-58,-55,-59,]),'AND':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,95,96,104,110,116,119,120,131,146,155,156,157,167,171,172,176,177,182,185,186,190,191,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-81,-85,-76,-90,-86,135,-84,-109,-82,-94,-93,-89,-74,-92,-88,-81,-85,-66,-91,-87,135,-83,]),'GREATER':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,141,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'INT':([0,1,13,14,35,45,103,125,],[-2,5,21,5,5,5,5,5,]),'DOUBLE':([0,1,13,14,35,45,103,125,],[-2,6,19,6,6,6,6,6,]),'LSQRTBRACKET':([10,15,40,48,60,81,89,106,],[-10,25,-106,69,-106,69,-106,69,]),'BOOL':([0,1,13,14,35,45,103,125,],[-2,7,22,7,7,7,7,7,]),'GREATEROREQUAL':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,96,104,110,116,120,131,155,156,157,167,171,172,182,185,186,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-85,-76,-90,-86,145,-109,-94,-93,-89,-74,-92,-88,-66,-91,-87,]),'CTEBOOL':([25,28,54,69,71,73,79,80,88,90,99,105,108,109,111,112,113,114,115,122,132,133,135,136,137,139,140,141,142,143,144,145,160,161,169,],[32,32,32,32,-73,-107,32,32,-108,32,32,32,-111,-107,-110,-112,-105,-104,-107,32,32,32,-96,-107,-97,-103,-101,-98,-99,-102,-107,-100,32,32,32,]),'RBRACKET':([3,14,23,35,44,53,55,56,58,61,62,64,66,78,82,103,117,127,151,158,159,162,166,173,174,178,179,181,184,187,188,192,196,],[-3,-4,-5,-4,-41,-44,-43,-41,-42,-46,-45,-47,84,-40,-48,-4,-53,-38,-41,-41,-60,-51,-39,187,-62,-64,-57,194,-49,-75,-58,-55,-59,]),'MAIN':([0,1,3,8,11,12,14,23,102,126,194,],[-2,-4,-3,-25,-24,17,-4,-5,-25,-26,-37,]),'OR':([30,32,33,37,38,40,46,47,48,70,74,75,76,91,92,95,96,104,110,116,119,120,131,146,155,156,157,167,171,172,176,177,182,185,186,190,191,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,-89,-92,-88,-81,-85,-76,-90,-86,137,-84,-109,-82,-94,-93,-89,-74,-92,-88,-81,-85,-66,-91,-87,137,-83,]),'MOD':([30,32,33,37,38,40,46,47,48,70,74,75,91,104,131,155,156,167,171,182,],[-22,-23,-21,-106,-106,-106,-20,-18,-77,-19,-93,-95,112,-76,-109,-94,-93,-74,112,-66,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'more_args':([101,180,],[124,193,]),'else_posible':([159,],[174,]),'arr':([15,],[24,]),'gen_read_quad':([154,],[170,]),'check_type':([118,149,],[134,164,]),'var_type':([1,14,35,45,103,125,],[4,4,4,67,4,150,]),'main_block':([26,],[34,]),'to_pilaOp':([37,38,40,60,89,],[46,47,48,81,106,]),'ao':([119,190,],[136,136,]),'var_cte':([28,54,69,79,80,90,99,105,122,132,133,160,161,169,],[39,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'vars_aux':([4,42,],[9,50,]),'arr_par':([48,81,106,],[70,98,130,]),'conc':([79,90,99,122,160,],[95,95,95,95,176,]),'return_stmt':([44,56,151,158,],[53,53,53,53,]),'conc_aux':([120,],[146,]),'is_valid_func':([40,60,],[49,49,]),'more_func':([8,102,],[12,126,]),'gen_era':([71,],[88,]),'term_aux':([91,171,],[110,185,]),'cycle_start':([65,],[83,]),'const':([25,28,54,69,79,80,90,99,105,122,132,133,160,161,169,],[31,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'vars':([1,14,35,103,],[3,3,3,3,]),'gen_return_quad':([77,],[93,]),'cycle_end':([179,],[192,]),'gen_end_quad':([84,],[100,]),'gen_term_quad':([76,157,],[92,172,]),'more_vars':([1,14,35,103,],[8,23,44,127,]),'write':([44,56,151,158,],[55,55,55,55,]),'gen_goto_main':([0,],[1,]),'program':([0,],[2,]),'params':([105,],[128,]),'arguments':([45,],[68,]),'statement':([44,56,151,158,],[56,56,56,56,]),'factor':([54,69,79,80,90,99,105,122,132,133,160,161,169,],[74,74,74,74,74,74,74,74,156,74,74,74,74,]),'main_to_proc_dir':([17,],[26,]),'actual_quad_no':([127,],[151,]),'register_space':([31,],[43,]),'var_assign':([24,],[29,]),'to_proc_dir':([27,],[36,]),'add_to_pilaOptr':([73,109,115,136,144,],[90,132,133,160,161,]),'gen_conc_quad':([95,176,],[119,190,]),'dm':([91,171,],[109,109,]),'to_args':([85,165,],[101,180,]),'func_type':([13,],[18,]),'comp':([120,],[144,]),'gen_comp_quad':([96,177,],[120,191,]),'gen_factor_quad':([74,156,],[91,171,]),'check_args':([129,183,],[153,195,]),'fill_end_condition':([174,],[188,]),'gen_write_quad':([121,],[147,]),'gen_goto':([175,],[189,]),'func':([8,102,],[11,11,]),'more_params':([153,195,],[168,198,]),'push_false_bottom':([88,],[105,]),'condition':([44,56,151,158,],[61,61,61,61,]),'cycle':([44,56,151,158,],[62,62,62,62,]),'func_call':([28,44,54,56,69,79,80,90,99,105,122,132,133,151,158,160,161,169,],[37,63,37,63,37,37,37,37,37,37,37,37,37,63,63,37,37,37,]),'term':([54,69,79,80,90,99,105,122,133,160,161,169,],[76,76,76,76,76,76,76,76,157,76,76,76,]),'main':([12,],[16,]),'assignation':([44,56,151,158,],[64,64,64,64,]),'func_block':([86,],[102,]),'read':([44,56,151,158,],[58,58,58,58,]),'pop_false_bottom':([128,131,],[152,155,]),'gen_endproc_quad':([166,],[181,]),'gen_go_sub':([167,],[182,]),'more_statement':([44,56,151,158,],[66,78,166,173,]),'to_var_table':([10,],[15,]),'gen_assignation_quad':([148,],[163,]),'more_vars_aux':([29,],[41,]),'expression_aux':([119,190,],[138,197,]),'pl':([92,172,],[115,115,]),'exp':([54,69,79,80,90,99,105,122,160,161,169,],[77,87,96,97,96,96,129,96,96,177,183,]),'expression':([79,90,99,122,],[94,107,123,148,]),'exp_aux':([92,172,],[116,186,]),'block':([134,164,189,],[159,179,196,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> gen_goto_main more_vars more_func main','program',4,'p_program','ObsidianParser.py',11),
  ('gen_goto_main -> <empty>','gen_goto_main',0,'p_gen_goto_main','ObsidianParser.py',15),
  ('more_vars -> vars','more_vars',1,'p_more_vars','ObsidianParser.py',20),
  ('more_vars -> <empty>','more_vars',0,'p_more_vars','ObsidianParser.py',21),
  ('vars -> var_type vars_aux SEMICOLON more_vars','vars',4,'p_vars','ObsidianParser.py',24),
  ('var_type -> BOOL','var_type',1,'p_var_type','ObsidianParser.py',27),
  ('var_type -> INT','var_type',1,'p_var_type','ObsidianParser.py',28),
  ('var_type -> DOUBLE','var_type',1,'p_var_type','ObsidianParser.py',29),
  ('vars_aux -> ID to_var_table arr var_assign more_vars_aux','vars_aux',5,'p_vars_aux','ObsidianParser.py',34),
  ('to_var_table -> <empty>','to_var_table',0,'p_to_var_table','ObsidianParser.py',38),
  ('var_assign -> EQUALS var_cte','var_assign',2,'p_var_assign','ObsidianParser.py',42),
  ('var_assign -> <empty>','var_assign',0,'p_var_assign','ObsidianParser.py',43),
  ('more_vars_aux -> COMMA vars_aux','more_vars_aux',2,'p_more_vars_aux','ObsidianParser.py',47),
  ('more_vars_aux -> <empty>','more_vars_aux',0,'p_more_vars_aux','ObsidianParser.py',48),
  ('arr -> LSQRTBRACKET const register_space RSQRTBRACKET','arr',4,'p_arr','ObsidianParser.py',51),
  ('arr -> <empty>','arr',0,'p_arr','ObsidianParser.py',52),
  ('register_space -> <empty>','register_space',0,'p_register_space','ObsidianParser.py',57),
  ('var_cte -> const to_pilaOp','var_cte',2,'p_var_cte','ObsidianParser.py',61),
  ('var_cte -> ID to_pilaOp arr_par','var_cte',3,'p_var_cte','ObsidianParser.py',62),
  ('var_cte -> func_call to_pilaOp','var_cte',2,'p_var_cte','ObsidianParser.py',63),
  ('const -> CTEINT','const',1,'p_const','ObsidianParser.py',67),
  ('const -> CTEDOUBLE','const',1,'p_const','ObsidianParser.py',68),
  ('const -> CTEBOOL','const',1,'p_const','ObsidianParser.py',69),
  ('more_func -> func','more_func',1,'p_more_func','ObsidianParser.py',73),
  ('more_func -> <empty>','more_func',0,'p_more_func','ObsidianParser.py',74),
  ('func -> FUNC func_type ID to_proc_dir LPAR arguments RPAR func_block more_func','func',9,'p_func','ObsidianParser.py',77),
  ('to_proc_dir -> <empty>','to_proc_dir',0,'p_to_proc_dir','ObsidianParser.py',80),
  ('func_type -> VOID','func_type',1,'p_func_type','ObsidianParser.py',84),
  ('func_type -> BOOL','func_type',1,'p_func_type','ObsidianParser.py',85),
  ('func_type -> INT','func_type',1,'p_func_type','ObsidianParser.py',86),
  ('func_type -> DOUBLE','func_type',1,'p_func_type','ObsidianParser.py',87),
  ('arguments -> var_type ID to_args more_args','arguments',4,'p_arguments','ObsidianParser.py',91),
  ('arguments -> <empty>','arguments',0,'p_arguments','ObsidianParser.py',92),
  ('more_args -> COMMA var_type ID to_args more_args','more_args',5,'p_more_args','ObsidianParser.py',96),
  ('more_args -> <empty>','more_args',0,'p_more_args','ObsidianParser.py',97),
  ('to_args -> <empty>','to_args',0,'p_to_args','ObsidianParser.py',100),
  ('func_block -> LBRACKET more_vars actual_quad_no more_statement gen_endproc_quad RBRACKET','func_block',6,'p_func_block','ObsidianParser.py',107),
  ('actual_quad_no -> <empty>','actual_quad_no',0,'p_actual_quad_no','ObsidianParser.py',110),
  ('gen_endproc_quad -> <empty>','gen_endproc_quad',0,'p_gen_endproc_quad','ObsidianParser.py',115),
  ('more_statement -> statement more_statement','more_statement',2,'p_more_statement','ObsidianParser.py',120),
  ('more_statement -> <empty>','more_statement',0,'p_more_statement','ObsidianParser.py',121),
  ('statement -> read','statement',1,'p_statement','ObsidianParser.py',124),
  ('statement -> write','statement',1,'p_statement','ObsidianParser.py',125),
  ('statement -> return_stmt','statement',1,'p_statement','ObsidianParser.py',126),
  ('statement -> cycle','statement',1,'p_statement','ObsidianParser.py',127),
  ('statement -> condition','statement',1,'p_statement','ObsidianParser.py',128),
  ('statement -> assignation','statement',1,'p_statement','ObsidianParser.py',129),
  ('statement -> func_call SEMICOLON','statement',2,'p_statement','ObsidianParser.py',130),
  ('read -> READ LPAR ID to_pilaOp arr_par RPAR gen_read_quad SEMICOLON','read',8,'p_read','ObsidianParser.py',133),
  ('gen_read_quad -> <empty>','gen_read_quad',0,'p_gen_read_quad','ObsidianParser.py',136),
  ('write -> WRITE LPAR exp RPAR gen_write_quad SEMICOLON','write',6,'p_write','ObsidianParser.py',141),
  ('gen_write_quad -> <empty>','gen_write_quad',0,'p_gen_write_quad','ObsidianParser.py',144),
  ('return_stmt -> RETURN exp gen_return_quad SEMICOLON','return_stmt',4,'p_return_stmt','ObsidianParser.py',149),
  ('gen_return_quad -> <empty>','gen_return_quad',0,'p_gen_return_quad','ObsidianParser.py',152),
  ('cycle -> WHILE cycle_start LPAR expression RPAR check_type block cycle_end','cycle',8,'p_cycle','ObsidianParser.py',158),
  ('cycle_start -> <empty>','cycle_start',0,'p_cycle_start','ObsidianParser.py',161),
  ('cycle_end -> <empty>','cycle_end',0,'p_cycle_end','ObsidianParser.py',165),
  ('condition -> IF LPAR expression RPAR check_type block else_posible fill_end_condition','condition',8,'p_condition','ObsidianParser.py',169),
  ('else_posible -> ELSE gen_goto block','else_posible',3,'p_else_posible','ObsidianParser.py',172),
  ('else_posible -> <empty>','else_posible',0,'p_else_posible','ObsidianParser.py',173),
  ('gen_goto -> <empty>','gen_goto',0,'p_gen_goto','ObsidianParser.py',176),
  ('fill_end_condition -> <empty>','fill_end_condition',0,'p_fill_end_condition','ObsidianParser.py',180),
  ('check_type -> <empty>','check_type',0,'p_check_type','ObsidianParser.py',184),
  ('assignation -> ID to_pilaOp arr_par EQUALS expression gen_assignation_quad SEMICOLON','assignation',7,'p_assignation','ObsidianParser.py',188),
  ('gen_assignation_quad -> <empty>','gen_assignation_quad',0,'p_gen_assignation_quad','ObsidianParser.py',191),
  ('func_call -> ID is_valid_func LPAR gen_era push_false_bottom params pop_false_bottom RPAR gen_go_sub','func_call',9,'p_func_call','ObsidianParser.py',196),
  ('params -> exp check_args more_params','params',3,'p_params','ObsidianParser.py',200),
  ('params -> <empty>','params',0,'p_params','ObsidianParser.py',201),
  ('more_params -> COMMA exp check_args more_params','more_params',4,'p_more_params','ObsidianParser.py',204),
  ('more_params -> <empty>','more_params',0,'p_more_params','ObsidianParser.py',205),
  ('check_args -> <empty>','check_args',0,'p_check_args','ObsidianParser.py',208),
  ('is_valid_func -> <empty>','is_valid_func',0,'p_is_valid_func','ObsidianParser.py',212),
  ('gen_era -> <empty>','gen_era',0,'p_gen_era','ObsidianParser.py',216),
  ('gen_go_sub -> <empty>','gen_go_sub',0,'p_gen_go_sub','ObsidianParser.py',220),
  ('block -> LBRACKET more_statement RBRACKET','block',3,'p_block','ObsidianParser.py',224),
  ('arr_par -> LSQRTBRACKET exp RSQRTBRACKET','arr_par',3,'p_arr_par','ObsidianParser.py',227),
  ('arr_par -> <empty>','arr_par',0,'p_arr_par','ObsidianParser.py',228),
  ('expression -> conc gen_conc_quad expression_aux','expression',3,'p_expression','ObsidianParser.py',233),
  ('expression_aux -> ao add_to_pilaOptr conc gen_conc_quad expression_aux','expression_aux',5,'p_expression_aux','ObsidianParser.py',237),
  ('expression_aux -> <empty>','expression_aux',0,'p_expression_aux','ObsidianParser.py',238),
  ('gen_conc_quad -> <empty>','gen_conc_quad',0,'p_gen_conc_quad','ObsidianParser.py',240),
  ('conc -> exp gen_comp_quad conc_aux','conc',3,'p_conc','ObsidianParser.py',245),
  ('conc_aux -> comp add_to_pilaOptr exp gen_comp_quad','conc_aux',4,'p_conc_aux','ObsidianParser.py',249),
  ('conc_aux -> <empty>','conc_aux',0,'p_conc_aux','ObsidianParser.py',250),
  ('gen_comp_quad -> <empty>','gen_comp_quad',0,'p_gen_comp_quad','ObsidianParser.py',253),
  ('exp -> term gen_term_quad exp_aux','exp',3,'p_exp','ObsidianParser.py',258),
  ('exp_aux -> pl add_to_pilaOptr term gen_term_quad exp_aux','exp_aux',5,'p_exp_aux','ObsidianParser.py',262),
  ('exp_aux -> <empty>','exp_aux',0,'p_exp_aux','ObsidianParser.py',263),
  ('gen_term_quad -> <empty>','gen_term_quad',0,'p_gen_term_quad','ObsidianParser.py',266),
  ('term -> factor gen_factor_quad term_aux','term',3,'p_term','ObsidianParser.py',271),
  ('term_aux -> dm add_to_pilaOptr factor gen_factor_quad term_aux','term_aux',5,'p_term_aux','ObsidianParser.py',275),
  ('term_aux -> <empty>','term_aux',0,'p_term_aux','ObsidianParser.py',276),
  ('gen_factor_quad -> <empty>','gen_factor_quad',0,'p_gen_factor_quad','ObsidianParser.py',279),
  ('factor -> LPAR add_to_pilaOptr expression RPAR pop_false_bottom','factor',5,'p_factor','ObsidianParser.py',284),
  ('factor -> var_cte','factor',1,'p_factor','ObsidianParser.py',285),
  ('ao -> AND','ao',1,'p_ao','ObsidianParser.py',292),
  ('ao -> OR','ao',1,'p_ao','ObsidianParser.py',293),
  ('comp -> GREATER','comp',1,'p_comp','ObsidianParser.py',297),
  ('comp -> LESS','comp',1,'p_comp','ObsidianParser.py',298),
  ('comp -> GREATEROREQUAL','comp',1,'p_comp','ObsidianParser.py',299),
  ('comp -> LESSOREQUAL','comp',1,'p_comp','ObsidianParser.py',300),
  ('comp -> EQUALEQUALS','comp',1,'p_comp','ObsidianParser.py',301),
  ('comp -> DIFFERENT','comp',1,'p_comp','ObsidianParser.py',302),
  ('pl -> PLUS','pl',1,'p_pl','ObsidianParser.py',306),
  ('pl -> MINUS','pl',1,'p_pl','ObsidianParser.py',307),
  ('to_pilaOp -> <empty>','to_pilaOp',0,'p_to_pilaOp','ObsidianParser.py',311),
  ('add_to_pilaOptr -> <empty>','add_to_pilaOptr',0,'p_add_to_pilaOptr','ObsidianParser.py',324),
  ('push_false_bottom -> <empty>','push_false_bottom',0,'p_push_false_bottom','ObsidianParser.py',328),
  ('pop_false_bottom -> <empty>','pop_false_bottom',0,'p_pop_false_bottom','ObsidianParser.py',332),
  ('dm -> MULTIPLICATION','dm',1,'p_dm','ObsidianParser.py',338),
  ('dm -> DIVISION','dm',1,'p_dm','ObsidianParser.py',339),
  ('dm -> MOD','dm',1,'p_dm','ObsidianParser.py',340),
  ('main -> MAIN main_to_proc_dir main_block','main',3,'p_main','ObsidianParser.py',344),
  ('main_to_proc_dir -> <empty>','main_to_proc_dir',0,'p_main_to_proc_dir','ObsidianParser.py',347),
  ('main_block -> LBRACKET more_vars more_statement RBRACKET gen_end_quad','main_block',5,'p_main_block','ObsidianParser.py',354),
  ('gen_end_quad -> <empty>','gen_end_quad',0,'p_gen_end_quad','ObsidianParser.py',356),
]
