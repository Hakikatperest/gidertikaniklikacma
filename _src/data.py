# -*- coding: utf-8 -*-
"""
gidertikaniklikacma.com veri katmanı.

⛔ Üretilen HTML'i ELLE DÜZENLEME — build.py her çalıştığında üzerine yazar.
   Değişiklik BURAYA yapılır, sonra:  python3 _src/build.py && python3 _src/denetim.py
"""

# ── Firma ───────────────────────────────────────────────────────────────────
# Kullanıcı 2026-10-07'de verdi: ad + telefon banner'dan, bölge "Anadolu Yakası" (banner'daki "Avrupa Yakası" YANLIŞ,
# o şerit kullanılmıyor). ⛔ Adres VERİLMEDİ → hizmet bölgesi işletmesi: şemada PostalAddress YOK, harita YOK.
SITE = {
    "marka":      "Gider Tıkanıklık Açma",
    "alan":       "https://gidertikaniklikacma.com",
    "cname":      "gidertikaniklikacma.com",
    "tel_goster": "0501 355 00 34",
    "tel_link":   "+905013550034",
    "wa":         "905013550034",
    "bolge":      "Anadolu Yakası",
    "hero_tema":  "koyu",
    # 2026-10-07: kullanıcı Google İşletme Profili haritasını verdi ("Çınar Dört Su Tesisatçısı markamız").
    # NAP tutarlılığı: şemada name = GBP adı, alternateName = site markası. Pin: Yunus Emre Mah., Sancaktepe
    # (OSM ters geokodlama). ⛔ Sokak/kapı no VERİLMEDİ → yalnız ilçe düzeyinde adres.
    "isletme":    "Çınar Dört Su Tesisatçısı",
    "konum_ilce": "Sancaktepe",
    "adres_sema": {"addressLocality": "Sancaktepe", "addressRegion": "İstanbul", "addressCountry": "TR"},
    "geo":        (41.01815641881674, 29.25504707594947),
    "harita":     "https://maps.google.com/?cid=14505024090943010980",
    "harita_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3010.324482972327!2d29.25504707594947!3d41.01815641881674!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14cad140b8e0e6f3%3A0xc94c328f4f2438a4!2zw4fEsW5hciBEw7ZydCBTdSBUZXNpc2F0w6fEsXPEsQ!5e0!3m2!1str!2str!4v1791370184475!5m2!1str!2str",
}

# Google Ads — boşken etiket basılmaz, tıklama dinleyicisi hiçbir şey göndermez.
ADS = {"etiket": "", "tel": "", "wa": ""}

# ✅ ONAYLI — kullanıcı 2026-10-07'de seçti ("hepsi"):
ONAYLI = ["7/24 hizmet", "ortalama 30 dakikada ulaşım", "kameralı tespit, kırmadan açma", "fiyat işe başlamadan söylenir"]
# ⚠️ Adalar ve Şile'de "ortalama 30 dakika" gerçekçi değil → data.ILCELER[*]["uzak"] = True olan ilçede bu ifade KULLANILMAZ.

# ⛔ Kullanıcı ONAYLAMADI (başka müşterinin sitesinde vardı ya da referans tasarımlarda) → denetim HATA verir.
TEYITSIZ = ["%100", "mutlu müşteri", "garanti", "lisanslı", "sigortalı", "yıllık deneyim", "yıllık tecrübe",
            "yılların tecrübesi", "ofisimiz", "merkezimiz", "ödeme iş bitince", "ödemeyi iş bitince",
            "ücret talep etmiyoruz", "ücret almıyoruz", "robot"]

# ⛔ Üstünlük iddiası (Ticari Reklam Yönetmeliği ispat ister) → denetim HATA.
YASAK_IDDIA = ["en iyi", "en ucuz", "lider", "bir numara", "1 numara", "rakipsiz", "en kaliteli", "en hızlı"]

# ── Türkçe ek tablosu ───────────────────────────────────────────────────────
# ⛔ Kodda "{ad}'da" gibi elle ek YAZMA → build.ek(i, "loc|dat|gen|abl")
#                 loc(-de)  dat(-e)  gen(-in)  abl(-den)
ILCE_EK = {
    "adalar":      ("'da", "'a",  "'ın",  "'dan"),
    "atasehir":    ("'de", "'e",  "'in",  "'den"),
    "beykoz":      ("'da", "'a",  "'un",  "'dan"),
    "cekmekoy":    ("'de", "'e",  "'ün",  "'den"),
    "kadikoy":     ("'de", "'e",  "'ün",  "'den"),
    "kartal":      ("'da", "'a",  "'ın",  "'dan"),
    "maltepe":     ("'de", "'ye", "'nin", "'den"),
    "pendik":      ("'te", "'e",  "'in",  "'ten"),
    "sancaktepe":  ("'de", "'ye", "'nin", "'den"),
    "sultanbeyli": ("'de", "'ye", "'nin", "'den"),
    "sile":        ("'de", "'ye", "'nin", "'den"),
    "tuzla":       ("'da", "'ya", "'nın", "'dan"),
    "umraniye":    ("'de", "'ye", "'nin", "'den"),
    "uskudar":     ("'da", "'a",  "'ın",  "'dan"),
}
# "Anadolu Yakası" bölge adının ekleri (hizmet sayfaları ve anasayfa)
BOLGE_EK = ("'nda", "'na", "'nın", "'ndan")

# ── Görseller ───────────────────────────────────────────────────────────────
# Kullanıcının tek görseli: yapay zekâ üretimi banner (_src/kaynak/banner-orijinal.webp).
# Sol yarısında "İstanbul Avrupa Yakası" yazıyor (YANLIŞ bölge) → yalnız sağ yarısı (usta + makaralı kamera) kırpılıp kullanılır.
# ⚠️ Gerçek saha fotoğrafı YOK → galeri bölümleri basılmaz; ⏳ kullanıcıdan saha fotoğrafı bekleniyor.
GORSEL = ("gider-tikaniklik-acma-kamerali-tespit",
          "Mutfak lavabosunun altında makaralı kamerayla gider hattını kontrol eden usta (temsilî görsel)")
SAHA_FOTO = []   # ("dosya-tabani", "dürüst alt metin") — gerçek saha fotoğrafı gelince eklenir, galeri kendiliğinden açılır


