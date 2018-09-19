function nextFilename(name) {
  var baseFilename = name.replace(".txt", "");
  var baseParts = baseFilename.split("__");
  var number = baseParts[1] || "01";
  var nextNumber = parseInt(number) + 1;
  var leadingZero = nextNumber < 10 ? "0" : "";
  return baseParts[0] + "__" + leadingZero + nextNumber + ".txt";
}

function resetElements() {
  document.getElementById("revealP").style.visibility = "visible";
  document.getElementById("skipKeepP").style.visibility = "hidden";
  document.getElementById("saveP").style.display = "none";
  document.getElementById("seen").value = "";

  document.getElementById("output").value = "";

  hideAnswer();
  hidePrompt();
}

function loadFile(files) {
  var file = files[0];
  var reader = new FileReader();

  // callback
  reader.onload = function(e) {
    var textFromFile = e.target.result;
    resetElements();
    
    quiz(textFromFile.trim());

    // set new filename
    var loadedFilename = file.name;

    // determine precomputed filename to be saved
    // if no number is given, set to loadedFilename__02.txt
    // otherwise add 1 to the loadedFilename
    
    document.getElementById("newFilename").value = nextFilename(file.name);

    // set up quiz restarts
    document.getElementById("p1").onclick = function () { resetElements(); quiz(textFromFile.trim()); };
    document.getElementById("p2").onclick = function () { resetElements(); quiz(textFromFile.trim()); };
    document.getElementById("p3").onclick = function () { resetElements(); quiz(textFromFile.trim()); };
    
  };
  reader.readAsText(file, "UTF-8");

}

function saveFile() {
  var filename = document.getElementById("newFilename").value;
  var data = document.getElementById("output").value;
  
  var blob = new Blob([data], { type: 'text/csv' });

  var elem = window.document.createElement('a');
  elem.href = window.URL.createObjectURL(blob);
  
  elem.download = filename;

  // handle A HREF
  document.body.appendChild(elem);
  elem.click();
  document.body.removeChild(elem);
}

// http://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}

function quiz(rawlist) {
  var nothingToAdd = true;
  
  var rawWords = rawlist.split("\n");
  var words = [];
  rawWords.forEach(function (e) {
    var parts = e.split(";");
    words.push({ 'chinese': parts[0],
                 'gwoyeu': parts[1],
                 'english': parts[2] });
  });

  words = shuffleArray(words);

  var promptChoice = document.querySelector('input[name=promptType]:checked').value;

  var sequence = ask(promptChoice, words);

  var activeWord = sequence();

  document.getElementById("reveal").onclick = function(e) {
    showAnswer(activeWord);
    document.getElementById("seen").value += activeWord.chinese + ";" + activeWord.gwoyeu + ";" + activeWord.english + "\n";
    document.getElementById("seen").scrollTop = document.getElementById("seen").scrollHeight;

    document.getElementById("revealP").style.visibility = "hidden";
    document.getElementById("skipKeepP").style.visibility = "visible";
    document.getElementById("promptP").style.display = "none";
  };
  
  document.getElementById("skip").onclick = function (e) {
    hideAnswer(); 
    document.getElementById("skipKeepP").style.visibility = "hidden";
    document.getElementById("revealP").style.visibility = "visible";
    activeWord = sequence();
  };

  document.getElementById("keep").onclick = function (e) {
    if (activeWord[promptChoice]) {
      document.getElementById("output").value += (activeWord.chinese + ";" + activeWord.gwoyeu + ";" + activeWord.english).trim() + "\n";
      document.getElementById("output").scrollTop = document.getElementById("output").scrollHeight;
    }

    hideAnswer();
    document.getElementById("skipKeepP").style.visibility = "hidden";
    document.getElementById("revealP").style.visibility = "visible";

    activeWord = sequence(true);
  };
  
  //console.log(document.querySelector('input[name="promptType"]:checked').value);
  //console.log(words);
}

function ask(promptChoice, wordlist) {
  var currentList = wordlist;
  var showSave = false;
  var currentWordIndex = 1;
  var totalWords = wordlist.length;
  
  // DAT CLOSURE THO!
  return function (shouldSave) {
    if (shouldSave) {
      showSave = true;
    }
    
    document.getElementById("promptP").style.display = "block";

    if (currentList.length === 0) {
      hideAnswer();
      document.getElementById("revealP").style.visibility = "hidden";
      document.getElementById("skipKeepP").style.visibility = "hidden";
      if (showSave) {
        document.getElementById("saveP").style.display = "block";
        showPrompt("All done!");
      } else {
        showPrompt("You knew all the words! Well done!");
      }
    } else {
      document.getElementById("progress").innerHTML = currentWordIndex + " of " + totalWords;
      currentWordIndex++;

      showPrompt(currentList[0][promptChoice]);
      
      activeWord = currentList[0];
      currentList = currentList.slice(1);

      return activeWord;
    }
  };
}

function showPrompt(content) {
  document.getElementById("prompt").innerHTML = content;
}

function hidePrompt() {
  document.getElementById("prompt").innerHTML = "";
}

function showAnswer(word) {
  document.getElementById("chinese").innerHTML = word.chinese;
  document.getElementById("gwoyeu").innerHTML = word.gwoyeu;
  document.getElementById("english").innerHTML = word.english;
}

function hideAnswer() {
  document.getElementById("chinese").innerHTML = "";
  document.getElementById("gwoyeu").innerHTML = "";
  document.getElementById("english").innerHTML = "";
}

function backspaceScratch() {
  var scratchText = document.getElementById("scratch");
  var scratchVal = scratchText.value;
  scratchText.value = scratchVal.slice(0, -1);
}

function newlineScratch() {
  var scratchText = document.getElementById("scratch");
  var scratchVal = scratchText.value;
  scratchText.value += "\n";
}

function keyShortcut(e) {
  e = e || window.event;
  var kc = e.keyCode;
  var ltr = String.fromCharCode(kc);
  if (kc == 13) {
    document.getElementById("reveal").click();
    // backspaceScratch();
    // newlineScratch();
  } else if (ltr == '1') {
    document.getElementById("keep").click();
    backspaceScratch();
  } else if (ltr == '0') {
    document.getElementById("skip").click();
    backspaceScratch();
  }
}
