<?php

// Use php -S 127.0.0.1:9999 to test

if (!isset($argv[1])) {
  die("Enter the base directory name, as in: php buildgreek.php en\n\n");
}


// /argv[1]/...
// becomes
// /html/argv[1]/...

// labels and messages, for each language
$labels = [
  "read" => ["en" => "Read",
             "pt" => "Ler", ],
  "practice" => ["en" => "Practice",
                 "pt" => "Praticar", ],
];


$interface_lang = $argv[1];

function common_header($title) {
  global $interface_lang;
  
  echo <<<_END
  <!DOCTYPE html>
  <html lang="$interface_lang">
  <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$title</title>
  <link rel="stylesheet" href="/css/styles.css">
_END;
}

function begin_body() {
  echo <<<_END
  </head>
  <body>
_END;
}

function page_header($title) {
  common_header($title);
  begin_body();
}

function common_footer() {
  global $interface_lang;
  
  echo <<<_END

  <div class="spacer"></div>
  <hr>

  <div class="center">
  <a href="/$interface_lang/contact.html"><img src="/img/icons/speechbubble.png" alt="bubble"></a>
  
  <!--
  <img src="/img/icons/spacer.png" alt="spacer">
  <a href="https://github.com/heitorchang/meleto" target="_blank"><img src="/img/icons/github.png" alt="GitHub"></a>
  -->
  
  </div>
  
  </body>
  </html>
_END;
}

function dir_header($title) {
  echo common_header($title);
  echo <<<_END
  <link rel="stylesheet" href="/css/styles.css">
_END;
  begin_body();
}

function breadcrumb($path) {
  $out = "";
  $components = explode("/", $path);

  if (count($components) > 1) {
    $out .= " &gt; ";
  }
  

  for ($i = 1; $i < count($components); $i++) {
    $index_filename = implode("/", array_slice($components, 0, $i + 1)) . "/index.php";
    $dots = str_repeat("../", count($components) - 1 - $i);
    
    $out .= "<a href='{$dots}index.html'>" . getPageTitle($index_filename) . "</a>";

    // $out .= "<a href='{$dots}index.html'>" . "STATIC" . "</a>";
    if ($i < count($components) - 1) {
      $out .= " &gt; ";
    }
  }

  // change $i limit to count($components) - 1 to exclude linking the last item
  // $out .= getPageTitle($path . "/index.php");
  return $out . "\n";
}

function navbar($base_dir) {
  global $interface_lang;
  echo "<div class='navbar'><a href='/html/$interface_lang/index.html'>Μελετώ</a> \n";
  echo breadcrumb($base_dir);

  // add flag / interface language change
  // two languages only for now, maybe add dropdown if more are added.

  echo "<div class='interface-lang'>";

  // INTERFACE LANG
  if ($interface_lang == "en") {
    echo "<a href='/html/pt/index.html'><img src='/img/icons/flags/br.png' alt='br'>Português</a>";
  } else {
    echo "<a href='/html/en/index.html'><img src='/img/icons/flags/us.png' alt='en'>English</a>";
  }
  
  echo "</div>";
  
  echo "</div>\n";
}

function list_dir($base_dir) {
  global $interface_lang;
  global $labels;
  
  // echo "WRITE TO: html/$base_dir/index.html\n";
  
  $folders = "<div class='folder-list'>";
  $pages = "";

  // add icon for previous folder
  $folders .= "<a href='../index.html'><img src='/img/icons/revert.png' alt='back'>";
  $folders .= getPageTitle($base_dir . "/../index.php");
  $folders .= "</a><br>\n";
  
  foreach (scandir($base_dir, SCANDIR_SORT_ASCENDING) as $filename) {
    $full_path = $base_dir . "/" . $filename;
    if (substr($full_path, -1) != ".") {      
      if (is_dir($full_path)) {
        // echo "IS DIR: $full_path\n";
        // read directory description from index.php

        $folders .= "<a href='" . basename($full_path) . "/index.html'>";
        $folders .= '<img src="/img/icons/folder.png" alt="folder">';
        $folders .= getPageTitle($full_path . "/index.php");
        $folders .= "</a><br>\n";
        
      } elseif (substr($full_path, -9) != "index.php") {
        // echo "IS FILE: $full_path\n";
        $pages .= "<tr>\n";

        // manually exclude introducao.php and 0_intro.php
        if (basename($full_path) == "introducao.php" || basename($full_path) == "0_intro.php") {
          $pages .= '<td class="center">&nbsp;</td>' . "\n";
        } else {
          $pages .= '<td class="center"><a href="' . basename($full_path, '.php') . '-list.html"><img src="/img/icons/list.png" alt="list"></a></td>' . "\n";
        }
        $pages .= '<td class="center"><a href="' . basename($full_path, '.php') . '.html"><img src="/img/icons/pencil.png" alt="list"></a></td>' . "\n";
        $pages .= '<td>' . getPageTitle($full_path) . '</td>';
        $pages .= "</tr>\n";
      }
    }
  }

  // end folder list div
  $folders .= "</div>\n";
  
  $html_dir = dirname($full_path);
  @mkdir($html_dir, 0755, true);

  ob_start();

  $page_title = getPageTitle($base_dir . "/index.php");
  $folder_desc = getFolderDesc($base_dir . "/index.php");

  // add line break
  if ($folder_desc != "") {
    $folder_desc = "<br>" . $folder_desc;
  }
  
  dir_header($page_title);

  navbar($base_dir);

  echo '<div class="main">' . "\n";
  
  echo $folders;

  echo <<<_END
  <table id="menu">
  <tr>
  <td colspan="3">
  <span class="title">$page_title</span>
  <br>
  $folder_desc
  </td>
  </tr>
  
  <tr>
    <td class="caption">{$labels["read"][$interface_lang]}</td>
    <td class="caption">{$labels["practice"][$interface_lang]}</td>
    <td>&nbsp;</td>
  </tr>
_END;
  
  echo $pages;

  echo "</table>\n</div>\n";
  
  common_footer();

  @mkdir("html/$base_dir", 0755, true);
  file_put_contents("html/$base_dir/index.html", ob_get_clean());
  // echo "Completed dir $base_dir \n";
}

