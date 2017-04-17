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