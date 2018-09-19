<?php

$page_title = "Introduction";

$quiz_js = <<<_END
var title = "Introduction";

var questions = [

  {
    prompt: "Welcome to meleto.org!<br>We can type in Greek to practice.<br>Try entering \"Γεια σου\"",
    answer: ["Γεια σου", "γεια σου"],
    partial: [],
  },

  {
    prompt: "Type ; (semicolon) before a vowel<br>to place an accent.<br>Try typing θέλω.",
    answer: ["θέλω"],
    partial: [],
  },

  {
    prompt: "To show the answer, click on the eye.",
    answer: ["εντάξει"],
    partial: [],
  },
    
];
_END;
