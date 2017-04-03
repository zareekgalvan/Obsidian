Blockly.JavaScript['main'] = function(block) {
  var statements_main = Blockly.JavaScript.statementToCode(block, 'main_method');

  var code = 'main {\n' + statements_main + '\n}\n';
  return code;
};