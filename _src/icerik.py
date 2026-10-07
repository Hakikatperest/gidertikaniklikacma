# -*- coding: utf-8 -*-
"""
Makale içerikleri — firma sahibinin ağzından (ghostwrite, kullanıcı 2026-10-07: "sen yaz, benim ağzımdan").
Üslup: samimi, dürüst, "siz" hitabı, yer yer :) — kutucuklar "Tavsiyemiz:", "Dikkat:", "Önemli:".

⛔ Uydurma vaka/rakam YOK ("geçen hafta X Mahallesi'nde…" yazma).
⛔ ONAYLI olmayan iddia yok: garanti, tecrübe yılı, ofis/adres, "ödeme iş bitince" → data.TEYITSIZ.
⛔ Fiyat RAKAMI yok (kullanıcı vermedi) → fiyatı belirleyen etkenler + "fiyat işe başlamadan söylenir".
İSKİ: kanalizasyon arıza/taşma hattı ALO 185 (7/24). Sınır kuralı: parsel bacası.

Metin içi bağlantı: [[yol|metin]] → "hizmet:<slug>" (aynı ilçenin o hizmet sayfası, ilçe yoksa hub),
                                     "ilce:<slug>" (ilçe sayfası) ya da düz göreli yol ("iletisim/").
"""