# ── Hizmetler (banner'daki 4 hizmet; her ilçede ayrı sayfa) ────────────────
# Kannibalizasyon ayrımı: lavabo = banyo/el yüzü lavabosu · banyo = duş, küvet, yer süzgeci · mutfak = evye.
# Anasayfa ("gider tıkanıklık açma") genel hedef; hizmet sayfaları alt konuya dar.
HIZMETLER = [
 {"slug":"tuvalet-tikanikligi-acma","ad":"Tuvalet Tıkanıklığı Açma","kisa":"Tuvalet tıkanıklığı açma","ikon":"klozet",
  "h1":"{ad} Tuvalet Tıkanıklığı Açma","title":"{ad} Tuvalet Tıkanıklığı Açma | Klozet, Alaturka · 7/24",
  "hub_h1":"Anadolu Yakası Tuvalet Tıkanıklığı Açma","hub_neden":"Tuvalet neden tıkanır?",
  "hub_title":"Anadolu Yakası Tuvalet Tıkanıklığı Açma | Klozet · 7/24",
  "ozet":"Klozet, asma klozet ve alaturka tuvalet tıkanıklığını çoğu zaman klozeti yerinden sökmeden, makineyle açıyoruz.",
  "isler":[
   ("Yere monte klozet","Sifon çekince yükselen suyu klozetin kendi dirseğinden spiral makineyle açıyoruz; klozet yerinde kalıyor."),
   ("Asma klozet","Gömme rezervuarlı klozette bağlantı duvarın içinde. Sökmek gerekirse contayı yenileyip sızdırmazlığı test ederek geri takıyoruz."),
   ("Alaturka tuvalet","Alaturkanın dirseği derin ve dar; spirali bu dirsekten geçirip tıkacı parçalıyor, ardından hattı suyla deniyoruz."),
   ("Düşen cisim","Diş fırçası, oyuncak, telefon kapağı… Önce kamerayla yerini görüyor, sonra iterek değil yakalayarak çıkarmaya çalışıyoruz."),
   ("Kolondan gelen tıkanma","Alt katlarda da şikâyet varsa sorun klozette değil bina kolonundadır; kolonu temizleme ağzından açıyoruz."),
   ("Koku ve fokurdama","Tıkanıklık olmadan da koku gelebilir: kuruyan sifon suyu, gevşeyen conta, tıkalı havalık. Sebebi ayırıp ona göre çözüyoruz."),
  ],
  "belirti":[
   "Sifonu çekince su klozetin ağzına kadar yükseliyor",
   "Su iniyor ama çok yavaş ve fokurdayarak iniyor",
   "Banyo yer süzgecinden tuvalet suyu geri geliyor",
   "Klozete bir cisim düştü ve o günden beri yavaş akıyor",
   "Tuvaletten geçmeyen bir koku geliyor",
   "Alt kattaki komşu kendi tuvaletinde de sorun olduğunu söylüyor",
   "Pompa ile denediniz, bir süre açıldı ama yine tıkandı",
  ],
  "oneri":[
   "Su yükseliyorsa sifona bir daha basmayın; rezervuarın suyu da eklenince klozet taşar.",
   "Rezervuarın altındaki ara musluğu kapatın; sızdıran rezervuar klozeti yavaş yavaş doldurmaya devam eder.",
   "Klozetin çevresine eski havlu serin, taşma olursa alt kata su inmesini azaltır.",
   "Sert bir cisim düştüyse pompa kullanmayın; cisim ileri gittikçe çıkarması zorlaşır.",
  ],
  "sss":[
   ("{ad}{loc} tuvalet tıkanıklığı için ne kadar sürede gelirsiniz?","[SURE] Tuvalet tıkanıklığı beklemeye gelmeyen bir iş olduğu için arama sırasında size tahmini varış süresini açıkça söylüyoruz."),
   ("Tuvalet açarken klozet sökülüyor mu?","Çoğu durumda hayır; tıkanıklığı klozetin içinden makineyle açıyoruz. Asma klozette ya da sıkışmış sert bir cisimde sökmek gerekebilir; söktüğümüzde contayı yenileyip yerine takıyoruz."),
   ("Islak mendil gerçekten tuvaleti tıkar mı?","Evet. Paketinde \"tuvalete atılabilir\" yazsa bile tuvalet kâğıdı gibi suda dağılmıyor; dirseklerde ve kolonun döndüğü noktada birikip tıkaç oluşturuyor."),
   ("Fiyatı önceden söylüyor musunuz?","Evet. Usta durumu yerinde gördükten sonra fiyatı söylüyor; onayınızı almadan işe başlamıyoruz."),
   ("Gece tuvalet tıkanırsa arayabilir miyim?","Evet. 7 gün 24 saat çalışıyoruz; gece yarısı da hafta sonu da arayabilirsiniz."),
  ]},

 {"slug":"lavabo-tikanikligi-acma","ad":"Lavabo Tıkanıklığı Açma","kisa":"Lavabo tıkanıklığı açma","ikon":"damla",
  "h1":"{ad} Lavabo Tıkanıklığı Açma","title":"{ad} Lavabo Tıkanıklığı Açma | Kırmadan · 7/24",
  "hub_h1":"Anadolu Yakası Lavabo Tıkanıklığı Açma","hub_neden":"Lavabo neden tıkanır?",
  "hub_title":"Anadolu Yakası Lavabo Tıkanıklığı Açma | Kırmadan · 7/24",
  "ozet":"Banyo ve el yüzü lavabosunda yavaş akan ya da hiç gitmeyen suyu sifondan ve hattan kırmadan açıyoruz.",
  "isler":[
   ("Sifon temizliği","Lavabonun altındaki kıvrımlı parçayı söküp içindeki saç, sabun ve diş macunu birikintisini temizliyor, contalarını kontrol ederek geri takıyoruz."),
   ("Duvar içi hat","Sifon temizse tıkanıklık duvarın içindedir. Spiral makineyi sifon çıkışından ilerletip bu bölümü açıyoruz."),
   ("Kireç ve tortu","Sert suyun bıraktığı kireç, diş macunu ve sabunla birleşip borunun içini daraltıyor; çeperi spiral uçla temizliyoruz."),
   ("Lavabo tıpası ve süzgeç","Bastır-aç tıpaların altına takılan saç yumağı en sık sebeplerden biri; tıpayı söküp mekanizmayı temizliyoruz."),
   ("Çift lavabolu banyolar","İki lavabo aynı hatta birleşiyorsa ikisi birden yavaşlar; birleşme noktasını bulup oradan açıyoruz."),
   ("Tekrarlayan tıkanıklık","Aynı lavabo birkaç haftada bir tıkanıyorsa hattın eğimine ya da çatlak bir bağlantıya kamerayla bakıyoruz."),
  ],
  "belirti":[
   "Lavabodaki su dakikalarca bekliyor, yavaş yavaş iniyor",
   "Lavabodan kötü bir koku geliyor",
   "Su giderken hırıltı ya da fokurdama sesi geliyor",
   "Lavabo tıpasının altında sürekli saç ve köpük birikiyor",
   "Banyodaki başka bir gider kullanılınca lavaboda su yükseliyor",
   "Sifonun altında ıslaklık ya da damlama var",
  ],
  "oneri":[
   "Lavaboya su dökmeye devam etmeyin; dolu lavabo hem işi zorlaştırır hem taşma riski yaratır.",
   "Kimyasal döktüyseniz bunu ustaya mutlaka söyleyin; makine çalışırken geri sıçrayabilir.",
   "Sifonu kendiniz sökecekseniz altına kova koyun ve contaları kaybetmeyin.",
   "Lavabonun bir fotoğrafını ya da kısa videosunu WhatsApp'tan gönderin; hangi ekipmanla geleceğimizi oradan anlıyoruz.",
  ],
  "sss":[
   ("{ad}{loc} lavabo tıkanıklığı için ne kadar sürede geliyorsunuz?","[SURE] Arama sırasında trafik ve iş yoğunluğuna göre size tahmini süreyi söylüyoruz."),
   ("Lavabo açmak için fayans kırılıyor mu?","Hayır. Lavabo tıkanıklığını sifondan ve sifon çıkışından makineyle açıyoruz. Kırma ancak boru kırılmış ya da çökmüşse gündeme gelir; onu da önce kamerayla görüp size gösteriyoruz."),
   ("Lavabo neden sürekli kokuyor?","En sık sebep sifonda biriken saç ve sabun tortusunun çürümesidir. Lavabo uzun süre kullanılmadıysa sifondaki su kurumuş da olabilir; o zaman kanalizasyon kokusu doğrudan içeri gelir."),
   ("Fiyatı ne zaman öğrenirim?","Fotoğraf ya da videoyla yaklaşık bilgi verebiliyoruz. Kesin fiyatı usta yerinde gördükten sonra, işe başlamadan söylüyor."),
   ("Gece ya da hafta sonu geliyor musunuz?","Evet. 7 gün 24 saat hizmet veriyoruz."),
  ]},

 {"slug":"banyo-gideri-acma","ad":"Banyo Gideri Açma","kisa":"Banyo gideri açma","ikon":"dus",
  "h1":"{ad} Banyo Gideri Açma","title":"{ad} Banyo Gideri Açma | Duş, Küvet, Yer Süzgeci · 7/24",
  "hub_h1":"Anadolu Yakası Banyo Gideri Açma","hub_neden":"Duş, küvet ve yer süzgeci neden tıkanır?",
  "hub_title":"Anadolu Yakası Banyo Gideri Açma | Duş, Küvet · 7/24",
  "ozet":"Duş teknesi, küvet ve banyo yer süzgecindeki tıkanıklığı kırmadan, süzgeç ağzından makineyle açıyoruz.",
  "isler":[
   ("Duş teknesi gideri","Duşta biriken suyun sebebi çoğu zaman süzgecin hemen altındaki dar dirsekte toplanan saç; süzgeci söküp dirseği temizliyoruz."),
   ("Küvet gideri","Küvetin taşma ve gider bağlantısı küvetin altında kalıyor; tıkanıklığı gider ağzından spiralle açıp taşma hattını da kontrol ediyoruz."),
   ("Yer süzgeci","Banyo zeminindeki süzgeçte kum, saç ve sabun birikir; ızgarayı kaldırıp sifonlu haznesini temizliyor, hattı suyla yıkıyoruz."),
   ("Duşakabin ve sıva altı gider","Sıva altı lineer giderlerde kanalın altındaki hazne kolay dolar; hazneyi açıp temizledikten sonra akışı deniyoruz."),
   ("Alt kata sızan su","Duş gideri yavaş akınca su conta ve derzlerden alt kata sızabiliyor; önce gideri açıyor, sonra sızıntının kaynağını gösteriyoruz."),
   ("Tekrarlayan tıkanma","Gider sık tıkanıyorsa hattın eğimine ve birleşme noktalarına kamerayla bakıyoruz."),
  ],
  "belirti":[
   "Duş alırken su bileğinize kadar birikiyor",
   "Küvetin suyu boşalması çok uzun sürüyor",
   "Banyo yer süzgecinden geri su ya da koku geliyor",
   "Duş gideri fokurduyor, hava çıkarıyor",
   "Alt kattaki komşunun tavanında lekelenme başladı",
   "Lavabo ya da tuvalet kullanılınca duş giderinde su yükseliyor",
  ],
  "oneri":[
   "Duş giderinin ızgarasını kaldırıp görünen saçı eldivenle alın; bazen sorun tam oradadır.",
   "Su birikiyorsa duşu kullanmaya devam etmeyin; uzun süre bekleyen su derzlerden sızabilir.",
   "Küvette pompa kullanacaksanız taşma deliğini ıslak bezle kapatın, yoksa hava oradan kaçar.",
   "Kimyasal açıcı kullandıysanız ustaya söyleyin; giderde bekleyen kimyasal geri sıçrayabilir.",
  ],
  "sss":[
   ("{ad}{loc} duş gideri için ne kadar sürede gelirsiniz?","[SURE] Arama sırasında size tahmini varış süresini söylüyoruz."),
   ("Duş gideri açarken fayans ya da tekne sökülüyor mu?","Hayır. Tıkanıklığı süzgeç ağzından makineyle açıyoruz. Duş teknesi ya da fayans ancak altındaki boru kırılmışsa gündeme gelir; bunu da önce kamerayla görüp size gösteriyoruz."),
   ("Banyo yer süzgecinden neden koku gelir?","Süzgecin içindeki küçük sifonun suyu kuruduğunda kanalizasyon kokusu doğrudan banyoya gelir. Süzgeç az kullanılıyorsa ara ara su dökmek kokuyu keser; geçmiyorsa haznede tortu birikmiştir."),
   ("Fiyatı önceden söylüyor musunuz?","Evet. Usta yerinde baktıktan sonra, işe başlamadan fiyatı söylüyor; onayınız olmadan işe başlamıyoruz."),
   ("Bayramda ya da gece arayabilir miyim?","Evet. 7 gün 24 saat açığız."),
  ]},

 {"slug":"mutfak-gideri-acma","ad":"Mutfak Gideri Açma","kisa":"Mutfak gideri açma","ikon":"evye",
  "h1":"{ad} Mutfak Gideri Açma","title":"{ad} Mutfak Gideri Açma | Evye Tıkanıklığı · 7/24",
  "hub_h1":"Anadolu Yakası Mutfak Gideri Açma","hub_neden":"Mutfak gideri neden tıkanır?",
  "hub_title":"Anadolu Yakası Mutfak Gideri Açma | Evye Tıkanıklığı · 7/24",
  "ozet":"Yağ ve yemek artığıyla tıkanan mutfak evyesini ve bağlı olduğu hattı kırmadan, makineyle açıyoruz.",
  "isler":[
   ("Evye sifonu","Evyenin altındaki sifonu ve bulaşık makinesi bağlantısını söküp içindeki yağlı tortuyu temizliyoruz."),
   ("Yağ tıkanıklığı","Soğuyup boru çeperine yapışan yağı spiral uçla söküyor, gerekirse basınçlı suyla çeperi yıkıyoruz."),
   ("Bulaşık makinesi suyu","Makine çalışınca evye doluyorsa tıkanıklık makinenin bağlandığı noktanın ilerisindedir; hattı o noktadan sonrasıyla birlikte açıyoruz."),
   ("Çift gözlü evye","İki gözün birleştiği bağlantıda yağ toplanıyor; bağlantıyı söküp temizledikten sonra iki gözü ayrı ayrı deniyoruz."),
   ("Mutfak kolonu","Apartmanda mutfaklar çoğu zaman ayrı bir kolona bağlanır; birkaç dairede birden evye doluyorsa kolonu açıyoruz."),
   ("Dükkân ve restoran mutfağı","Yoğun yağlı iş yeri mutfaklarında hattı açtıktan sonra yağın nerede biriktiğini kamerayla gösteriyoruz."),
  ],
  "belirti":[
   "Evyedeki su yavaş gidiyor, dipte yağlı bir tabaka kalıyor",
   "Bulaşık makinesi çalışınca evye doluyor",
   "Mutfak giderinden ekşi ya da çürük bir koku geliyor",
   "Çift gözlü evyenin bir gözüne su dökünce diğerinden su çıkıyor",
   "Alt katlardaki komşuların evyesi de geri tepiyor",
   "Evyenin altında, sifon bağlantısında sızıntı başladı",
  ],
  "oneri":[
   "Bulaşık ve çamaşır makinesini çalıştırmayın; ikisinin suyu da aynı gidere gelir.",
   "Evyedeki suyu bir kapla boşaltın ama üzerine sıcak su dökmeye devam etmeyin.",
   "Kızartma yağını gidere dökmeyin; soğutup şişeye koyun ya da kâğıtla silip çöpe atın.",
   "Kimyasal açıcı kullandıysanız ustaya söyleyin; evyede bekleyen kimyasal geri sıçrayabilir.",
  ],
  "sss":[
   ("{ad}{loc} mutfak gideri için ne kadar sürede gelirsiniz?","[SURE] Trafik ve iş yoğunluğuna göre değişebileceği için arama sırasında size tahmini süreyi söylüyoruz."),
   ("Mutfak gideri neden sürekli tıkanıyor?","Neredeyse her zaman yağ yüzünden. Sıcakken akan yağ borunun soğuk bölümünde donup çepere yapışıyor; üzerine gelen yemek artığıyla boru her gün biraz daha daralıyor. Sadece sifonu açmak bu yüzden kalıcı olmuyor."),
   ("Mutfak gideri açarken dolap ya da tezgâh sökülüyor mu?","Hayır. Evyenin altındaki sifondan ve temizleme noktalarından makineyle çalışıyoruz; dolabı ve tezgâhı sökmüyoruz."),
   ("Fiyatı önceden öğrenebilir miyim?","Evet. Usta durumu yerinde gördükten sonra, işe başlamadan fiyatı söylüyor."),
   ("Gece mutfak gideri taşarsa arayabilir miyim?","Evet. 7 gün 24 saat hizmet veriyoruz."),
  ]},
]

