<?php

// Generates Meleto /html/en/index.html

$page_title = "Μελετώ homepage";

navbar("en");

echo <<<_END
<div>
<img src="/img/icons/spacer.png" alt=" ">
</div>

<div class="center">
<div class="title">Μελετώ, let's study Greek</div>

<p>
<a href="/html/en/filoglossia/index.html"><img src="/img/icons/flags/gr_round.png" alt="Greek flag" style="vertical-align: middle;"><br><span class="title">Exercises for ILSP Filoglossia</span></a>
</p>

  <p class="title">
    <a href="/html/pt/coletividade-helenica/index.html"><img src="/img/icons/flags/br.png" alt="br">Aulas da Coletividade Helênica</a>
  </p>

</div>
_END;