# ── İlçe makaleleri (2026-10-07) ─────────────────────────────────────────
# ulasim/gece/belediye/fiyat/acil/yakin + yerel[4 hizmet]. Sancaktepe = GBP konumu.
ILCE_METIN = {'kadikoy': {'ulasim': "Kadıköy'e sahil yolundan, D-100'den ya da Bağdat Caddesi'ne paralel ara yollardan geliyoruz; hangisinin o saatte akıp "
                       'akmadığına göre karar veriyoruz. Telefonda sokağı, bina adını ve kaçıncı kat olduğunuzu söylerseniz yeter. Moda ya da '
                       "Yeldeğirmeni'nde iseniz park durumunu da belirtin. Tıkanan yerin kısa bir videosunu atarsanız doğru makineyi baştan alıp "
                       'çıkıyoruz.',
             'gece': "Kadıköy gece de hareketli bir ilçe; çarşı ve Moda'daki kafe ve restoranlar kapanırken mutfak gideri tıkanan işletmeler bizi "
                     'gece yarısından sonra arayabiliyor. Konutlarda ise hafta sonu misafir kalabalığında tuvalet sorunları artıyor. 7/24 açığız; '
                     'gece gelirken apartmanı rahatsız etmemek için gürültülü makineyi en son çare olarak kullanıyoruz.',
             'belediye': "Kadıköy Belediyesi evinizdeki gidere ekip göndermez; İstanbul'da kanalizasyon şebekesi İSKİ'nin. Sokaktaki ana hat "
                         "taşıyorsa İSKİ ALO 185'i arayın. Fikirtepe gibi dönüşüm bölgelerinde bir ipucu: sorun komşu inşaattan sonra başladıysa ve "
                         'sokak rögarı normalse, tıkanıklık büyük ihtimalle sizin bina bağlantınızda; burası binanın sorumluluğunda ve bizim işimiz.',
             'fiyat': "Kadıköy'de tutarı belirleyen asıl şey binanın yaşı. Moda'daki eski bir apartmanda pik döküm kolon ve sıva altında kalmış "
                      "temizleme kapağı işi uzatabiliyor; Suadiye'deki yeni bir binada aynı tıkanıklık çok daha kısa sürüyor. Bu yüzden önce "
                      'bakıyoruz, gerekirse kamerayla görüyoruz, fiyatı işe başlamadan söylüyoruz.',
             'acil': "Kadıköy'ün eski apartmanlarında acil durum genelde bodrum ya da zemin katta yaşanıyor: kolon tıkandığında üst katların suyu en "
                     'alttaki dairenin tuvaletinden ya da yer süzgecinden geri geliyor. Arayınca önce apartmana su kullanımını kesmesini nasıl '
                     'duyuracağınızı, taşan klozetin musluğunu nasıl kapatacağınızı anlatıyoruz. Biz yolda olurken bu ilk adımlar hasarı küçültüyor.',
             'yakin': "Kadıköy'e en yakın tıkanıklık açma servisi hangisi diye soruyorsanız dürüst olalım: Kadıköy'de bir ofis ya da dükkân açmış "
                      "değiliz. Gün boyu Anadolu yakasının sokaklarında dolaşıyoruz ve Kadıköy'e ortalama 30 dakikada ulaşıyoruz. Göztepe, "
                      'Fenerbahçe ya da Kozyatağı fark etmez; o an ekibin nerede olduğuna göre tahmini süreyi arayınca açıkça söylüyoruz.',
             'yerel': {'tuvalet-tikanikligi-acma': "Kadıköy'ün eski apartmanlarında tuvalet tıkanıklığı çoğu zaman klozetin değil, klozetten çıkan "
                                                   'borunun kolona bağlandığı noktanın sorunu. Eski binalarda bu bağlantı dar ve keskin; ıslak '
                                                   'mendil ve kâğıt havlu burada takılıyor. Klozeti sökmeden önce spiralle bu noktayı açmayı '
                                                   'deniyoruz, sorun tekrarlıyorsa kamerayla bağlantının içine bakıyoruz.',
                       'lavabo-tikanikligi-acma': "Caferağa ve Osmanağa'daki eski binalarda banyo lavabosu genelde duvara gömülü eski bir boruyla "
                                                  'bağlı. Saç, sabun ve diş macunu kalıntısı sifonun hemen arkasındaki bu boruda kireçle birleşip '
                                                  'sertleşiyor. Önce sifonu söküp temizliyoruz, yetmezse ince spiralle duvardaki boruya giriyoruz; '
                                                  'seramiği kırmadan açmak her zaman ilk tercihimiz.',
                       'banyo-gideri-acma': "Kadıköy'de eski banyoları yenilenmiş dairelerde duşakabin altındaki yer süzgecinin eğimi genelde "
                                            'yetersiz kalıyor; su yavaş gidiyor, saç ve sabun birikintisi süzgecin altında hızla toplanıyor. Uzun '
                                            'süre böyle kalınca su alt kattaki dairenin tavanına sızabiliyor. Süzgeci açıp hattı temizliyor, sorun '
                                            'eğimdeyse bunu size açıkça söylüyoruz.',
                       'mutfak-gideri-acma': "Kadıköy çarşısı ve Moda'da yoğun çalışan kafe ve restoranların mutfak gideri, evlerden çok daha hızlı "
                                             'yağlanıyor. Konutlarda ise eski binaların ortak mutfak kolonunda yıllardır biriken yağ alt katlarda '
                                             'evyeden geri gelme yapıyor. Dükkânda yağ tutucunun durumuna, apartmanda kolonun temizleme kapağına '
                                             'bakıp basınçlı su ya da spiralle açıyoruz.'}},
 'uskudar': {'ulasim': "Üsküdar'a gelirken iki ana yol var: sahil boyunca Boğaz kıyısı ya da D-100'den Altunizade ve Kısıklı üstünden. Kuzguncuk "
                       "veya Çengelköy'de oturuyorsanız evin sahil yolundan mı yoksa yukarıdaki yokuştan mı ulaşıldığını söylemeniz çok işe yarıyor. "
                       'Ahşap ev ya da yalıysa bunu da belirtin; ekipmanı ona göre hazırlıyoruz.',
             'gece': "Üsküdar'da gece çağrılarının önemli bir kısmı Çamlıca yamacındaki büyük sitelerden ve Altunizade'deki bloklardan geliyor; bir "
                     'dairedeki sorun bütün kolonu etkilediğinde site yönetimi gece de bizi arıyor. Boğaz kıyısındaki evlerde ise lodoslu gecelerde '
                     'gider ağırlaşabiliyor. 7/24 çalışıyoruz, gece ulaşabilecek ekibin konumunu arayınca söylüyoruz.',
             'belediye': 'Üsküdar Belediyesi evinizdeki gidere ekip göndermez; şehirdeki kanalizasyon şebekesinden İSKİ sorumlu. Sokak hattı '
                         "taşıyorsa İSKİ ALO 185'e haber verin. Boğaz kıyısındaki evler için ufak bir ayrım: lodoslu havada sokaktaki rögarlar da "
                         'dolu görünüyorsa sorun ana hatta olabilir; sokak normal ama sizin bahçe rögarınız doluysa tıkanıklık parsel tarafında '
                         'demektir.',
             'fiyat': "Üsküdar'da işin bedelini çoğu zaman hatta ulaşmanın ne kadar zor olduğu belirliyor. Kuzguncuk'taki bir ahşap evde dar kat "
                      "aralarında çalışmak, Ünalan'daki bir sitede bodrumdaki temizleme kapağından girmekle aynı iş değil. Önce yerinde bakıyor, "
                      'gerekiyorsa kamerayla hattı görüyor ve ne yapacağımızı, ne tutacağını işe başlamadan söylüyoruz.',
             'acil': "Üsküdar'da acil durumun yerel bir yüzü var: eski ahşap evlerde taşan su döşemenin altına çok hızlı işliyor ve kalıcı hasar "
                     'bırakabiliyor. Bu yüzden telefonda ilk iş ana vanayı ya da klozetin ara musluğunu nerede bulacağınızı tarif ediyoruz. Havlu ve '
                     'kovayla suyu tahta zeminden uzak tutmanızı da rica ediyoruz.',
             'yakin': "Üsküdar'a yakın bir servis arayanlara açık cevabımız şu: Üsküdar'da bir dükkân ya da tabela beklemeyin, biz Anadolu yakasında "
                      "araçla sahada dolaşan bir ekibiz. Bulgurlu, Selimiye ya da Beylerbeyi'ne ortalama 30 dakikada ulaşıyoruz. Sahil yolu "
                      'kilitliyse bu süre uzayabilir; aradığınızda o anki gerçek tahmini veriyoruz.',
             'yerel': {'tuvalet-tikanikligi-acma': 'Sonradan kat çıkılmış Üsküdar binalarında alt katlardaki tuvalet sık tıkanıyor, çünkü alttaki '
                                                   "eski boru üst katlardan gelen yükü taşıyacak çapta değil. Kuzguncuk'un eski evlerinde ise bazı "
                                                   'tuvaletler hâlâ alaturka ve sifonu derin. Alaturkada spiralle dikkatli çalışıyor, klozetlerde '
                                                   'ise önce dirseği açıp sonra kolona doğru ilerliyoruz.',
                       'lavabo-tikanikligi-acma': "Üsküdar'ın eski evlerinde banyo lavabosu sifonları çoğu zaman metal ve içi kireçle kaplanmış; saç "
                                                  've sabun bu pürüzlü yüzeye çok kolay tutunuyor. Sifonu söküp temizlemek çoğu zaman yetiyor ama '
                                                  'boru duvara girdikten sonra da daralmışsa ince spiral kullanıyoruz. Gerekirse eski sifonu '
                                                  'değiştirmeyi öneriyor, kararı size bırakıyoruz.',
                       'banyo-gideri-acma': 'Çamlıca yamacındaki sitelerde ve Altunizade bloklarında küvet ile duş gideri genelde aynı yatay hatta '
                                            'birleşiyor; saç ve sabun birikintisi bu birleşimde toplanıyor. Ahşap evlerde ise yer süzgecinden geri '
                                            'gelen su döşeme tahtasına işliyor. Süzgeci ve küvet sifonunu açıp hattı spiralle temizliyor, sızıntı '
                                            'izi varsa size gösteriyoruz.',
                       'mutfak-gideri-acma': "Üsküdar'ın Selimiye ve Salacak tarafındaki eski apartmanlarında mutfak kolonu yıllanmış ve içi yağla "
                                             'kalınlaşmış durumda; alt katta evye su tutmaya başlıyorsa sorun çoğu zaman kolonda. Çarşıdaki lokanta '
                                             've fırınlarda ise yağ ve un hamuru gideri ağırlaştırıyor. Kolonun temizleme kapağından basınçlı suyla '
                                             'girerek yağı söküyoruz.'}},
 'atasehir': {'ulasim': "Ataşehir'e D-100 ve TEM'in arasından giriyoruz; Kozyatağı, Kayışdağı Caddesi ya da Ataşehir Bulvarı'ndan hangisi açıksa "
                        'oradan. Telefonda site adını, blok harfini ve kapı numarasını söylemeniz bizim için en önemli bilgi; büyük sitelerde doğru '
                        'bloğu bulmak bazen yoldan uzun sürüyor :) Güvenliğe gelişimizi haber verirseniz kapıda beklemiyoruz.',
              'gece': "Ataşehir'de gece çağrıları genelde büyük sitelerden geliyor; akşam yemeğinden sonra çalıştırılan bulaşık makineleri mutfak "
                      'kolonunu zorladığında sorun gece yarısı alt katlarda patlak veriyor. Rezidanslarda ise teknik ekip gece çalışmadığı için '
                      'doğrudan bizi arıyorlar. Hafta sonu da dahil 7/24 açığız, telefonu her saatte açıyoruz.',
              'belediye': "Ataşehir Belediyesi evinizdeki gidere ekip göndermez; İstanbul'un kanalizasyon şebekesi İSKİ'ye ait. Caddedeki ana hattan "
                          'taşma varsa İSKİ ALO 185 numarası 7/24 açık. Büyük sitelerde dikkat edilmesi gereken nokta şu: bloklardan çıkıp site '
                          "içinde dolaşan ortak hat İSKİ'nin değil sitenin. Site içindeki rögar taşıyorsa önce yönetime haber verin.",
              'fiyat': "Ataşehir'de fiyatı asıl ayıran soru, tıkanıklığın daire içinde mi yoksa sitenin ortak hattında mı olduğu. Bir daire sifonu "
                       'ile bir sitenin bloklar arasındaki ortak hattı aynı emeği istemiyor. Kamerayla hattın neresinde olduğuna bakıyor, yönetimle '
                       'konuşulması gerekiyorsa bunu belirtiyor ve tutarı onayınızı almadan önce söylüyoruz.',
              'acil': 'Yüksek bloklu Ataşehir sitelerinde acil durum genelde zemin ve birinci katta: kolon tıkandığında yirmi katın suyu en alttaki '
                      'dairenin yer süzgecinden taşıyor. Telefonda önce yönetimin ya da güvenliğin apartmana duyuru yapmasını, sizin de taşan yerin '
                      'vanasını kapatmanızı istiyoruz. Bu süre içinde yoldayız.',
              'yakin': "Ataşehir'de en yakın servisi arıyorsanız bilmeniz gereken şu: ilçede bir büromuz bulunmuyor, ekibimiz Anadolu yakasının "
                       "içinde sahada geziyor. Bu sayede İçerenköy, Barbaros ya da Ferhatpaşa'daki bir adrese ortalama 30 dakikada geliyoruz, çoğu "
                       'zaman da yakındaki bir işten doğrudan size dönüyoruz. Kozyatağı kavşağının durumuna göre bu süre değişebiliyor; aradığınızda '
                       'tahminimizi açıkça söylüyoruz.',
              'yerel': {'tuvalet-tikanikligi-acma': "Ataşehir'in yeni sitelerinde gömme rezervuarlı asma klozetler yaygın; sifonu duvarın içinde "
                                                    'kaldığı için tıkanıklığa dışarıdan ulaşmak zor. Klozeti sökmeden, ağızdan uygun spiralle '
                                                    "giriyoruz. Ferhatpaşa ve Esatpaşa'daki eski binalarda ise tuvalet borusu farklı çapta bir hatta "
                                                    'bağlandığı için tıkanma bu geçiş noktasında oluyor.',
                        'lavabo-tikanikligi-acma': 'Ataşehir dairelerinde tezgâhlı, çanak tipi banyo lavaboları çok; dekoratif sifonları dar ve saç, '
                                                   'diş macunu ile sabun çok kısa sürede bu darlığı kapatıyor. Sifonu söküp temizliyor, tezgâhın '
                                                   'arkasında duvara giren bağlantıyı kontrol ediyoruz. Üst kat dairelerde sorun bazen lavabo değil, '
                                                   'banyodaki yatay hattın sarkması oluyor.',
                        'banyo-gideri-acma': "Ataşehir'deki sitelerde duşakabin yer süzgeçleri çoğu zaman ince ızgaralı ve sığ; saç ve sabun "
                                             'birikintisi buradan aşağı inince yatay hatta toplanıyor. Zemin yalıtımı iyi değilse su alt kata iniyor '
                                             've komşunun tavanında leke olarak çıkıyor. Süzgeci açıp hattı temizliyor, alt kata sızma varsa '
                                             'kamerayla kaynağını arıyoruz.',
                        'mutfak-gideri-acma': "Ataşehir'deki yüksek bloklarda mutfak kolonu çok uzun ve yağ en alttaki dirseğe toplanıyor; "
                                              'tıkanıklık genelde zemin kattaki dairenin evyesinden geri tepme olarak görünüyor. Finans Merkezi '
                                              'çevresindeki restoran ve kafelerde ise yoğun öğle servisi yağ tutucuyu hızla dolduruyor. Bodrumdaki '
                                              'temizleme kapağını açıp yağı basınçlı suyla parçalıyoruz.'}},
 'umraniye': {'ulasim': "Ümraniye'ye TEM, Alemdağ Caddesi ya da Kuzey Marmara Otoyolu bağlantılarından ulaşıyoruz; hangi yolun açık olduğu saatten "
                        "saate değişiyor. Telefonda mahalleyi, caddeyi ve binanın bir yer işaretini söylemeniz yardımcı oluyor. Dudullu'da bir iş "
                        'yeriyseniz firma adını ve giriş kapısını belirtin, konutsa bina adını ve kat bilgisini verin; video da çok işe yarar.',
              'gece': "Ümraniye'de gece gelen çağrılar ikiye ayrılıyor: Çakmak ve Madenler gibi kalabalık mahallelerde aile evleri ile Dudullu ve "
                      "Şerifali'de gece vardiyası çalışan iş yerleri. Üretimi durmasın diye iş yerleri gece de bizi çağırabiliyor. 7/24 hizmet "
                      'veriyoruz; gece geldiğimizde komşuları uyandırmamak için mümkün olduğunca sessiz çalışıyoruz.',
              'belediye': "Ümraniye Belediyesi evinizdeki gidere ekip göndermez, iş yerleri için de durum aynı; şebeke İSKİ'nin sorumluluğunda. "
                          "Taşan sokak hattıysa bildirimi İSKİ ALO 185'e yapın. Ümraniye'ye özgü bir ipucu: bitişik eski binalarda bağlantılar bazen "
                          'ortak geçiyor; komşu binanın rögarı da doluysa sorun ortak bağlantıda olabilir.',
              'fiyat': "Ümraniye'de ücreti en çok binanın yıllar içinde nasıl büyüdüğü değiştiriyor. Kat çıkılmış eski bir binada sıva altında "
                       'kalmış kolon kapağına ulaşmak ve farklı çaptaki boruların geçişini açmak, yeni bir sitedeki daire sifonundan çok daha uzun '
                       'sürüyor. Bunu yerinde görüp size söylüyor, onay almadan makineyi çalıştırmıyoruz.',
              'acil': "Ümraniye'de acil durumun en çok görüldüğü yer giriş katları ve dükkânlar; üstteki kat sayısı arttıkça alttaki tuvaletten geri "
                      "gelen su da artıyor. Dudullu'daki iş yerlerinde ise tıkanıklık üretimi ya da yemekhaneyi durdurabiliyor. Arayınca önce hangi "
                      'vanayı kapatacağınızı, apartmanın su kullanımını nasıl durduracağınızı anlatıyoruz.',
              'yakin': "Ümraniye için en yakın tıkanıklık açma servisini arıyorsanız şunu baştan söyleyelim: Ümraniye'de bir şubemiz yok; Google "
                       "Haritalar'daki kaydımız komşu ilçe Sancaktepe'de. Anadolu yakasının içinde sahada çalışıyoruz; Atakent, Tantavi ya da Yukarı "
                       "Dudullu'ya ortalama 30 dakikada varıyoruz. TEM'in yoğun olduğu saatlerde bu süre uzayabilir, aradığınızda gerçek tahmini "
                       'veriyoruz.',
              'yerel': {'tuvalet-tikanikligi-acma': "Çakmak, Ihlamurkuyu ve Madenler'deki kat eklenmiş binalarda giriş kattaki tuvalet, binanın en "
                                                    'zayıf noktası: üstten gelen her şey buradaki dar borudan geçmek zorunda. Hâlâ alaturka tuvalet '
                                                    'kullanan evler de var. Klozet ya da alaturka fark etmeden önce spiralle açıyor, sık '
                                                    'tekrarlıyorsa kamerayla bina bağlantısına bakıyoruz.',
                        'lavabo-tikanikligi-acma': "Ümraniye'nin yeni sitelerinde banyo lavabosunun plastik sifonu çoğu zaman montajda gevşek "
                                                   'bırakılıyor ve sarkıyor; saç ile sabun bu sarkan bölümde birikiyor. Eski binalarda ise sifonun '
                                                   'arkasındaki boru kireçle daralmış. Sifonu söküp temizliyor, gerekiyorsa doğru eğimle yeniden '
                                                   'bağlıyor, duvar içine spiralle giriyoruz.',
                        'banyo-gideri-acma': "Ümraniye'deki eski binaların banyolarında yer süzgeci çoğu zaman sonradan yapılmış şapın altında "
                                             'kalmış, eğimi de kendiliğinden ters dönmüş durumda. Duşta biriken su süzgece değil kenarlara gidiyor, '
                                             'saç ve kum hattı tıkıyor. Süzgeci ve küvet gideri hattını spiralle açıyor, alt kata sızma şikâyeti '
                                             'varsa kaynağını bulmaya çalışıyoruz.',
                        'mutfak-gideri-acma': "Dudullu ve Şerifali'deki iş yerlerinin yemekhanelerinde evye hatları kısa sürede yağ bağlıyor; yağ "
                                              'tutucu yoksa ya da bakımı aksadıysa hat birkaç haftada daralıyor. Konutlarda ise bulaşık makinesi '
                                              'hortumunun sifona yanlış bağlanması sık. Evyeyi ve bağlantıyı düzeltiyor, kolonda yağ varsa basınçlı '
                                              'suyla temizliyoruz.'}},
 'beykoz': {'ulasim': "Beykoz'a çoğunlukla Fatih Sultan Mehmet Köprüsü bağlantısından Kavacık üzerinden ya da Boğaz sahil yolundan ulaşıyoruz. Riva "
                      "veya Polonezköy'deyseniz orman yolundan gideceğimiz için konumunuzu WhatsApp'tan göndermeniz şart gibi. Villa sitesindeyseniz "
                      'site adını ve güvenlik kulübesini, yalıdaysanız sahil yolundan girişi tarif edin.',
            'gece': "Beykoz'da gece çağrıları kıyı ile iç kesim arasında farklılaşıyor. Kavacık apartmanlarından gelen gece çağrıları klasik tuvalet "
                    "ve mutfak tıkanıklığı oluyor; Riva ve Polonezköy'deki hafta sonu evlerinde ise misafir kalabalığı fosseptiği ya da bahçe "
                    'hattını zorluyor. 7/24 açığız ama gece orman yolundan geleceğimiz için süreyi arayınca söylüyoruz.',
            'belediye': "Beykoz Belediyesi evinizdeki gidere ekip göndermez; şehrin kanalizasyonu İSKİ'ye bağlı. Yolda taşan bir ana hat "
                        "görüyorsanız İSKİ ALO 185 doğru adres. Beykoz'da bir ayrım önemli: Riva ya da köy mahallelerinde eviniz şebekeye değil "
                        'fosseptiğe bağlıysa, sorun çoğu zaman tıkanıklık değil dolu fosseptik olabiliyor; bunu ayırt etmeye yardım ediyoruz.',
            'fiyat': "Beykoz'da işin tutarına yön veren iki şey var: yolun uzunluğu ve bahçe hattının uzunluğu. Kavacık'taki bir dairede sifon açmak "
                     "ile Polonezköy'deki bir villada uzun bahçe hattında kök kesmek aynı iş değil. Yerinde bakıyoruz, kök varsa kamerayla "
                     'gösteriyoruz ve yapılacak işi, bedeliyle birlikte başlamadan önce size söylüyoruz.',
            'acil': "Beykoz'un villa ve yalılarında acil durum çoğu zaman bodrum katta yaşanıyor: ana çıkış tıkandığında üstteki banyoların suyu en "
                    'alttaki banyodan taşıyor. Telefonda önce evdeki herkesin musluk ve rezervuar kullanmayı bırakmasını, taşan banyonun vanasının '
                    'kapanmasını istiyoruz. Yolumuz uzunsa bu sürede hasarı nasıl sınırlayacağınızı adım adım anlatıyoruz.',
            'yakin': "Beykoz'da en yakın servis kim sorusuna kestirme bir cevap vermeyelim: ilçede bir yerimiz yok, ekibimiz Anadolu yakasında "
                     'sahada çalışıyor. Kavacık, Kanlıca ve Çubuklu gibi kıyıya yakın yerlere ortalama 30 dakikada ulaşıyoruz. Riva ya da Anadolu '
                     'Kavağı gibi uzak noktalar biraz daha uzun sürüyor; aradığınızda bunu açıkça söylüyoruz.',
            'yerel': {'tuvalet-tikanikligi-acma': "Beykoz'un villalarında bodrum ve zemin kattaki tuvaletler ana çıkışın hemen üstünde kaldığı için "
                                                  'tıkanıklık önce burada kendini gösteriyor; üst kattaki banyoların suyu buradan geri geliyor. Eski '
                                                  'yalılarda ise yenilenmiş klozet eski bir boruya bağlanmış; geçişte darlık var. Spiral makineyle '
                                                  'açtıktan sonra, sorun dönüp duruyorsa kamerayı eski-yeni boru geçişine sokuyoruz.',
                      'lavabo-tikanikligi-acma': "Beykoz'un Boğaz evlerinde banyo lavaboları çoğu zaman antika ya da özel tasarım; sifonları "
                                                 'standart değil ve sökerken dikkat istiyor. Saç ve sabunun yanı sıra kıyı nemiyle artan kireç de '
                                                 'sifonu daraltıyor. Lavaboya zarar vermeden sifonu söküyor, temizliyor ve duvardaki bağlantıya ince '
                                                 'spiralle giriyoruz.',
                      'banyo-gideri-acma': 'Beykoz villalarında çok sayıda banyo var ve her birinde duş ve yer süzgeci aynı ana hatta iniyor; saç ve '
                                           'sabun ana hatta birleştiğinde tüm banyolar yavaş akmaya başlıyor. Riva tarafındaki yazlık evlerde ise '
                                           'denizden gelen kum yer süzgecini dolduruyor. Süzgeçleri ve ana hattı spiralle temizliyoruz.',
                      'mutfak-gideri-acma': "Beykoz'da Anadolu Hisarı, Kanlıca ve Çubuklu sahilindeki balık lokantalarında mutfak gideri yağ ve "
                                            'balık artığıyla hızlı doluyor. Villalarda ise evye suyu sokağa varmadan bahçede epey yol aldığı için '
                                            'yağ bahçede soğuyup birikiyor. Evyeden başlayıp gerekirse bahçe hattının sonuna kadar basınçlı suyla '
                                            'ilerliyoruz.'}},
 'cekmekoy': {'ulasim': "Çekmeköy'e Alemdağ Caddesi, Şile yolu ya da Kuzey Marmara Otoyolu bağlantısından geliyoruz. İlçe merkezindeki sitelerde "
                        'blok ve kapı numarası yeterli; Ömerli, Reşadiye veya Sultançiftliği tarafındaysanız konum paylaşmanız işimizi çok '
                        "kolaylaştırıyor. Taşdelen'deki villa sitelerinde güvenlik kulübesine adınızı bildirirseniz kapıda vakit kaybetmiyoruz.",
              'gece': "Çekmeköy'de gece çağrılarının çoğu yeni sitelerden ve villalardan geliyor; özellikle hafta sonları kalabalık sofralardan "
                      'sonra mutfak ve tuvalet giderleri zorlanıyor. Ömerli tarafındaki evlerde ise yağmurlu gecelerde bahçe rögarları doluyor. 7/24 '
                      'çalışıyoruz; gece köy mahallelerine gelirken yolu tarif etmeniz bize çok zaman kazandırıyor.',
              'belediye': 'Çekmeköy Belediyesi evinizdeki gidere ekip göndermez; şebekeyi işleten kurum İSKİ. Mahallenizdeki ana hat dışarı '
                          "taşıyorsa İSKİ ALO 185'i tuşlayın. Ömerli havzasındaki evlerde şunu bilmekte fayda var: eviniz fosseptikle çalışıyorsa "
                          'sorunun bir kısmı tıkanıklık değil fosseptiğin dolması olabilir; hangisi olduğunu yerinde ayırt ediyoruz.',
              'fiyat': "Çekmeköy'de fiyat çoğunlukla bahçe hattının ne kadar uzun olduğuna ve içinde ne bulduğumuza bağlı. İlçe merkezindeki bir "
                       "dairede evye açmak kısa sürerken, Taşdelen'de uzun bir bahçe hattında kök ya da inşaat harcıyla uğraşmak ayrı bir iş. "
                       'Kamerayla görüp ne gerektiğini anlatıyoruz, tutarı da işe başlamadan söylüyoruz.',
              'acil': 'Çekmeköy villalarında acil durum genelde bodrum katta yaşanıyor; bahçe hattı tıkandığında evin tüm suyu en alttaki süzgeçten '
                      'taşıyor. Yağmurlu havalarda bahçe rögarı da dolup eve doğru geri gelebiliyor. Arayınca önce su kullanımını durdurmanızı ve '
                      'bodrumdaki eşyaları kaldırmanızı söylüyoruz; bu sırada yola çıkıyoruz.',
              'yakin': "Çekmeköy'de size en yakın tıkanıklık açıcıyı arıyorsanız dürüst cevabımız şu: ilçede bir dükkânımız bulunmuyor; araçtaki "
                       "ekipmanla Taşdelen, Mehmet Akif ya da Hamidiye'ye ortalama 30 dakikada ulaşıyoruz. Ömerli ve köy mahalleleri biraz daha uzak "
                       'kalıyor; aradığınızda o anki tahmini süreyi açıkça söylüyoruz.',
              'yerel': {'tuvalet-tikanikligi-acma': "Çekmeköy'ün yeni sitelerinde ilk yıllarda tuvalet tıkanıklığına inşaattan kalan harç parçaları "
                                                    'sebep oluyor; klozetten inen hatta bir daralma oluşuyor ve ıslak mendil burada takılıyor. '
                                                    'Villalarda bodrum tuvaleti ana çıkışın dibinde olduğu için ilk sinyali o veriyor. Spiralle açıp '
                                                    'gerekirse kamerayla harç kalıntısına bakıyoruz.',
                        'lavabo-tikanikligi-acma': "Çekmeköy'ün yeni yapılmış dairelerinde banyo lavabosu sifonları çoğunlukla plastik ve montajda "
                                                   'boşluk bırakılmış; saç ve diş macunu bu boşlukta birikiyor. Ömerli ve köy mahallelerinde ise '
                                                   'kuyu ya da sert şebeke suyuyla kireç birikimi fazla. Sifonu söküp temizliyor, kireçlenmiş '
                                                   'bağlantıyı spiralle açıyoruz.',
                        'banyo-gideri-acma': 'Çekmeköy villalarında duş, küvet ve yer süzgecinden gelen sular katın altında tek boruda buluşuyor; '
                                             'saç ile sabun da tam bu buluşma noktasında kalıyor. Bahçeden gelen toprak ve kum da ayakkabıyla '
                                             'taşınıp yer süzgecine doluyor. Süzgeçleri temizliyor, ana hattı spiralle açıyor, sızma varsa kaynağını '
                                             'kamerayla arıyoruz.',
                        'mutfak-gideri-acma': "Çekmeköy'deki villalarda mutfak gideri uzun bir bahçe hattına bağlı; yağ bu hatta soğuyup duvar gibi "
                                              'birikiyor ve evye yavaş akmaya başlıyor. Sitelerde ise bulaşık makinesi bağlantısının yanlış '
                                              'takılması sık görülüyor. Evye sifonunu ve bağlantıyı düzeltiyor, bahçedeki hattı yüksek basınçlı '
                                              'suyla baştan sona yıkıyoruz.'}},
 'sile': {'ulasim': "Şile'ye Şile yolu üzerinden, Çekmeköy ve Ömerli'yi geçerek ormanın içinden ulaşıyoruz; Ağva için ayrıca sahil yönüne dönüyoruz. "
                    "Yazlık sitedeyseniz site adı ve blok, köy mahallesindeyseniz konum paylaşımı şart. Ağva'da dere kenarındaki bir evdeyseniz "
                    "hangi derenin, Göksu'nun mu Yeşilçay'ın mı kenarında olduğunuzu söyleyin; ekipmanı ona göre hazırlıyoruz.",
          'gece': "Şile'de gece ve hafta sonu çağrıları mevsime göre çok değişiyor. Yaz aylarında yazlıklar ve pansiyonlar dolduğunda giderler "
                  'kapasitesinin üstünde çalışıyor ve sorunlar gece de çıkabiliyor; kışın ise evlerin çoğu boş olduğu için çağrı azalıyor. 7/24 '
                  'açığız; ancak gece Şile yoluna çıkmak zaman aldığı için süreyi arayınca netleştiriyoruz.',
          'belediye': "Şile Belediyesi evinizdeki gidere ekip göndermez; Şile dahil bütün İstanbul'da kanalizasyon İSKİ'nin. Yoldaki rögar dışarı su "
                      "veriyorsa İSKİ ALO 185 ile görüşün. Şile'de bilmeniz gereken ayrım: köy mahallelerinde ve bazı yazlıklarda ev şebekeye değil "
                      'fosseptiğe bağlı olabiliyor; giderler ağırsa önce fosseptiğin dolu olup olmadığına bakmak gerekiyor.',
          'fiyat': "Şile'de ücreti yol mesafesi ile işin cinsi birlikte belirliyor. Uzun yolu gelip bir pansiyonda kolon açmak ile bir yazlığın "
                   'bahçe hattında kum ve kökle uğraşmak farklı emek istiyor. Yola çıkmadan önce telefonda ne olabileceğini konuşuyor, yerinde '
                   'gördükten sonra tutarı işe başlamadan söylüyoruz.',
          'acil': "Şile'de acil durum çoğu zaman sezon başında yaşanıyor: aylarca kapalı kalan bir yazlık açıldığında kireçlenmiş hatlar ilk yoğun "
                  'kullanımda taşıyor. Fosseptikli evlerde ise dolu çukur tüm giderleri geri tepiyor. Telefonda ilk iş evde kimsenin musluk '
                  'açmamasını ve taşan noktanın vanasının kapatılmasını rica ediyoruz; yol uzun olduğu için bu adımlar çok önemli.',
          'yakin': "Şile'de en yakın tıkanıklık açma servisini arayanlara açık konuşalım: Şile'de bir yerimiz yok, Anadolu yakasının iç kesimlerinde "
                   "sahada çalışıyoruz ve Şile bizim için gerçekten uzun bir yol. Balibey, Kumbaba ya da Ağva'ya gelirken başka ilçelerde verdiğimiz "
                   'ortalama süre burada geçerli değil; aradığınızda gerçekçi süreyi açıkça söylüyoruz.',
          'yerel': {'tuvalet-tikanikligi-acma': "Şile'nin yazlıklarında tuvalet tıkanıklığı en çok sezonun ilk haftalarında görülüyor; aylarca "
                                                'kullanılmayan klozetin sifonunda kireç ve tortu kurumuş, ilk yoğun kullanımda kâğıt bu darlığa '
                                                'takılıyor. Fosseptikli evlerde ise tuvalet ağır akıyorsa önce çukurun durumuna bakıyoruz. Klozeti '
                                                'sökmeden spiralle açıyor, gerekirse kamerayla bahçeye çıkan hattı izliyoruz.',
                    'lavabo-tikanikligi-acma': "Şile'nin pansiyon ve yazlıklarında banyo lavabosu sifonu kışın kuruyor, kireç ve sabun kalıntısı "
                                               'sertleşiyor; yazın ilk kullanımda saç bu sertleşmiş tabakaya tutunuyor. Deniz havası metal sifonları '
                                               'da çabuk paslandırıyor. Sifonu söküp temizliyor, paslıysa değiştirmeyi öneriyor ve duvardaki boruya '
                                               'spiralle giriyoruz.',
                    'banyo-gideri-acma': "Şile'de denize giren herkes kumla eve dönüyor :) Duşta yıkanan kum yer süzgecinin altına ve duş hattının "
                                         'dirseğine çöküyor, saçla birleşince su akmaz oluyor. Sahile yakın yazlıklarda bu çok yaygın. Süzgeci '
                                         'açıyor, kumu ve saçı spiralle çıkarıyor, hattı basınçlı suyla yıkıyoruz.',
                    'mutfak-gideri-acma': "Şile çarşısındaki balık lokantaları ve Ağva'daki dere kenarı restoranlarında yaz yoğunluğunda mutfak "
                                          'gideri çok hızlı yağlanıyor. Yazlıklarda ise kalabalık aile sofralarından sonra evye ve bulaşık makinesi '
                                          'gideri tıkanıyor. Evyeyi açıyor, gerekiyorsa yağ tutucuyu ve dükkânın arkasındaki bağlantıyı basınçlı '
                                          'suyla yıkıyoruz; sezon ortasında işinizi durdurmamaya çalışıyoruz.'}},
 'maltepe': {'ulasim': "Maltepe'ye genelde D-100 ya da sahil yolundan iniyoruz; yamaç mahallelere gitmemiz gerekirse E-5'in kuzeyinden dolaşıyoruz. "
                       'Bize mahalleyi, sokağı ve sitedeyseniz blok adını söylemeniz yeterli. Telefonla bir de kısa video atarsanız suyun nerede '
                       'durduğunu görüp makineyi ona göre seçiyoruz; böylece kapıda bir de araca dönmek zorunda kalmıyoruz.',
             'gece': "Maltepe'de gece çağrılarının çoğu sahil tarafındaki eski apartmanlardan geliyor; akşam yemeğinden sonra bulaşık, çamaşır ve "
                     'banyo aynı saate denk gelince yaşlı kolon yetişemiyor. Hafta sonları da dolgu alanındaki etkinlik günlerinde sahil yolu '
                     'kalabalık oluyor, ona göre rota çiziyoruz. Hizmetimiz 7/24; gece yarısı aradığınızda karşınıza telesekreter değil, '
                     'konuşabileceğiniz biri çıkıyor.',
             'belediye': "Maltepe Belediyesi evinizdeki gidere ekip göndermez; İstanbul'da kanalizasyon İSKİ'nin. Sokaktaki ana hat taşıyorsa doğru "
                         'adres İSKİ ALO 185. Ayırt etmek için şuna bakın: sitenizin ya da binanızın bahçe rögarı doluyken sokaktaki rögar normal '
                         "akıyorsa sorun sizin parselinizde, bize düşüyor; sokak rögarından da su çıkıyorsa İSKİ'yi arayın.",
             'fiyat': "Maltepe'de fiyatı en çok belirleyen şey tıkanıklığın daire içinde mi yoksa eski kolonda mı olduğu. Bir sifonu açmakla "
                      "İdealtepe'deki yarım asırlık bir pik kolonu temizlemek aynı iş değil. Gelip kamerayla bakıyoruz, sebebi görüyoruz ve fiyatı "
                      'işe başlamadan söylüyoruz; siz onay vermeden makineyi çalıştırmıyoruz.',
             'acil': "Maltepe'nin eski sahil apartmanlarında acil durum genelde alt katta yaşanıyor: üst katlardan inen su kolonda takılınca zemin "
                     'kattaki tuvaletten ya da süzgeçten geri çıkıyor. Böyle bir durumda telefonda önce binadakilere suyu kesmeleri için nasıl haber '
                     'vereceğinizi ve hangi vanayı kapatacağınızı anlatıyoruz, sonra yola çıkıyoruz.',
             'yakin': "Maltepe'ye en yakın tıkanıklık açma servisi sorusunu soranlara açık söyleyelim: ilçede bir dükkân açıp beklemiyoruz, ekibimiz "
                      'Anadolu yakasının sokaklarında sahada çalışıyor. İdealtepe, Altıntepe ya da Başıbüyük fark etmez, kapınıza ortalama 30 '
                      "dakikada geliyoruz. D-100'ün tıkalı olduğu saatlerde bu uzayabilir; telefonda size gerçekçi bir saat veriyoruz.",
             'yerel': {'tuvalet-tikanikligi-acma': "Maltepe'de tuvalet tıkanıklığı en çok eski sahil apartmanlarının zemin ve bodrum katlarında "
                                                   'karşımıza çıkıyor. Klozetten geçen ıslak mendil, yaşlı pik kolonun dibindeki daralmada takılıyor '
                                                   've üst katların suyu alt kattaki tuvaletten geri geliyor. Bu durumda klozeti zorlamak işe '
                                                   'yaramıyor; kolonun temizleme kapağından spiral makineyle girip hattı açıyoruz.',
                       'lavabo-tikanikligi-acma': "Maltepe'nin yenilenmiş dairelerinde banyo lavabosu genelde şık ama sifonu dar, kısa bir şişe "
                                                  'sifon oluyor. Saç, sabun artığı ve diş macunu bu dar sifonda birikip suyu ağırlaştırıyor; sahil '
                                                  'tarafının kireçli suyu da üstüne biniyor. Sifonu söküp temizliyor, sorun daha içerideyse duvara '
                                                  'giden hatta ince spiral veriyoruz.',
                       'banyo-gideri-acma': 'Gülsuyu ve Gülensu gibi yamaç mahallelerdeki kat eklenmiş binalarda duş süzgeçleri çoğu zaman yeterli '
                                            'eğimle yapılmamış. Su süzgece yavaş gidiyor, saç ve sabun birikiyor, bir süre sonra fayans arasından '
                                            'alt kata sızma başlıyor. Süzgeci açıp hattı temizliyoruz; sızma varsa kamerayla nereden kaçtığını '
                                            'gösteriyoruz.',
                       'mutfak-gideri-acma': "Maltepe'de E-5 ve sahil boyundaki dükkânlarda, özellikle büfe ve kafelerde mutfak hattı yağdan çabuk "
                                             'daralıyor; üstteki dairelerle aynı kolonu paylaşınca sorun herkese yansıyor. Evlerde de bulaşık '
                                             'makinesinin sıcak suyuyla inen yağ kolonda soğuyup katılaşıyor. Basınçlı suyla yağ tabakasını söküyor, '
                                             'yağ tutucu yoksa bunu da size söylüyoruz.'}},
 'kartal': {'ulasim': "Kartal'a D-100'den ya da sahil yolundan giriyoruz; Yakacık ve Esentepe gibi yukarı mahallelere çıkmamız gerekiyorsa TEM "
                      'tarafını da kullanıyoruz. Aradığınızda sokağınızı, apartman adını ve kaçıncı katta olduğunuzu söylemeniz yeterli. Taşan yerin '
                      'bir videosunu gönderirseniz yolda hangi makinenin lazım olduğuna karar veriyoruz.',
            'gece': "Kartal'da gece çağrıları çoğunlukla çarşı çevresindeki eski binalardan geliyor; gün boyu açık kalan dükkânların atığı akşam "
                    'kolonu doldurunca üst katlardaki evlerde sorun başlıyor. Yakacık tarafında ise kış gecelerinde yokuşlar hesaba katılıyor. Pazar '
                    'akşamı ya da gece ikide, fark etmez: 7/24 telefonun başındayız.',
            'belediye': 'Kartal Belediyesi evinizdeki gidere ekip göndermez; bu şehirde kanalizasyonun sahibi İSKİ, sokaktaki ana hat taşarsa '
                        "başvuracağınız yer ALO 185. Kartal'ın yokuş mahallelerinde şu ipucu işe yarar: sizin bahçedeki rögar doluyken bir alt "
                        'sokaktaki rögar da taşıyorsa sorun ana hatta olabilir; yalnızca sizin rögar doluysa hat parselinizin içinde tıkalı '
                        'demektir.',
            'fiyat': "Kartal'da fiyatı asıl belirleyen, işin binanın ortak hattında mı yoksa tek dairede mi olduğu. Çarşı içindeki eski binalarda "
                     'dükkân ve konut aynı kolonu paylaştığı için iş bazen bodrumdaki temizleme kapağına kadar iniyor. Önce bakıyoruz, sebebi '
                     'gösteriyoruz, fiyatı işe başlamadan söylüyoruz; onayınız olmadan başlamıyoruz.',
            'acil': "Kartal'da acil çağrının yerel hali çoğunlukla zemin kat dükkânı ya da bodrum dairesinde su yükselmesi oluyor. Aradığınızda önce "
                    'binaya haber verip yukarıdaki dairelerin suyu kısmasını istemenizi, sonra elektrikli cihazları yerden kaldırmanızı söylüyoruz. '
                    'Su yükselmesi durunca hasar da büyümüyor; biz o sırada yoldayız.',
            'yakin': "Kartal'a en yakın tıkanıklık açma servisini arayanlara samimi cevabımız: Kartal'ın içinde bekleyen bir dükkânımız yok. "
                     "Ekibimiz Anadolu yakasında sahada; Kordonboyu'na, Soğanlık'a ya da Yakacık'a ortalama 30 dakika içinde varıyor. Yakacık "
                     'yokuşunda ya da çarşı trafiğinde bu biraz uzayabiliyor; aradığınızda o anki gerçek süreyi size söylüyoruz.',
            'yerel': {'tuvalet-tikanikligi-acma': "Yakacık ve Esentepe'nin yamaç binalarında tuvalet tıkanıklığı çoğu zaman klozetin hemen altında "
                                                  'değil, kolonun alt kattaki ilk dirseğinde oluyor. Dik inen su oraya çarpıyor, kâğıt havlu ve '
                                                  'ıslak mendil burada birikiyor. Alaturka tuvaletli eski dairelerde ayna taşının altındaki dar '
                                                  'sifon da sık sebep. Makaralı kamerayla dirseği bulup spiralle açıyoruz, gereksiz yere klozet '
                                                  'sökmüyoruz.',
                      'lavabo-tikanikligi-acma': "Kartal'da çarşı çevresindeki eski dairelerde banyo lavabosu çoğunlukla eski tip, duvara gömülü "
                                                 'metal borulu. Yıllarca biriken saç, sabun ve diş macunu artığı borunun içini kireçle birlikte '
                                                 'daraltıyor. Sifonu söküp temizliyor, metal boruyu zorlamadan ince spiralle açıyoruz; boru '
                                                 'çürümüşse kırmadan önce size durumu gösteriyoruz.',
                      'banyo-gideri-acma': "Soğanlık ve Uğur Mumcu'daki yeni sitelerde duşakabin süzgeçleri ince ve yatay; inşaat döneminden kalan "
                                           'harç ve silikon parçaları saçla birleşip suyu tutuyor. Eski binalarda ise küvet altında kum ve sabun '
                                           'çamuru birikmiş oluyor. Süzgeci söküp hattı temizliyor, alt kata sızma şüphesi varsa kamerayla kontrol '
                                           'ediyoruz.',
                      'mutfak-gideri-acma': 'Kartal çarşısında lokanta ve fırınların bulunduğu binalarda mutfak kolonu yağla sertleşmiş bir tabaka '
                                            "tutuyor; üst kattaki evin evyesi bu yüzden yavaş akıyor. Yakacık'ta ise kalabalık ailelerin evlerinde "
                                            'bulaşık makinesi ve evye aynı dar hatta bağlı. Önce evyeyi açıyor, sorun kolondaysa basınçlı suyla '
                                            'oraya iniyoruz.'}},
 'pendik': {'ulasim': "Pendik'in sahil mahallelerine D-100'den, Kurtköy ve Yenişehir'e ise otoyol bağlantısından ulaşıyoruz. İlçe geniş olduğu için "
                      'aradığınızda havalimanı tarafında mı, sahil tarafında mı olduğunuzu ilk cümlede söylemeniz bize çok şey kazandırıyor. Bir de '
                      'sitedeyseniz blok adı ve kısa bir video gönderin, ona göre hazırlanıp geliyoruz.',
            'gece': "Pendik'te gece çağrılarında iki farklı tablo görüyoruz: Kaynarca ve Velibaba'da kalabalık binalarda akşam saatlerinde kolonun "
                    "yetişememesi, Kurtköy'de ise havalimanında çalışan, vardiyadan gece dönen sakinlerin aradığı arızalar. Hangi saatte olursa "
                    'olsun 7/24 çalışıyoruz; gece de hafta sonu da aynı şekilde çıkıyoruz.',
            'belediye': "Pendik Belediyesi evinizdeki gidere ekip göndermez. İstanbul'da kanalizasyondan İSKİ sorumlu; cadde ya da sokaktaki ana "
                        "hatta taşma görürseniz 7/24 açık ALO 185 hattını arayın. Kurtköy ve Yenişehir'deki büyük sitelerde ayrıca şunu bilin: "
                        "sitenin kendi iç hatları ve rögarları da site yönetiminin sorumluluğunda; sokağa çıkana kadar olan kısım İSKİ'nin işi "
                        'değil.',
            'fiyat': "Pendik'te fiyatı en çok değiştiren şey hattın uzunluğu ve erişim. Kurtköy'deki geniş sitelerde tıkanıklık bazen dairede değil, "
                     'iki blok arasındaki rögarda çıkıyor; sahildeki eski yazlıklarda ise parsel bacasını bulmak zaman alıyor. Bu yüzden telefonda '
                     'kesin söz vermiyoruz; bakıp sebebi gördükten sonra fiyatı işe başlamadan söylüyoruz.',
            'acil': "Pendik'te acil durum çoğunlukla Kaynarca ve Esenyalı'daki sık binalarda alt kat dairesinin yükselen suyla uğraşması oluyor. "
                    'Telefonda önce klozetin arkasındaki ara musluğu kapatmanızı, çamaşır ve bulaşık makinesini durdurmanızı, komşulara da kısa süre '
                    'su kullanmamasını söylemenizi istiyoruz; bu sırada biz yola çıkıyoruz.',
            'yakin': "Pendik'te en yakın tıkanıklık açma servisini kim verir diye merak ediyorsanız, şunu bilin: ilçede tabelalı bir yerimiz yok, "
                     "araçla Anadolu yakasında sahada hareket eden bir ekibiz. Güzelyalı'dan Kurtköy'e, Kaynarca'dan Çamçeşme'ye genelde ortalama 30 "
                     'dakikada yanınızdayız. Havalimanı yolu yoğun saatlerde bu süreyi uzatabiliyor; arayınca net bilgi veriyoruz.',
            'yerel': {'tuvalet-tikanikligi-acma': "Pendik'in Kaynarca ve Velibaba gibi sonradan katlanmış binalarında tuvalet tıkanıklığı çoğunlukla "
                                                  'dar kalan kolonda oluyor. Klozet tek başına sorun değil; ama aynı hatta yeni katlar bağlanınca '
                                                  'ıslak mendil ve kâğıt havlu daralmada takılıyor. Kolonun temizleme kapağından makineyle girip '
                                                  'açıyor, kamerayla tekrar takılacak bir nokta var mı bakıyoruz.',
                      'lavabo-tikanikligi-acma': "Kurtköy ve Yenişehir'in yeni rezidanslarında banyo lavabosu çoğunlukla tezgâh üstü, alttan gizli "
                                                 'sifonlu. Saç ve diş macunu bu kısa sifonda çabuk birikiyor; ilk yıllarda inşaattan kalan silikon '
                                                 'parçaları da işin içine giriyor. Sifonu söküp temizliyor, hat içerideyse spiral ile açıyoruz, '
                                                 'mobilyaya zarar vermeden çalışıyoruz.',
                      'banyo-gideri-acma': 'Pendik sahilindeki eski yazlıktan dönme dairelerde duş ve küvet giderleri yazın kum getiriyor; denizden '
                                           'dönüldükçe kum süzgeçten aşağı iniyor ve sabunla birleşip hattı daraltıyor. Eğimi zayıf eski banyolarda '
                                           'bu hızla tıkanmaya dönüyor. Süzgeci açıp hattı basınçlı suyla yıkıyor, alt kata sızma varsa söylüyoruz.',
                      'mutfak-gideri-acma': 'Pendik çarşısında ve sahil boyundaki balıkçı ve lokantalarda mutfak hattı yağ ve balık artığıyla hızlı '
                                            'doluyor; üstündeki dairelerin evyeleri de bundan etkileniyor. Evlerde ise bulaşık makinesinin yağlı '
                                            'suyu kolonun alt kısmında soğuyup katılaşıyor. Basınçlı suyla yağı temizliyor, işyerlerinde yağ tutucu '
                                            'durumuna da bakıyoruz.'}},
 'tuzla': {'ulasim': "Tuzla'ya D-100, sahil yolu ya da otoyoldan geliyoruz; İçmeler ve Aydınlı için sahil tarafı, Akfırat ve Orhanlı için otoyol "
                     'bağlantısı daha uygun oluyor. Tuzla doğu-batı uzanan bir ilçe; arayınca mahallenizin yanında sahilde mi, tersane tarafında mı '
                     'yoksa yukarıda mı olduğunuzu söyleyin. Kısa bir video da gönderirseniz hazırlıklı geliyoruz.',
           'gece': "Tuzla'da gece çağrıları çoğunlukla Aydınlı ve İçmeler'deki tersane çalışanlarının oturduğu binalardan, vardiya dönüşü "
                   'saatlerinde geliyor. Yaz gelip sahil tarafındaki eski yazlıklar dolunca cumartesi ve pazar telefonlarımız sıklaşıyor. Tuzla için '
                   'de saat sınırımız yok, 7/24 çalışıyoruz; pazar sabahı ya da gece üçte aramanız sorun değil.',
           'belediye': "Tuzla Belediyesi evinizdeki gidere ekip göndermez; şebeke İstanbul genelinde İSKİ'ye ait ve sokakta taşan bir ana hat için "
                       'numara ALO 185. Sanayi bölgesindeki işyerleri için ayrı bir not: organize sanayi içindeki hatlar genelde bölge yönetiminin '
                       'sorumluluğunda olabiliyor, önce bağlı olduğunuz yönetime danışmak işe yarar.',
           'fiyat': "Tuzla'da işin bedelini en çok değiştiren, konutta mı yoksa sanayi ya da tersane çevresindeki bir işyerinde mi olduğu. Bir daire "
                    'lavabosu ile metal tozu ve yağ dolmuş bir atölye hattı aynı iş değil. Sahil tarafındaki eski yazlıklarda da hat bulmak zaman '
                    'alabiliyor. Görüp sebebi anlatıyor, fiyatı işe başlamadan söylüyoruz.',
           'acil': "Tuzla'da acil durumun yerel bir hali, kış boyu kapalı kalmış sahil yazlığının açıldığı ilk gün yaşanıyor: kurumuş sifonlardan "
                   'koku geliyor, ilk kullanımda su geri çıkıyor. Aradığınızda önce hangi muslukların kapanması gerektiğini, evde suyu nasıl '
                   'durduracağınızı söylüyoruz; sonra kamerayla hattı kontrol etmeye geliyoruz.',
           'yakin': "Tuzla'ya en yakın tıkanıklık açma servisi meselesinde açık konuşalım: Tuzla'da kapısını açtığımız bir yer yok. Anadolu "
                    "yakasının her yerinde iş yapan ekibimiz İçmeler, Aydınlı ya da Akfırat'taki bir eve ortalama 30 dakikada çıkıyor. Tepeören gibi "
                    'uzak noktalarda bu süre uzayabiliyor; aradığınızda gerçekçi süreyi baştan söylüyoruz.',
           'yerel': {'tuvalet-tikanikligi-acma': 'Tuzla sahilindeki eski yazlık sitelerde tuvalet tıkanıklığı genelde ince ve eğimi zayıf bir hatta '
                                                 "oluyor; yaz aylarında kalabalıkla birlikte kâğıt ve ıslak mendil hattı tıkıyor. Tepeören'in "
                                                 'müstakil evlerinde ise bazen alaturka tuvaletin bahçeye uzanan hattında kök çıkıyor. Spiralle açıp '
                                                 'kamerayla hattın gerisine bakıyoruz.',
                     'lavabo-tikanikligi-acma': "Akfırat ve Orhanlı'daki yeni sitelerde banyo lavabosu tıkanıklığı çoğunlukla ilk yıllarda "
                                                'görülüyor; inşaattan kalan derz dolgusu ve silikon parçaları saç ile diş macununa karışıp sifonu '
                                                'tutuyor. Sahil tarafının eski dairelerinde ise kireç asıl sebep. Sifonu söküp temizliyor, gerekirse '
                                                'duvarın içindeki boruya ince bir spiral gönderiyoruz.',
                     'banyo-gideri-acma': "Tuzla'da sahile yakın evlerde yazın duş ve küvet giderinden bolca kum iniyor; deniz dönüşü yıkanan havlu "
                                          've ayakkabılar da buna ekleniyor. Kum sabunla birleşip yer süzgecinde çamur gibi bir tabaka oluşturuyor '
                                          've su bekliyor. Süzgeç kapağını kaldırıp kum çamurunu çekiyor, ardından hattı yıkıyoruz; aşağıdaki '
                                          'komşuda leke varsa kaçağın yerine kamerayla bakıyoruz.',
                     'mutfak-gideri-acma': "Tuzla'nın tersane ve sanayi çevresinde işçi yemekhaneleri ve lokantalar çok; buraların mutfak hattı "
                                           "yoğun yağla kısa sürede daralıyor. Konutlarda ise Akfırat'ın yüksek bloklarında yağ, kolonun dibine "
                                           'inene kadar soğuyup birikiyor. Evyeyi açtıktan sonra gerekirse kolon dibine basınçlı suyla iniyor, '
                                           'işyerinde yağ tutucuyu da kontrol ediyoruz.'}},
 'sancaktepe': {'ulasim': "Sancaktepe'ye çoğunlukla TEM ya da Ataşehir üzerinden, Samandıra tarafına ise Kuzey Marmara bağlantısından giriyoruz. "
                          'Sarıgazi, Samandıra ve Yenidoğan aynı ilçede olsa da birbirinden epey ayrı yerler; telefonda önce hangi tarafta '
                          'olduğunuzu, sonra sokak adınızı ve bina adını söyleyin. Telefondan kısa bir video gönderebilirseniz hangi makineyle '
                          'geleceğimizi netleştiriyoruz.',
                'gece': "Sancaktepe'de gece çağrılarının çoğu kalabalık ailelerin oturduğu Sarıgazi ve Yenidoğan apartmanlarından geliyor; akşam "
                        "saatlerinde herkes aynı anda suyu kullanınca zayıf bağlantılar tıkanıyor. Samandıra'daki yeni sitelerde ise hafta sonu "
                        'çağrıları daha yoğun. Bayram, pazar, gece yarısı demeden 7/24 çalışıyoruz.',
                'belediye': "Sancaktepe Belediyesi evinizdeki gidere ekip göndermez, çünkü kanalizasyon belediyenin değil İSKİ'nin işi. Sokaktaki "
                            "rögardan su fışkırıyorsa ALO 185'e bildirin. Sancaktepe'de yol ve altyapı çalışmalarının sık olduğu sokaklarda sorun "
                            "bazen yeni bağlantıdan çıkıyor; sokakta kazı yapılmışsa bunu bize ve İSKİ'ye söylemeniz ayrım yapmayı kolaylaştırıyor.",
                'fiyat': "Sancaktepe'de fiyatı belirleyen başlıca konu binanın nasıl büyüdüğü. Sarıgazi'de katları zamanla eklenmiş bir apartmanda "
                         'kolon farklı çaplarda ilerlediği için iş birkaç noktadan girmeyi gerektirebiliyor; yeni sitelerde ise genelde tek bir '
                         'noktadan çözülüyor. İki iş arasındaki farkı ancak hatta bakınca biliyoruz; kamerayla gördükten sonra rakamı söylüyor, siz '
                         'kabul edince başlıyoruz.',
                'acil': "Sancaktepe'de acil durumun yerel karakteri bodrum ve zemin kat daireleri; sonradan eklenmiş katların suyu kolonda takılınca "
                        'en alttaki daire su altında kalabiliyor. Telefonda ilk işimiz, kapı kapı dolaşıp komşulardan musluk açmamalarını rica '
                        'etmenizi istemek. Sonra sizin evde rezervuar ve makine vanalarını tek tek kapattırıyor, ardından yola çıkıyoruz.',
                'yakin': "Sancaktepe'de en yakın tıkanıklık açma servisini arıyorsanız: Google Haritalar'daki kaydımız zaten Sancaktepe'de, Çınar "
                         'Dört Su Tesisatçısı adıyla. Ama biz bir dükkânda beklemiyoruz, Anadolu yakasında sahada çalışıyoruz; Sarıgazi, Yenidoğan '
                         "ya da Emek'e ortalama 30 dakikada ulaşıyoruz. Paşaköy gibi uç noktalar biraz daha sürebiliyor; arayınca tahmini saati "
                         'söylüyoruz.',
                'yerel': {'tuvalet-tikanikligi-acma': "Sancaktepe'de tuvalet tıkanıklığı çoğunlukla Sarıgazi ve Yenidoğan'ın aşama aşama yükselmiş "
                                                      'binalarında, kolonun çap değiştirdiği ek yerinde oluyor. Kalabalık evlerde günlük kullanım '
                                                      'fazla; ıslak mendil ve bebek bezi parçaları bu daralmada takılıyor. Spiral makineyle hattı '
                                                      'açıyor, kamerayla ek yerinin durumunu size gösteriyoruz.',
                          'lavabo-tikanikligi-acma': 'Samandıra çevresindeki yeni toplu konutlarda banyo lavabosu küçük ve yoğun kullanılıyor; tel '
                                                     'tel saç ve sabun artığı dar sifonda toplanıyor. Eski binalarda ise sifon çoğu zaman sonradan '
                                                     'değişmiş, uyumsuz parçalarla bağlanmış oluyor. Sifonu söküp temizliyor, uyumsuz bağlantı varsa '
                                                     'söylüyor, gerekirse hatta spiral veriyoruz.',
                          'banyo-gideri-acma': "Sancaktepe'nin kat eklenmiş binalarında üst katlardaki banyolar çoğu zaman sonradan yapılmış; yer "
                                               'süzgecinin eğimi zayıf, su süzgece gitmek yerine fayansta bekliyor. Saç ve sabun da toplanınca su '
                                               'derzlerden aşağı süzülmeye başlıyor. Süzgeç ile arkasındaki hattı temizliyor, sızıntının yerini '
                                               'kamerayla göstererek kırmadan açıyoruz.',
                          'mutfak-gideri-acma': "Sancaktepe'de kalabalık hanelerin mutfağında günde birkaç kez yemek pişiyor; evyeye giden yağ, kat "
                                                'bağlantısının olduğu yerde soğuyup birikiyor. Sarıgazi çarşısında fırın ve lokantaların atığı da '
                                                'üstteki evlerle ortak kolona karışabiliyor. İlk iş evyenin sifonunu temizlemek; su yine inmiyorsa '
                                                'kat bağlantısından girip yağ katmanını basınçlı suyla parçalıyoruz.'}},
 'sultanbeyli': {'ulasim': "Sultanbeyli'ye TEM ya da Kuzey Marmara bağlantısından girip Fatih Bulvarı üzerinden mahallelere dağılıyoruz. Tabelası "
                           'eksik sokaklar olduğu için arayınca mahalle ve sokak adının yanında yakındaki bir cami, okul ya da durak adı vermeniz '
                           'bizi doğrudan kapınıza getiriyor. Telefonla çekilmiş birkaç saniyelik görüntü de yolda hazırlanmamıza yetiyor.',
                 'gece': "Sultanbeyli'de gece çağrıları çoğunlukla akşam yemeği ve banyo saatlerinden sonra, bitişik apartmanlarda alt kat "
                         'dairelerinden geliyor. Ramazan ayında iftar sonrası ve sahur saatlerinde mutfak hattıyla ilgili telefonlar belirgin '
                         'biçimde çoğalıyor. Bizim için gece ile gündüz arasında fark yok, 7/24 çalışıyoruz; sabaha kadar beklemeniz gerekmiyor.',
                 'belediye': "Sultanbeyli Belediyesi evinizdeki gidere ekip göndermez; İstanbul'un kanalizasyon şebekesini İSKİ işletiyor ve "
                             'sokaktaki ana hatla ilgili taşmalar ALO 185 üzerinden bildiriliyor. Bitişik nizam sokaklarda şu ayrım işe yarar: '
                             'yalnızca sizin binanızın bodrumunda su varsa sorun büyük ihtimalle bina bağlantınızda; yan binalarda da aynı anda '
                             'taşma varsa ana hatta bakılmalı.',
                 'fiyat': "Sultanbeyli'de bedeli en çok oynatan, tesisatın ne kadar parça parça yapıldığı. Farklı dönemlerde eklenmiş katlarda kolon "
                          'bazen birkaç yerden dirsek yapıyor, iş tek noktadan bitmiyor. Parsel bacası olmayan binalarda da erişim zorlaşıyor. Hatta '
                          'kamera sokup ne gördüğümüzü gösteriyoruz; fiyatı işe başlamadan, makineye dokunmadan önce duyuyorsunuz.',
                 'acil': "Sultanbeyli'de acil durum genelde bodrum dairesinde ya da zemin kattaki dükkânda geri tepen suyla ortaya çıkıyor. Arayınca "
                         'önce üst katlara su kullanımını durdurmalarını söylemenizi, evinizde de rezervuar ve makinelerin vanasını kapatmanızı '
                         'istiyoruz. Taşan suyu bahçeye ya da sokağa yönlendirmeyin; bu bölgede havza ve komşu ilişkisi açısından sorun çıkarır.',
                 'yakin': "Sultanbeyli'ye en yakın tıkanıklık açma servisi kim sorusuna kendi adımıza şunu diyoruz: burada bir dükkân tutmuyoruz, "
                          "ekibimiz Anadolu yakası genelinde sahada. Battalgazi, Hasanpaşa ya da Mecidiye'ye ortalama 30 dakikada ulaşıyoruz. Fatih "
                          'Bulvarı kilitlendiğinde gecikebiliriz; o zaman bunu telefonda saklamadan belirtiyoruz.',
                 'yerel': {'tuvalet-tikanikligi-acma': "Sultanbeyli'de tuvalet tıkanıklığının sık sebebi, sonradan eklenmiş katların klozet hattının "
                                                       'kolona dik ya da ters açıyla bağlanmış olması. Bu bağlantıda ıslak mendil ve kâğıt kolayca '
                                                       'takılıyor. Alaturka hela kullanılan evlerde taş haznenin çıkışı da daralmış olabiliyor. '
                                                       'Spiral makineyle açıyor, kamerayla bağlantının açısına bakıp tekrar etmemesi için ne '
                                                       'yapılabileceğini söylüyoruz.',
                           'lavabo-tikanikligi-acma': "Sultanbeyli'nin eski dairelerinde banyo lavabosu çoğu zaman yıllar içinde birkaç kez "
                                                      'değişmiş; altında farklı çaplarda parçalarla uzatılmış sifonlar görüyoruz. Saç ile diş macunu '
                                                      'artığı tam bu dönüşlerde tutunuyor. Sifonu söküp temizliyor, uyumsuz parçaları gösteriyor, '
                                                      'hat duvar içinde tıkalıysa ince spiralle açıyoruz.',
                           'banyo-gideri-acma': "Sultanbeyli'de katları sonradan eklenmiş binalarda banyo zemini çoğu zaman yeterli eğim almamış; "
                                                'duş suyu süzgece varamadan birikiyor. Kalabalık evlerde saç ve sabun artığı süzgeçte hızla '
                                                'toplanıyor, zamanla alt kat tavanına sızma başlıyor. Süzgeci ve hattı açıyor, sızma varsa kamerayla '
                                                'yerini bulup kırmadan çözmeye çalışıyoruz.',
                           'mutfak-gideri-acma': "Sultanbeyli'de Fatih Bulvarı boyundaki fırın, lokanta ve kasapların mutfak hattı yağla çabuk "
                                                 'doluyor; aynı binada oturanlar da evyelerinin yavaşladığını fark ediyor. Evlerde ise kalabalık '
                                                 'sofraların yağı evyeden inip kolonun dirseğinde katılaşıyor. Evyeyi açıp kolona basınçlı suyla '
                                                 'iniyor, işyerlerine yağ tutucu konusunda bilgi veriyoruz.'}},
 'adalar': {'ulasim': "Adalar'a ekipmanı vapurla ya da deniz taksiyle geçiriyoruz; iskeleden sonra adada motorlu araç olmadığı için makineyi el "
                      'arabasıyla ve elde evinize kadar taşıyoruz. Arayınca hangi adada olduğunuzu, iskeleye uzaklığınızı ve evin yolunu tarif edin. '
                      'Kısa bir video çok önemli; karşıya geçmeden doğru makineyi almamızı sağlıyor.',
            'gece': "Adalar'da gece çağrısının karakteri farklı: son vapurdan sonra adaya geçmek deniz taksiye bağlı ve hava durumu belirleyici. "
                    'Telefonumuz 7/24 açık; gece aradığınızda durumu dinliyor, suyu nasıl durduracağınızı söylüyor, geçiş imkânına göre ne zaman '
                    'gelebileceğimizi açıkça konuşuyoruz. Yazın hafta sonu yoğunluğunda da aynı şekilde planlıyoruz.',
            'belediye': "Adalar Belediyesi evinizdeki gidere ekip göndermez; adalarda da şebeke İSKİ'nin elinde, yoldaki ana hat taşıyorsa ALO 185'e "
                        "haber verin. Adalar'a özgü bir not: bazı eski köşklerde evin şebekeye nereden bağlandığı bilinmiyor; sokak rögarı normalken "
                        'sizin bahçede taşma varsa sorun büyük ihtimalle parselinizin içindeki eski hatta.',
            'fiyat': "Adalar'da işin bedelini önce ulaşım ve taşıma belirliyor. Ekipmanı denizden geçirip iskeleden eve elle taşımak karadaki bir "
                     'işle aynı değil; evin iskeleye uzaklığı ve yokuşu da işin süresini belirliyor. Ahşap köşklerde hattın izini sürmek de zaman '
                     'alıyor. Bunların hepsini konuşup fiyatı işe başlamadan söylüyoruz.',
            'acil': "Adalar'da acil durumda yardımın gelmesi denize bağlı olduğu için ilk dakikalarda yapacağınız şey daha önemli. Aradığınızda önce "
                    'klozetin ara musluğunu ya da evin ana vanasını nasıl kapatacağınızı söylüyoruz; ahşap döşemeli evlerde suyun tahtaya işlememesi '
                    'için neleri kaldırmanız gerektiğini de anlatıyoruz. Sonra geçişi planlıyoruz.',
            'yakin': "Adalar'da oturup en yakın tıkanıklık açma servisini merak edenlere gerçeği söyleyelim: adaların hiçbirinde bekleyen ekibimiz "
                     "yok, karşı kıyıda, Anadolu yakasında çalışıyoruz. Büyükada, Heybeliada, Burgazada ya da Kınalıada'ya geliş süremiz vapur ve "
                     'deniz taksi saatlerine, havaya bağlı. Bu yüzden karadaki gibi süre vaat etmiyoruz; aradığınızda gerçekçi saati söylüyoruz.',
            'yerel': {'tuvalet-tikanikligi-acma': "Adalar'daki ahşap köşklerde tuvalet çoğu zaman sonradan bir odanın köşesine eklenmiş; hattı "
                                                  'döşeme altından uzun ve dönüşlü bir yolla dışarı çıkıyor. Islak mendil bu dönüşlerde takılıyor. '
                                                  'Kışın kapalı kalan yazlıklarda da sifon kuruyup koku başlıyor. Makaralı kamerayla hattın yolunu '
                                                  'izliyor, döşemeyi kırmadan spiralle açmaya çalışıyoruz.',
                      'lavabo-tikanikligi-acma': "Adalar'daki eski evlerde banyo lavabolarının çoğu antika tarzı, ayaklı ya da duvara asılı; "
                                                 'altlarındaki sifonlar eski metal ve kireç tutmuş. Yaz kalabalığında saç ile sabun köpüğü bu '
                                                 'daralmış sifonda hızla tutunuyor. Eski parçalara zarar vermeden sifonu açıyor, gerekirse duvardaki '
                                                 'hatta ince spiralle giriyoruz.',
                      'banyo-gideri-acma': "Adalar'da yaz aylarında denizden dönülüp yıkanılan duşlarda süzgece bol miktarda kum iniyor; Burgazada "
                                           "ve Kınalıada'nın yazlık dairelerinde bu çok sık. Ahşap köşklerde ise duş teknesinin altındaki hat yaşlı "
                                           've eğimi zayıf, su bekleyince döşemeye sızma riski var. Süzgeci açıp hattı yıkıyor, sızma şüphesinde '
                                           'kamerayla bakıyoruz.',
                      'mutfak-gideri-acma': "Adalar'da yaz sezonunda iskele çevresindeki balık lokantaları ve kafeler yoğun çalışıyor; mutfak "
                                            'hatlarına giden yağ ve balık artığı eski borularda çabuk birikiyor. Evlerde ise kışın az kullanılan '
                                            'evyeler yazın birden yükleniyor. Evyeyi açıp gerekirse hattı basınçlı suyla yıkıyor, ekipmanı adaya '
                                            'taşıdığımız için işi tek seferde bitirmeye çalışıyoruz.'}}}

