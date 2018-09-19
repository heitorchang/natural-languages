<?php

$page_title = "Introdução ao meleto.org";

$quiz_js = <<<_END
var title = "Introdução";

var questions = [

  {
    prompt: "Bem-vindos ao meleto.org!<br>Podemos digitar em grego para praticar.<br>Experimente digitar \"Γεια σου\"",
    answer: ["Γεια σου", "γεια σου"],
    partial: [],
  },

  {
    prompt: "Digite ç (cedilha) ou ; (ponto-e-vírgula)<br>antes de uma vogal para pôr um acento.<br>Experimente digitar θέλω.",
    answer: ["θέλω"],
    partial: [],
  },

  {
    prompt: "Para mostrar a resposta de uma questão,<br>clique no olho para revelá-la e continuar.",
    answer: ["εντάξει"],
    partial: [],
  },
  
];
_END;
