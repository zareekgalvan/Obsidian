var workspace = Blockly.inject('blocklyDiv',
        {media: '../dependencies/blockly/media/',
         toolbox: document.getElementById('toolbox')});

    Blockly.Xml.domToWorkspace(document.getElementById('startBlocks'),
                               workspace);

    function showCode() {
      // Generate JavaScript code and display it.
      Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
      var code = Blockly.JavaScript.workspaceToCode(workspace);
      alert(code);
    }