# ── Hizmet makaleleri (ilçe ve hub sayfalarında ortak iskelet) ─────────────
# {ad}{loc}{dat}{gen}{abl}{kisa} yer tutucuları build.yer() ile doldurulur. Hub'da {ad}="Anadolu Yakası".
HIZMET_METIN = {
 "tuvalet-tikanikligi-acma": {
  "neden_giris": "Tuvalet tıkandığında beklemek diye bir seçenek yok, bunu biliyoruz. Ama sebebini bilmek hem doğru müdahaleyi seçtiriyor hem de aynı şeyin bir ay sonra tekrar yaşanmasını önlüyor.",
  "nedenler": [
   ("Islak mendil ve havlu kâğıt", "Tuvalet kâğıdı suda dağılır, bunlar dağılmaz. Klozet dirseğinde ya da kolonun döndüğü noktada birbirine tutunup tıkaç olur."),
   ("Hijyenik ped ve bebek bezi", "Suyu emip şişer, dirseğe sıkışır. Arkasından gelen kâğıt da üstüne yığılır."),
   ("Düşen sert cisim", "Diş fırçası, oyuncak, deodorant kapağı… Sert bir cisim dirsekte durur ve süzgeç gibi her şeyi tutar."),
   ("Dar ya da yanlış eğimli bağlantı", "Alaturkadan klozete çevrilmiş tuvaletlerde altta kalan eski dirsek ya da tadilatta eğimi az verilmiş boru suyu yavaşlatır."),
   ("Bina kolonu", "Siz klozeti kullanmasanız da su yükseliyorsa ya da alt katlarda da şikâyet varsa sorun ortak kolondadır."),
  ],
  "yontem": "Tuvalet tıkanıklığını çoğu zaman klozeti sökmeden, klozetin ağzından spiral makineyle açıyoruz. Klozet için ucu korumalı spiral kullanıyoruz ki sırlı yüzey çizilmesin. Asma klozette ya da sıkışmış sert bir cisimde sökmek gerekebilir; söktüğümüzde contayı yenileyip sızdırmazlığı test ediyoruz. Tıkanıklık tekrar ediyorsa makaralı kamerayı hattın içine sürüp sebebi görüyoruz.",
  "belediye": "{ad}{loc} tuvaletiniz tıkandığında belediye ya da İSKİ evinize ekip göndermez; klozet, daire içindeki boru ve bina kolonu mülk sahibinin sorumluluğundadır. İSKİ'yi (ALO 185) yalnızca sokaktaki ana kanalizasyon hattı taşıyorsa aramanız gerekir.",
 },
 "lavabo-tikanikligi-acma": {
  "neden_giris": "Lavabo genelde bir anda tıkanmaz; önce suyun inmesi biraz uzar, sonra koku başlar, en sonunda bir sabah su hiç gitmez. Yavaşlamanın ilk günlerinde müdahale etmek işi hem kolaylaştırır hem kısaltır.",
  "nedenler": [
   ("Saç", "Lavabo tıpasının altına takılan saç, sabunla birleşip keçe gibi bir yumak oluşturur ve sifonun girişini kapatır."),
   ("Sabun ve diş macunu", "Sıvı sabun ve diş macunu borunun iç yüzeyinde ince, yapışkan bir tabaka bırakır; her gün biraz daha kalınlaşır."),
   ("Kireç", "Sert suyun bıraktığı kireç borunun içini pürüzlendirir; pürüzlü yüzey saçın ve tortunun tutunmasını kolaylaştırır."),
   ("Küçük eşyalar", "Küpe, kapak, diş fırçası başlığı gibi küçük parçalar sifona düşüp akışı daraltır."),
   ("Ortak hat", "Lavabo banyodaki diğer giderlerle aynı hatta birleşir; tıkanıklık birleşme noktasındaysa lavabo ile birlikte duş da yavaşlar."),
  ],
  "yontem": "Önce lavabonun sifonunu söküp temizliyoruz; tıkanıklığın şaşırtıcı bir kısmı tam burada. Sifon temizse spiral makineyi sifon çıkışından duvar içindeki hatta ilerletiyor, birikintiyi söküp hattı suyla deniyoruz. Fayans kırmıyoruz. Aynı lavabo sık sık tıkanıyorsa kamerayla hattın içine bakıp eğimi ve bağlantıları kontrol ediyoruz.",
  "belediye": "{ad}{loc} lavabonuz tıkandığında belediyeyi ya da İSKİ'yi aramanız sorunu çözmez; dairenizin içindeki tesisat mülk sahibinin sorumluluğundadır. İSKİ yalnızca sokaktaki ana kanalizasyon hattına bakar ve ona ALO 185'ten ulaşılır.",
 },
 "banyo-gideri-acma": {
  "neden_giris": "Duşta su birikmesi küçük bir sorun gibi görünür ama uzun süre bekleyen su derzlerden ve contalardan alt kata sızabilir. Banyo giderinin neden tıkandığını bilmek bu yüzden önemli.",
  "nedenler": [
   ("Saç", "Duş ve küvet giderinin bir numaralı sebebi. Saç, şampuan ve sabun kalıntısıyla birleşip süzgecin altındaki dar dirseği kapatır."),
   ("Kum ve kir", "Plaj dönüşü, inşaat ya da bahçe işinden sonra duşa giren kum gider haznesinin dibine çöker."),
   ("Sabun tortusu", "Katı sabun ve yağlı kozmetikler borunun çeperinde sertleşen bir tabaka bırakır."),
   ("Az eğim", "Yerden ısıtma ya da duşakabin tadilatında gider hattına yeterli eğim verilmediyse su yavaş akar ve taşıdığını yolda bırakır."),
   ("Yer süzgeci haznesi", "Banyo yer süzgecinin içindeki küçük sifonlu hazne zamanla dolar; hem tıkanır hem koku yapar."),
  ],
  "yontem": "Duş teknesi, küvet ya da yer süzgecinin ızgarasını kaldırıp önce görünen birikintiyi alıyoruz. Ardından spiral makineyi süzgeç ağzından ilerletip dirsekteki saçı ve tortuyu söküyoruz; gerekirse hattı basınçlı suyla yıkıyoruz. Fayansa ve tekneye dokunmuyoruz. Sorun sık tekrarlıyorsa kamerayla eğime ve birleşme noktalarına bakıyoruz.",
  "belediye": "{ad}{loc} duş, küvet ya da yer süzgeci tıkandığında belediye ya da İSKİ evinize ekip göndermez; banyonuzdaki tesisat mülk sahibinin sorumluluğundadır. Sokaktaki ana kanalizasyon hattı taşıyorsa İSKİ'yi ALO 185'ten arayın.",
 },
 "mutfak-gideri-acma": {
  "neden_giris": "Mutfak giderini tıkayan şey neredeyse her zaman aynıdır: yağ. İşin kötüsü, yağ tıkanıklığı sessiz ilerler; evye haftalarca biraz yavaş akar, sonra bir akşam yemekten sonra hiç gitmez.",
  "nedenler": [
   ("Kızartma ve yemek yağı", "Sıcakken su gibi akan yağ, borunun soğuk bölümünde donup çepere yapışır. Üstüne gelen her şey bu yapışkan tabakaya tutunur."),
   ("Yemek artığı ve telve", "Pirinç, makarna, kahve telvesi ve çay posası yağlı tabakaya takılıp boruyu daraltır."),
   ("Bulaşık makinesi", "Makine her çalıştığında sıcak, deterjanlı ve yağlı suyu bir anda gidere boşaltır; hat zaten darsa evye geri tepar."),
   ("Deterjan birikimi", "Bol deterjan yağı kısa süreliğine çözer ama ileride soğuyunca yağ sabunlaşıp daha sert bir tortuya dönüşür."),
   ("Ortak mutfak kolonu", "Apartmanlarda mutfaklar çoğu zaman ayrı bir kolona bağlıdır; kolondaki yağ birikimi en alt kattaki evyeden geri gelir."),
  ],
  "yontem": "Evyenin sifonunu ve bulaşık makinesi bağlantısını söküp temizliyoruz, ardından spiral makineyle hattın içindeki yağı söküyoruz. Yağ çepere yapışmışsa basınçlı suyla yıkayıp çeperi temizliyoruz; sadece delik açıp geçmiyoruz, çünkü o zaman tıkanıklık kısa sürede geri gelir. Tezgâh ve dolabı sökmüyoruz. Sık tekrarlayan durumlarda yağın nerede biriktiğini kamerayla gösteriyoruz.",
  "belediye": "{ad}{loc} mutfak gideriniz ya da apartmanınızın mutfak kolonu tıkandığında belediye ya da İSKİ ekip göndermez; bina içindeki hatlar mülk sahibinin ve bina yönetiminin sorumluluğundadır. İSKİ yalnızca sokaktaki ana hatta bakar (ALO 185).",
 },
}