# ── Hizmete göre ilçe sayfası köprü cümlesi ─────────────────────────────────
KOPRU = {
 "tuvalet-tikanikligi-acma": "{ad}{loc} tuvalet tıkanıklığına geldiğimizde önce suyun nerede durduğunu ayırıyoruz: klozetin kendi dirseği mi, daireden kolona giden hat mı, yoksa binanın ortak kolonu mu?",
 "lavabo-tikanikligi-acma":  "{ad}{loc} lavabo çağrısında ilk iş sifonu açıp içine bakmak; sifon temizse tıkanıklığın duvar içinde mi yoksa banyonun birleşme noktasında mı olduğunu buluyoruz.",
 "banyo-gideri-acma":        "{ad}{loc} banyo giderinde önce hangi giderin hangisine bağlı olduğunu çıkarıyoruz; duş, küvet ve yer süzgeci çoğu zaman aynı hatta birleşiyor ve tıkanıklık birleşme noktasında oluyor.",
 "mutfak-gideri-acma":       "{ad}{loc} mutfak giderinde ilk sorumuz şu: sorun yalnız sizin evyenizde mi, yoksa alt ya da üst katlarda da var mı? Cevaba göre ya evyeyi ya mutfak kolonunu açıyoruz.",
}

# ── Müşteri yorumları ───────────────────────────────────────────────────────
# ⛔ YALNIZ GERÇEK yorum (Google İşletme Profili vb.). Uydurma yorum = Google yaptırımı + Ticari Reklam Yönetmeliği.
# Biçim: ("Ad S.", "İlçe", puan 1-5, "yorum metni", "Google yorumu")   Boşken bölüm sitede görünmez, aggregateRating basılmaz.
YORUMLAR = []

