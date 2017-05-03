// var workspace = Blockly.inject('blocklyDiv',
//         {media: '../dependencies/blockly/media/',
//          toolbox: document.getElementById('toolbox')});

    // Blockly.Xml.domToWorkspace(document.getElementById('startBlocks'),
    //                            workspace);

var blocklyArea = document.getElementById('blocklyArea');

var blocklyDiv = document.getElementById('blocklyDiv');

var workspace = Blockly.inject(blocklyDiv, {media: '../dependencies/blockly/media/', toolbox: document.getElementById('toolbox')});

var onresize = function(e) {
  console.log("RESISEZ");
  // Compute the absolute coordinates and dimensions of blocklyArea.
  var element = blocklyArea;
  var x = 0;
  var y = 0;
  do {
    x += element.offsetLeft;
    y += element.offsetTop;
    element = element.offsetParent;
  } while (element);
  // Position blocklyDiv over blocklyArea.
  blocklyDiv.style.left = x + 'px';
  blocklyDiv.style.top = y + 'px';
  blocklyDiv.style.width = blocklyArea.offsetWidth + 'px';
  blocklyDiv.style.height = blocklyArea.offsetHeight + 'px';
};

window.addEventListener('resize', onresize, false);
onresize();
Blockly.svgResize(workspace);

function showCode() {
  // Generate JavaScript code and display it.
  Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
  var code = Blockly.JavaScript.workspaceToCode(workspace);
  alert(code);
}

function showCode() {

}