# ── Anasayfa ve Hakkımızda ──────────────────────────────────────────────────
TANITIM = ("Çınar Dört Su Tesisatçısı olarak İstanbul Anadolu Yakası'nın 14 ilçesinde tuvalet, lavabo, banyo ve mutfak gideri "
           "tıkanıklığı açıyoruz. Tıkanıklığın yerini gerektiğinde makaralı kamerayla görüp kırmadan açıyor, fiyatı işe "
           "başlamadan söylüyoruz. 7 gün 24 saat ulaşabilirsiniz.")
FIYAT_SOZ = ("Fiyatı usta yerinde gördükten sonra, işe başlamadan söylüyoruz; onayınızı almadan işe başlamıyoruz. "
             "Fotoğraf ya da videoyla yaklaşık bilgi de verebiliyoruz.")

HAKKIMIZDA = [
 ("Biz kimiz?", [TANITIM,
   "Bu site, Çınar Dört Su Tesisatçısı'nın gider ve tıkanıklık açma hizmetini anlattığımız sitedir. Google Haritalar'da da bu adla bulunuyoruz; konumumuz Sancaktepe'de. Burada tıkanıklık ve su kaçağı işini anlattık: hangi giderin neden tıkandığını, nasıl açtığımızı, kaçağı nasıl bulduğumuzu ve evde neleri kendiniz deneyebileceğinizi."]),
 ("Nasıl çalışıyoruz?", [
   "Arıyorsunuz ya da WhatsApp'tan yazıyorsunuz; mümkünse sorunun kısa bir videosunu atıyorsunuz. Videoya bakıp hangi makineyle geleceğimize karar veriyoruz. Anadolu yakasında adrese ortalama 30 dakikada ulaşıyoruz; Adalar ve Şile gibi uzak noktalarda süreyi arayınca açıkça söylüyoruz.",
   "Usta önce sorunun yerini buluyor: klozet mi, lavabo sifonu mu, duş gideri mi, mutfak kolonu mu? Gerekiyorsa kamerayı hattın içine sürüp tıkanıklığı ekranda birlikte görüyoruz. Fiyatı işe başlamadan söylüyor, onayınızı aldıktan sonra kırmadan açıyoruz."]),
 ("Neden kırmadan?", [
   "Çünkü tıkanıklıkların çok büyük kısmı borunun kırılmasından değil, içinde biriken bir şeyden kaynaklanıyor. Birikintiyi makineyle söküp çıkardığınızda fayansa, tezgâha ya da duvara dokunmanız gerekmiyor.",
   "Kırma gerçekten gerekiyorsa, yani boru çatlamış ya da çökmüşse, bunu tahminle değil kamera görüntüsüyle söylüyoruz ve yalnızca sorunlu noktayı işaretliyoruz."]),
 ("Hangi bölgelere hizmet veriyoruz?", [
   "Anadolu yakasının 14 ilçesine geliyoruz: Adalar, Ataşehir, Beykoz, Çekmeköy, Kadıköy, Kartal, Maltepe, Pendik, Sancaktepe, Sultanbeyli, Şile, Tuzla, Ümraniye ve Üsküdar. Her ilçenin sayfasında o ilçedeki binalarda en sık gördüğümüz durumları da anlattık."]),
]

