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
  
  result = '<span class="hint--top" data-hint="' + trad + '">' +
    trad + "</span> " +
    '<span class="hint--top simsun" data-hint="' + simpl + '">' +
    simpl + "</span> " +
    pyPhrase2gr(py) +
    parts.slice(2).join(" ") + "<br>";
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


document.getElementById("getEnglish").addEventListener("click", function() {
  searchStr = "/" + document.getElementById("term").value;
  if (searchStr.trim() == "" || searchStr.length < 3 && searchStr.match(/^[a-z]+$/)) {
    document.getElementById("word").innerHTML = "Enter 3 or more characters.";
    document.getElementById("term").value = "";
  } else {
    document.getElementById("word").innerHTML = findDefinition(searchStr);
    document.getElementById("term").value = "";
    setTimeout(function () { document.getElementById("term").focus(); }, 200);
  }
});

document.getElementById("getChinese").addEventListener("click", function() {
  searchStr = document.getElementById("term").value;
  if (searchStr.trim() == "" || searchStr.length < 1 && searchStr.match(/^[a-z]+$/)) {
    document.getElementById("word").innerHTML = "Enter one or more characters.";
    document.getElementById("term").value = "";
  } else {
    document.getElementById("word").innerHTML = findDefinition(searchStr);
    document.getElementById("term").value = "";
    setTimeout(function () { document.getElementById("term").focus(); }, 200);
  }
});

document.getElementById("getGRFuzzy").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findByFuzzyGR(document.getElementById("term").value);
  document.getElementById("term").value = "";
  setTimeout(function () { document.getElementById("gr").focus(); }, 200);
});

document.getElementById("getGRExact").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findByExactGR(document.getElementById("term").value);
  document.getElementById("term").value = "";
  setTimeout(function () { document.getElementById("gr").focus(); }, 200);
});
