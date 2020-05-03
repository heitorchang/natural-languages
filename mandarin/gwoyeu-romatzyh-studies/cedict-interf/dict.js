
/*
function findLine(lineNumber) {
  return words[lineNumber];
}

document.getElementById("getLineNumber").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findLine(parseInt(
    document.getElementById("lineNumber").value, 10));
});
*/

/* SAMPLE ENTRY
"一團糟 一团糟 [yi1 tuan2 zao1] /chaos/bungle/complete mess/"
*/

// build fuzzy GR map
var fuzzyGRDict = {};
var exactGRDict = {};

for (var wordIndex = 0, wordlistLen = words.length; wordIndex < wordlistLen; wordIndex++) {
  var pyPhrase = words[wordIndex].match(/\[.*?\]/)[0];
  var exactPyPhrase = pyPhrase.replace(/[\[\]]/g, "");
  pyPhrase = pyPhrase.replace(/[0-9\[\]]/g, "");

  pySyllables = pyPhrase.split(" ");
  exactPySyllables = exactPyPhrase.split(" ");
  
  var grPhrase = "";
  var exactGRPhrase = "";
  
  for (var j = 0, pyPhraseLen = pySyllables.length; j < pyPhraseLen; j++) {
    grPhrase += py2gr(pySyllables[j] + "1") + " ";
    exactGRPhrase += py2gr(exactPySyllables[j]) + " ";
  }
  grPhrase = grPhrase.trim();
  exactGRPhrase = exactGRPhrase.trim();
  
  if (!fuzzyGRDict[grPhrase]) {
    fuzzyGRDict[grPhrase] = [wordIndex];
  } else {
    fuzzyGRDict[grPhrase].push(wordIndex);
  }

  if (!exactGRDict[exactGRPhrase]) {
    exactGRDict[exactGRPhrase] = [wordIndex];
  } else {
    exactGRDict[exactGRPhrase].push(wordIndex);
  }
}

function pyPhrase2gr(pyPhrase) {
  var grPhrase = "";
  var pySyllables = pyPhrase.split(" ");
  for (var i = 0, len = pySyllables.length; i < len; i++) {
    grPhrase += py2gr(pySyllables[i]) + " ";
  }
  return grPhrase;
}

function htmlifyWord(word) {
  var parts = word.split(" ");
  var trad = parts[0];
  var simpl = parts[1];
  var py = word.match(/\[.*?\]/)[0];
  py = py.slice(1, py.length - 1);

  var py_english = parts.slice(2).join(" ");
  var py_english_pyend = py_english.indexOf("]");
  py_english = py_english.substr(py_english_pyend+1);
  
  result = "<a href='#s' onclick='a(\"" + trad + "\")'>" + 
    '<span class="hint--top" data-hint="' + trad + '">' +
    trad + "</span></a> " +
    '<span class="hint--top simsun" data-hint="' + simpl + '">' +
    simpl + "</span> " +
    pyPhrase2gr(py) +
    // parts.slice(2).join(" ") + "<br>";  // print Pinyin
    py_english + "<br>";
  return result;
}

function findDefinition(definition) {
  var resultBlock = "";
  var searchTerm = definition.toLowerCase().trim();
  for (var i = 0, len = words.length; i < len; i++) {
    if (words[i].toLowerCase().indexOf(searchTerm) !== -1) {
      resultBlock += htmlifyWord(words[i]);
    }
  }
  return resultBlock;
}

function findStartChar(c) {
  c = c.trim();
  var resultBlock = "";
  var clen = c.length;
  for (var i = 0, len = words.length; i < len; i++) {
    if (words[i].substr(0, clen) === c) {
      resultBlock += htmlifyWord(words[i]);
    }
  }
  return resultBlock;
}

function findByFuzzyGR(fuzzyGR) {
  var grSyllables = fuzzyGR.split(" ");
  var grToneless = "";
  // convert to pinyin, strip tones, then add tone 1, and reconvert to GR
  for (var i = 0, grSyllablesLen = grSyllables.length; i < grSyllablesLen; i++) {
    grToneless += py2gr(gr2py(grSyllables[i]).replace(/[0-9]/g, "") + "1") + " ";
  }

  try {
    var wordIndices = fuzzyGRDict[grToneless.trim()];

    var resultBlock = "";
    
    for (var i = 0, wordlistLen = wordIndices.length; i < wordlistLen; i++) {
      resultBlock += htmlifyWord(words[wordIndices[i]]);
    }
  } catch (e) {
    var resultBlock = "Cannot convert GR or no words found.";
  }
  
  return resultBlock;
}

function findByExactGR(exactGR) {
  try {
    var wordIndices = exactGRDict[exactGR.trim()];

    var resultBlock = "";
    
    for (var i = 0, wordlistLen = wordIndices.length; i < wordlistLen; i++) {
      resultBlock += htmlifyWord(words[wordIndices[i]]);
    }
  } catch (e) {
    var resultBlock = "Cannot convert GR or no words found.";
  }
  return resultBlock;
}

document.getElementById("getDefinition").addEventListener("click", function() {
  hideRad();
  searchStr = document.getElementById("definition").value
  if (searchStr.trim() == "" || searchStr.length < 3 && searchStr.match(/^[a-z]+$/)) {
    document.getElementById("word").innerHTML = "Enter 3 or more characters.";
    document.getElementById("definition").value = "";
  } else {
    document.getElementById("word").innerHTML = findDefinition(document.getElementById("definition").value);
    document.getElementById("definition").value = "";
    setTimeout(function () { document.getElementById("definition").focus(); }, 200);
  }
});

document.getElementById("getStartChar").addEventListener("click", function() {
  hideRad();
  searchStr = document.getElementById("startChar").value
  if (searchStr.length < 1) {
    document.getElementById("word").innerHTML = "Enter 1 or more characters.";
    document.getElementById("definition").value = "";
  } else {
    document.getElementById("word").innerHTML = findStartChar(document.getElementById("startChar").value);
    document.getElementById("startChar").value = "";
    setTimeout(function () { document.getElementById("startChar").focus(); }, 200);
  }
});

document.getElementById("getGR").addEventListener("click", function() {
  hideRad();
  document.getElementById("word").innerHTML = findByFuzzyGR(document.getElementById("gr").value);
  document.getElementById("gr").value = "";
  setTimeout(function () { document.getElementById("gr").focus(); }, 200);
});

document.getElementById("getGRExact").addEventListener("click", function() {
  hideRad();
  document.getElementById("word").innerHTML = findByExactGR(document.getElementById("grExact").value);
  document.getElementById("grExact").value = "";
  setTimeout(function () { document.getElementById("grExact").focus(); }, 200);
});