# ── Kameralı tespit sayfası (tek sayfa; ilçe sürümü YOK) ────────────────────
KAMERA = {
 "giris": "Tıkanıklığı açmak bir iş, neden tıkandığını bilmek başka bir iş. Makaralı kamerayı gider ağzından hattın içine sürüyor, tıkanıklığın kaç metre ileride olduğunu, neyden kaynaklandığını ve borunun sağlam olup olmadığını ekranda sizinle birlikte görüyoruz.",
 "ne_zaman": [
  ("Aynı gider tekrar tekrar tıkanıyorsa", "Açtırdınız, iki hafta sonra yine tıkandı. Bu, içeride açmakla geçmeyen bir sebep olduğunu gösterir: ters eğim, çökmüş bir boru, kök ya da sıkışmış bir cisim."),
  ("Biri \"kırmak lazım\" diyorsa", "Kırma kararını görüntüye bakmadan vermeyin. Çoğu tıkanıklık kırmadan açılır; kırmak gerekiyorsa bile kamera hangi noktanın kırılacağını gösterir."),
  ("Gidere bir cisim düştüyse", "Kamera cismin yerini ve konumunu gösterir; körlemesine itmek yerine yakalayıp çıkarmayı deneriz."),
  ("Sebebi bilinmeyen koku ya da nem varsa", "Duvarda ya da tavanda açıklanamayan bir leke varsa hattaki çatlak ya da gevşek bağlantı kamerada görülebilir."),
  ("Tadilattan ya da ev almadan önce", "Fayans döşenmeden önce gider hattının durumunu görmek, sonradan kırmaktan çok daha zahmetsizdir."),
 ],
 "neler": [
  ("Tıkanıklığın yeri", "Ekrandaki mesafe sayacı tıkanıklığın gider ağzından kaç metre ileride olduğunu gösterir; hangi dirsekte durduğunu buradan anlarız."),
  ("Tıkanıklığın sebebi", "Yağ, saç, kireç, ıslak mendil, kök ya da sert bir cisim; her birinin görüntüsü farklıdır ve her biri farklı uçla açılır."),
  ("Borunun durumu", "Çatlak, çökme, kayan bağlantı ya da ters eğim varsa görüntüde görülür."),
  ("Açma sonrası temizlik", "Tıkanıklığı açtıktan sonra kamerayı yeniden sürüp birikintinin gerçekten temizlendiğini kontrol ederiz."),
 ],
 "fiyat": [
  ("Hattın uzunluğu ve dirsekler", "Lavabo altındaki kısa bir hat ile birkaç kat inen bir kolon aynı iş değildir."),
  ("Giriş noktası", "Kamerayı gider ağzından mı, temizleme kapağından mı, rögardan mı süreceğimiz süreyi değiştirir."),
  ("Açma ile birlikte mi?", "Görüntülemenin ardından tıkanıklığı açmak da gerekiyorsa iki iş birlikte değerlendirilir; fiyatı işe başlamadan söyleriz."),
 ],
 "sss": [
  ("Kameralı tespit için bir yer kırılıyor mu?", "Hayır. Kamerayı gider ağzından, sifon yerinden ya da temizleme kapağından sürüyoruz. Zaten amacımız kırmadan önce görmek."),
  ("Kamera görüntüsünü ben de görebilir miyim?", "Evet. Ekranı sizinle birlikte izliyoruz; isterseniz ekran görüntüsünü telefonunuza da gönderiyoruz."),
  ("Her tıkanıklıkta kamera gerekir mi?", "Hayır. Basit bir sifon ya da klozet tıkanıklığında gerekmez. Kamerayı tekrarlayan, sebebi anlaşılmayan ya da kırma konuşulan durumlarda kullanıyoruz."),
  ("Fiyatı önceden söylüyor musunuz?", "Evet. Usta hattı görüp işin kapsamını belirledikten sonra, işe başlamadan fiyatı söylüyor."),
 ],
}

