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
        .appendField(new Blockly.FieldDropdown([ ["int", "int"], ["double", "double"], ["void", "void"],["bool", "bool"] ]), "type")
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
        .appendField(new Blockly.FieldDropdown([ ["int", "int"], ["double", "double"], ["bool", "bool"] ]), "type")
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

// CONDITIONS
Blockly.Blocks['condition_value'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("value"), "value_param")
    this.setOutput(true, null);
    this.setColour(210);
    this.setTooltip('');
  }
};

// VARIABLES
Blockly.Blocks['variable_definition'] = {
  init: function() {
    this.appendValueInput('extra_vars')
        .appendField(new Blockly.FieldDropdown([["bool", "bool"], ["int", "int"], ["double", "double"]]), "TYPE")
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('');
  }
};

Blockly.Blocks['extra_variable'] = {
  init: function() {
    this.appendValueInput('extra_vars')
        .appendField(new Blockly.FieldTextInput("id"), "ID")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
  }
};