function recurse_dir($base_dir) {
  foreach (scandir($base_dir) as $filename) {
    $full_path = $base_dir . "/" . $filename;
    if (substr($full_path, -1) != ".") {
      if (is_dir($full_path)) {
        recurse_dir($base_dir . "/" . $filename);
        list_dir($full_path);
      } else {
        // full path is a file
        convert_to_html($full_path);
      }
    }
  }
}

function getPageTitle($filename) {
  if (substr($filename, -4) == ".php") {
    $fp_page_php = fopen($filename, "r");
    while (($line = fgets($fp_page_php)) !== false) {
      if (substr($line, 0, 11) == '$page_title') {
        $line_components = explode('"', $line);
        
        fclose($fp_page_php);
        return $line_components[1];
      }
    }
  } // else {
  // return "getPageTitle: Not php";
  // }
}

function getFolderDesc($filename) {
  if (substr($filename, -4) == ".php") {
    $fp_page_php = fopen($filename, "r");
    while (($line = fgets($fp_page_php)) !== false) {
      if (substr($line, 0, 12) == '$folder_desc') {
        $line_components = explode('"', $line);
        
        fclose($fp_page_php);
        return $line_components[1];
      }
    }
  } else {
    return "";
  }
}


function convert_to_html($php_filename) {
  global $interface_lang;

  if (substr($php_filename, -4) != ".php") {
    return;
  }
  
  $html_filename = "./html/" . substr($php_filename, 0, -4) . ".html";
  $base_filename = basename($php_filename, ".php");
    
  $page_title = getPageTitle($php_filename);

  // echo "  Converting $base_filename $page_title\n";
  if ($php_filename == "$interface_lang/index.php") {
    // special case
    ob_start();
    page_header($page_title);

    include $php_filename;
    common_footer();
    file_put_contents("./html/$interface_lang/index.html", ob_get_clean());
    
  } else if(substr($php_filename, -9) !== "index.php") {
    @mkdir(dirname($html_filename), 0755, true);
    
    ob_start();

    $quiz_js = "";
    
    include $php_filename;

    if ($quiz_js != "") {  // page contains js, create quiz and list
      echo <<<_END
<!DOCTYPE html>
<html lang="$interface_lang">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
    <title>Μελετώ: $page_title</title>
    <link rel="stylesheet" href="/css/greek-visual-keyboard.css">
    <link rel="stylesheet" href="/css/quiz.css">
    <link rel="stylesheet" href="/css/styles.css">
  </head>
  <body>
_END;
      
      navbar(dirname($php_filename));
      echo <<<_END
      
      <div class="quizWrapper">
      
      <div id="loading"><img src="/img/icons/spin.gif" alt="spinner"></div>
      
      $page_title<br>
      
      <div class="quiz">
      
      <p id="quizTitle"></p>
      
        <div class="answer-row">
          <div class="icon-box" id="showAnswer"><img src="/img/icons/eye.png" alt="show"></div>
          <input type="text" class="greek-keyboard" id="answer" size="18" autocapitalize="off" autocorrect="off" autocomplete="off" autofocus>
          <div class="icon-box" id="result"><img src="/img/icons/eraser.png" alt="erase"></div>
          <div class="icon-box hidden" id="nextQuestion"><input type="image" src="/img/icons/rightarrow.png" id="nextQuestionImage" alt="next"></div>
          <div class="icon-box display-none" id="back"><a href="index.html"><img src="/img/icons/revert.png" alt="back"></a></div>

          <br>
          <span id="prompt"></span>
        </div>



      </div>
    </div>

    <div id="visual-keyboard"></div>

    <br>
    <div class="center">
        <a href="index.html"><img src="/img/icons/revert.png" alt="back"></a>
        <img src="/img/icons/spacer.png" alt=" ">
        
        <a href="/html/$interface_lang/index.html"><img src="/img/icons/home.png" alt="home"></a>

      <!--
        <img src="/img/icons/spacer.png" alt=" ">
        
        <a href="/$interface_lang/help.html"><img src="/img/icons/question.png" alt="question"></a>
      -->
    </div> <!-- end center -->

    <script src="/js/jquery.js"></script>

    <!-- preload icons -->
    <script src="/js/preload-icons.js"></script>
    
    <!-- quiz scripts -->
    <script src="$base_filename.js"></script>
    <script src="/js/quiz.js"></script>

    <script src="/js/greek-charmap.js"></script>
    <script src="/js/greek-keymap.js"></script>
    <script src="/js/greek-by-replacement.js"></script>    
    <script src="/js/greek-visual-keyboard.js"></script>

      <script>
      $(window).load(function () {
        $("#loading").hide();
      });
      </script>
      
  </body>
</html>
_END;
    }
    
    file_put_contents($html_filename, ob_get_clean());

    // generate javascript
    create_quiz_javascript($php_filename);
      
    // generate ????-list page
    create_quiz_list($php_filename);
  }
}

