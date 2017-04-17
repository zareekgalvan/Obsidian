// MAIN
Blockly.Blocks['main'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Main");
    this.appendStatementInput("main_method")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setColour(300);
    this.setTooltip('');
  }
};

// FUNCTIONS
Blockly.Blocks['function'] = {
  init: function() {
    this.appendValueInput("params")
        .setCheck(null)
        .appendField("func")
        .appendField(new Blockly.FieldDropdown([ ["int", "int"], ["double", "double"], ["string", "string"], ["void", "void"],["bool", "bool"] ]), "type")
        .appendField(new Blockly.FieldTextInput("id"), "id");
    this.appendStatementInput("statement")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
  }
};

// PARAMETERS IN FUNCTION
Blockly.Blocks['parameters'] = {
  init: function() {
    this.appendValueInput('parameters_list')
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([ ["int", "int"], ["double", "double"], ["string", "string"], ["bool", "bool"] ]), "type")
        .appendField(new Blockly.FieldTextInput("'name'"), "name_param")
        .appendField(new Blockly.FieldDropdown([ [",", ","], ["no comma", ""] ]), "comma");
    this.setOutput(true, null);
    this.setColour(210);
    this.setTooltip('');
  }
};

// RETURN IN FUNCTION
Blockly.Blocks['return'] = {
  init: function() {
    this.appendValueInput("RETURN")
        .setCheck(null)
        .appendField("Return");
    this.setPreviousStatement(true, null);
    this.setColour(255);
    this.setTooltip('');
  }
};

// VARIABLES

