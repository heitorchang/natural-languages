; var gul = document.getElementById("g");

// EDIT appMobile.js ALSO

var f = document.getElementById("f");
var q = document.getElementById("q");
var w = document.getElementById("w");

function makeClickable(s) {
  var out = document.createElement("span");
  var words = s.split(" ");
  words.forEach(function(w) {
    var wspan = document.createElement("span");
    w = w.replace("''", "'");
    wspan.appendChild(document.createTextNode(w + " "));
    wspan.onclick = function() {
      q.value = w;
      search();
    };
    wspan.onmouseup = function() {
      q.focus();
    };
    out.appendChild(wspan);
  });
  return out;
}

function search() { 
  var qval = q.value;

  if (qval.trim() == "") {
    return;
  }

  // remove punctuation
  qval = qval.replace(/[,.;'"]/g, "");
  qval = qval.toLowerCase();
  
  w.innerText = qval;

  qval = qval.replace(/\s/g, "_");
  
  q.value = "";
  q.focus();
  
  gul.innerHTML = "";

  var sids = synset[qval];
  if (sids) {
    sids.forEach(function(sid) {
      var gs = gloss[sid];
      gs.forEach(function(g) {
        var gli = document.createElement("li");
        gli.appendChild(makeClickable(g));
        gul.appendChild(gli);
      });
    });
  }
}

document.getElementById("s").onclick = function() {
  search();
};

document.getElementById("q").addEventListener("keyup", function (event) {
  event.preventDefault();
  if (event.keyCode === 13) {
    search();
  }
});
