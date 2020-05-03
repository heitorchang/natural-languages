function buildTable(raw) {
  var words = raw.split('\n');
  var tableElem = document.getElementById("data");
  words.forEach(function (word) {
    var parts = word.split(";");
    tableElem.innerHTML += '<tr><td class="lg">' +
      parts[0] + "</td></tr><tr><td>" +
      parts[1] + "</td></tr><tr><td>" +
      parts[2] + "</td></tr><tr><td><hr></td></tr>";
  });
}

var text = "小王子;sheau wang .tzy;\n六歲時，有一次，;liow suey shyr, yeou yi tsyh,;\n我在一本敘述有關原始森林，;woo tzay i been shiuh shuh yeou guan yuan shyy sen lin;\n名叫<<大自然的真相>>的書中，;ming jiaw 'dah tzyh ran .de jen shianq' .de shu jong,;\n看到一幅奇特的畫。;kann daw i fwu chyi teh .de huah;\n畫中一條大蟒蛇正在吞噬一隻野獸;huah jong yih tyau dah maang sher jenq tzay tuen shyh yih jy yee show;\n這就是那張畫的影印本。;jeh jiow shyh nah jang huah .de yiing yinn been;\n書上說;shu shanq shuo;\n大蟒蛇連嚼都不嚼，;dah maang sher lian jyau dou buh jyau,;\n就把獵物整個兒吞進肚子裡;jiow baa lieh wuh jeeng geh erl tuen jinn duh .tzy lii;\n然後一動也不動的睡上六個月;ran how i donq yee bwu donq .de shuey shanq liow .ge yueh;\n慢慢消化掉肚子裡的東西;mann .man shiau huah diaw duh .tzy lii .de dong shi;\n那時候，我對這類;nah shyr how, woo duey jeh ley;\n發生在叢林中的怪事很感興趣;fa sheng tzay tsorng lin jong .de guay shyh heen gaan shinq chiuh,;\n想了一會兒就拿起一枝彩色鉛筆，;sheang .le yih huey erl jiow na chii yih jy tsae seh chian bii,;\n完成了我生平第一幅畫。;wan cherng .le woo sheng pyng dih yih fwu huah; \n我的第一幅畫就像這樣;woo .de dih yih fwu huah jiow shianq jeh yanq;\n我把這幅傑作拿給大人看，;woo baa jeh fwu jye tzuoh na geei dah ren kann,;\n問他們有沒有被我的畫嚇著。;wenn ta .men yeou mei yeou bey woo .de huah heh .je;";

buildTable(text);    
