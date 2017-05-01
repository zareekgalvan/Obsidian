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
        .appendField(new Blockly.FieldDropdown([ ["int", "int"], ["double", "double"], ["void", "void"] ]), "type")
        .appendField(new Blockly.FieldTextInput("id"), "id");
    this.appendStatementInput("statement")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip('Function that takes zero or several parameters.');
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
        .appendField(new Blockly.FieldTextInput("Value or condition"), "value_param")
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
        .appendField(new Blockly.FieldTextInput("id"), "id")
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
        .appendField(new Blockly.FieldTextInput("id"), "id")
        .appendField("=")
        .appendField(new Blockly.FieldTextInput("value"), "VALUE");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
  }
};

Blockly.Blocks['variable_assign'] = {
  init: function() {
    this.appendValueInput("value")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "id")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
  }
};


//IO
Blockly.Blocks['read'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("read")
        .appendField(new Blockly.FieldTextInput("id"), "id")
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(250);
    this.setTooltip('');
  }
};

Blockly.Blocks['write'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("write")
        .appendField(new Blockly.FieldTextInput("id"), "id")
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(250);
    this.setTooltip('');
  }
};

// ARRAYS
Blockly.Blocks['array_def'] = {
  init: function() {
    this.appendValueInput("name")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["double", "double"], ["bool", "bool"]]), "type")
        .appendField(new Blockly.FieldTextInput("id"), "id")
        .appendField("[")
        .appendField(new Blockly.FieldNumber(0, 1), "size")
        .appendField("]")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
  }
};

Blockly.Blocks['array_assign'] = {
  init: function() {
    this.appendValueInput("name")
        .setCheck(null)
        .appendField(new Blockly.FieldTextInput("id"), "id")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("value"), "pos")
        .appendField("]")
        .appendField("=");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(225);
  }
};

Blockly.Blocks['array_access'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("id"), "id")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("value"), "pos")
        .appendField("]");
    this.setOutput(true, null);
    this.setColour(225);
  }
};