var blocklyArea = document.getElementById('blocklyArea');
var blocklyDiv = document.getElementById('blocklyDiv');
var workspace = Blockly.inject(blocklyDiv, {media: '../dependencies/blockly/media/', toolbox: document.getElementById('toolbox')});

var onresize = function(e) {
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
}

function downloadFile() {
  Blockly.JavaScript.INFINITE_LOOP_TRAP = null;
  var code = Blockly.JavaScript.workspaceToCode(workspace);

  //Generate a file name
    var fileName = "obsidian_code";

    //Initialize file format you want csv or xls
    var uri = 'data:text/csv;charset=utf-8,' + escape(code);

    //this trick will generate a temp <a /> tag
    var link = document.createElement("a");
    link.href = uri;

    //set the visibility hidden so it will not effect on your web-layout
    link.style = "visibility:hidden";
    link.download = fileName + ".txt";

    //this part will append the anchor tag and remove it after automatic click
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function changeCode() {
  Blockly.mainWorkspace.clear();
  Blockly.Xml.domToWorkspace(document.getElementById('fuckthis'),workspace);
}

function reset() {
  Blockly.mainWorkspace.clear();
}

function downloadXML() {
  var xml = Blockly.Xml.workspaceToDom(workspace);
  console.log(xml);
}

function runCode() {
  var code = Blockly.JavaScript.workspaceToCode(workspace);

  $.ajax({
    url: "http://localhost:8000/archivos",
    type: "POST",
    data: {code: code },
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    success: function(response){
      console.log(response);
    }
  });
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