# ── İlçeler ─────────────────────────────────────────────────────────────────
# Alanlar: yapi (yapı stoğu) · gider (daire/bina içi) · dis (bina dışı hat) · saha (sahada dikkat) · uzak (30 dk geçerli değil)
# mahalle: ⛔ sayfa AÇILMAZ, yalnız metinde geçer (ölçeklendirilmiş içerik riski).
ILCELER = [{'ad': 'Adalar',
  'slug': 'adalar',
  'komsu': ['maltepe', 'kartal', 'kadikoy'],
  'mahalle': ['Maden', 'Nizam', 'Heybeliada', 'Burgazada', 'Kınalıada'],
  'yapi': "Adalar'da Büyükada'nın Maden ve Nizam taraflarında, Heybeliada ve Burgazada'da asırlık ahşap köşkler, kagir konaklar ve eski taş evler "
          "var. Kınalıada'da daha çok betonarme yazlık apartmanlar görülüyor. Pek çok yapı tarihî koruma altında; içerideki tesisat ise onlarca yıl "
          'içinde parça parça yenilenmiş, eski ile yeni karışık.',
  'gider': 'Ahşap köşklerde gider boruları çoğu zaman sonradan döşeme altından ya da duvar dışından geçirilmiş; eğimler ve dirsekler alışılmışın '
           'dışında. Kışın kapalı kalan yazlıklarda sifonlar kuruyor, borularda tortu sertleşiyor. Yazın nüfus birden artınca, aylarca az çalışmış '
           'hatlar yükü kaldıramayıp tıkanmaya başlıyor.',
  'dis': 'Kayalık ve eğimli arazide bahçe hatları taş duvarların, eski bahçe merdivenlerinin altından geçebiliyor; çam ve ağaç kökleri bu hatlarda '
         "sık karşımıza çıkıyor. Adalar'da da kanalizasyon şebekesi İSKİ'nin, ama eski yapıların bir kısmında evin şebekeye nereden bağlandığı "
         'bilinmiyor; kamerayla önce bunu buluyoruz.',
  'saha': "Adalar'da motorlu araç yok, ekipmanı vapurla ya da deniz taksiyle karşıya geçiriyor, iskeleden eve el arabasıyla ve elde taşıyoruz. "
          'Yokuşlu sokaklar ve uzak koylardaki evler bu taşımayı uzatıyor. O yüzden adaya geçmeden videoya bakıp hangi makineyi alacağımızı '
          'netleştiriyoruz; ikinci sefer geri dönmek burada saatler demek.',
  'uzak': True},
 {'ad': 'Ataşehir',
  'slug': 'atasehir',
  'komsu': ['kadikoy', 'umraniye', 'maltepe', 'sancaktepe'],
  'mahalle': ['Atatürk',
              'Barbaros',
              'İçerenköy',
              'Kayışdağı',
              'Küçükbakkalköy',
              'Yenisahra',
              'Ferhatpaşa',
              'Esatpaşa',
              'Yeni Çamlıca',
              'Mustafa Kemal',
              'Örnek',
              'Fetih',
              'İnönü',
              'Mevlana'],
  'yapi': "Ataşehir'in batı yakasında, Atatürk ve Barbaros mahallelerinde doksanlarda kurulmuş büyük siteler ve Finans Merkezi çevresindeki rezidans "
          "kuleleri var. İçerenköy ve Küçükbakkalköy'de eski apartmanlar ile depo ve atölyeler iç içe; Ferhatpaşa, Esatpaşa ve Kayışdağı "
          'yamaçlarında ise gecekondudan dönüşen, sonradan kat eklenmiş bitişik nizam binalar çoğunlukta.',
  'gider': 'Rezidans ve yüksek bloklarda kolon çok uzun; üst katlardan inen su zemin katlara geldiğinde ciddi bir hıza ulaşıyor ve mutfak yağı alt '
           "dirsekte toplanıyor. Ferhatpaşa ve Esatpaşa'da kat eklenmiş binalarda ise farklı dönemlerde döşenmiş, birbirine uymayan çapta borular "
           'birleşmiş durumda. Daire içinde en sık sorun, ankastre mutfaklarda tezgâhın altına sıkıştırılmış sifonlar.',
  'dis': 'Büyük sitelerde bloklardan çıkan hatlar önce sitenin kendi kanalına toplanıyor, sonra sokağa bağlanıyor; bu ortak hat sitenin '
         "sorumluluğunda. Kayışdağı ve Ferhatpaşa'nın eğimli arazisinde bina bağlantıları kısa ama dik, yağmur suyu da çoğu zaman aynı rögara "
         "giriyor. İçerenköy'de atölyelerden gelen talaş ve tortu bina bağlantılarını beklenmedik yerde tıkayabiliyor.",
  'saha': "Ataşehir'deki sitelerin çoğunda güvenlik kulübesi var; aracın içeri girmesi için yönetimin ya da sizin güvenliğe haber vermeniz işimizi "
          "çok hızlandırıyor. Rezidanslarda yük asansörü ve otopark girişi kuralları farklı oluyor. Kozyatağı kavşağı, D-100 ve TEM'in kesiştiği "
          'bölgede yoğun saatlerde güzergâhı anlık trafiğe göre seçiyoruz.',
  'uzak': False},
 {'ad': 'Beykoz',
  'slug': 'beykoz',
  'komsu': ['uskudar', 'umraniye', 'cekmekoy', 'sile'],
  'mahalle': ['Kavacık',
              'Rüzgarlıbahçe',
              'Göksu',
              'Anadolu Hisarı',
              'Kanlıca',
              'Çubuklu',
              'Paşabahçe',
              'Yalıköy',
              'Anadolu Kavağı',
              'Acarlar',
              'Çiğdem',
              'Soğuksu',
              'Tokatköy',
              'Riva',
              'Polonezköy'],
  'yapi': "Beykoz'un Boğaz kıyısında Anadolu Hisarı, Kanlıca ve Çubuklu'da yalılar ve eski ahşap evler var. Kavacık ve Rüzgarlıbahçe köprü "
          'bağlantısının etrafında apartmanlar ve plazalarla kalabalıklaşmış durumda. Acarlar ve Çiğdem tarafında korunaklı villa siteleri, Riva ve '
          "Polonezköy'de ise orman içinde dağınık müstakil evler ve hafta sonu evleri yer alıyor.",
  'gider': 'Yalı ve eski Boğaz evlerinde tesisat genelde birkaç kez yenilenmiş, eski ve yeni borular aynı hatta çalışıyor; bu geçişler tıkanmaya '
           'açık noktalar. Villa sitelerinde banyo sayısı fazla, ancak bu banyoların hepsi tek bir ana çıkışa bağlanıyor ve yükü bu çıkış taşıyor. '
           'Kavacık apartmanlarında ise klasik mutfak kolonu yağlanması öne çıkıyor.',
  'dis': "Beykoz'un iç kesimleri ormanlık; Riva, Polonezköy ve bazı köy mahallelerinde şebekeye bağlı olmayan, fosseptikle çalışan evler var. "
         'Korunaklı sitelerdeki villalarda evden sokağa giden hat upuzun, yaşlı ağaçların kökleri de bu hattı sarıyor. Boğaz kıyısındaki yalılarda '
         'ise gider denize yakın kotta toplanıyor; eğim az olduğu için bağlantı borusu kolayca çamurla doluyor.',
  'saha': "Beykoz'un mesafeleri geniş: Kavacık'a köprü çıkışından hemen ulaşırken Riva veya Anadolu Kavağı'na orman yolundan gitmek ayrı bir "
          'yolculuk. Sahil yolu tek şeritli ve dar, park yeri az. Villa sitelerinde güvenlik kaydı istendiği için adınızı ve blok bilginizi önceden '
          'alıyoruz; yalılarda çalışırken eşyaları koruyup ortalığı temiz bırakıyoruz.',
  'uzak': False},
 {'ad': 'Çekmeköy',
  'slug': 'cekmekoy',
  'komsu': ['umraniye', 'sancaktepe', 'beykoz', 'sile'],
  'mahalle': ['Taşdelen',
              'Ömerli',
              'Alemdağ',
              'Reşadiye',
              'Hamidiye',
              'Mehmet Akif',
              'Çatalmeşe',
              'Nişantepe',
              'Sultançiftliği',
              'Ekşioğlu',
              'Kirazlıdere',
              'Merkez'],
  'yapi': "Çekmeköy'ün ilçe merkezi, Mehmet Akif ve Hamidiye tarafı son yirmi yılda yapılmış apartman ve sitelerle dolu. Taşdelen ve Nişantepe'de "
          'bahçeli müstakil evler ve villa siteleri öne çıkıyor. Ömerli, Reşadiye ve Alemdağ gibi kuzey mahallelerinde ise köy dokusu sürüyor; '
          'barajın etrafında az katlı evler ve çiftlik tipi yapılar var.',
  'gider': 'Yeni sitelerde ortak sorun, inşaattan kalan harç ve beton parçalarının ilk yıllarda hattı daraltması. Villalarda zemin kat ve bodrumdaki '
           "banyolar ana çıkışa yakın olduğu için tıkanıklık önce orada kendini gösteriyor. Taşdelen'deki eski müstakil evlerde ise mutfak gideri "
           'çoğu zaman doğrudan bahçeye, uzun ve eğimi az bir hatla çıkıyor.',
  'dis': 'Ömerli barajının koruma havzası ilçenin önemli bir bölümünü kaplıyor; şebekenin ulaşmadığı ya da yeni ulaştığı yerlerde fosseptikli evler '
         'hâlâ var. Villa sitelerinde bahçe hattı uzun, peyzaj ağaçlarının kökleri hattı sarıyor. Yağmurlu havalarda eğimli bahçelerden toprak ve '
         'kum rögara dolarak bağlantı borusunu doldurabiliyor.',
  'saha': "Çekmeköy'de mahalleler arasındaki mesafe kısa görünse de bağlantılar Alemdağ Caddesi ve Şile yoluna dayanıyor; akşam trafiğinde Kuzey "
          'Marmara Otoyolu bağlantısını değerlendiriyoruz. Villa ve site girişlerinde güvenlik onayı gerekiyor. Ömerli ve Reşadiye gibi köy '
          'mahallelerinde adresi tarif etmek zor olabildiği için konum paylaşmanızı istiyoruz.',
  'uzak': False},
 {'ad': 'Kadıköy',
  'slug': 'kadikoy',
  'komsu': ['uskudar', 'atasehir', 'maltepe'],
  'mahalle': ['Caferağa',
              'Osmanağa',
              'Rasimpaşa',
              'Fenerbahçe',
              'Feneryolu',
              'Göztepe',
              'Erenköy',
              'Suadiye',
              'Bostancı',
              'Caddebostan',
              'Kozyatağı',
              'Koşuyolu',
              'Fikirtepe',
              'Hasanpaşa',
              'Zühtüpaşa',
              'Sahrayıcedit'],
  'yapi': "Kadıköy'de iki ayrı dünya var. Moda, Yeldeğirmeni ve Osmanağa tarafında elli altmış yıllık, ışıklığı olan dar cepheli apartmanlar "
          "sıralanıyor; Bağdat Caddesi boyunca Erenköy, Suadiye ve Bostancı'da ise eski köşklerin yerine yapılmış yenilenmiş binalar ve kentsel "
          'dönüşümden çıkmış yeni bloklar çoğunlukta. Fikirtepe ise neredeyse baştan sona şantiyeden yükselen yeni yapılardan oluşuyor.',
  'gider': 'Eski Kadıköy apartmanlarında kolonlar çoğu zaman pik döküm; içi yıllar içinde pas ve yağla daralmış durumda. Üst katlarda yapılan banyo '
           'tadilatlarında yatay hatlara yeterli eğim verilmediği için dairenin kendi gideri ağır akıyor. Mutfak kolonunda biriken yağ ise en çok '
           'zemin ve bodrum katlarda geri tepme olarak ortaya çıkıyor.',
  'dis': 'Bağdat Caddesi ile sahil arasında kalan bölge kısmen dolgu zemin üstünde; burada bina bağlantı borusunun oturma yapması ve eğimini '
         'kaybetmesi sık karşılaştığımız bir durum. Eski bahçeli binalarda çınar ve çam kökleri parsel bacasına giren borunun eklerinden içeri '
         "sızıyor. Fikirtepe'de ise dönüşüm inşaatlarından gelen harç ve beton kalıntısı komşu binaların bağlantılarını daraltabiliyor.",
  'saha': 'Moda, Kadıköy çarşısı ve Bahariye çevresinde araç park etmek neredeyse imkânsız, sokakların bir kısmı da yaya düzeninde. Bu yüzden '
          "taşınabilir spiral makine ve kamerayı elde taşıyacak şekilde hazırlanıyoruz. Bağdat Caddesi'nin yoğun saatlerinde ara sokaklardan "
          'dolaşıyor, binaya gelmeden önce yöneticiyle ya da kapıcıyla konuşup bodrum anahtarını hazır ettiriyoruz.',
  'uzak': False},
 {'ad': 'Kartal',
  'slug': 'kartal',
  'komsu': ['maltepe', 'pendik', 'sultanbeyli', 'sancaktepe'],
  'mahalle': ['Atalar',
              'Cumhuriyet',
              'Çavuşoğlu',
              'Esentepe',
              'Gümüşpınar',
              'Hürriyet',
              'Karlıktepe',
              'Kordonboyu',
              'Orhantepe',
              'Orta',
              'Petrol İş',
              'Soğanlık Yeni',
              'Topselvi',
              'Uğur Mumcu',
              'Yakacık Çarşı',
              'Yukarı'],
  'yapi': "Kartal'da sahile yakın Kordonboyu, Atalar ve Orta mahallesinde eski çarşı dokusu ile yaşlı apartmanlar iç içe. Yakacık ve Esentepe tarafı "
          "yamaca yayılmış, sonradan büyümüş bir yerleşim; Soğanlık ve Uğur Mumcu'da yeni siteler çoğalırken eski sanayi alanlarının yerinde yüksek "
          'konut projeleri yükseliyor.',
  'gider': 'Kartal çarşısının çevresindeki eski binalarda zemin katlar dükkân olduğu için kolonun dibine hem konut hem işyeri atığı iniyor. '
           "Yakacık'taki yamaç binalarında ise daire hatları kısa ama kolon dik; yükten gelen su alt kattaki ilk dirsekte hızlanıp çarpıyor, ıslak "
           'mendil ve kâğıt orada takılıp kalıyor.',
  'dis': "Yakacık ve Karlıktepe'de bahçe hatları yokuş aşağı uzun bir yol izleyip sokağa bağlanıyor; bu hatların eski beton boruları çatlakta kök "
         'alabiliyor. Sahil tarafında ise düz arazide bina bağlantısı yavaş akıyor. Eski sanayi bölgesindeki dönüşüm şantiyeleri çevresinde sokak '
         'hattına toprak karışması da dikkat ettiğimiz bir şey.',
  'saha': "Kartal merkezde ve çarşı içinde araç durdurmak zor; ekipmanı taşınabilir tutup aracı biraz geride bırakıyoruz. Yakacık'a çıkan yokuşlarda "
          "kışın sabah saatlerinde yol kayganlaşabiliyor, onu hesaba katıyoruz. Soğanlık'taki büyük sitelerde blok numarasını ve hangi kapıdan "
          'gireceğimizi baştan söylemeniz işimizi çok kolaylaştırıyor.',
  'uzak': False},
 {'ad': 'Maltepe',
  'slug': 'maltepe',
  'komsu': ['kadikoy', 'atasehir', 'kartal', 'sancaktepe'],
  'mahalle': ['Altayçeşme',
              'Altıntepe',
              'Aydınevler',
              'Bağlarbaşı',
              'Başıbüyük',
              'Büyükbakkalköy',
              'Çınar',
              'Esenkent',
              'Feyzullah',
              'Fındıklı',
              'Girne',
              'Gülensu',
              'Gülsuyu',
              'İdealtepe',
              'Küçükyalı',
              'Zümrütevler'],
  'yapi': "Maltepe'de sahil şeridindeki İdealtepe, Küçükyalı ve Altayçeşme'de 70'ler ve 80'lerden kalma apartmanlar hızla kentsel dönüşümle "
          "yenileniyor. E-5'in kuzeyinde Gülsuyu, Gülensu ve Başıbüyük yamaçlarında gecekondudan dönüşen, kat eklenmiş binalar var; Büyükbakkalköy "
          'tarafında ise bahçeli siteler, villa tipi yapılar ve kooperatif blokları ağırlıkta.',
  'gider': 'Eski sahil apartmanlarında kolonlar çoğu zaman pik döküm ve yarım asırlık; içi kireç ve yağ tortusuyla daralmış oluyor. Dönüşüm görmemiş '
           'binalarda yenilenmiş bir dairenin plastik borusu eski kolona bağlanıyor ve tıkanıklık genelde tam o geçiş noktasında, iki farklı '
           'malzemenin buluştuğu ek yerinde çıkıyor.',
  'dis': 'Sahile yakın düz arazide bina bağlantı hatlarının eğimi az olduğu için atık su yavaş akıyor ve parsel bacasında tortu birikiyor. Yamaç '
         'mahallelerinde ise tersine, dik inen hat ile sokak arasında yapılmış gelişigüzel bağlantılar sorun çıkarıyor. Yan parselde süren dönüşüm '
         'inşaatının çamuru ve molozu da bahçe hattına karışabiliyor.',
  'saha': "İdealtepe ve Küçükyalı'nın ara sokaklarında park yeri neredeyse yok, o yüzden makineyi elde taşıyacak şekilde hazırlanıyoruz. Gülsuyu ve "
          "Başıbüyük'ün dik yokuşlarında aracı uygun yere bırakıp yürüyoruz; Büyükbakkalköy sitelerinde de güvenliğe önceden haber vermeniz girişi "
          'kısaltıyor; yoksa kapıda telefonla onay beklemek zaman yiyor.',
  'uzak': False},
 {'ad': 'Pendik',
  'slug': 'pendik',
  'komsu': ['kartal', 'tuzla', 'sultanbeyli'],
  'mahalle': ['Batı',
              'Doğu',
              'Çamçeşme',
              'Çınardere',
              'Dumlupınar',
              'Esenyalı',
              'Fevzi Çakmak',
              'Güzelyalı',
              'Harmandere',
              'Kavakpınar',
              'Kaynarca',
              'Kurtköy',
              'Sülüntepe',
              'Velibaba',
              'Yenişehir'],
  'yapi': "Pendik'in sahil tarafında Batı, Doğu ve Güzelyalı'da eski apartmanlar ile yazlıktan kalma binalar duruyor. Kaynarca, Velibaba ve Esenyalı "
          "sık yapılaşmış, gecekondudan apartmana dönmüş mahalleler. Kurtköy ve Yenişehir'de ise havalimanı çevresinde son yıllarda yükselen büyük "
          'siteler, rezidanslar ve iş merkezleri çoğunlukta.',
  'gider': "Kaynarca ve Velibaba'daki sonradan kat çıkılmış binalarda kolon çapı yeni kat sayısına göre küçük kalabiliyor; yoğun saatlerde alt "
           "katlarda geri tepme bundan oluyor. Kurtköy'ün yeni sitelerinde ise daire içi tesisat düzgün, ama inşaat artığı harç ve silikon parçaları "
           'ilk yıllarda süzgeç ve sifonlarda karşımıza çıkıyor.',
  'dis': 'Sahil mahallelerinde eski yazlıkların bahçe hatları bazen planına uymayan yollardan sokağa bağlanmış oluyor ve parsel bacası '
         "bulunamayabiliyor. Kurtköy ve Yenişehir'de geniş sitelerin uzun iç hatları ve çok sayıda rögarı var. Esenyalı ve Kavakpınar'da çevredeki "
         'dönüşüm inşaatları sokak hattına çamur taşıyabiliyor.',
  'saha': "Pendik'te D-100 ile sahil arasındaki dar sokaklarda araç sığdırmak zor, Kaynarca'da da pazar kurulan günler işi yavaşlatıyor. Kurtköy "
          'tarafına çoğunlukla otoyol bağlantısından giriyoruz; havalimanı çevresindeki sitelerde güvenlik kayıtlı ziyaret istiyor, geleceğimizi '
          'önceden bildirmeniz kapıda beklemeyi kısaltıyor; otoparka inip inemeyeceğimizi de sorarsanız iyi olur.',
  'uzak': False},
 {'ad': 'Sancaktepe',
  'slug': 'sancaktepe',
  'komsu': ['atasehir', 'umraniye', 'maltepe', 'sultanbeyli'],
  'mahalle': ['Abdurrahmangazi',
              'Akpınar',
              'Atatürk',
              'Emek',
              'Eyüp Sultan',
              'Fatih',
              'Hilal',
              'İnönü',
              'Kemal Türkler',
              'Meclis',
              'Merve',
              'Osmangazi',
              'Paşaköy',
              'Sarıgazi',
              'Veysel Karani',
              'Yenidoğan'],
  'yapi': "Sancaktepe; Sarıgazi, Samandıra ve Yenidoğan'ın birleşmesiyle kurulmuş genç bir ilçe. Sarıgazi ve Yenidoğan'da gecekondudan apartmana "
          "dönmüş sık yapılaşma, Samandıra çevresinde ve Abdurrahmangazi'de yeni siteler ve toplu konutlar var. Paşaköy'de ise ilçenin kırsala "
          'yakın, bahçeli müstakil evlerden ve eski köy evlerinden oluşan yüzü sürüyor.',
  'gider': "Sarıgazi ve Yenidoğan'da aşama aşama büyümüş binalarda her katın tesisatı farklı dönemde yapılmış; kolonda çap değişen, ek yeri çok "
           'noktalar tıkanmaya açık. Yeni toplu konutlarda ise kalabalık aileler ve yoğun kullanım yüzünden mutfak ve banyo hatları hızlı '
           'yükleniyor, sorun genelde kat bağlantısında başlıyor.',
  'dis': "İlçenin hızlı büyümesi yüzünden bazı sokaklarda bina bağlantısı ana hatta sonradan, düzensiz eğimle eklenmiş. Paşaköy'deki bahçeli evlerde "
         'uzun bahçe hatları ve ağaç kökü sık sorun. Yeni yol ve metro çalışmalarının, dönüşüm şantiyelerinin çevresinde de sokak bağlantısına çamur '
         've moloz karışabiliyor.',
  'saha': "Sancaktepe'ye çoğunlukla TEM ve Kuzey Marmara bağlantılarından ya da Ataşehir üzerinden giriyoruz. Sarıgazi'nin iç sokakları dar ve "
          'eğimli, çarşı saatlerinde araç ilerlemiyor. Samandıra çevresindeki büyük sitelerde blok ve kapı numarasını önceden bilmek yarım saatlik '
          "kaybı önlüyor; Paşaköy'de ise ev numarasından çok tarif işe yarıyor.",
  'uzak': False},
 {'ad': 'Şile',
  'slug': 'sile',
  'komsu': ['beykoz', 'cekmekoy'],
  'mahalle': ['Balibey', 'Çavuş', 'Hacı Kasım', 'Kumbaba'],
  'yapi': "Şile'de merkezdeki Balibey, Çavuş ve Hacı Kasım'da az katlı apartmanlar ve pansiyonlar var. Sahil boyunca, Kumbaba ve Sahilköy tarafında "
          "yazlık siteler ile yaz aylarında dolan müstakil evler yer alıyor. Ağva'da dere kenarında butik oteller ve ahşap evler, iç kesimdeki köy "
          'mahallelerinde ise bahçeli tek katlı evler çoğunlukta.',
  'gider': 'Yazlıklarda gider aylarca kullanılmıyor; kışın sifonlardaki su buharlaşıyor ya da donuyor, kireç ve tortu borulara yapışıyor. Sezon '
           'başında evler açıldığında ilk günlerde gelen şikâyetler genelde bu yüzden. Pansiyon ve otellerde ise yaz yoğunluğunda aynı anda çok '
           'sayıda banyonun kullanılması, tek bir kolonu kapasitesinin üstünde zorluyor.',
  'dis': "Şile'nin önemli bir bölümünde, özellikle köy mahallelerinde ve bazı yazlıklarda fosseptik kullanılıyor; dolu bir fosseptik evdeki tüm "
         "giderlerin ağırlaşmasına yol açıyor. Kumsala yakın evlerde bahçe hattına kum giriyor. Ağva'da Göksu ve Yeşilçay derelerinin kenarındaki "
         'yapılarda zemin suyu yüksek olduğu için rögarlar yağışlı havada çabuk doluyor.',
  'saha': 'Şile, Anadolu yakasının içinden bakınca uzak bir ilçe; Şile yolu üzerinden ormanın içinden geçerek ulaşıyoruz. Yaz hafta sonlarında bu '
          'yol çok yoğunlaşıyor, kışın ise yağışlı ve sisli havalarda yavaş gitmek gerekiyor. Ağva ve köy mahallelerinde adresler net olmadığı için '
          'konum paylaşmanız işimizi gerçekten kolaylaştırıyor.',
  'uzak': True},
 {'ad': 'Sultanbeyli',
  'slug': 'sultanbeyli',
  'komsu': ['sancaktepe', 'kartal', 'pendik'],
  'mahalle': ['Abdurrahmangazi',
              'Adil',
              'Ahmet Yesevi',
              'Akşemsettin',
              'Battalgazi',
              'Fatih',
              'Hamidiye',
              'Hasanpaşa',
              'Mecidiye',
              'Mehmet Akif',
              'Mimar Sinan',
              'Necip Fazıl',
              'Orhangazi',
              'Turgut Reis',
              'Yavuz Selim'],
  'yapi': "Sultanbeyli kısa sürede kendiliğinden büyümüş bir ilçe; Fatih Bulvarı'nın iki yanında ve Battalgazi, Hasanpaşa, Mehmet Akif gibi "
          'mahallelerde tek katlı evlerin üstüne katlar çıkılarak oluşmuş apartmanlar çoğunlukta. Son yıllarda dönüşüm projeleriyle yer yer yeni '
          'bloklar yükseliyor, ama dokunun büyük kısmı hâlâ bitişik nizam, sık apartman.',
  'gider': 'Katlar zamanla eklendiği için bir binada farklı ustaların farklı çapta döşediği borular yan yana çalışıyor. Kolonun dirsek ve redüksiyon '
           'yaptığı yerlerde atık takılıyor; özellikle zemin kat ve bodrum dairelerde üst katların suyu geri tepiyor. Kalabalık hanelerde mutfak '
           'hattı da kısa sürede yağla daralıyor.',
  'dis': 'Yamaçlara yayılmış sokaklarda bina bağlantıları kimi zaman ana hatta sonradan ve gelişigüzel eklenmiş. Bahçe hatları kısa olsa da parsel '
         'bacası olmayan, bağlantının toprak altından doğrudan sokağa gittiği yapılar var. İlçenin kuzeyi su havzasına yakın, bu yüzden taşan atık '
         'suyu bahçeye ya da dereye yönlendirmek kesinlikle olmaz.',
  'saha': "Sultanbeyli'de Fatih Bulvarı ana eksen; akşam saatlerinde yoğunlaşıyor, iç mahallelere ara yollardan geçiyoruz. Sokaklar dar ve dik "
          'olduğu için aracı yukarıda bırakıp makineyi elde indirmemiz gerekebiliyor. Sokak tabelası eksik yerler olduğundan yakındaki cami, okul ya '
          'da market gibi bir işaret söylemeniz bizi doğru kapıya getiriyor.',
  'uzak': False},
 {'ad': 'Tuzla',
  'slug': 'tuzla',
  'komsu': ['pendik', 'kartal'],
  'mahalle': ['Akfırat',
              'Anadolu',
              'Aydınlı',
              'Aydıntepe',
              'Cami',
              'Evliya Çelebi',
              'Fatih',
              'İçmeler',
              'İstasyon',
              'Mescit',
              'Mimar Sinan',
              'Orhanlı',
              'Postane',
              'Şifa',
              'Tepeören',
              'Yayla'],
  'yapi': "Tuzla'da sahildeki Cami, İstasyon ve Postane mahallelerinde eski yazlık siteler ve alçak apartmanlar var. Aydınlı ve İçmeler tersaneler "
          "bölgesinin çevresinde işçi konutlarıyla büyümüş; Akfırat ve Orhanlı'da son yıllarda yükselen yeni siteler, Tepeören'de ise hâlâ köy "
          'dokusuna yakın müstakil evler görülüyor.',
  'gider': 'Sahildeki eski yazlıklarda tesisat yıl boyu kullanılmak için yapılmamış; borular ince, eğimler gelişigüzel. Kışın evde oturulmaya '
           "başlanınca bu hatlar yükü kaldıramıyor. Akfırat'ın yeni bloklarında ise sorun daha çok mutfak kolonunda; çok katlı binada yağ aşağıya "
           'inene kadar soğuyup kolon dibinde birikiyor.',
  'dis': "Tuzla'da tersane, organize sanayi ve deri, kimya gibi sanayi bölgeleri konutlara yakın; işyeri hatlarında yağ, metal tozu ve endüstriyel "
         "artık başka bir iş demek. Sahil dolgu kesimlerinde düz arazi yüzünden bahçe hatları yavaş akıyor, Tepeören'in müstakil evlerinde de uzun "
         'bahçe hatlarında kök sık çıkıyor.',
  'saha': "Tuzla geniş bir ilçe; sahilden Tepeören'e gitmek ayrı bir yol, o yüzden aradığınızda tam yeri sormamız önemli. Tersane bölgesinde vardiya "
          "çıkışlarında trafik yoğunlaşıyor. Akfırat ve Orhanlı'daki sitelerde güvenlik kapıda kimlik soruyor; sanayi tesislerinde ise iş güvenliği "
          'girişini sizinle önceden ayarlıyoruz.',
  'uzak': False},
 {'ad': 'Ümraniye',
  'slug': 'umraniye',
  'komsu': ['uskudar', 'atasehir', 'cekmekoy', 'sancaktepe'],
  'mahalle': ['Atakent',
              'Çakmak',
              'Şerifali',
              'Yukarı Dudullu',
              'Aşağı Dudullu',
              'Tantavi',
              'Ihlamurkuyu',
              'Altınşehir',
              'Esenşehir',
              'Madenler',
              'Namık Kemal',
              'Hekimbaşı',
              'Armağanevler',
              'Saray',
              'Elmalıkent'],
  'yapi': 'Ümraniye hızlı büyümüş bir ilçe. Atakent, Tantavi ve Saray çevresinde yeni siteler ve iş merkezleri yükseliyor; Çakmak, Ihlamurkuyu ve '
          "Madenler'de gecekondudan apartmana dönüşmüş, sonradan kat çıkılmış bitişik binalar sık. Dudullu ve Şerifali tarafında ise organize sanayi "
          'bölgesi, depolar ve atölyeler konutlarla aynı caddeyi paylaşıyor.',
  'gider': 'Kat eklenen eski binalarda alttaki boru çapı üstteki banyo ve mutfakların yükünü kaldırmıyor; özellikle giriş katta tuvaletten geri '
           'gelme şikâyeti bu yüzden çok. Yeni sitelerde ise sorun daha çok daire içinde: tezgâh altında bulaşık makinesi bağlantısının sifona '
           'yanlış takılması ve plastik boruların sarkması. Kolon temizleme kapağı eski binalarda çoğu zaman sıva altında kalmış.',
  'dis': 'Çakmak ve Madenler gibi yamaç mahallelerde bina bağlantıları yıllar içinde elle eklenmiş, bazı yerlerde komşu binanın hattından geçiyor. '
         "Bu yüzden bir binadaki tıkanıklık bitişikteki binayı da etkileyebiliyor. Dudullu ve Şerifali'deki iş yerlerinde yemekhane ve üretim atığı "
         'bağlantı hattına yağ ve tortu bırakıyor; Elmalıkent tarafında ise bahçeli evlerde kök sorunu görülüyor.',
  'saha': "Ümraniye'nin ana arterleri akşam saatlerinde dolu; TEM ve Kuzey Marmara bağlantılarını kullanarak mahalleye arkadan girmeyi tercih "
          "ediyoruz. Dudullu OSB'deki iş yerlerinde vardiya saatleri ve fabrika giriş kuralları olduğu için gelmeden önce kiminle görüşeceğimizi "
          "soruyoruz. Çakmak'ın dik sokaklarında aracı düz bir yere bırakıp çıkıyoruz.",
  'uzak': False},
 {'ad': 'Üsküdar',
  'slug': 'uskudar',
  'komsu': ['kadikoy', 'atasehir', 'umraniye', 'beykoz'],
  'mahalle': ['Kuzguncuk',
              'Beylerbeyi',
              'Çengelköy',
              'Kandilli',
              'Kuleli',
              'Salacak',
              'Selimiye',
              'Sultantepe',
              'Altunizade',
              'Kısıklı',
              'Bulgurlu',
              'Ünalan',
              'Burhaniye',
              'Ferah',
              'Küçük Çamlıca',
              'Güzeltepe'],
  'yapi': "Üsküdar'ın Boğaz kıyısında Kuzguncuk ve Çengelköy'ün ahşap evleri, Beylerbeyi ve Kandilli'nin yalıları duruyor. Salacak ve Selimiye'de "
          "eski kâgir apartmanlar sık; Altunizade ve Burhaniye'de yetmişlerden kalma bloklar dönüşümle yenileniyor. Çamlıca yamaçlarında, Bulgurlu "
          "ve Ünalan'da ise çok katlı siteler ve sonradan kat çıkılmış eski evler yan yana.",
  'gider': "Kuzguncuk ve Çengelköy'deki ahşap evlerde tesisat genelde sonradan eklenmiş; dar bir alana sıkıştırılmış hatlar ve keskin dirsekler var. "
           'Sonradan kat çıkılmış binalarda alt kattaki eski boru, üstteki yeni banyonun yükünü taşıyamıyor. Altunizade ve Ünalan sitelerinde ise '
           'uzun kolonlar ve ortak mutfak hatları yağ birikintisiyle zemin katı zorluyor.',
  'dis': "Boğaz'a inen yamaçlarda eğim fazla olduğu için gider hızlı akıyor ama katı atık yolda dağılmadan aşağıdaki dönüşte toplanıyor. Kıyıya "
         "yakın evlerde ise parsel bacası deniz seviyesine çok yakın, lodosta sokak hattının yükseldiği olabiliyor. Çamlıca ve Kısıklı'nın bahçeli "
         'evlerinde çam kökleri bahçe hattındaki eski künk borulara dadanıyor.',
  'saha': "Kuzguncuk, Sultantepe ve Beylerbeyi'nin dik ve dar sokaklarına büyük araçla girmek zor; makineyi aşağıda bırakıp elde taşıdığımız da "
          "oluyor. Sahil yolundaki trafik akşamüstü kilitlenebildiği için Çengelköy ve Kandilli'ye bazen arka yollardan, Bağlarbaşı ve Kısıklı "
          'üstünden iniyoruz. Ahşap evlerde döşemeye zarar vermemek için yere koruma serip çalışıyoruz.',
  'uzak': False}]
