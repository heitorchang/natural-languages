<?php

// Generates Meleto /html/pt/index.html

$page_title = "Homepage";

navbar("pt");

echo <<<_END
<div>
<img src="/img/icons/spacer.png" alt=" ">
</div>

<div class="center">
<div class="title">Μελετώ, vamos estudar grego</div>

<p>
<a href="/html/pt/coletividade-helenica/index.html"><img src="/img/icons/flags/gr_round.png" alt="Greek flag" style="vertical-align: middle;"><br><span class="title">Aulas da Coletividade Helênica</span></a>
</p>

  <p class="title">
    <a href="/html/en/filoglossia/index.html"><img src="/img/icons/flags/us.png" alt="us">Exercises for ILSP Filoglossia</a>
  </p>

</div>
_END;
