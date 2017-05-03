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

workspace.addChangeListener(printCode);

function showCode() {
  // Generate JavaScript code and display it.
  Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
  var code = Blockly.JavaScript.workspaceToCode(workspace);
  alert(code);
}

function printCode() {
  Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
  var code = Blockly.JavaScript.workspaceToCode(workspace);

  $("#obsidian-code").text(code).removeClass("prettyprinted");

  PR.prettyPrint();

  console.log(code);
}


// $('input[type=button]').click( function() {
//     $("#jsExample").text("    var user = 'private'; //Do NOT store your API Key on a script.")
//         .parent().removeClass("prettyprinted");
    
//    prettyPrint();
// });

// var primaryWorkspace = Blockly.inject('primaryDiv',
//         {media: '../../media/',
//          toolbox: document.getElementById('toolbox')});
//     // Inject secondary workspace.
//     var seconaryWorkspace = Blockly.inject('secondaryDiv',
//         {media: '../../media/',
//          readOnly: true});
//     // Listen to events on primary workspace.
//     primaryWorkspace.addChangeListener(mirrorEvent);

//     function mirrorEvent(primaryEvent) {
//       if (primaryEvent.type == Blockly.Events.UI) {
//         return;  // Don't mirror UI events.
//       }
//       // Convert event to JSON.  This could then be transmitted across the net.
//       var json = primaryEvent.toJson();
//       console.log(json);
//       // Convert JSON back into an event, then execute it.
//       var secondaryEvent = Blockly.Events.fromJson(json, seconaryWorkspace);
//       secondaryEvent.run(true);