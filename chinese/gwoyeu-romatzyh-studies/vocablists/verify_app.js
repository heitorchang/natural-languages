function loadFile(files) {
  var file = files[0];
  var reader = new FileReader();

  // callback
  reader.onload = function(e) {
    var textFromFile = e.target.result;
    document.getElementById("data").innerHTML = "";
    buildTable(textFromFile.trim());    
  };
  reader.readAsText(file, "UTF-8");

}

function buildTable(raw) {
  var words = raw.split('\n');
  var tableElem = document.getElementById("data");
  words.forEach(function (word) {
    var parts = word.split(";");
    tableElem.innerHTML += '<tr><td class="lg">' +
      parts[0] + "</td></tr><tr><td>" +
      parts[1] + "</td></tr><tr><td>" +
      parts[2] + "</td></tr><tr><td><hr></td></tr>";
  });
}