# ── Tıkanıklık Rehberi ─────────────────────────────────────────────────────
# Soru varyasyonları NİYETE göre 4 yazıda toplandı; ⛔ her varyasyon için ayrı sayfa AÇMA.
#   lavabo-tikanirsa-ne-yapmali     : "lavabo tıkanırsa ne yapmalı / ne yapmak lazım", "kendim açabilir miyim", "en kolay yolu"
#   tuvalet-tikanirsa-ne-yapmali    : "tuvalet tıkanırsa ne yapmalı", "klozet nasıl açılır", "alaturka tuvalet tıkanıklığı"
#   mutfak-gideri-tikanirsa-ne-yapmali : "mutfak gideri tıkandı ne yapmalı", "evye nasıl açılır", "yağ tıkanıklığı"
#   dus-gideri-nasil-acilir         : "duş gideri nasıl açılır", "duşta su birikiyor", "yer süzgeci kokusu"
# Bölüm öğeleri: düz metin = paragraf · ("h3", başlık, metin) · ("liste", [..]) · ("adim", [..]) · ("ipucu"/"dikkat", metin) · ("tablo", başlıklar, satırlar)
REHBER = [
 {"slug": "lavabo-tikanirsa-ne-yapmali", "ikon": "damla",
  "h1": "Lavabo Tıkanırsa Ne Yapmalı? Evde Deneyebileceğiniz Yollar",
  "title": "Lavabo Tıkanırsa Ne Yapmalı? Evde Deneyebileceğiniz Yollar",
  "aciklama": "Lavabo tıkanırsa ne yapmak lazım, tıkalı lavaboyu kendiniz açabilir misiniz, en kolay yol hangisi? Adım adım, güvenlik uyarılı rehber.",
  "ozet": "Lavabonuz tıkandı ve hemen birini çağırmak istemiyorsunuz; anlıyoruz :) Banyo lavabosundaki tıkanıklıkların önemli bir kısmını evde kendiniz açabilirsiniz. Bu yazıda kolaydan zora doğru neleri deneyebileceğinizi ve hangi noktada artık usta gerektiğini açıkça anlattık.",
  "hizmet": "lavabo-tikanikligi-acma",
  "bolum": [
   ("Lavabo tıkanırsa ilk ne yapmak lazım?", [
     ("adim", ["Musluğu kapatın; tıkalı lavaboya su akıtmaya devam etmek sadece taşma riskini artırır.",
               "Lavabodaki suyu bir bardakla kovaya alın. Boş lavaboda ne yaptığınızı görmeniz kolaylaşır.",
               "Lavabo tıpasını çıkarın ya da yukarı çekin; altına takılan saç ve köpük yumağını eldivenle temizleyin.",
               "Lavabonun altına bakın: sifon bağlantısında damlama varsa altına bir kap koyun."]),
     "Bu adımlar sorunu her zaman çözmez ama durumu kontrol altına alır. Tıkanıklıkların bir kısmı zaten tıpanın hemen altında çıkar."]),
   ("Tıkalı lavaboyu kendim açabilir miyim?", [
     "Tıkanıklık tıpanın altında ya da sifonun içindeyse çoğu zaman evet. Bunun için özel bir alete gerek yok; eldiven, bir kova ve biraz sabır yeter.",
     "Tıkanıklık sifondan sonra, yani duvarın içindeki borudaysa evdeki aletler oraya pek ulaşmaz. Bu durumda zorladıkça eski bağlantıları gevşetme ihtimaliniz artar.",
     ("ipucu", "Lavabo ile birlikte duş da yavaşladıysa ya da tuvalet çekilince lavabo fokurduyorsa tıkanıklık banyonun birleşme noktasındadır. Lavaboyla uğraşmak bu durumda sonuç vermez.")]),
   ("Lavabo açmanın en kolay yolu hangisi?", [
     "Aşağıdaki yolları sırasıyla deneyin; birinde su gitmeye başlarsa devamına gerek yok.",
     ("h3", "1. Tıpa ve süzgeç temizliği", "Bastır-aç tıpalar genelde döndürerek ya da yukarı çekerek çıkar. Altında biriken saç yumağı, lavabo tıkanıklığının en yaygın sebebidir."),
     ("h3", "2. Pompa", "Lavabonun taşma deliğini ıslak bir bezle sıkıca kapatın, yoksa bastığınız hava oradan kaçar. Pompanın lastiğini örtecek kadar su bırakıp gider ağzına tam oturtun ve kısa, kuvvetli hareketlerle 15-20 kez basıp çekin."),
     ("h3", "3. Sifonu sökmek", "Lavabonun altındaki kıvrımlı parça sifondur. Altına kova koyup elle çevrilen somunları gevşetin, sifonu çıkarıp içini temizleyin. Takarken contaların yerine oturduğuna dikkat edin."),
     ("h3", "4. Plastik dişli şerit", "Hırdavatçılarda satılan ince plastik şerit, gider ağzından sokulup çekilince saçı yakalayıp dışarı çıkarır. Banyo lavabosunda çok işe yarar."),
     ("dikkat", "Tel askı, şiş ya da bıçak gibi sert aletlerle gidere girmeyin. Sifonu çizebilir, contayı yerinden oynatabilir ya da kırık bir parçayı içeride bırakabilirsiniz.")]),
   ("Karbonat, sirke ya da kaynar su işe yarar mı?", [
     "Açık konuşalım: karbonat ile sirkenin köpürmesi gözle görülür ama saç yumağını ya da sertleşmiş tortuyu sökmez. Hafif bir kokuyu azaltabilir, o kadar.",
     "Kaynar su ise plastik sifonu ve bağlantıları yumuşatıp şekil bozukluğuna yol açabilir. Kullanacaksanız çok sıcak musluk suyu yeterli; kaynatıp dökmeyin."]),
   ("Kimyasal açıcı dökmeden önce bilmeniz gerekenler", [
     "Tuz ruhu, kostik ve çamaşır suyu en sık başvurulan çözümler ama en riskli olanlar da bunlar. Farklı kimyasallar karıştığında zehirli gaz çıkabilir; küçük, penceresiz bir banyoda bu ciddi bir tehlikedir.",
     "Kimyasal tıkanıklığı açamazsa giderin içinde bekler. Sonra pompayla ya da makineyle müdahale edildiğinde geri sıçrayıp gözünüze, cildinize gelebilir.",
     ("dikkat", "Kimyasal döktüyseniz pompa kullanmayın ve çağırdığınız ustaya mutlaka söyleyin.")]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Sifonu söktünüz, temizlediniz ama su hâlâ gitmiyorsa", "Lavabo ile birlikte duş ya da tuvalet de yavaşladıysa",
                "Lavabodan geçmeyen bir koku geliyorsa", "Alt kattaki komşunuz tavanında ıslaklık görüyorsa",
                "Kimyasal döktünüz ve gider hâlâ tıkalıysa", "Aynı lavabo birkaç haftada bir yeniden tıkanıyorsa"]),
     "Bu durumlarda tıkanıklık evdeki aletlerin ulaşamayacağı bir yerdedir. [[hizmet:lavabo-tikanikligi-acma|Lavabo tıkanıklığı açma]] hizmetimizde sifondan ve duvar içindeki hattan kırmadan açıyor, gerekirse [[kamerali-tikaniklik-tespiti/|kamerayla]] hattın içine bakıyoruz."]),
   ("Lavabo tıkanmasın diye neler yapabilirsiniz?", [
     ("liste", ["Lavaboya saç tutucu süzgeç takın; birkaç günde bir temizlemek yeter.", "Tıpayı ayda bir çıkarıp altını temizleyin.",
                "Haftada bir lavabodan bir süre sıcak musluk suyu akıtın.", "Diş macunu ve sabun artığını bol suyla gönderin."])]),
  ],
  "sss": [("Lavabo tıkanırsa ne yapmalıyım?", "Musluğu kapatın, suyu boşaltın, tıpanın altını temizleyin. Olmazsa taşma deliğini kapatıp pompayla deneyin, ardından sifonu söküp temizleyin. Su hâlâ gitmiyorsa tıkanıklık duvar içindedir."),
          ("Tıkalı lavaboyu kendim açabilir miyim?", "Tıkanıklık tıpanın altında ya da sifonun içindeyse evet. Duvar içindeki boruda ya da banyonun ortak hattındaysa evdeki aletler genellikle yetmez."),
          ("Lavabo açmanın en kolay yolu nedir?", "Tıpayı çıkarıp altındaki saçı temizlemek. İkinci sırada taşma deliğini kapatarak pompa kullanmak gelir."),
          ("Kaynar su lavabo açar mı?", "Önermiyoruz; plastik sifon ve bağlantılar ısıyla şekil değiştirebilir. Çok sıcak musluk suyu yeterlidir.")]},

 {"slug": "tuvalet-tikanirsa-ne-yapmali", "ikon": "klozet",
  "h1": "Tuvalet Tıkanırsa Ne Yapmalı? Klozet ve Alaturka İçin Adım Adım",
  "title": "Tuvalet Tıkanırsa Ne Yapmalı? Klozet ve Alaturka Rehberi",
  "aciklama": "Tuvalet tıkanırsa ne yapmak lazım, klozeti kendiniz açabilir misiniz, alaturka tuvalet nasıl açılır? Taşmayı önleyen ilk adımlar ve sınırlar.",
  "ozet": "Tuvalet tıkanınca ilk dakikalarda yapılan iki şey sonucu belirliyor: sifona bir daha basmamak ve suyu kesmek. Bu yazıda taşmayı nasıl önleyeceğinizi, klozet ve alaturka tuvaleti evde nasıl açmayı deneyebileceğinizi ve nerede durmanız gerektiğini anlattık.",
  "hizmet": "tuvalet-tikanikligi-acma",
  "bolum": [
   ("Tuvalet tıkanırsa ilk ne yapmak lazım?", [
     ("adim", ["Sifona bir daha basmayın. Su yükseliyorsa ikinci basış taşmaya sebep olur.",
               "Rezervuarın altındaki ara musluğu saat yönünde çevirip kapatın.",
               "Klozetin çevresine eski havlu serin; taşma olursa alt kata su inmesini azaltır.",
               "Klozetteki su çok yüksekse bir kapla bir kısmını kovaya alın."]),
     "Bu dört adım birkaç dakikanızı alır ama taşmanın önüne geçer. Sonra sakin kafayla aşağıdakileri deneyebilirsiniz."]),
   ("Tuvalet tıkanıklığını kendim açabilir miyim?", [
     "Fazla tuvalet kâğıdı atıldıysa ya da yumuşak bir tıkanıklıksa çoğu zaman evet; bir klozet pompası işinizi görür.",
     "Islak mendil, ped, bez ya da düşmüş sert bir cisim varsa pompa genelde onu daha ileri iter ve çıkarmayı zorlaştırır. Bu durumda zorlamayın.",
     ("ipucu", "Banyonun yer süzgecinden su geliyorsa ya da alt katlarda da sorun varsa tıkanıklık klozette değil bina kolonundadır. Bunu evde açmanız mümkün değil.")]),
   ("Klozet tıkanıklığı nasıl açılır?", [
     ("h3", "Doğru pompa", "Lavabo pompası değil, alt kısmında uzantı olan klozet pompası kullanın; klozetin gider ağzına tam oturur. Lastiği örtecek kadar su olsun, pompayı yavaşça oturtup havasını alın, ardından 15-20 kez kuvvetli basıp çekin."),
     ("h3", "Sıvı sabun ve sıcak su", "Yalnızca kâğıt tıkanıklığında işe yarar: klozete biraz sıvı bulaşık deterjanı ekleyin, üzerine çok sıcak ama kaynamamış musluk suyu dökün ve 15-20 dakika bekleyin. Kaynar su seramiği çatlatabilir."),
     ("h3", "Klozet spirali", "Ucu kılıflı klozet spirali sırlı yüzeyi çizmeden dirseğe ulaşır. Spirali nazikçe ilerletip çevirin; takıldığı yerde ileri geri hareket ettirin."),
     ("dikkat", "Telefon, diş fırçası ya da oyuncak düştüyse pompa kullanmayın. Cisim ilerledikçe çıkarmak zorlaşır; bu durumda kamerayla yerini görüp çıkarmak gerekir.")]),
   ("Alaturka tuvalet tıkanıklığı nasıl açılır?", [
     "Alaturkanın dirseği klozete göre daha derin ve dardır, tıkanıklık genellikle bu dirseğin dibinde olur. İyi tarafı şu: gider ağzı geniş olduğu için pompa ve spiral daha rahat çalışır.",
     ("h3", "Geniş ağızlı pompa", "Hazneye pompanın lastiğini örtecek kadar su doldurun, pompayı gider ağzına tam oturtup kısa ve kuvvetli hareketlerle çalışın."),
     ("h3", "Kova ile su", "Hafif bir kâğıt tıkanıklığında bir kova ılık suyu tek seferde ve biraz yüksekten dökmek tıkanıklığı ilerletebilir. Su yükseliyorsa ikinci kovayı dökmeyin."),
     ("dikkat", "Alaturkadan klozete çevrilmiş tuvaletlerde altta eski, dar bir dirsek kalmış olabilir. Böyle bir tuvalet sık tıkanıyorsa evde açmak geçici çözümdür.")]),
   ("Tuvalete neler atılmamalı?", [
     ("liste", ["Islak mendil (paketinde \"tuvalete atılabilir\" yazsa bile)", "Hijyenik ped, tampon, bebek bezi", "Kâğıt havlu ve peçete",
                "Kulak çubuğu, pamuk, diş ipi", "Yemek artığı ve yağ", "Kedi kumu"]),
     "Bunların hiçbiri tuvalet kâğıdı gibi suda dağılmaz; dirseklerde ve kolonun döndüğü noktada birikip tıkaç oluşturur."]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Pompayla iki üç denemede sonuç alamadıysanız", "Sert bir cisim düştüyse", "Yer süzgecinden ya da başka bir giderden su geliyorsa",
                "Alt katlarda da şikâyet varsa", "Tuvalet sık sık tıkanıyorsa"]),
     "[[hizmet:tuvalet-tikanikligi-acma|Tuvalet tıkanıklığı açma]] hizmetimizde çoğu durumda klozeti sökmeden açıyoruz; sökmek gerekirse contayı yenileyip yerine takıyoruz. Fiyatı işe başlamadan söylüyoruz."]),
  ],
  "sss": [("Tuvalet tıkanırsa ne yapmalıyım?", "Sifona tekrar basmayın, rezervuarın ara musluğunu kapatın, klozetin çevresine havlu serin ve klozet pompasıyla deneyin. Sert bir cisim düştüyse pompa kullanmayın."),
          ("Alaturka tuvalet tıkanıklığı nasıl açılır?", "Geniş ağızlı bir pompa ya da spiral ile çoğu zaman açılır. Hafif kâğıt tıkanıklığında bir kova ılık suyu tek seferde dökmek işe yarayabilir; su yükseliyorsa devam etmeyin."),
          ("Tuvalete kaynar su dökülür mü?", "Hayır. Seramik ani ısıdan çatlayabilir; çok sıcak musluk suyu yeterlidir."),
          ("Islak mendil tuvaleti tıkar mı?", "Evet. Tuvalet kâğıdı gibi suda dağılmaz; tuvalet tıkanıklığının en sık sebeplerinden biridir.")]},

 {"slug": "mutfak-gideri-tikanirsa-ne-yapmali", "ikon": "evye",
  "h1": "Mutfak Gideri Tıkanırsa Ne Yapmalı? Evye ve Yağ Tıkanıklığı",
  "title": "Mutfak Gideri Tıkanırsa Ne Yapmalı? Evye ve Yağ Tıkanıklığı",
  "aciklama": "Mutfak evyesi tıkanırsa ne yapmak lazım, yağ tıkanıklığı evde nasıl açılır, bulaşık makinesi suyu neden evyeye geliyor? Adım adım rehber.",
  "ozet": "Mutfak gideri tıkandığında suçlu neredeyse her zaman yağdır. Bu yazıda evyeyi evde nasıl açmayı deneyebileceğinizi, bulaşık makinesinin suyu neden evyeye bastığını ve yağ tıkanıklığının neden geri döndüğünü anlattık.",
  "hizmet": "mutfak-gideri-acma",
  "bolum": [
   ("Mutfak gideri tıkanırsa ilk ne yapmalı?", [
     ("adim", ["Bulaşık ve çamaşır makinesini çalıştırmayın; ikisinin suyu da aynı gidere gelir.",
               "Evyedeki suyu bir kapla boşaltın ve süzgeci çıkarıp içini temizleyin.",
               "Evyenin altındaki dolabı boşaltın; sifona ulaşmanız gerekebilir.",
               "Çift gözlü evyeyse kullanmadığınız gözün giderini bir tıpa ya da ıslak bezle kapatın."])]),
   ("Evye evde nasıl açılır?", [
     ("h3", "Çok sıcak su", "Tıkanıklık yağdansa çok sıcak musluk suyu yağı yumuşatabilir. Birkaç dakika akıtın; su hiç gitmiyorsa daha fazla doldurmayın."),
     ("h3", "Pompa", "Evyeye pompanın lastiğini örtecek kadar su bırakın, diğer gözü kapatın ve kısa, kuvvetli hareketlerle pompalayın."),
     ("h3", "Sifon temizliği", "Evyenin altındaki sifonu ve bulaşık makinesi hortumunun bağlandığı parçayı altına kova koyarak sökün. İçindeki yağlı tortuyu temizleyip contalarla birlikte geri takın."),
     ("dikkat", "Sifonu söküp temizlediniz ama su yine gitmiyorsa tıkanıklık duvarın içinde ya da mutfak kolonundadır. Bu noktadan sonra evdeki aletler genellikle yetmez.")]),
   ("Bulaşık makinesinin suyu neden evyeye geliyor?", [
     "Bulaşık makinesi suyunu evyenin sifonuna ya da hemen yanındaki bağlantıya boşaltır. Hat ileride daralmışsa makinenin bir anda pompaladığı su gidecek yer bulamaz ve evyeden yükselir.",
     "Bu belirti tıkanıklığın sifonda değil, makinenin bağlandığı noktanın ilerisinde olduğunu gösterir. Makineyi ya da hortumunu değiştirmek sorunu çözmez; hattın açılması gerekir."]),
   ("Yağ tıkanıklığı neden tekrar ediyor?", [
     "Yağ borunun içinde bir halka gibi çepere yapışır. Hattın ortasından bir delik açmak suyu geçirir ama çeperdeki yağ yerinde kalır; birkaç hafta sonra yeni yağ ve artıklar ona tutunup tıkanıklık geri gelir.",
     "Kalıcı çözüm çeperi temizlemektir. Biz bu yüzden spiralle açtıktan sonra gerekirse basınçlı suyla yıkıyor, çok sık tekrarlayan durumlarda kamerayla yağın nerede toplandığına bakıyoruz.",
     ("ipucu", "Deterjanı bol kullanmak yağı ortadan kaldırmaz; sadece biraz daha ileri taşır.")]),
   ("Kimyasal açıcı evyeye dökülür mü?", [
     "Önermiyoruz. Yağ tıkanıklığında kimyasal yüzeyde bir yol açabilir ama çeperdeki yağı sökmez. Açamazsa evyede bekler ve sonraki müdahalede geri sıçrayabilir. Farklı ürünleri karıştırmak ise zehirli gaz riski taşır.",
     ("dikkat", "Kimyasal döktüyseniz pompa kullanmayın ve ustaya mutlaka söyleyin.")]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Sifonu temizlediniz ama su gitmiyorsa", "Bulaşık makinesi her çalıştığında evye doluyorsa",
                "Alt ya da üst kattaki komşuların evyesi de geri tepiyorsa", "Evye birkaç haftada bir yeniden tıkanıyorsa"]),
     "[[hizmet:mutfak-gideri-acma|Mutfak gideri açma]] hizmetimizde evyeyi ve bağlı olduğu hattı makineyle açıyor, yağı çeperden temizliyoruz. Tezgâh ve dolap sökmüyoruz."]),
   ("Mutfak gideri tıkanmasın diye ne yapabilirsiniz?", [
     ("liste", ["Kızartma yağını soğutup şişeye koyun; gidere dökmeyin.", "Yağlı tava ve tencereleri yıkamadan önce kâğıtla silin.",
                "Evyeye süzgeç takın; pirinç, telve, çay posası çöpe gitsin.", "Bulaşıktan sonra bir süre sıcak musluk suyu akıtın."])]),
  ],
  "sss": [("Mutfak gideri tıkanırsa ne yapmalıyım?", "Makineleri çalıştırmayın, evyedeki suyu boşaltın, süzgeci temizleyin. Çok sıcak su ve pompayla deneyin; olmazsa sifonu söküp temizleyin."),
          ("Bulaşık makinesi çalışınca evye neden doluyor?", "Makinenin bağlandığı noktanın ilerisinde hat daralmıştır. Makinenin bir anda boşalttığı su gidecek yer bulamayıp evyeden yükselir."),
          ("Evyeye kaynar su dökülür mü?", "Kaynar su plastik sifonu ve bağlantıları bozabilir. Çok sıcak musluk suyu yeterlidir."),
          ("Yağ tıkanıklığı neden geri geliyor?", "Ortadan açılan delik suyu geçirir ama çepere yapışan yağ kalır. Çeper temizlenmezse tıkanıklık birkaç hafta içinde geri gelir.")]},

 {"slug": "dus-gideri-nasil-acilir", "ikon": "dus",
  "h1": "Duş Gideri Nasıl Açılır? Duşta Su Birikiyorsa Ne Yapmalı",
  "title": "Duş Gideri Nasıl Açılır? Duşta Su Birikiyorsa Ne Yapmalı",
  "aciklama": "Duş gideri nasıl açılır, duşta su birikiyorsa ne yapmak lazım, banyo yer süzgeci neden kokar? Evde deneyebileceğiniz yollar ve sınırları.",
  "ozet": "Duş alırken suyun bileğinize kadar birikmesi hem can sıkıcı hem de alt kata sızma riski taşıyor. Duş ve küvet giderinin büyük kısmı saç yüzünden tıkanır ve iyi haber şu: çoğunu evde açabilirsiniz.",
  "hizmet": "banyo-gideri-acma",
  "bolum": [
   ("Duşta su birikiyorsa ilk ne yapmalı?", [
     ("adim", ["Duşu kapatın; biriken suyun derzlerden sızmasını beklemeyin.",
               "Süzgecin ızgarasını kaldırın. Vidalıysa küçük bir tornavida yeter, oturmalıysa kenarından kaldırın.",
               "Görünen saçı ve köpüğü eldivenle alın.",
               "Biriken suyu bir kapla boşaltıp süzgecin içine bakın."])]),
   ("Duş gideri evde nasıl açılır?", [
     ("h3", "Izgara altı ve hazne temizliği", "Pek çok duş süzgecinin içinde çıkarılabilen küçük bir hazne vardır. Bunu çıkarıp içindeki saç ve sabun tortusunu temizlemek çoğu zaman yeter."),
     ("h3", "Plastik dişli şerit", "Süzgeç ağzından sokup çevirerek çekin; dirsekteki saç yumağını yakalayıp dışarı çıkarır. Duş gideri için en pratik aparat budur."),
     ("h3", "Pompa", "Duş teknesine pompanın lastiğini örtecek kadar su bırakıp süzgecin üzerine tam oturtun ve kısa hareketlerle pompalayın. Küvette taşma deliğini ıslak bezle kapatmayı unutmayın."),
     ("dikkat", "Lineer, sıva altı duş giderlerinde kanalın altındaki hazneyi zorlayarak sökmeye çalışmayın; kırılırsa değişimi zahmetli olur.")]),
   ("Banyo yer süzgeci neden kokar?", [
     "Yer süzgecinin içinde kanalizasyon kokusunu tutan küçük bir su haznesi vardır. Süzgeç az kullanılıyorsa bu su buharlaşır ve koku doğrudan banyoya gelir. Ara ara bir bardak su dökmek çoğu zaman kokuyu keser.",
     "Su döktüğünüz hâlde koku geçmiyorsa haznede tortu birikmiş ya da süzgeç tıkanmaya başlamıştır."]),
   ("Duş gideri tıkanıklığı alt kata zarar verir mi?", [
     "Verebilir. Uzun süre bekleyen su, duş teknesinin kenar silikonundan ve derzlerden alttaki döşemeye sızar. Alt kattaki komşunuzun tavanında leke görünüyorsa önce gideri açmak, sonra sızıntının kaynağına bakmak gerekir.",
     ("ipucu", "Duş gideriniz yavaşladıysa silikon ve derzleri de kontrol edin; çatlak silikon sızıntıyı hızlandırır.")]),
   ("Ne zaman usta çağırmalısınız?", [
     ("liste", ["Hazneyi temizlediniz ama su yine birikiyorsa", "Duş ile birlikte lavabo ya da tuvalet de yavaşladıysa",
                "Alt kattan sızıntı şikâyeti geldiyse", "Yer süzgecinden geri su geliyorsa"]),
     "[[hizmet:banyo-gideri-acma|Banyo gideri açma]] hizmetimizde duş, küvet ve yer süzgecini süzgeç ağzından makineyle açıyoruz; fayansa ve tekneye dokunmuyoruz."]),
   ("Duş gideri tıkanmasın diye ne yapabilirsiniz?", [
     ("liste", ["Duş süzgecine saç tutucu takın.", "Haftada bir ızgarayı kaldırıp saçı temizleyin.",
                "Plaj ya da bahçe dönüşü kumlu ayakları önce dışarıda yıkayın.", "Az kullanılan yer süzgeçlerine ara ara su dökün."])]),
  ],
  "sss": [("Duş gideri nasıl açılır?", "Izgarayı kaldırıp görünen saçı alın, süzgecin haznesini temizleyin. Olmazsa plastik dişli şerit ya da pompa deneyin."),
          ("Duşta su neden birikiyor?", "Çoğu zaman süzgecin altındaki dar dirsekte toplanan saç ve sabun tortusu yüzünden. Az eğimli hatlarda kum da birikebilir."),
          ("Yer süzgecinden gelen koku nasıl geçer?", "Süzgeç az kullanılıyorsa içindeki su kurumuştur; bir bardak su dökmek kokuyu keser. Geçmiyorsa hazne temizlenmelidir."),
          ("Duş gideri açarken fayans kırılır mı?", "Hayır. Gideri süzgeç ağzından makineyle açıyoruz; fayansa ve duş teknesine dokunmuyoruz.")]},
]

