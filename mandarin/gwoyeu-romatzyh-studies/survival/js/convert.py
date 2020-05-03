# Convert a raw GR file to Pinyin

import sys

table = {
    "a1": 'a',
    "a2": 'ar',
    "a4": 'ah',
    "ai1": 'ai',
    "ai2": 'air',
    "ai3": 'ae',
    "ai4": 'ay',
    "an1": 'an',
    "an3": 'aan',
    "an4": 'ann',
    "ang1": 'ang',
    "ang2": 'arng',
    "ang4": 'anq',
    "ao1": 'au',
    "ao2": 'aur',
    "ao3": 'ao',
    "ao4": 'aw',
    "ba1": 'ba',
    "ba2": 'bar',
    "ba3": 'baa',
    "ba4": 'bah',
    "bai1": 'bai',
    "bai2": 'bair',
    "bai3": 'bae',
    "bai4": 'bay',
    "ban1": 'ban',
    "ban3": 'baan',
    "ban4": 'bann',
    "bang1": 'bang',
    "bang3": 'baang',
    "bang4": 'banq',
    "bao1": 'bau',
    "bao2": 'baur',
    "bao3": 'bao',
    "bao4": 'baw',
    "bei1": 'bei',
    "bei3": 'beei',
    "bei4": 'bey',
    "ben1": 'ben',
    "ben3": 'been',
    "ben4": 'benn',
    "beng1": 'beng',
    "beng2": 'berng',
    "beng3": 'beeng',
    "beng4": 'benq',
    "bi1": 'bi',
    "bi2": 'byi',
    "bi3": 'bii',
    "bi4": 'bih',
    "bian1": 'bian',
    "bian3": 'bean',
    "bian4": 'biann',
    "biao1": 'biau',
    "biao3": 'beau',
    "biao4": 'biaw',
    "bie1": 'bie',
    "bie2": 'bye',
    "bie3": 'biee',
    "bie4": 'bieh',
    "bin1": 'bin',
    "bin4": 'binn',
    "bing1": 'bing',
    "bing3": 'biing',
    "bing4": 'binq',
    "bo1": 'bo',
    "bo2": 'bor',
    "bo3": 'boo',
    "bo4": 'boh',
    "bu1": 'bu',
    "bu2": 'bwu',
    "bu3": 'buu',
    "bu4": 'buh',
    "ca1": 'tsa',
    "cai1": 'tsai',
    "cai2": 'tsair',
    "cai3": 'tsae',
    "cai4": 'tsay',
    "can1": 'tsan',
    "can2": 'tsarn',
    "can3": 'tsaan',
    "can4": 'tsann',
    "cang1": 'tsang',
    "cang2": 'tsarng',
    "cang3": 'tsaang',
    "cao1": 'tsau',
    "cao2": 'tsaur',
    "cao3": 'tsao',
    "cao4": 'tsaw',
    "ce1": 'tse',
    "ce4": 'tseh',
    "cen1": 'tsen',
    "cen2": 'tsern',
    "ceng1": 'tseng',
    "ceng2": 'tserng',
    "ceng4": 'tsenq',
    "cha1": 'cha',
    "cha2": 'char',
    "cha3": 'chaa',
    "cha4": 'chah',
    "chai1": 'chai',
    "chai2": 'chair',
    "chai3": 'chae',
    "chai4": 'chay',
    "chan1": 'chan',
    "chan2": 'charn',
    "chan3": 'chaan',
    "chan4": 'chann',
    "chang1": 'chang',
    "chang2": 'charng',
    "chang3": 'chaang',
    "chang4": 'chanq',
    "chao1": 'chau',
    "chao2": 'chaur',
    "chao3": 'chao',
    "chao4": 'chaw',
    "che1": 'che',
    "che3": 'chee',
    "che4": 'cheh',
    "chen1": 'chen',
    "chen2": 'chern',
    "chen4": 'chenn',
    "cheng1": 'cheng',
    "cheng2": 'cherng',
    "cheng3": 'cheeng',
    "cheng4": 'chenq',
    "chi1": 'chy',
    "chi2": 'chyr',
    "chi3": 'chyy',
    "chi4": 'chyh',
    "chong1": 'chong',
    "chong2": 'chorng',
    "chong3": 'choong',
    "chong4": 'chonq',
    "chou1": 'chou',
    "chou2": 'chour',
    "chou3": 'choou',
    "chou4": 'chow',
    "chu1": 'chu',
    "chu2": 'chwu',
    "chu3": 'chuu',
    "chu4": 'chuh',
    "chua1": 'chua',
    "chuai1": 'chuai',
    "chuai3": 'choai',
    "chuai4": 'chuay',
    "chuan1": 'chuan',
    "chuan2": 'chwan',
    "chuan3": 'choan',
    "chuan4": 'chuann',
    "chuang1": 'chuang',
    "chuang2": 'chwang',
    "chuang3": 'choang',
    "chuang4": 'chuanq',
    "chui1": 'chuei',
    "chui2": 'chwei',
    "chun1": 'chuen',
    "chun2": 'chwen',
    "chun3": 'choen',
    "chuo1": 'chuo',
    "chuo4": 'chuoh',
    "ci1": 'tsy',
    "ci2": 'tsyr',
    "ci3": 'tsyy',
    "ci4": 'tsyh',
    "cong1": 'tsong',
    "cong2": 'tsorng',
    "cou4": 'tsow',
    "cu1": 'tsu',
    "cu2": 'tswu',
    "cu4": 'tsuh',
    "cu4": 'tsuh',
    "cuan1": 'tsuan',
    "cuan2": 'tswan',
    "cuan4": 'tsuann',
    "cui1": 'tsuei',
    "cui3": 'tsoei',
    "cui4": 'tsuey',
    "cun1": 'tsuen',
    "cun2": 'tswen',
    "cun3": 'tsoen',
    "cun4": 'tsuenn',
    "cuo1": 'tsuo',
    "cuo2": 'tswo',
    "cuo3": 'tsuoo',
    "cuo4": 'tsuoh',
    "da1": 'da',
    "da2": 'dar',
    "da3": 'daa',
    "da4": 'dah',
    "dai1": 'dai',
    "dai3": 'dae',
    "dai4": 'day',
    "dan1": 'dan',
    "dan3": 'daan',
    "dan4": 'dann',
    "dang1": 'dang',
    "dang3": 'daang',
    "dang4": 'danq',
    "dao1": 'dau',
    "dao3": 'dao',
    "dao4": 'daw',
    "de1": 'de',
    "de2": 'der',
    "dei1": 'dei',
    "dei3": 'deei',
    "deng1": 'deng',
    "deng3": 'deeng',
    "deng4": 'denq',
    "di1": 'di',
    "di2": 'dyi',
    "di3": 'dii',
    "di4": 'dih',
    "dian1": 'dian',
    "dian3": 'dean',
    "dian4": 'diann',
    "diao1": 'diau',
    "diao4": 'diaw',
    "die1": 'die',
    "die2": 'dye',
    "ding1": 'ding',
    "ding3": 'diing',
    "ding4": 'dinq',
    "diu1": 'diou',
    "dong1": 'dong',
    "dong3": 'doong',
    "dong4": 'donq',
    "dou1": 'dou',
    "dou3": 'doou',
    "dou4": 'dow',
    "du1": 'du',
    "du2": 'dwu',
    "du3": 'duu',
    "du4": 'duh',
    "duan1": 'duan',
    "duan3": 'doan',
    "duan4": 'duann',
    "dui1": 'duei',
    "dui4": 'duey',
    "dun1": 'duen',
    "dun3": 'doen',
    "dun4": 'duenn',
    "duo1": 'duo',
    "duo2": 'dwo',
    "duo3": 'duoo',
    "duo4": 'duoh',
    "e1": 'e',
    "e2": 'er',
    "e3": 'ee',
    "e4": 'eh',
    "ei1": 'ei',
    "ei3": 'eei',
    "ei4": 'ey',
    "en1": 'en',
    "en2": 'ern',
    "en3": 'een',
    "en4": 'enn',
    "er1": 'el',
    "er2": 'erl',
    "er3": 'eel',
    "er4": 'ell',
    "fa1": 'fa',
    "fa2": 'far',
    "fa3": 'faa',
    "fa4": 'fah',
    "fan1": 'fan',
    "fan2": 'farn',
    "fan3": 'faan',
    "fan4": 'fann',
    "fang1": 'fang',
    "fang2": 'farng',
    "fang3": 'faang',
    "fang4": 'fanq',
    "fei1": 'fei',
    "fei2": 'feir',
    "fei3": 'feei',
    "fei4": 'fey',
    "fen1": 'fen',
    "fen2": 'fern',
    "fen3": 'feen',
    "fen4": 'fenn',
    "feng1": 'feng',
    "feng2": 'ferng',
    "feng3": 'feeng',
    "feng4": 'fenq',
    "fo1": 'fo',
    "fo2": 'for',
    "fou1": 'fou',
    "fou2": 'four',
    "fou3": 'foou',
    "fu1": 'fu',
    "fu2": 'fwu',
    "fu3": 'fuu',
    "fu4": 'fuh',
    "ga1": 'ga',
    "ga2": 'gar',
    "ga4": 'gah',
    "gai1": 'gai',
    "gai3": 'gae',
    "gai4": 'gay',
    "gan1": 'gan',
    "gan3": 'gaan',
    "gan4": 'gann',
    "gang1": 'gang',
    "gang3": 'gaang',
    "gang4": 'ganq',
    "gao1": 'gau',
    "gao3": 'gao',
    "gao4": 'gaw',
    "ge1": 'ge',
    "ge2": 'ger',
    "ge3": 'gee',
    "ge4": 'geh',
    "gei1": 'gei',
    "gei3": 'geei',
    "gen1": 'gen',
    "gen3": 'geen',
    "gen4": 'genn',
    "geng1": 'geng',
    "geng3": 'geeng',
    "geng4": 'genq',
    "ging1": "ging",
    "gong1": 'gong',
    "gong3": 'goong',
    "gong4": 'gonq',
    "gou1": 'gou',
    "gou3": 'goou',
    "gou4": 'gow',
    "gu1": 'gu',
    "gu2": 'gwu',
    "gu3": 'guu',
    "gu4": 'guh',
    "gua1": 'gua',
    "gua3": 'goa',
    "gua4": 'guah',
    "guai1": 'guai',
    "guai3": 'goai',
    "guai4": 'guay',
    "guan1": 'guan',
    "guan3": 'goan',
    "guan4": 'guann',
    "guang1": 'guang',
    "guang3": 'goang',
    "guang4": 'guanq',
    "gui1": 'guei',
    "gui3": 'goei',
    "gui4": 'guey',
    "gun3": 'goen',
    "gun1": 'guen',
    "gun4": 'guenn',
    "guo1": 'guo',
    "guo2": 'gwo',
    "guo3": 'guoo',
    "guo4": 'guoh',
    "ha1": 'ha',
    "ha2": 'har',
    "ha3": 'haa',
    "hai1": 'hai',
    "hai2": 'hair',
    "hai3": 'hae',
    "hai4": 'hay',
    "han1": 'han',
    "han2": 'harn',
    "han3": 'haan',
    "han4": 'hann',
    "hang1": 'hang',
    "hang2": 'harng',
    "hang4": 'hanq',
    "hao1": 'hau',
    "hao2": 'haur',
    "hao3": 'hao',
    "hao4": 'haw',
    "he1": 'he',
    "he2": 'her',
    "he4": 'heh',
    "hei1": 'hei',
    "hen2": 'hern',
    "hen3": 'heen',
    "hen4": 'henn',
    "heng1": 'heng',
    "heng2": 'herng',
    "heng4": 'henq',
    "hm1": 'hm',
    "hong1": 'hong',
    "hong2": 'horng',
    "hong3": 'hoong',
    "hong4": 'honq',
    "hou1": 'hou',
    "hou2": 'hour',
    "hou3": 'hoou',
    "hou4": 'how',
    "hu1": 'hu',
    "hu2": 'hwu',
    "hu3": 'huu',
    "hu4": 'huh',
    "hua1": 'hua',
    "hua2": 'hwa',
    "hua4": 'huah',
    "huai1": 'huai',
    "huai2": 'hwai',
    "huai4": 'huay',
    "huan1": 'huan',
    "huan2": 'hwan',
    "huan3": 'hoan',
    "huan4": 'huann',
    "huang1": 'huang',
    "huang2": 'hwang',
    "huang3": 'hoang',
    "huang4": 'huanq',
    "hui1": 'huei',
    "hui2": 'hwei',
    "hui3": 'hoei',
    "hui4": 'huey',
    "hun1": 'huen',
    "hun2": 'hwen',
    "hun3": 'hoen',
    "hun4": 'huenn',
    "huo1": 'huo',
    "huo2": 'hwo',
    "huo3": 'huoo',
    "huo4": 'huoh',
    "ji1": 'ji',
    "ji2": 'jyi',
    "ji3": 'jii',
    "ji4": 'jih',
    "jia1": 'jia',
    "jia2": 'jya',
    "jia3": 'jea',
    "jia4": 'jiah',
    "jian1": 'jian',
    "jian3": 'jean',
    "jian4": 'jiann',
    "jiang1": 'jiang',
    "jiang3": 'jeang',
    "jiang4": 'jianq',
    "jiao1": 'jiau',
    "jiao2": 'jyau',
    "jiao3": 'jeau',
    "jiao4": 'jiaw',
    "jie1": 'jie',
    "jie2": 'jye',
    "jie3": 'jiee',
    "jie4": 'jieh',
    "jin1": 'jin',
    "jin3": 'jiin',
    "jin4": 'jinn',
    "jing1": 'jing',
    "jing3": 'jiing',
    "jing4": 'jinq',
    "jiong1": 'jiong',
    "jiong3": 'jeong',
    "jiu1": 'jiou',
    "jiu3": 'jeou',
    "jiu4": 'jiow',
    "ju1": 'jiu',
    "ju2": 'jyu',
    "ju3": 'jeu',
    "ju4": 'jiuh',
    "juan1": 'jiuan',
    "juan3": 'jeuan',
    "juan4": 'jiuann',
    "jue1": 'jiue',
    "jue2": 'jyue',
    "jue3": 'jeue',
    "jue4": 'jiueh',
    "jun1": 'jiun',
    "jun4": 'jiunn',
    "ka1": 'ka',
    "ka3": 'kaa',
    "ka4": 'kah',
    "kai1": 'kai',
    "kai3": 'kae',
    "kai4": 'kay',
    "kan1": 'kan',
    "kan3": 'kaan',
    "kan4": 'kann',
    "kang1": 'kang',
    "kang2": 'karng',
    "kang3": 'kaang',
    "kang4": 'kanq',
    "kao1": 'kau',
    "kao3": 'kao',
    "kao4": 'kaw',
    "ke1": 'ke',
    "ke2": 'ker',
    "ke3": 'kee',
    "ke4": 'keh',
    "ken1": 'ken',
    "ken3": 'keen',
    "ken4": 'kenn',
    "keng1": 'keng',
    "keng3": 'keeng',
    "kong1": 'kong',
    "kong3": 'koong',
    "kong4": 'konq',
    "kou1": 'kou',
    "kou3": 'koou',
    "kou4": 'kow',
    "ku1": 'ku',
    "ku3": 'kuu',
    "ku4": 'kuh',
    "kua1": 'kua',
    "kua3": 'koa',
    "kua4": 'kuah',
    "kuai1": 'kuai',
    "kuai3": 'koai',
    "kuai4": 'kuay',
    "kuan1": 'kuan',
    "kuan3": 'koan',
    "kuang1": 'kuang',
    "kuang2": 'kwang',
    "kuang4": 'kuanq',
    "kui1": 'kuei',
    "kui2": 'kwei',
    "kui3": 'koei',
    "kui4": 'kuey',
    "kun1": 'kuen',
    "kun3": 'koen',
    "kun4": 'kuenn',
    "kuo4": 'kuoh',
    "la1": 'lha',
    "la2": 'la',
    "la3": 'laa',
    "la4": 'lah',
    "lai1": 'lhai',
    "lai2": 'lai',
    "lai4": 'lay',
    "lan1": 'lhan',
    "lan2": 'lan',
    "lan3": 'laan',
    "lan4": 'lann',
    "lang1": 'lhang',
    "lang2": 'lang',
    "lang3": 'laang',
    "lang4": 'lanq',
    "lao1": 'lhau',
    "lao2": 'lau',
    "lao3": 'lao',
    "lao4": 'law',
    "le1": 'lhe',
    "le2": 'le',
    "le4": 'leh',
    "lei1": 'lhei',
    "lei2": 'lei',
    "lei3": 'leei',
    "lei4": 'ley',
    "leng1": 'lheng',
    "leng2": 'leng',
    "leng3": 'leeng',
    "leng4": 'lenq',
    "li1": 'lhi',
    "li2": 'li',
    "li3": 'lii',
    "li4": 'lih',
    "lia1": 'lia',
    "lia3": 'lea',
    "lian1": 'lhian',
    "lian2": 'lian',
    "lian3": 'lean',
    "lian4": 'liann',
    "liang1": 'lhiang',
    "liang2": 'liang',
    "liang3": 'leang',
    "liang4": 'lianq',
    "liao1": 'lhiau',
    "liao2": 'liau',
    "liao3": 'leau',
    "liao4": 'liaw',
    "lie1": 'lhie',
    "lie2": 'lie',
    "lie3": 'liee',
    "lie4": 'lieh',
    "lin1": 'lhin',
    "lin2": 'lin',
    "lin3": 'liin',
    "lin4": 'linn',
    "ling1": 'lhing',
    "ling2": 'ling',
    "ling3": 'liing',
    "ling4": 'linq',
    "liu1": 'lhiou',
    "liu2": 'liou',
    "liu3": 'leou',
    "liu4": 'liow',
    "long1": 'lhong',
    "long2": 'long',
    "long3": 'loong',
    "long4": 'lonq',
    "lou1": 'lhou',
    "lou2": 'lou',
    "lou3": 'loou',
    "lou4": 'low',
    "lu1": 'lhu',
    "lu2": 'lu',
    "lu3": 'luu',
    "lu4": 'luh',
    "lü1": 'lhiu',
    "lü2": 'liu',
    "lü3": 'leu',
    "lü4": 'liuh',
    "lu:1": 'lhiu',
    "lu:2": 'liu',
    "lu:3": 'leu',
    "lu:4": 'liuh',
    "lu:an1": 'lhiuan',
    "lu:an2": 'liuan',
    "lu:an3": 'leuan',
    "lüe4": 'liueh',
    "lu:e4": 'liueh',
    "luan1": 'lhuan',
    "luan2": 'luan',
    "luan3": 'loan',
    "luan4": 'luann',
    "lun1": 'lhuen',
    "lun2": 'luen',
    "lun4": 'luenn',
    "luo1": 'lhuo',
    "luo2": 'luo',
    "luo3": 'luoo',
    "luo4": 'luoh',
    "m2": 'm',
    "m5": '.m',
    "ma5": '.ma',
    "ma1": 'mha',
    "ma2": 'ma',
    "ma3": 'maa',
    "ma4": 'mah',
    "mai1": 'mhai',
    "mai2": 'mai',
    "mai3": 'mae',
    "mai4": 'may',
    "man1": 'mhan',
    "man2": 'man',
    "man3": 'maan',
    "man4": 'mann',
    "mang1": 'mhang',
    "mang2": 'mang',
    "mang3": 'maang',
    "mao1": 'mhau',
    "mao2": 'mau',
    "mao3": 'mao',
    "mao4": 'maw',
    "me1": 'mhe',
    "me2": 'me',
    "me3": 'mee',
    "me4": 'meh',
    "mei1": 'mhei',
    "mei2": 'mei',
    "mei3": 'meei',
    "mei4": 'mey',
    "men1": 'mhen',
    "men2": 'men',
    "men4": 'menn',
    "meng1": 'mheng',
    "meng2": 'meng',
    "meng3": 'meeng',
    "meng4": 'menq',
    "mi1": 'mhi',
    "mi2": 'mi',
    "mi3": 'mii',
    "mi4": 'mih',
    "mian1": 'mhian',
    "mian2": 'mian',
    "mian3": 'mean',
    "mian4": 'miann',
    "miao1": 'mhiau',
    "miao2": 'miau',
    "miao3": 'meau',
    "miao4": 'miaw',
    "mie1": 'mhie',
    "mie4": 'mieh',
    "min2": 'min',
    "min3": 'miin',
    "ming1": 'mhing',
    "ming2": 'ming',
    "ming3": 'miing',
    "ming4": 'minq',
    "miu1": 'miou',
    "miu4": 'miow',
    "mo1": 'mho',
    "mo2": 'mo',
    "mo3": 'moo',
    "mo4": 'moh',
    "mou1": 'mhou',
    "mou2": 'mou',
    "mou3": 'moou',
    "mou4": 'mow',
    "mu1": 'mhu',
    "mu2": 'mu',
    "mu3": 'muu',
    "mu4": 'muh',
    "na1": 'nha',
    "na2": 'na',
    "na3": 'naa',
    "na4": 'nah',
    "nai1": 'nhai',
    "nai2": 'nai',
    "nai3": 'nae',
    "nai4": 'nay',
    "nai5": '.nai',
    "nan1": 'nhan',
    "nan2": 'nan',
    "nan3": 'naan',
    "nan4": 'nann',
    "nang2": 'nang',
    "nang3": 'naang',
    "nao2": 'nau',
    "nao3": 'nao',
    "nao4": 'naw',
    "ne2": 'ne',
    "ne4": 'neh',
    "nei3": 'neei',
    "nei4": 'ney',
    "nen4": 'nenn',
    "neng2": 'neng',
    "neng4": 'nenq',
    "ni1": 'nhi',
    "ni2": 'ni',
    "ni3": 'nii',
    "ni4": 'nih',
    "nian1": 'nhian',
    "nian2": 'nian',
    "nian3": 'nean',
    "nian4": 'niann',
    "niang2": 'niang',
    "niang4": 'nianq',
    "niao3": 'neau',
    "niao4": 'niaw',
    "nie1": 'nhie',
    "nie2": 'nie',
    "nie4": 'nieh',
    "nin2": 'nin',
    "ning2": 'ning',
    "ning3": 'niing',
    "ning4": 'ninq',
    "niu1": 'nhiou',
    "niu2": 'niou',
    "niu3": 'neou',
    "niu4": 'niow',
    "nong2": 'nong',
    "nong4": 'nonq',
    "nou4": 'now',
    "nu2": 'nu',
    "nu3": 'nuu',
    "nu4": 'nuh',
    "nu:3": 'neu',
    "nu:4": 'niuh',
    "nü3": 'neu',
    "nü4": 'niuh',
    "nu:e4": 'niueh',
    "nüe4": 'niueh',
    "nuan3": 'noan',
    "nuo2": 'nuo',
    "nuo3": 'nuoo',
    "nuo4": 'nuoh',
    "o1": 'o',
    "o2": 'or',
    "ou1": 'ou',
    "ou3": 'oou',
    "ou4": 'ow',
    "pa1": 'pa',
    "pa2": 'par',
    "pa4": 'pah',
    "pai1": 'pai',
    "pai2": 'pair',
    "pai3": 'pae',
    "pai4": 'pay',
    "pan1": 'pan',
    "pan2": 'parn',
    "pan4": 'pann',
    "pang1": 'pang',
    "pang2": 'parng',
    "pang4": 'panq',
    "pao1": 'pau',
    "pao2": 'paur',
    "pao3": 'pao',
    "pao4": 'paw',
    "pei1": 'pei',
    "pei2": 'peir',
    "pei4": 'pey',
    "pen1": 'pen',
    "pen2": 'pern',
    "peng1": 'peng',
    "peng2": 'perng',
    "peng3": 'peeng',
    "peng4": 'penq',
    "pi1": 'pi',
    "pi2": 'pyi',
    "pi3": 'pii',
    "pi4": 'pih',
    "pian1": 'pian',
    "pian2": 'pyan',
    "pian3": 'pean',
    "pian4": 'piann',
    "piao1": 'piau',
    "piao2": 'pyau',
    "piao3": 'peau',
    "piao4": 'piaw',
    "pie1": 'pie',
    "pie3": 'piee',
    "pin1": 'pin',
    "pin2": 'pyn',
    "pin3": 'piin',
    "pin4": 'pinn',
    "ping1": 'ping',
    "ping2": 'pyng',
    "ping4": 'pinq',
    "po1": 'po',
    "po2": 'por',
    "po3": 'poo',
    "po4": 'poh',
    "pou1": 'pou',
    "pou2": 'pour',
    "pou3": 'poou',
    "pu1": 'pu',
    "pu2": 'pwu',
    "pu3": 'puu',
    "pu4": 'puh',
    "qi1": 'chi',
    "qi2": 'chyi',
    "qi3": 'chii',
    "qi4": 'chih',
    "qia1": 'chia',
    "qia2": 'chya',
    "qia3": 'chea',
    "qia4": 'chiah',
    "qian1": 'chian',
    "qian2": 'chyan',
    "qian3": 'chean',
    "qian4": 'chiann',
    "qiang1": 'chiang',
    "qiang2": 'chyang',
    "qiang3": 'cheang',
    "qiang4": 'chianq',
    "qiao1": 'chiau',
    "qiao2": 'chyau',
    "qiao3": 'cheau',
    "qiao4": 'chiaw',
    "qie1": 'chie',
    "qie2": 'chye',
    "qie3": 'chiee',
    "qie4": 'chieh',
    "qin1": 'chin',
    "qin2": 'chyn',
    "qin3": 'chiin',
    "qin4": 'chinn',
    "qing1": 'ching',
    "qing2": 'chyng',
    "qing3": 'chiing',
    "qing4": 'chinq',
    "qiong1": 'chiong',
    "qiong2": 'chyong',
    "qiu1": 'chiou',
    "qiu2": 'chyou',
    "qiu3": 'cheou',
    "qu1": 'chiu',
    "qu2": 'chyu',
    "qu3": 'cheu',
    "qu4": 'chiuh',
    "quan1": 'chiuan',
    "quan2": 'chyuan',
    "quan3": 'cheuan',
    "quan4": 'chiuann',
    "que1": 'chiue',
    "que2": 'chyue',
    "que4": 'chiueh',
    "qun1": 'chiun',
    "qun2": 'chyun',
    "r2": "el",
    "ran2": 'ran',
    "ran3": 'raan',
    "rang1": 'rhang',
    "rang2": 'rang',
    "rang3": 'raang',
    "rang4": 'ranq',
    "rao2": 'rau',
    "rao3": 'rao',
    "rao4": 'raw',
    "re3": 'ree',
    "re4": 'reh',
    "ren2": 'ren',
    "ren3": 'reen',
    "ren4": 'renn',
    "reng1": 'rheng',
    "reng2": 'reng',
    "ri4": 'ryh',
    "rong2": 'rong',
    "rong3": 'roong',
    "rou2": 'rou',
    "rou3": 'roou',
    "rou4": 'row',
    "ru2": 'ru',
    "ru3": 'ruu',
    "ru4": 'ruh',
    "ruan3": 'roan',
    "rui2": 'ruei',
    "rui3": 'roei',
    "rui4": 'ruey',
    "run2": 'ruen',
    "run4": 'ruenn',
    "ruo2": 'ruo',
    "ruo4": 'ruoh',
    "sa1": 'sa',
    "sa3": 'saa',
    "sa4": 'sah',
    "sai1": 'sai',
    "sai4": 'say',
    "san1": 'san',
    "san3": 'saan',
    "san4": 'sann',
    "sang1": 'sang',
    "sang3": 'saang',
    "sang4": 'sanq',
    "sao1": 'sau',
    "sao3": 'sao',
    "sao4": 'saw',
    "se1": 'se',
    "se4": 'seh',
    "sen1": 'sen',
    "seng1": 'seng',
    "sha1": 'sha',
    "sha2": 'shar',
    "sha3": 'shaa',
    "sha4": 'shah',
    "shai1": 'shai',
    "shai3": 'shae',
    "shai4": 'shay',
    "shan1": 'shan',
    "shan3": 'shaan',
    "shan4": 'shann',
    "shang1": 'shang',
    "shang3": 'shaang',
    "shang4": 'shanq',
    "shao1": 'shau',
    "shao2": 'shaur',
    "shao3": 'shao',
    "shao4": 'shaw',
    "she1": 'she',
    "she2": 'sher',
    "she3": 'shee',
    "she4": 'sheh',
    "shei1": 'shei',
    "shei2": 'sheir',
    "shen1": 'shen',
    "shen2": 'shern',
    "shen3": 'sheen',
    "shen4": 'shenn',
    "sheng1": 'sheng',
    "sheng2": 'sherng',
    "sheng3": 'sheeng',
    "sheng4": 'shenq',
    "shi1": 'shy',
    "shi2": 'shyr',
    "shi3": 'shyy',
    "shi4": 'shyh',
    "shou1": 'shou',
    "shou2": 'shour',
    "shou3": 'shoou',
    "shou4": 'show',
    "shu1": 'shu',
    "shu2": 'shwu',
    "shu3": 'shuu',
    "shu4": 'shuh',
    "shua1": 'shua',
    "shua3": 'shoa',
    "shua4": 'shuah',
    "shuai1": 'shuai',
    "shuai3": 'shoai',
    "shuai4": 'shuay',
    "shuan1": 'shuan',
    "shuan4": 'shuann',
    "shuang1": 'shuang',
    "shuang3": 'shoang',
    "shui1": 'shuei',
    "shui2": 'shwei',
    "shui3": 'shoei',
    "shui4": 'shuey',
    "shun1": 'shuen',
    "shun3": 'shoen',
    "shun4": 'shuenn',
    "shuo1": 'shuo',
    "shuo4": 'shuoh',
    "si1": 'sy',
    "si3": 'syy',
    "si4": 'syh',
    "song1": 'song',
    "song3": 'soong',
    "song4": 'sonq',
    "sou1": 'sou',
    "sou3": 'soou',
    "sou4": 'sow',
    "su1": 'su',
    "su2": 'swu',
    "su4": 'suh',
    "suan1": 'suan',
    "suan3": 'soan',
    "suan4": 'suann',
    "sui1": 'suei',
    "sui2": 'swei',
    "sui3": 'soei',
    "sui4": 'suey',
    "sun1": 'suen',
    "sun3": 'soen',
    "sun4": 'suenn',
    "suo1": 'suo',
    "suo2": 'swo',
    "suo3": 'suoo',
    "ta1": 'ta',
    "ta3": 'taa',
    "ta4": 'tah',
    "tai1": 'tai',
    "tai2": 'tair',
    "tai4": 'tay',
    "tan1": 'tan',
    "tan2": 'tarn',
    "tan3": 'taan',
    "tan4": 'tann',
    "tang1": 'tang',
    "tang2": 'tarng',
    "tang3": 'taang',
    "tang4": 'tanq',
    "tao1": 'tau',
    "tao2": 'taur',
    "tao3": 'tao',
    "tao4": 'taw',
    "te1": 'te',
    "te4": 'teh',
    "teng1": 'teng',
    "teng2": 'terng',
    "ti1": 'ti',
    "ti2": 'tyi',
    "ti3": 'tii',
    "ti4": 'tih',
    "tian1": 'tian',
    "tian2": 'tyan',
    "tian3": 'tean',
    "tian4": 'tiann',
    "tiao1": 'tiau',
    "tiao2": 'tyau',
    "tiao3": 'teau',
    "tiao4": 'tiaw',
    "tie1": 'tie',
    "tie3": 'tiee',
    "tie4": 'tieh',
    "ting1": 'ting',
    "ting2": 'tyng',
    "ting3": 'tiing',
    "ting4": 'tinq',
    "tong1": 'tong',
    "tong2": 'torng',
    "tong3": 'toong',
    "tong4": 'tonq',
    "tou1": 'tou',
    "tou2": 'tour',
    "tou3": 'toou',
    "tou4": 'tow',
    "tu1": 'tu',
    "tu2": 'twu',
    "tu3": 'tuu',
    "tu4": 'tuh',
    "tuan1": 'tuan',
    "tuan2": 'twan',
    "tuan3": 'toan',
    "tuan4": 'tuann',
    "tui1": 'tuei',
    "tui2": 'twei',
    "tui3": 'toei',
    "tui4": 'tuey',
    "tun1": 'tuen',
    "tun2": 'twen',
    "tun3": 'toen',
    "tun4": 'tuenn',
    "tuo1": 'tuo',
    "tuo2": 'two',
    "tuo3": 'tuoo',
    "tuo4": 'tuoh',
    "wa1": 'ua',
    "wa2": 'wa',
    "wa3": 'woa',
    "wa4": 'wah',
    "wai1": 'uai',
    "wai4": 'way',
    "wan1": 'uan',
    "wan2": 'wan',
    "wan3": 'woan',
    "wan4": 'wann',
    "wang1": 'uang',
    "wang2": 'wang',
    "wang3": 'woang',
    "wang4": 'wanq',
    "wei1": 'uei',
    "wei2": 'wei',
    "wei3": 'woei',
    "wei4": 'wey',
    "wen1": 'uen',
    "wen2": 'wen',
    "wen3": 'woen',
    "wen4": 'wenn',
    "weng1": 'ueng',
    "weng3": 'woeng',
    "weng4": 'wenq',
    "wo1": 'uo',
    "wo3": 'woo',
    "wo4": 'woh',
    "wu1": 'u',
    "wu2": 'wu',
    "wu3": 'wuu',
    "wu4": 'wuh',
    "xi1": 'shi',
    "xi2": 'shyi',
    "xi3": 'shii',
    "xi4": 'shih',
    "xia1": 'shia',
    "xia2": 'shya',
    "xia4": 'shiah',
    "xian1": 'shian',
    "xian2": 'shyan',
    "xian3": 'shean',
    "xian4": 'shiann',
    "xiang1": 'shiang',
    "xiang2": 'shyang',
    "xiang3": 'sheang',
    "xiang4": 'shianq',
    "xiao1": 'shiau',
    "xiao2": 'shyau',
    "xiao3": 'sheau',
    "xiao4": 'shiaw',
    "xie1": 'shie',
    "xie2": 'shye',
    "xie3": 'shiee',
    "xie4": 'shieh',
    "xin1": 'shin',
    "xin2": 'shyn',
    "xin4": 'shinn',
    "xing1": 'shing',
    "xing2": 'shyng',
    "xing3": 'shiing',
    "xing4": 'shinq',
    "xiong1": 'shiong',
    "xiong2": 'shyong',
    "xiong4": 'shionq',
    "xiu1": 'shiou',
    "xiu3": 'sheou',
    "xiu4": 'shiow',
    "xu1": 'shiu',
    "xu2": 'shyu',
    "xu3": 'sheu',
    "xu4": 'shiuh',
    "xuan1": 'shiuan',
    "xuan2": 'shyuan',
    "xuan3": 'sheuan',
    "xuan4": 'shiuann',
    "xue1": 'shiue',
    "xue2": 'shyue',
    "xue3": 'sheue',
    "xue4": 'shiueh',
    "xun1": 'shiun',
    "xun2": 'shyun',
    "xun4": 'shiunn',
    "ya1": 'ia',
    "ya2": 'ya',
    "ya3": 'yea',
    "ya4": 'yah',
    "yai1": 'iai',
    "yai2": 'yai',
    "yan1": 'ian',
    "yan2": 'yan',
    "yan3": 'yean',
    "yan4": 'yann',
    "yang1": 'iang',
    "yang2": 'yang',
    "yang3": 'yeang',
    "yang4": 'yanq',
    "yao1": 'iau',
    "yao2": 'yau',
    "yao3": 'yeau',
    "yao4": 'yaw',
    "ye1": 'ie',
    "ye2": 'ye',
    "ye3": 'yee',
    "ye4": 'yeh',
    "yi1": 'i',
    "yi2": 'yi',
    "yi3": 'yii',
    "yi4": 'yih',
    "yin1": 'in',
    "yin2": 'yn',
    "yin3": 'yiin',
    "yin4": 'yinn',
    "ying1": 'ing',
    "ying2": 'yng',
    "ying3": 'yiing',
    "ying4": 'yinq',
    "yo1": 'io',
    "yong1": 'iong',
    "yong2": 'yong',
    "yong3": 'yeong',
    "yong4": 'yonq',
    "you1": 'iou',
    "you2": 'you',
    "you3": 'yeou',
    "you4": 'yow',
    "yu1": 'iu',
    "yu2": 'yu',
    "yu3": 'yeu',
    "yu4": 'yuh',
    "yuan1": 'iuan',
    "yuan2": 'yuan',
    "yuan3": 'yeuan',
    "yuan4": 'yuann',
    "yue1": 'iue',
    "yue4": 'yueh',
    "yun1": 'iun',
    "yun2": 'yun',
    "yun3": 'yeun',
    "yun4": 'yunn',
    "za1": 'tza',
    "za2": 'tzar',
    "zai1": 'tzai',
    "zai3": 'tzae',
    "zai4": 'tzay',
    "zan1": 'tzan',
    "zan2": 'tzarn',
    "zan3": 'tzaan',
    "zan4": 'tzann',
    "zang1": 'tzang',
    "zang3": 'tzaang',
    "zang4": 'tzanq',
    "zao1": 'tzau',
    "zao2": 'tzaur',
    "zao3": 'tzao',
    "zao4": 'tzaw',
    "ze1": 'tze',
    "ze2": 'tzer',
    "ze3": 'tzee',
    "ze4": 'tzeh',
    "zei1": 'tzei',
    "zei2": 'tzeir',
    "zen1": 'tzen',
    "zen3": 'tzeen',
    "zen4": 'tzenn',
    "zeng1": 'tzeng',
    "zeng4": 'tzenq',
    "zha1": 'ja',
    "zha2": 'jar',
    "zha3": 'jaa',
    "zha4": 'jah',
    "zhai1": 'jai',
    "zhai2": 'jair',
    "zhai3": 'jae',
    "zhai4": 'jay',
    "zhan1": 'jan',
    "zhan3": 'jaan',
    "zhan4": 'jann',
    "zhang1": 'jang',
    "zhang3": 'jaang',
    "zhang4": 'janq',
    "zhao1": 'jau',
    "zhao2": 'jaur',
    "zhao3": 'jao',
    "zhao4": 'jaw',
    "zhe1": 'je',
    "zhe2": 'jer',
    "zhe3": 'jee',
    "zhe4": 'jeh',
    "zhei1": 'jei',
    "zhei4": 'jey',
    "zhen1": 'jen',
    "zhen3": 'jeen',
    "zhen4": 'jenn',
    "zheng1": 'jeng',
    "zheng3": 'jeeng',
    "zheng4": 'jenq',
    "zhi1": 'jy',
    "zhi2": 'jyr',
    "zhi3": 'jyy',
    "zhi4": 'jyh',
    "zhong1": 'jong',
    "zhong3": 'joong',
    "zhong4": 'jonq',
    "zhou1": 'jou',
    "zhou2": 'jour',
    "zhou3": 'joou',
    "zhou4": 'jow',
    "zhu1": 'ju',
    "zhu2": 'jwu',
    "zhu3": 'juu',
    "zhu4": 'juh',
    "zhua1": 'jua',
    "zhua3": 'joa',
    "zhuai1": 'juai',
    "zhuai3": 'joai',
    "zhuai4": 'juay',
    "zhuan1": 'juan',
    "zhuan3": 'joan',
    "zhuan4": 'juann',
    "zhuang1": 'juang',
    "zhuang4": 'juanq',
    "zhui1": 'juei',
    "zhui4": 'juey',
    "zhun1": 'juen',
    "zhun3": 'joen',
    "zhuo1": 'juo',
    "zhuo2": 'jwo',
    "zi1": 'tzy',
    "zi3": 'tzyy',
    "zi4": 'tzyh',
    "zong1": 'tzong',
    "zong3": 'tzoong',
    "zong4": 'tzonq',
    "zou1": 'tzou',
    "zou3": 'tzoou',
    "zou4": 'tzow',
    "zu1": 'tzu',
    "zu2": 'tzwu',
    "zu3": 'tzuu',
    "zu4": 'tzuh',
    "zuan1": 'tzuan',
    "zuan3": 'tzoan',
    "zuan4": 'tzuann',
    "zui3": 'tzoei',
    "zui4": 'tzuey',
    "zun1": 'tzuen',
    "zun3": 'tzoen',
    "zuo1": 'tzuo',
    "zuo2": 'tzwo',
    "zuo3": 'tzuoo',
    "zuo4": 'tzuoh',
    'xie': '.shie',
    'ne': '.ne',
    
}    

grpy = {v: k for k, v in table.items()}

if __name__ == "__main__":
    jsname = sys.argv[1]
    fname = jsname.split('.')[0]
    
    with open(jsname, encoding="utf-8") as gr, open(fname + "_py.js", 'w', encoding="utf-8") as out:
        for line in gr:
            parts = line.split(" ")
            if len(line) < 2 or line[0] == " " or parts[0] == "const" or line[0] == "`" or line[0] == "]":
                print(line, end="", file=out)
                continue
            try:
                py = grpy[parts[0]]
                print(py + " " + " ".join(parts[1:]), end="", file=out)
            except KeyError:
                print("Warning: {} not found in table.".format(parts[0]))
                print(line, end="", file=out)
            
