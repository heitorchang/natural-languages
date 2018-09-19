<?php

$page_title = "Ser, estar";

$quiz_js = <<<_END
var title = "Conjugue o verbo <i>ser, estar</i>. Não inclua a pessoa.";

var questions = [

  {
    prompt: "(eu) sou, estou",
    answer: ["είμαι"],
    partial: ["ειμαι"],
  },

  {
    prompt: "(tu) és, estás",
    answer: ["είσαι"],
    partial: [],
  },

  {
    prompt: "(ele) é, está",
    answer: ["είναι"],
    partial: [],
  },

  {
    prompt: "(nós) somos, estamos",
    answer: ["είμαστε"],
    partial: [],
  },

  {
    prompt: "(vós) sois, estais",
    answer: ["είστε", "είσαστε"],
    partial: [],
  },

  {
    prompt: "(eles) são, estão",
    answer: ["είναι"],
    partial: [],
  },

];
  
_END;