REHBER_GIRIS = ("Tıkanıklıkta herkesin aklına aynı sorular geliyor: Kendim açabilir miyim? Neyi yapmamalıyım? Ne zaman birini "
                "çağırmalıyım? Bu rehberde bu soruları dürüstçe cevapladık. Evde çözebileceğiniz durumu açıkça söylüyoruz; "
                "usta gerektiren durumu da :)")

# ── Usta çağırırken dikkat edilecekler — ⛔ kimseyi isimle hedef alma, genel uyarı dili.
USTA_DIKKAT_GIRIS = [
 "Tıkanıklık acil olunca insan ilk bulduğu numarayı arıyor; çok anlaşılır. Ama cihazı olmadan gider açacağını söyleyen biri tesisatınıza zarar verebilir ve küçük bir işin masrafı büyüyebilir. Kimi çağırırsanız çağırın, aşağıdakilere dikkat edin.",
 "Gider açmak basit görünür ama yanlış yapıldığında boruyu çizebilir, contayı kaçırtabilir ya da gereksiz yere fayans kırdırabilir. Usta çağırmadan önce birkaç soruyu baştan sormanız sizi büyük masraftan kurtarır.",
 "Bize gelen çağrıların bir kısmı, daha önce birinin müdahale ettiği ve sorunun büyüdüğü işler. O yüzden kimi çağıracağınızı seçerken şunlara bakmanızı öneriyoruz.",
]
USTA_DIKKAT = [
 ("Fiyatı işe başlamadan sorun", "Usta durumu gördükten sonra fiyatı söylemeli ve onayınızı almadan işe başlamamalı. \"Bakarız, sonra konuşuruz\" cevabına dikkat edin."),
 ("Hangi cihazla geleceğini sorun", "Gider açma makine işidir: spiral makinesi, gerektiğinde basınçlı su ve kamera. Cihazı olmadan iş yapmaya çalışmak tesisata zarar verebilir."),
 ("Kırma önerisine hemen evet demeyin", "\"Burayı kırmak lazım\" deniyorsa önce kamera görüntüsü isteyin. Çoğu tıkanıklık kırmadan açılır; kırmak gerekse bile yalnızca sorunlu nokta kırılmalıdır."),
 ("Yalnız kimyasalla gelene dikkat", "Kimyasal kalıcı çözüm değildir; eski borulara ve contalara zarar verebilir, açamazsa giderde bekleyip sonraki müdahaleyi tehlikeli hâle getirir."),
 ("Ulaşabileceğiniz birini seçin", "Sorun tekrar ederse yeniden ulaşabileceğiniz, telefonu açılan ve size ne yaptığını anlatan biriyle çalışın."),
 ("Akışı birlikte test edin", "İş bitince suyu birlikte akıtın; suyun gittiğini kendi gözünüzle görmeden işi bitmiş saymayın."),
]

