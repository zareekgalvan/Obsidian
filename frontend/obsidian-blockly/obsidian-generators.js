// MAIN
Blockly.JavaScript['main'] = function(block) {
  var statements = Blockly.JavaScript.statementToCode(block, 'main_method');
  var code = 'main {\n' + statements + '\n}\n';
  return code;
};

// FUNCTIONS
Blockly.JavaScript['function'] = function(block) {
  var dropdownType = block.getFieldValue('type');
  var textId = block.getFieldValue('id');
  var statements = Blockly.JavaScript.statementToCode(block, 'statement');
  var valueParams = Blockly.JavaScript.valueToCode(block, 'params', Blockly.JavaScript.ORDER_ATOMIC);

  valueParams = valueParams.replace(/[()]/g,'');
  var code = 'func '+ dropdownType + ' ' + textId + ' (' + valueParams +')' + '{\n' + statements + '\n}\n';
  return code;
};

// PARAMS IN FUNCTION
Blockly.JavaScript['parameters'] = function(block) {
  var nameParam = block.getFieldValue('name_param');
  var dropdownType = block.getFieldValue('type');

  var otherParams = Blockly.JavaScript.valueToCode(block, 'parameters_list', Blockly.JavaScript.ORDER_ATOMIC);

  var comma = block.getFieldValue('comma');

  otherParams = otherParams.replace(/[(]/g, " ");
  otherParams = otherParams.replace(/[)]/g, "");

  var code = dropdownType + ' ' + nameParam + comma + otherParams;
  return [code, Blockly.JavaScript.ORDER_NONE];
};

// RETURN IN FUNCTION
Blockly.JavaScript['return'] = function(block) {
  var val = Blockly.JavaScript.valueToCode(block, 'RETURN', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'return ' + val + ';\n';
  code = code.replace(/[()]/g,'');
  code = code.replace(/[¿]/g,'(');
  code = code.replace(/[?]/g,')');
  return code;
};

// CONDITION
Blockly.JavaScript['condition_value'] = function(block) {
  var val = block.getFieldValue('value_param');
  return val;
};


// VARIABLES
Blockly.JavaScript['variable_definition'] = function(block) {
  var dropdownType = block.getFieldValue('TYPE');
  var id = block.getFieldValue('ID');
  var textVal = block.getFieldValue('VALUE');

  var extraVars = Blockly.JavaScript.valueToCode(block, 'extra_vars', Blockly.JavaScript.ORDER_ATOMIC);

  extraVars = extraVars.replace(/[()]/g,'');
  extraVars = extraVars.replace(/[¿]/g,'(');
  extraVars = extraVars.replace(/[?]/g,')');

  console.log("var definition block");

  console.log(extraVars)

  if (textVal) {
    var code = dropdownType + ' ' + id + '=' + textVal + extraVars + ';\n';
  } else {
    var code = dropdownType + ' ' + id + extraVars + ';\n';
  }

  
  console.log("returning var definition block");
  return code;
};

Blockly.JavaScript['extra_variable'] = function(block) {
  var id = block.getFieldValue('ID');
  var textVal = block.getFieldValue('VALUE');

  var extraVars = Blockly.JavaScript.valueToCode(block, 'extra_vars', Blockly.JavaScript.ORDER_ATOMIC);

  console.log("extra var block");

  if (textVal) {
    var code = ', ' + id + '=' + textVal + extraVars;
  } else {
    var code = ', ' + id + extraVars;
  }
  
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//IO
Blockly.JavaScript['read'] = function(block) {
  var id = block.getFieldValue('ID');
  var code = 'read (' + id + ');\n';
  return code;
};

Blockly.JavaScript['write'] = function(block) {
  var id = block.getFieldValue('ID');
  var code = 'write (' + id + ');\n';
  return code;
};


