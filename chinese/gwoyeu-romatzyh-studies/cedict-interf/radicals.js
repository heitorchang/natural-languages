var fc = String.fromCodePoint;

function a(c) {
  var startCharInput = document.getElementById("startChar");
  startCharInput.value += c;

  var radicalsSpan = document.getElementById("radicals");
  radicalsSpan.style.display = "none";

  var strokesSpan = document.getElementById("st");
  strokesSpan.style.display = "none";

  // scroll to top
  location.hash = "#top";
}

function hideRad() {
  var radicalsSpan = document.getElementById("radicals");
  radicalsSpan.style.display = "none";

  var strokesSpan = document.getElementById("st");
  strokesSpan.style.display = "none";
}

function showRadicals() {
  var radicalsSpan = document.getElementById("radicals");
  radicalsSpan.style.display = "inline";

  var strokesSpan = document.getElementById("st");
  strokesSpan.style.display = "none";
}

function showStrokes(id) {
  var radicalsSpan = document.getElementById("radicals");
  radicalsSpan.style.display = "none";

  var strokesSpan = document.getElementById("st");
  strokesSpan.style.display = "inline";

  strokesSpan.innerHTML = strokeContents[id];
}