// helper for more compact definition of questions
// generateQuizJS("TITLE", [["PROMPT", ["ANS1, "ANS2"], ["PARTIALS"],
//                          ["PROMPT", ... ]]);
function generateQuizJS($title, $questions) {
  $quiz_js = "var title = '$title';\n\n";

  $quiz_js .= "var questions = [\n\n";
  
  foreach ($questions as $question) {
    $quiz_js .= " {\n   prompt: \"$question[0]\",\n   answer: [";

    foreach ($question[1] as $answer) {
      $quiz_js .= "\"$answer\", ";
    }
    
    // close answer
    $quiz_js .= "],\n   partial: [";

    if (count($question) > 2) {
      foreach ($question[2] as $partial) {
        $quiz_js .= "\"$partial\", ";
      }    
    }
    
    // close partial
    $quiz_js .= "], \n";
    
    // close question object
    $quiz_js .= " },\n\n";
  }

  // close questions array
  $quiz_js .= "];";
  
  return $quiz_js;
}


function create_quiz_javascript($php_filename) {
  global $interface_lang;
  $js_filename = "./html/" . substr($php_filename, 0, -4) . ".js";
  //  echo "    Create JS to $js_filename\n";
  
  ob_start();
    
  include $php_filename;

  if (isset($quiz_js) && $quiz_js != "") {
    echo $quiz_js;
  }

  file_put_contents($js_filename, ob_get_clean());
}


// copied most from convert_to_html
function create_quiz_list($php_filename) {
  global $interface_lang;

  $html_filename = "./html/" . substr($php_filename, 0, -4) . "-list.html";
  
  $base_filename = basename($php_filename, ".php");
    
  $page_title = getPageTitle($php_filename);
    
  ob_start();

  include $php_filename;
  
  echo <<<_END
<!DOCTYPE html>
<html lang="$interface_lang">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Μελετώ: $page_title</title>
    <link rel="stylesheet" href="/css/greek-visual-keyboard.css">
    <link rel="stylesheet" href="/css/quiz.css">
    <link rel="stylesheet" href="/css/styles.css">    
  </head>
  <body>
_END;
  
  navbar(dirname($php_filename));

  echo <<<_END
  <div class="center">

  $page_title<br>
  
      <p id="quizTitle"></p>

  <div id="loading"><img src="/img/icons/spin.gif" alt="spinner"></div>
  
      <table id="list">
      </table>
      <p>
        <a href="index.html"><img src="/img/icons/revert.png" alt="back"></a>
        <img src="/img/icons/spacer.png" alt=" ">

        <a href="$base_filename.html"><img src="/img/icons/pencil_plain.png" alt="pencil"></a>
        <img src="/img/icons/spacer.png" alt=" ">
        
        <a href="/html/$interface_lang/index.html"><img src="/img/icons/home.png" alt="home"></a>

      </p>
    </div> <!-- end center -->

    <script src="/js/jquery.js"></script>

    <!-- preload icons -->
    <script src="/js/preload-icons.js"></script>
    
    <!-- quiz scripts -->
    <script src="$base_filename.js"></script>
  <script src="/js/list.js"></script>
  <script>
  $(window).load(function () {
    $("#loading").hide();
  });
  </script>
  </body>
</html>

_END;
    
  file_put_contents($html_filename, ob_get_clean());
}

// MAIN FUNCTION
echo "Converting $interface_lang\n\n";
recurse_dir($interface_lang);
