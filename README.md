<p># Mindstorm-air-student Mindstorm csapat - Auton&oacute;m &eacute;s Intelligens Robotok 2021 ősz kurzus</p>

<h2>Csapat tagok:</h2>

<ul>
	<li>Csabai Szabolcs</li>
	<li>D&oacute;zsa Zsombor</li>
	<li>V&eacute;gh Attila</li>
</ul>

<p>&nbsp;</p>

<h2>Első alkalom:</h2>

<p>Az előadás után neki álltunk szétbontani az alapkészlet csomagját és megismerkedtünk a
tartalmával. Kis diskurzus után nekiálltunk a robot alapjának. Tervek szerint lánctalpakon
fog közlekedni a robot. Sok időt vett igénybe, hogy megtervezzünk és összeépítsünk egy
olyan futóművet, ami kellően széles és magas. Miután sikerült véglegesíteni vázat, egy
olyan hibával találkoztunk, hogy a saját tömege miatt „terpeszteni” kezdett a lánctalp. Ezt
a hibát kiküszöbölni egy a lánctalpakra merőleges merevítővel tudtuk megoldani. A lánctalp 3 keréken fekszik egy háromszöget idéző formában. A
felső(középső) lánckeréken keresztül fogjuk megoldani a hajtást két nagyobb nyomatékkal
rendelkező villanymotorral. Tervek között szerepel, áttét beépítése a lánckerék és a
villanymotor köz.
További teveink még nem teljesen kiforrottak.
</p>

<p align="left">
  <img width="400" src="https://github.com/robotlabor-education/Mindstorm-air-student/blob/main/images/img13.png">
  <img width="400" src="https://github.com/robotlabor-education/Mindstorm-air-student/blob/main/images/img12.png">
</p>

<p>&nbsp;</p>

<h2>Második alkalom:</h2>

<p>Ezenen a laboron megpróbáltuk tovább fejleszteni a már elkezdett kis robotunk. A lánctalp további erősítést kapott kívülről ami kis plusz merevséget biztosít neki. Első tesztek során kiderült, hogy az előre és hátra mozgatás során, ugye ezekben az esetekben azonos irányba dolgozik a két nagy villanymotor, semmi féle gond nincs és jól működik. Mindazonáltal az ellentétes mozgás során, tehát a függőleges tengely fordulásnál a láncot hajtó kerekek nem fogtak rendesen és emiatt nem tudott fordulni egyenletesen. Ennek orvosolására áttét helyzetünk be a hajtott tengely és a lánckerék közé. Tesztek során eredményként kaptuk azt, hogy javult a fordulás dinamikussága és egyenletessége de nem tökéletes még. További terveink, hogy tovább növeljük az áttét méretét és azzal oldjuk meg ezt a fennálló mozgásbeli problémát. Egyéb fejlesztésünk sorát gyarapítja a kis villanymotor felszerelése, amivel majd egy fogas lécet fogunk meghajtani menetiránynak párhuzamosan. Ennek segítségével szeretnénk majd tárgyakat juttatni arra felületre, amin mozog a robotunk. Ezen tárgyak lejutását fogja segíteni a második és negyedik képen jól látható hajlított ívű zárt rendszer. Ez a rendszer teljesen le nyúl a talajig a biztonságos lehelyezés érdekében. További fejlesztéseink tervei az, hogy ezt a zárt rendszert még tovább fejlesszük és tökélesítsük.</p>

<p align="left">
  <img width="400" src="https://github.com/robotlabor-education/Mindstorm-air-student/blob/main/images/img24.png">
  <img width="400" src="https://github.com/robotlabor-education/Mindstorm-air-student/blob/main/images/img21.png">
</p>

<p>A lánctalpas meghajtást tovább tökéletesítettük. A kerekeket távtartókkal fix távolságra eltoltuk a vázszerkezettől, kissé összehúztuk az egész szerkezetet, így egy-egy láncszemet is ki kellett venni. Így sokkal feszesebb láncot kaptunk eredményül, ami a csúszásokon javított. A fogaskerekek szétugrását a flexibilis műanyag elemek gyenge nyomatékátviteli képessége nagyban befolyásolta. Hogy növeljük a nyomatéktovábbításra használható felületet, egymás mellé elhelyezett dupla fogaskerekes rendszert alakítottunk ki a szimpla helyett. Ezek a változtatások már kiküszöböltek minden hajtással kapcsolatos hibát.
Az adagoló kart felülről rögzítettük, hogy ne tudjon kiugrani a helyéről, valamit a felső vázszerkezetet is elkezdtük átalakítani. Ez utóbbi még további kidolgozásra szorul.
A teszteléshez használt program a lehető legegyszerűbb felépítésű, aminek a célja az volt, hogy a kontroller egységen található öt gombbal előre, hátra, jobbra és balra tudjuk mozgatni a robotot, valamint a középső gombbal megállítani. Minden szükséges inputot figyel és megnyomásukra a szükséges mozgásutasítást kiadja.</p>
<p align="left">
	<img height="400" src="https://github.com/robotlabor-education/Mindstorm-air-student/blob/main/images/img26.png">
</p>

<h2>Harmadik alkalom:</h2>

<p>A laboron tökéletesítve lett néhány meglévő funkció és néhány új is applikálva lett. A lánctalp jobb tartásának érdekében át lett építve. Külső oldalakon további merevítés mellett még a két oldal összekötése történt meg elöl és hátul. Dinamikussága javult ezáltál a robotnak és már terpesztés sem olyan látványos.
A kilövő szerkezet áttétének újra építése és javítása is megtörtént. Így biztosabban és nagyobb sebességgel tudja a lövedékeket kilőni, aminek egy függőleges tárja a robot elején helyezkedik el. 
A számítógép középen kapott helyett annak érdekében, hogy jobb legyen a súly eloszlás.
Felkerült egy távolságmérő szenzor, ami azt nézi, hogy mi van a robot elött. Felkerült továbbá egy giroscop és RGB szenzor is. Az RGB szenzort nem tudtuk rendesen beüzemelni, mert a talajon lévő szigetelőszalag színét nem tudta rendesen meghatározni. Ez további fejlesztést igényel.
A programon belül felmerült egy kérdés a broadcast message résznél. Itt arra jöttem rá, hogy ezt az elemet használva tudunk egy „üzenetet” küldeni, amit fogadni tud ez az elem: 

A program az RGB szenzor sikertelen használta miatt csak az alábbit tudja:
Elindul előre addig amíg a robot elé nem kerül vmi 25cm-en belül. Megáll és tolat egy sec-ig. Vár sec-et majd vissza számol és lő egyet. Ezután elfordul jobbra 90°-ot és indul megint előre. Ha kifogy a töltényből, azaz ellőtte magát 10-szer akkor kikapcsol.
<br />
&nbsp;</p>
