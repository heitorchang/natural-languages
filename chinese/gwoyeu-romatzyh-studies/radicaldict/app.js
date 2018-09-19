

function displayChar(uni) {
  if (uni.substr(0, 2) === "U+") {
    uni = uni.substr(2);
  }
  return String.fromCharCode(parseInt(uni, 16));
}

// build radical index

var radicalsHTML = "";

for (var i = 1; i <= 214; i++) {
  radicalsHTML += "<a href='radical" + i + ".html'>";
  radicalsHTML += displayChar(radicals[i]);
  radicalsHTML += "</a> ";
}

document.getElementById("radicals").innerHTML = radicalsHTML;