# ── Su kaçağı tespiti (tek sayfa; ilçe sürümü YOK) ─────────────────────────
# 2026-10-07: kullanıcı gerçek fotoğraf + video yükledi (cihazla tespit, noktasal açma, PPR onarım).
# ⛔ Fotoğrafta görünmeyen yöntem iddia etme (termal kamera, gaz yöntemi vb. YAZILMADI). ⛔ "kırmadan" DEME: su kaçağında
#    kaçak noktası açılıyor (fotoğrafta görünüyor) → doğru ifade "yalnız kaçağın olduğu noktayı açıyoruz".
SU_KACAGI = {
 "giris": "Su kaçağı tıkanıklık gibi kendini hemen göstermez. Duvarda bir nem lekesi, alt kattan gelen bir şikâyet ya da bir anda kabaran su faturası… Kaçağın tam yerini bilmeden fayansları sırayla kırmak hem pahalı hem gereksiz. Biz önce cihazla dinleyip kaçağın yerini buluyor, sonra yalnızca o noktayı açıyoruz.",
 "belirti": [
  "Bütün musluklar kapalıyken su sayacı dönmeye devam ediyor",
  "Su faturası kullanımınız değişmediği hâlde arttı",
  "Duvarda, tavanda ya da süpürgelik hizasında nem ve kabarma var",
  "Alt kattaki komşunun tavanında lekelenme başladı",
  "Banyo ya da mutfak zemininde fayans derzleri sürekli ıslak",
  "Kombinin basıncı sık sık düşüyor (ısıtma tesisatında kaçak olabilir)",
 ],
 "sayac": [
  "Evdeki bütün muslukları, rezervuarları, çamaşır ve bulaşık makinesini kapatın.",
  "Su sayacının üzerindeki küçük yıldız ya da çark şeklindeki göstergeye bakın.",
  "Gösterge hiç su kullanılmadığı hâlde dönüyorsa sayaçtan sonraki tesisatta bir kaçak var demektir.",
  "Emin olmak için sayaçtaki rakamı not edin, bir iki saat hiç su kullanmadan bekleyip yeniden bakın.",
 ],
 "yontem": [
  ("Önce dinliyoruz", "Kaçak su dinleme cihazının algılayıcısını zemine ve duvara yerleştirip borudan kaçan suyun sesini dinliyoruz. Ses en güçlü olduğu noktada kaçağa en yakın yerdeyiz demektir."),
  ("Noktayı işaretliyoruz", "Algılayıcıyı adım adım kaydırıp sesin en net geldiği noktayı buluyor ve işaretliyoruz. Açılacak yeri size bu noktada gösteriyoruz."),
  ("Yalnız o noktayı açıyoruz", "Bütün banyoyu ya da koridoru kırmıyoruz; işaretlediğimiz noktada küçük bir alan açıp boruya ulaşıyoruz."),
  ("Boruyu onarıyoruz", "Kaçak yapan bölümü kesip yeni parçayı PPR kaynak makinesiyle yerine kaynatıyoruz. Ardından hattı basınç altında deneyip kaçağın kesildiğini birlikte görüyoruz."),
 ],
 "sorumluluk": "İstanbul'da su sayacına kadar olan şebeke hattı İSKİ'nin, sayaçtan sonraki tesisat abonenin sorumluluğundadır. Sayaç dönmüyor ama sokakta su akıyorsa ya da sayaçtan önce bir kaçak görüyorsanız İSKİ'yi ALO 185'ten arayın; sayaç musluklar kapalıyken dönüyorsa kaçak evinizin içindedir ve bizi arayabilirsiniz.",
 "acil": "Tavandan su damlıyor ya da zeminden su çıkıyorsa önce sayacın yanındaki ana vanayı kapatın; vana kapanınca kaçak da durur. Elektrik prizlerine ya da aydınlatmaya su geliyorsa sigortayı da kapatın. Sonra bizi arayın; 7 gün 24 saat açığız.",
 "gizli": "Gizli su kaçağı, gözle göremediğiniz bir yerde, yani duvarın, zeminin ya da tavanın içinden geçen boruda olur. Sayaç döner, fatura artar ama ortada su yoktur; ya da su, kaçağın olduğu yerden metrelerce uzakta bir lekede ortaya çıkar. Bu yüzden lekenin olduğu yeri kırmak çoğu zaman yanlış yeri kırmak demektir. Önce dinleyip kaçağın gerçek yerini buluyoruz.",
 "sizinti": [
  ("Lavabo altı sızıntı", "Lavabonun altındaki dolapta ıslaklık varsa sebep çoğu zaman sifon contası, gevşeyen bağlantı ya da ara musluk ile batarya arasındaki fleks hortumdur. Bunlar kırma gerektirmez; parçayı değiştirip sıkılığını deniyoruz."),
  ("Klozet altı su kaçağı", "Klozetin dibinde biriken su ya klozet ile gider arasındaki contadan ya da rezervuarın bağlantısından gelir. Hangisi olduğunu ayırıp contayı ya da bağlantıyı yeniliyoruz."),
  ("Musluk sızıntısı", "Musluğun gövdesinden ya da altından sızan su, iç parçanın ya da bağlantının yorulduğunu gösterir. Yerinde bakıp parçayı ya da musluğu değiştiriyoruz."),
 ],
 "patlak": "Sıcak su borusu ya da soğuk su borusu patladığında ilk iş sayacın yanındaki ana vanayı kapatmak. Sıcak su hattıysa kombiyi de kapatın. Biz geldiğimizde patlağın yerini buluyor, o noktayı açıp patlayan bölümü kesiyor ve yeni boru parçasını PPR kaynak makinesiyle yerine kaynatıyoruz. Ardından hattı basınç altında deneyip suyu birlikte açıyoruz.",
 "fiyat": [
  ("Kaçağın yeri", "Banyo zeminindeki bir boru ile duvar içinden geçen uzun bir hat aynı iş değildir."),
  ("Açılacak alan", "Kaçağın derinliği ve üzerindeki zemin türü, açma ve kapatma işinin süresini etkiler."),
  ("Onarım", "Tek bir bağlantının değişmesi ile bozulmuş bir boru bölümünün yenilenmesi farklı emek ister."),
 ],
 "sss": [
  ("Su kaçağı kırmadan bulunur mu?", "Kaçağın yerini kırmadan, cihazla dinleyerek buluyoruz. Boruyu onarmak için ise o noktayı açmak gerekir; biz yalnızca kaçağın olduğu küçük alanı açıyoruz."),
  ("Su kaçağı olup olmadığını nasıl anlarım?", "Bütün muslukları kapatıp su sayacına bakın. Hiç su kullanılmadığı hâlde sayacın küçük göstergesi dönüyorsa sayaçtan sonraki tesisatta bir kaçak var demektir."),
  ("Su kaçağı İSKİ'nin mi sorumluluğunda?", "Sayaca kadar olan hat İSKİ'nin, sayaçtan sonraki tesisat abonenin sorumluluğundadır. Ev içindeki kaçak için İSKİ ekip göndermez."),
  ("Fiyatı ne zaman öğrenirim?", "Kaçağın yerini bulup ne kadar alanın açılacağını gördükten sonra, işe başlamadan söylüyoruz; onayınız olmadan açmıyoruz."),
 ],
}

# ── Acil su tesisatçısı (tek sayfa; ilçe sürümü YOK) ───────────────────────
# 2026-10-07: kullanıcının niş kelime listesinden (musluk, batarya, rezervuar, boru patladı, acil/gece tesisatçı).
# ⛔ YALNIZ KANITLI işler: Google yorumlarında geçen (musluk montajı, klozet montajı, iç takım değişikliği, gömme rezervuar akıntısı,
#    sıcak su sorunu) + PPR boru onarım fotoğrafı. Kombi, su sayacı, tesisat yenileme, çatı/oluk YAZILMADI.
SU_TESISAT = {
 "giris": "Tıkanıklığın yanında su tesisatının günlük arızalarına da geliyoruz: damlatan musluk, su akıtan rezervuar, sızdıran bağlantı, patlayan boru. Aracımızda ekipmanla adresinize geliyor, sorunu yerinde görüp fiyatı işe başlamadan söylüyoruz. Gece, pazar günü ve bayramda da açığız.",
 "isler": [
  ("Musluk ve batarya değişimi", "Damlatan, sızdıran ya da eskiyen lavabo, evye ve duş bataryasını söküp yenisini takıyoruz. Bazen musluğun tamamını değil yalnız iç parçasını değiştirmek yeter; yerinde bakıp söylüyoruz."),
  ("Rezervuar ve klozet iç takımı", "Rezervuar sürekli su akıtıyor, sifon düğmesi basmıyor ya da su kesilmiyorsa sorun iç takımdadır. Gömme ve dış rezervuarın iç takımını değiştiriyoruz."),
  ("Klozet montajı", "Yeni klozeti yerine oturtuyor, gider ve su bağlantısını yapıp sızdırmazlığını deniyoruz."),
  ("Boru patlağı ve sızıntı", "Patlayan ya da sızdıran sıcak ve soğuk su borusunun yalnız sorunlu noktasını açıp yeni parçayı PPR kaynak makinesiyle kaynatıyoruz."),
  ("Su kaçağı tespiti", "Sayaç dönüyor ama su görünmüyorsa kaçağın yerini cihazla dinleyerek buluyoruz. [[su-kacagi-tespiti/|Su kaçağı tespiti]] sayfamızda anlattık."),
  ("Tıkanıklık açma", "Tuvalet, lavabo, banyo ve mutfak gideri tıkanıklığını kırmadan, makineyle açıyoruz."),
 ],
 "musluk": "Musluk damlatıyorsa önce lavabonun ya da evyenin altındaki ara musluğu kapatın; damlama hemen durur ve acele etmenize gerek kalmaz. Damlamanın sebebi çoğu zaman musluğun içindeki parçanın yorulmasıdır. Geldiğimizde musluğa bakıp iç parçayı mı yoksa bataryanın tamamını mı değiştirmek gerektiğini söylüyor, fiyatı işe başlamadan veriyoruz.",
 "rezervuar": "Rezervuarın suyu klozete sürekli akıyorsa ya da rezervuar dolup durmuyorsa şamandıra ya da sifon mekanizması arızalıdır. Gömme rezervuarda bu parçalar duvardaki kapağın arkasındadır; kapağı söküp iç takımı değiştiriyoruz. Bu arada rezervuarın ara musluğunu kapatırsanız boşa akan su durur.",
 "su_gelmiyor": [
  ("Önce ana vanaya ve sayaca bakın", "Ana vana kapalı kalmış olabilir. Sayaç ve vana açıksa ve bütün evde su yoksa sebep bina ya da şebeke tarafındadır."),
  ("Şebeke kesintisi mi?", "Bütün sokakta su yoksa planlı ya da arıza kaynaklı bir kesinti olabilir. İSKİ'yi ALO 185'ten arayıp sorabilirsiniz; bu durumda tesisatçı çağırmanız gerekmez."),
  ("Yalnız bir muslukta su yoksa", "Sorun o musluğun ara vanasında, filtresinde ya da iç parçasındadır; bu bizim işimiz."),
  ("Yalnız sıcak su gelmiyorsa", "Kombinin kendisindeki arıza kombi servisinin işidir. Sıcak su hattındaki sızıntı, patlak ya da tıkalı bağlantı için bizi arayabilirsiniz."),
 ],
 "yerler": [
  ("Ev ve daire", "Daire içindeki musluk, rezervuar, bağlantı ve boru arızalarına geliyoruz."),
  ("Apartman", "Ortak kolon, bodrum kat gideri ve bina bağlantısı gibi apartmanın ortak tesisatında yönetimle birlikte çalışıyoruz."),
  ("Site", "Sitelerde blok ve ortak hat arızalarında site yönetiminin bilgisiyle çalışıyoruz."),
  ("İş yeri", "Dükkân, ofis, kafe ve restoranlarda iş saatini aksatmamak için çalışma saatini sizinle planlıyoruz."),
 ],
 "sss": [
  ("Gece ya da pazar günü tesisatçı geliyor mu?", "Evet. 7 gün 24 saat açığız; gece yarısı, sabah erken, pazar günü ve bayramda da arayabilirsiniz."),
  ("Musluk damlatıyorsa ne yapmalıyım?", "Lavabonun ya da evyenin altındaki ara musluğu kapatın, damlama durur. Sonra bizi arayın; iç parçayı mı bataryayı mı değiştirmek gerektiğini yerinde söylüyoruz."),
  ("Rezervuar sürekli su akıtıyor, ne yapmalıyım?", "Rezervuarın ara musluğunu kapatın. Sorun çoğu zaman şamandıra ya da sifon mekanizmasındadır; gömme ve dış rezervuarın iç takımını değiştiriyoruz."),
  ("Su gelmiyorsa tesisatçı mı çağırmalıyım?", "Önce ana vanaya bakın ve sokakta kesinti olup olmadığını İSKİ ALO 185'ten öğrenin. Yalnız sizin evinizde ya da tek bir muslukta su yoksa bizi arayın."),
  ("Fiyatı ne zaman öğrenirim?", "Usta sorunu yerinde gördükten sonra, işe başlamadan fiyatı söylüyor; onayınız olmadan işe başlamıyoruz."),
 ],
}
