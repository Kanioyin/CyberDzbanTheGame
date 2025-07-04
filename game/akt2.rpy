label a2intro:
    scene akt2
    play music "a2amb.mp3"
    $ akt = 2
    $ bigquest = 0
    $ Frakcja = oldFrakcja
    if helper < 0:
        $ helper = 0
        
    sb "Aj karamba, bolało! Mam nadzeję, że jesteś cały"
    sb "Zobaczmy z czego jesteś zbudowany"
    menu:
        "Co jest moją mocną stroną?"
        "Siła":
            if helper == 0:
                $ cechy["BC"] = 6
                $ MaxHP = 40

            elif helper > 50:
                $ cechy["BC"] = 4
                $ MaxHP = 30

            elif helper > 0:
                $ cechy["BC"] = 5
                $ MaxHP = 35

        "Zwinność":
            if helper == 0:
                $ cechy["ZW"] = 6

            elif helper > 50:
                $ cechy["ZW"] = 4

            elif helper > 0:
                $ cechy["ZW"] = 5

        "Charyzma":
            if helper == 0:
                $ cechy["CHAR"] = 6

            elif helper > 50:
                $ cechy["CHAR"] = 4

            elif helper > 0:
                $ cechy["CHAR"] = 5

        "Mózg":
            $ cechy["Myslenie"] = 3
            if helper == 0:
                $ cechy["INT"] = 6

            elif helper > 50:
                $ cechy["INT"] = 4

            elif helper > 0:
                $ cechy["INT"] = 5

    menu:
        "Gdy trzeba walczyć, co robię?"
        "Strzelam":
            $ skile["Bron"] = 4

        "Spierdalam":
            $ skile["Atletyka"] = 4

        "Perswaduje":
            $ skile["Gadanie"] = 4

        "Zastanawiam się: Dlaczego?":
            $ skile["Myslenie"] = 4

    sb "No dobra, pora otworzyć oczy"
    scene opor
    show kris
    sb "Dzień dobry [player_name]"
    p "Kim ty kurwa jesteś?"
    sb "Faktycznie, wypada się przedstawić. Krzysztof Czerownopolski"
    cr "Do usług"
    p "Dobra kurwa ale skąd ty wiesz jak ja się nazywam?"
    cr "Mam swoje źródła. Oto przed tobą: Jax"
    show jax at left
    ja "Witam"
    cr "I VIO"
    show vio at right
    vi "Vitam"
    p "On nie jest kurwa Vistą?"
    vi "Jestem, takim udomowionym"
    p "Ok, zrozumiałe"
    p "To powiesz mi co ty ode mnie chcesz?"
    cr "Ano tak. Mamy jeden prosty plan. Drużyna już o tobie zapomniała"
    $ player_name = "Zbigniew"
    cr "Od teraz jesteś Zbigniew"
    p "Co kurwa?"
    cr "Spokojnie, mamy zapisane twoje dawne imię. Jak nie zapomnę to kiedyś wróci"
    p "I co mam teraz zrobić?"
    cr "Jako tajny agent musisz odzyskać chipy ze wspomnieniami"
    p "Jaki kurwa tajny agent?"
    cr "Specjalna jednostka pułkownika Sójeczki"
    p "A kim jest kurwa ten fagas?"
    cr "Nowy dowódca armi w NC"
    p "No dobra, to o jakie cipy chodzi?"
    cr "No bo widzisz. Cały twój poprzedni gang trafił do pierdla"
    p "O cholipka"
    cr "Ale nie martw się, to tylko tymczasowe"
    p "Czyli nie dostali dożywocia?"
    cr "Nie. Oni są tam w sumie na wakacjach"
    p "Czyli cała robota trafia znowu na moje barki"
    cr "No nie. Masz tu dwóch dzielnych wojowników. Będą mogli Ci pomagać w trudnych chwilach"
    cr "Ale wracając do roboty, po całym mieście są chipy z danymi."
    cr "Musisz je zdobyć a ja je sprawdzę czy są właściwe"
    p "A co się będzie na nich znajdować?"
    cr "Brudy na lokalnego giga fixera, pana Szybkiego Bena"
    p "A co on ma tam za uszami?"
    cr "Tego właśnie będzie trzeba się dowiedzieć"
    p "Czyli latam po mieście szukając wiatru w polu"
    vi "Vingo!"
    p "Popierdoli mnie, na chuj ja tu w ogóle przyjeżdżałem?"
    ja "Pewnie szukałeś szybkich pieniędzy i wpadłeś w szambo"
    p "W sumie, to ma trochę sensu"
    ja "Spokojnie, jeszcze kilka lat i się przyzwyczaisz"
    cr "No to co, zaczynamy pierdolnik?"
    p "Chyba nie mam innego wyjścia"
    show screen hud
    jump opor

label opor:
    stop music
    play music "a2amb.mp3"
    call checktime from _call_checktime_1
    show screen hud
    show screen oportalk
    window hide
    pause 10

label bufor:
    $ czas -= 1
    jump opor

label jaxowo:
    scene opor
    show jax
    $ talkloop = 0
    $ czas -= 1
    while talkloop == 0:
        menu:
            ja "Co tam chcesz [player_name]?"
            "Potrzebuję Cię w moim składzie!" if kompan == 0:
                ja "Spoczko foczko"
                $ kompan = 2
                "JAX dołącza jako kompan"

            "Wyskakujesz może na piwko?" if kompan == 2 and postacie2["Jax"] < 3:
                ja "Spoczko, da się zrobić"
                jump piwko

            "Idę questować solo" if kompan == 2:
                ja "Żaden problem mordeczko"
                $ kompan = 0
                "JAX wraca do swoich zajęć"

            "Mam dla Ciebie przesyłkę" if stan2["BB"] == 6 and inventory.has_item(Wytrych) == True:
                $ czas -= 4
                p "Cześć Jax, mam coś dla Ciebie"
                ja "Co to takiego [player_name]?"
                p "A taki fajny wytryszek znalazłem, uznałem, że może Ci się przydać"
                ja "Kurde balans [player_name], w dobrym momencie z tym przyszedłeś."
                p "Co ty dajesz"
                ja "Serio, znalazłem jakąś dziwną skrzynkę z wojskowym znakiem. A wojsko to znak dobrego lootu"
                p "No to co, otwieramy chyba"
                ja "Proste że tak, zaraz ją przyniosę"
                "Jax przeszedł się po czesta"
                p "Spore to to. Ciekawe, co będzie w środku"
                ja "Mam nadzieję, że wojskowe wszczepy, wtedy będziemy bogaci"
                p "No to dobra, otwieram ją!"
                $ inventory.remove_item(Wytrych)
                p "Co to kurwa jest? Miałem nadzieję na wszczepy a nie na dokumenty"
                ja "Może być jeszcze lepiej tak na prawdę, wojskowe tajne akta. Daj mi chwilę to je przeczytam"
                "Dałeś mu chwilę"
                ja "Ale jaja. Kennedy ma stanąć przed sądem wojennym"
                p "Co do kurwy, jak on to niby zrobił?"
                ja "Okazuje się, że umowy z nami były nielegalne i teraz jest ścigany po hawajach"
                p "Niech zgadnę, podpisywał umowy o działo a nie o dzieło?"
                ja "Nie napisali dokładnie ale bardziej mi to wygląda na nieautoryzowane korzystanie z osób trzecich"
                p "Czyli już nie będziemy mieli chyba umów z wojskiem"
                ja "Nie powiedział bym, w wojsku jest teraz nowy szef, tylko nikt nie wie jak to u niego wygląda"
                p "Zobaczymy później pewnie. Ja będę się już zbierał, trzymaj się Jax"
                $ stan2["BB"] =7
            
            "Co powiesz na mały trening?" if exp > 9:
                ja "Jasne mordeczko"
                $ exp -= 10
                menu:
                    ja "Co chciałbyś ulepszyć?"
                    "Wytłumacz mi o co chodzi":
                        ja "Jak sprawdzasz swoje umiejętności, zdobywasz doświadczenie. Gdy zdobędziesz go wystarczająco dużo, to przychodzisz do mnie"
                        ja "Ja Ci pokażę jak wykożystać to doświadczenie w praktyce a tobie następne testy idą łatwiej"
                        p "Wow, to takie proste?"
                        ja "Proste że tak!"
                        $ exp += 10

                    "Bieganie" if skile["Atletyka"] < 7:
                        achieve UPG
                        ja "No to lecimy, czas trenować cardio"
                        $ skile["Atletyka"] += 1
                        "Spędziłeś trochę czasu na bieganiu"
                        $ czas -= 10

                    "Strzelanie" if skile["Bron"] < 7:
                        achieve UPG
                        ja "Kierunek strzelnica!"
                        $ skile["Bron"] += 1
                        "Udało Ci się trafić nawet 10"
                        $ czas -= 10

                    "Rozmawianie" if skile["Gadanie"] < 7:
                        achieve UPG
                        ja "No to opowiadaj, jak Ci życie mija"
                        $ skile["Gadanie"] += 1
                        "Opowiedziałeś JAX-owi o swoich problemach"
                        $ czas -= 10

                    "Rozmyślanie" if skile["Myslenie"] < 7:
                        achieve UPG
                        ja "Zastanów się, co było pierwsze: Egg czy Qra?"
                        $ skile["Myslenie"] += 1
                        "Obstawiasz że egg"
                        $ czas -= 10

            "To chyba na tyle":
                ja "Luz"
                $ talkloop = 1

    jump opor

label viocha:
    scene opor
    show vio
    $ talkloop = 0
    while talkloop == 0:
        menu:
            vi "Vitam [player_name]"
            "Potrzebuję Cię w moim składzie!" if kompan == 0:
                vi "Vaden vroblem"
                $ kompan = 1
                "VIO dołącza jako kompan"

            "Idę questować solo" if kompan == 1:
                vi "Vozumiem"
                $ kompan = 0
                "VIO vraca do swoich zajęć"

            "Idziesz na vrowara?":
                vi "Vevnie"
                jump piwko

            "Możesz mnie uleczyć?" if HP < MaxHP:
                if inventory.has_item(HuMeat) == True:
                    $ inventory.remove_item(HuMeat)
                    vi "Vuzik vrbuzik"
                    $ HP = MaxHP
                    $ umieram = 0
                    p "Dzięki VIO"

                else:
                    vi "Vłopie, tu nie ma nic za darmo"
                    p "To ile chcesz tych edków?"
                    vi "Va vcę vięsa, vudzkiego vakiego"
                    p "Ale żeby je zdobyć to muszę kogoś zabić"
                    vi "Vak"
                    p "I jak mam mało HP, to oni mogą mnie zabić"
                    vi "Vo vdź vpać"
                    p "AHA66"
            
            "To chyba na tyle":
                vi "Vuz"
                $ talkloop = 1

    jump opor

label krzis:
    scene opor
    show kris
    if bigquest == 0:
        if stan2["Kris"] == 0:
            cr "Dobra [player_name], pora na twoje zadanie, musisz połazić trochę po mieście i poszukać chipów"
            p "I co, tak randomowo będą na ulicy?"
            cr "To nie jest aż takie proste. Masz tu wykrywacz"
            cr "Jak będziesz w okolicy to będzie brzęczeć"
            p "WOW! I co wtedy?"
            cr "Wtedy ruszasz dzielnie tam gdzie pika. Może tam być niebezpiecznie, więc radzę iść z kimś"
            cr "VIO i JAX się polecają do napierdalania"
            p "A nie mogę wziąć ich obu?"
            cr "W sensie że do walki tak?"
            p "Tak"
            cr "Uf, nie możesz bo:"
            cr "a) To by było zbyt proste"
            cr "b) Jak walczą razem to wpadają w dziki szał i potrafi im czasem odjebać aż za bardzo"
            cr "Ostatnio prawie rozjebali pół osiedla a ja nie wiem jak to powstrzymać"
            cr "Odkąd Arasaka porwała JAX-a to jest z nim coraz gorzej ale dobra, czas kończyć ten Ted tok"
            cr "Ruszaj dzielnie do roboty"
            p "Tajest!"
            $ stan2["Kris"] = 1
            jump opor

        elif stan2["Kris"] == 1 and chipy == 1:
            cr "O! Widzę że udało Ci się zdobyć pierwszego Chipa. Gratulacje [player_name]"
            cr "Nie wiem czy widziałeś ale dodałem Ci do pokoju możliwość czytania tych danych"
            p "Wow, po chuj mi to?"
            cr "Jakby cię lore interesował to możesz sobie przeczytać"
            p "Fantastycznie, czy coś"
            cr "Dobra, nie truj mi dupy"
            $ stan2["Kris"] = 2
            jump opor

        elif (stan2["Kris"] == 2 or stan2["Kris"] == 1) and chipy == 5:
            cr "Gratulacje [player_name]! Zebrałeś je wszystkie"
            cr "Pozwól, że ja je teraz wezmę"
            $ chipy = 5
            p "Ale co w sumie z tego, jak na tych cipach gówno jest o Benku"
            cr "To dobry omen"
            p "Ale jak kurwa"
            cr "To znaczy, że nasi informatorzy to gówno ale na spokojnie, zaraz ruszysz na misje, która nam wszystko wyjaśni"
            cr "Ten ostatni chip jaki znalazłeś będzie naszym kluczem, idziesz teraz do kowala, on może coś ci wyjaśni"
            cr "No, to lecisz! Powodzenia"
            jump cipfin

        else:
            cr "Zajęty jestem, przyjdź jak zrobisz jakieś postępy"
            jump opor

    elif bigquest == 1:
        if stan2["Kris"] == 0:
            p "No, pogadałem z kowalem"
            cr "No to klawo, teraz masz kilka dni na przygotowanie się"
            p "Ale na co?"
            cr "Na specjalną misję w gnieździe anomalii"
            p "Czyli?"
            cr "Wasza dawna baza"
            p "Co tam się kurwa stało?"
            cr "Jacyś debile stwierdzili, że umyją Cyphera"
            p "I co tam się teraz dzieje?"
            cr "Takie sprawy co się nawet fizjologom nie śniły"
            cr "Musisz kupić sobie outfit na radiacje"
            if inventory.has_item(RadArm) == True:
                p "Już mam"
                cr "No to git"

            cr "Więc się przygotuj ze wszystkim i jak będziesz gotowy to wracaj"
            cr "Bo z tego co słyszałem, wielu śmiałków tam już zeszło. Jeszcze nikt nie wyszedł"
            p "No to grubo"
            cr "Niech busz będzie z tobą"
            $ stan2["Kris"] = 1
            jump opor

        elif stan2["Kris"] == 1 and inventory.has_item(RadArm) == True:
            p "Jestem gotowy"
            cr "No to ruszaj"
            jump anomalia

        elif stan2["Kris"] == 2:
            cr "Jak znajdziesz jakieś info to przyjdź"

        elif stan2["Kris"] == 3:
            p "SZEFIE MAM INFO"
            cr "Po co się drzesz?"
            p "Sorki, trochę się podnieciłem"
            "Opowiedziałeś o swoich znaleziskach"
            cr "No dobra, przynajmniej jest coś. Dam twoje dane do kowala i zobaczymy co on z tego zrobi"
            p "Nie będę musiał tam iść sam?"
            cr "Dzień dziecka jest dziś. Możesz zająć się swoimi sprawami"
            $ stan2["Kris"] = 4

        elif stan2["Kris"] == 4 and dzien > 30:
            cr "Dobra [player_name], mam info od kowala"
            p "Co takiego Ci powiedział?"
            cr "Zrobił inprint i go sprawdził. Dane które zebrałeś są faktycznie czyste"
            cr "Czyli wracasz do Bo szukać kolejnych"
            p "Się robi szefie"
            $ stan2["Kris"] = 5

        elif stan2["Kris"] == 6:
            p "Przyniosłem kolejne dane z bazy"
            cr "Coś ciekawego na nich w ogóle było?"
            p "Bo mówi, że nie"
            cr "Dam go do kowalowania i zobaczymy"
            p "Bo mówił, że to mógł być ostatni którego szukaliśmy"
            cr "To prawda, twoi kumple wracają, przez nich raczej nie będziemy w stanie spokojnie szukać"
            p "To znaczy, że przerwiemy zadanie?"
            cr "Delikatnie zmienimy jego założenia"
            p "Co to znaczy?"
            cr "Jak już połączysz się z resztą wrócicie do normalnego życia"
            cr "Trafią wam się pewnie jakieś zadania od Bena"
            p "I na nich będę szpiegował?"
            cr "Bingo"
            p "To mogę wracać cieszyć się wolnym"
            cr "Bingo, odmaszerować"
            $ bigquest = 2        

        else:
            cr "Zdupcaj, przeszkadzasz mi"


    elif bigquest == 2:
        if stan2["BB"] == 0:
            cr "Dobra młody, nowe zadanie bojowe Ciebie czeka."
            p "O rety kotlety, co tym razem, mordowanie korposów, polowanie w strefie radiacji czy może inwigilacja Arasaki?"
            cr "Zostaniesz kurierem."
            p "Odkleiłeś się w tym momencie. Co ma wspólnego kurier z tajną misją?"
            cr "Znajomy prowadzi firmę kurierską, a ja czasami dostaję od niego info o sus paczkach"
            p "I mam jeździć aż nie będę miał jakieś sus paczki?"
            cr "Dokładnie. Trochę u niego popracujesz, może nawet coś zarobisz i wrócisz do zadań specjalnych"
            p "Nie podoba mi się ten plan ale chuj, jak trzeba, to to zrobię"
            cr "Zuch chłopak! Kieruj się na Pierdex."
            $ stan2["BB"] = 1

        elif stan2["BB"] == 9:
            p "Skończyłem dostawy, prawie mnie rozerwało jak dowoziłem bombę na wypizdów"
            cr "Oj, a pamiętasz komu to może przewoziłeś?"
            p "Taki czarnuch z afro, Astolfo chyba"
            cr "Rozumiem, zostałeś pewnego rodzaju wysłannikiem do wojny narkotykowej"
            p "Co ty w ogóle pierdolisz, jakich wojen?"
            cr "W Glenn był wcześniej potężny kucharz towaru, nazywał się pan Biały. Niestety umarł"
            cr "Teraz, każdy głodny pies walczy o swój kawałek terenu i wpływów"
            p "Czy to może jakkolwiek pomóc w naszej sprawie?"
            cr "Oczywiście, opowiem Ci o tym jutro, idź się przespać."
            p "Kurwa, sranie w banie, tylko przedłuża mi tę grę, kutasiarz jebany"
            $ bigquest = 3
            $ czas = 0
            $ stan2["Kris"] = 0

    elif bigquest == 3:
        if stan2["Kris"] == 0:
            cr "Dobra, teraz czeka Ciebie takie powaga2 zadanie. Musisz zrobić inwigilację kasyna Benka"
            p "Ty kurwa nie przesadzasz z poziomem trudności?"
            cr "To nie jest aż takie trudne jak myślisz, wpierw zrobisz zwiad, potem akcję"
            p "A dasz mi jakieś dodatkowe instrukcje?"
            cr "Wszystko po koleji młody. Przygotuj się i wróć jak będziesz gotowy"
            $ stan2["Kris"] = 1

        elif stan2["Kris"] == 1:    
            cr "No dobra, jak jesteś gotowy, to ruszysz sobie do kasynka"
            p "Tak po prostu?"
            cr "No tak, idziesz sobie do kasynka, troszeczke gamblniesz, pooglądasz sobie ludzi i wrócisz"
            p "Kurde balans, to jest życie. A dostanę jakiś hajs na gambe?"
            cr "Ty chyba na łep updałeś, tracisz tylko swoje środki"
            p "Wiedziałem, że to nie będzie tak kolorowo. Chuj, raczej mam pieniądze na hazard"
            cr "No widzisz, zdolniacha z Ciebie, teraz ruszaj na gambling"
            p "ZAPIERDALAM"
            "I w cztery minuty dotarłeś do świątyni hazardu"
            scene kasyno
            p "O JA PIERDOLE! Dlaczego ja tu nie mogłem przyjść wcześniej"
            p "To jest o niebo lepsza wersja farmienia mamony niż zdrapeczki"
            p "Skoro moim aktualnym celem jest badanie gruntu"
            p "To pora iść zacząć gamblować, najpierw zdobędę miliony edków. Potem zdobędę info"
            $ edki = edki/2
            "I w taki sposób, straciłeś połowę majątku"
            p "Chuj, dupa, cyce. Teraz zostaje mi tylko przepytanie ludzi na sali"
            "Więc ruszyłeś przypytaywać każdego, kto był w okolicy"
            gg "Nie no, Benek to taki sztywny gicior jest. Robotę ogarnia, płaci całkiem dobrze."
            gg "Jak coś od niego chcesz, to idź na piętro do jego pokoju"
            p "Poleciałeś do następnego gagatka."
            ko "Ben jest ważnym beneficjentem w naszej firmie, często robimy z nim interesy"
            ko "Jestem dumny, z całego systemu bezpieczeństwa w tym budynku"
            ko "Dostanie się nieproszonym w nieodpowiednie miejsca jest niemożliwe"
            ko "A w razie większego problemu, cały budynek się izoluje i traci powietrze"
            p "Cholipka, robi się grubo, ciekawe co mi powie następny typek"
            show cypher at left with moveinleft
            c "Wiele ciekawostek panie kolego"
            p "Czy ty możesz się odpierdolić w końcu?"
            c "Nie, polubiłem cie, dostaniesz ode mnie wiele przydatnych wskazówek do swojej misji"
            p "Ta, pewnie, co niby takiego możesz mi powiedzieć?"
            c "Szybki Ben nie lubi ananasa"
            p "Moje życie zmieniło się o 360 stopni w tym momencie"
            c "To nie dobrze, będzie Ci się kręcić w głowie od tego"
            c "Teraz ciekawostka nr 2. Oczkiem w głowie Benka, jest ta jego baba w słoiku"
            p "Czekaj kurwa, jaka baba w słoiku?"
            c "To ty nie wiesz? Jena sie ona chyba nazywa. Wszczepy drugiej ręki to jej zrobiły"
            c "I teraz Benek lata w poszukiwaniu tych gówien w poszukiwaniu jakiegoś lekarstwa"
            p "Dobra kurwa, tym razem zmiotłeś mnie z planszy"
            c "Widzisz Stefan, ja mam wiele asów w rękawie"
            "W tym momencie pojawiło się kilku ochroniarzy"
            gu "Dlatego musi pan opuścić teren kasyna"
            c "Ciemny chuj, dorwali mnie, spierdalam Stefan"
            hide cypher
            p "Ale ja nie jestem Stefan"
            gu "Przepraszam pana, ten klient zawsze do nas wraca i przeszkadza. Proszę przyjąć te edwardy jako rekompensatę"
            $ edki = edki * 2
            p "Dziękuję"
            "Ochrona poszła w pizdu"
            p "Dobra kurwa, jestem na zero z hajsem, mam trochę info i małego bruda. Teraz mogę wracać"
            $ stan2["Kris"] = 2

        elif stan2["Kris"] == 2:
            cr "No, opowiadaj, czego ty się dowiedziałeś?"
            p "Trochę info, trochę pierdół, mam kilka przydatnych newsów. Niestety, prawdopodobnie Cypher będzie potrzebny do akcji."
            cr "Tak jak planowałem."
            p "Co kurwa? Jak to? Od kiedy Cypher jest powiązany z całą akcją?"
            cr "Specjalny kontrakt przewidział użycie niemieckich najemników w inwigilacyjnej misji ale dopiero w drugiej części"
            p "To to jest podzielone na party?"
            cr "Tak, część pierwsza, to inwigilacja, szukanie tropów i wyciąganie wniosków. Część druga, to pełnoprawne włamaie."
            p "A czy przypadkiem sama inwigilacja nie jest już włamaniem?"
            cr "Nie mędrkuj mi tutaj, szpiegostwo, to jest tylko włamanie pośrednie."
            p "Zostawmy tę papierologię, powiedz mi co mam teraz zrobić"
            cr "Musisz załatwić sobie odpowiedni ekwipunek. Potrzebujesz haka, liny, morfiny i ładunków wybuchowych"
            p "I co, rozpiszesz mi to teraz w kajecie a ja będę tego szukał?"
            cr "Nie. Pojedziesz do bazy wojskowej, zabierzesz część sprzętu i zajmiesz się szukaniem C4"
            p "Tak po prostu wbiję na teren wojska i wezmę eq? To brzmi zbyt prosto"
            cr "Zrobiłem Ci tymczasowe konto jako poborowy. Zabierzesz startówkę i będziesz mógł wyjść bez problemu"
            p "Karwasz, nie wiedziałem, że masz takie pojebane wpływy"
            cr "Jeszcze wielu faktów nie wiesz o mnie. W sumie, to lepiej dla Ciebie, łatwiej Ci zasnąć."
            p "Dobra szefie, to ja lecę do armii"
            cr "Ruszaj dzielnie"
            scene black
            "Dzielnie ruszyłeś, zabrałeś sprzęt i nawet wyszedłeś bez problemów"
            p "Kurde balans, to jest życie. Darmowe itemki, salutujące kasztany, może powinienem iść do wojska"
            p "Miałbym lepsze perspektywy, wypłatę i ogólnie jakość życia"
            p "Nah. To nie byłoby cyberpunkowe. Wolę ogarniać chyba krzywe bomby"
            p "Tylko gdzie ja mogę takową dostać? Poprzednio Krateus ją wynajął. Ty kurwa, pomysła mam"
            p "Cypher pewnie ma takich na pęczki, pewnie się podzieli ze mną"
            scene bazadh
            show cypher at left
            c "Proszę proszę, kogo tu nogi sprowadziły?"
            p "Cześć Cypher, sprawę mam"
            c "Opowiadaj, sam wiesz, że ja nigdzie się stąd nie ruszam"
            p "Potrzebuję bomby, takiej co potrafi zrobić bum"
            c "Przyszedłeś w idealnym momencie. Właśnie miałem wyrzucać jedną z takich"
            p "Kurwa perfekcyjnie, oddałbyś mi ją?"
            c "No chyba na łep upadłeś, 100 edków się należy"
            p "Co kurwa? Przecież chciałeś ją wyrzucić. Czemu chcesz teraz za nią pieniądze?"
            c "Czwarte prawo ekonomi wg mnie"
            c "Jeśli coś może mieć wartość, sprzedaj to. Wcześniej chciałem to wyjebać, bo mi nie była potrzebna"
            c "Teraz jak wytowrzyłeś popyt, to mogę na tym jeszcze zarobić."
            p "A potem się dziwisz, że nikt nie chce się z tobą zadawać"
            call cipflash from _call_cipflash_19
            c "Wrrr. To i tak nie wpłynie na cenę"
            p "Chuj, niech stracę"
            $ edki -= 100
            "Zapłaciłeś Cypherowi i dostałeś bombę"
            c "Tylko sobie przypadkiem krzywdy tym nie zrób."
            p "Od kiedy się martwisz o kogokolwiek?"
            c "Od momentu, w którym zostałeś moim klientem"
            p "A spierdalaj"
            "I wyszedłeś w pizdu"
            $ stan2["Kris"] == 3
        
        elif stan2["Kris"] == 3:
            cr "Dobra młody, masz już ekwipunek. Pora na trening szpiegowski"
            p "Na czym to będzie polegało?"
            cr "Po pierwsze, wentowanie. Jak dobrze wiesz, wentylacja w budynkach jest wielka. Zmieści się w niej typ o BC max 12"
            p "Czyli ja nie powinienem mieć nawet z tym problemu"
            cr "Dokładnie. Czołganie się, trwa sporo czasu ale pozwala się dostać w specjalne miejsca. Spróbuj się przecisnąć przez ten szyb"
            p "Się zrobi szefie"
            "Przeczołgałeś się przez dwumetrowy szyb testowy. Masz teraz na głowie trochę pajęczyn"
            p "Nikt tego wcześniej nie używał ani nie czyścił?"
            cr "A po co? To jest tylko do uczenia takich rodzynków jak ty"
            p "Aha 66. Coś jeszcze muszę umieć przed akcją?"
            cr "Umiesz podkładać bombę?"
            p "Absolutnie nie!"
            cr "No to dobrze, będziesz musiał tylko uważać by jej przypadkiem nie uruchomić."
            p "To będę musiał ją komuś przekazać czy jak to robimy?"
            cr "Jak będziesz w wencie, musisz ją zostawić w odpowiednim kącie."
            p "I to będzie tajemniczy mysi sprzęt o którym zapomnimy na zawsze?"
            cr "Tak. Cyberowe standardy tego od nas wymagają. Pamiętaj jednak, zawsze jest promil szans, że sobie o tym ktoś przypomni."
            p "Ta pewnie, tylko Wielki Dzik nie będzie tego pamiętał i plan w pizdu"
            mg "Spierdalaj"
            cr "On zawsze słucha, on wszystko pamięta. Nie próbuj podważać jego autorytetu"
            p "Wiem, potrafi zkraszować grę i usuwać zapisy."
            cr "To prawda, jego moc rośnie z każdą aktualizacją."
            p "Ale dobra, wracajmy do tematu? Coś jeszcze ze szkolenia?"
            cr "Powiedz mi, jak twoja orientacja?"
            menu:
                "Homo":
                    p "Jestem homo"
                    $ relacja = 1

                "Hetero":
                    p "Jestem prosty"

                "Dziura to dziura":
                    p "Jestem Bi"
                    $ relacja = 2

            cr "W terenie orientacja! Nie seksualna"
            p "AAAAA. Trzeba było tak od razu mówić. Dobra chyba"
            cr "Oby tak było, inaczej zgubisz się w pizdu w wentylach. A tam jest cały, pokręcony system."
            p "To gdzie będę musiał iść?"
            cr "Odpowiednia trasa to: góra, góra, prawo, prawo, góra, góra, lewo, góra"
            p "A dostanę jakąś mapę może?"
            cr "Sam sobie powinieneś ją zrobić."
            mg "Nie chce mi się tego rysować"
            p "No dobra, raczej zapamiętałem"
            cr "Miejmy nadzieję, to będzie kończyło twój trening. Poćwicz sobie torchę jeszcze przy wencie i będziesz mógł ruszać"
            p "Jasna sprawa szefie"
            cr "I pamiętaj o słuchawce do gadania. Lepiej być w kontakcie w czasie akcji"
            $ stan2["Kris"] = 4

        elif stan2["Kris"] == 4:
            scene kasyno
            p "Agent 69 na miejscu i gotowy do akcji"
            cr "Zamknij się tam, przygotuj się do akcji lepiej. Na pewno masz wszystko ze sobą?"
            p "No pewnie, przygotowywałem się do tego całe siedemnaście sekund"
            cr "Jak na twoje standardy, to nawet sporo."
            p "Ja jestem agent specjalny, zostajemy na łączach?"
            cr "Ja jestem tutaj cały czas, ty, jak będziesz coś chciał, to dzwoń. Inaczej będą mogli nas wykryć"
            p "Zrozumiano szefunciu, [player_name] bez odbioru."
            p "Dobra, teraz muszę iść do kibla i wskoczyć do wenta"
            show cypher at right
            c "A skąd wiesz, że akurat musisz iść do kibla?"
            p "Jak ty tu kurwa znowu wszedłeś?"
            c "Drzwiami (:"
            p "Mogłem się spodziewać. Wiem, że muszę iść do kibla, bo mi się chce lać"
            c "A. Zrozumiałe, powodzenia w celnym szczaniu"
            p "Dzieki Cypher"
            hide cypher
            p "To teraz szybki sik i do wenta"
            play sound "zip.mp3"
            scene pee
            p "AH. Szybciutki sik i życie staje się piękniejsze"
            p "Teraz, z pustym siurem, mogę ruszać do wentylacji"
            scene vent
            p "Dobra kurwa, gdzie ja mam teraz iść?"
            p "Chuj, trasa srasa. Będę chodził po wentach aż znajdę jakieś wyjście"
            "Jak ostatni debil, dreptałeś sobie po kasynowej wentylacji"
            p "Hmmm, tu na ścianie widzę symbol bomby. Pewnie mój genialny, przystojnu i zajebiście skromny GM, daje mi wskazówkę"
            p "Zignoruję ją w pełni"
            "Pełzasz sobie dalej i docierasz do wyjścia z wenta"
            scene black
            p "Kurwa, jak tu jest ciemno. Kolejny event bez grafiki albo Benka nie stać na elektryczność"
            p "Dobra, calluje do Krisa. Halo alo, czy mnie słychać?"
            cr "Niestety, jaka jest twoja lokacja?"
            p "Wyszedłem z wenta, jestem w czarnej dupie. Nic nie widzę ale jestem cały."
            cr "Zrozumiałe. Poczekaj chwilę"
            p "Na co?"
            cr "Masz w słuchawce mały chip, pozwala mi on dostać się zdalnie do okolicznej sieci"
            p "Ty potrafisz tobić takie tricki?"
            cr "Nie. Ja mam od tego ludzi."
            p "Faktycznie, zapomniałem, że wojsko ma bandę netrunnerów"
            cr "Tylko zaufanych w tej akcji. Pamiętaj, jesteś tajnym agentem."
            p "Tak, tak, tak. Wiem, podpisałem cyrograf"
            cr "Ty głupi jesteś. Niczego nie podpisałeś. Nie ma żadnych dowodów."
            cr "Hack skończony, możesz próbować wyjść"
            p "To tylko po to ja się tutaj dostawałem?"
            cr "Tak, więcej nie powinieneś próbować lepiej."
            p "No dobra, to ja wracam do wenta. [player_name] bez odbioru"
            cr "Tylko pamiętaj o.."
            p "Nie słucham tego"
            scene vent
            p "Będzie mi tutaj pierdolił o jakiś głupotach. Ja wiem co mam robić"
            p "Kurwa, znowu się zgubiłem. Ty, tu jest coś luźne"
            play sound "fall.mp3"
            scene kasyno
            p "Kolejne udane lądowanie"
            show cypher at left with moveinleft
            c "Oj kolego, ty chyba coś tu szmęcisz"
            p "Zamknij się Cypher, z misji wracam"
            gu "Obawiam się, że będzie pan musiał iść z nami"
            p "Jasna dupa, ochrona"
            c "Spokojnie Eustachy, ja mam plan"
            gu "Pójdzie pan pokojowo czy po mojemu?"
            c "A co pan ochroniarz powie o dyrektywie 17, ustępie 4 z rozporządzenia burmistrza NC?"
            gu "W sensie?"
            c "Bazując na prawie do ochrony robotników fizycznych, ten oto ziutek, ma prawo do ucieczki, przez następne 7 sekund"
            gu "Nie wiem czy to prawo obowiązuje w kasynie. To jest taka mała szara strefa"
            scene black
            "W czasie ich gadania, wyszedłeś z kasyna"
            p "Cypher jednak potrafi zagadać człowieka, moc Janka na niego spłynęła."
            p "Pora wracać do Krisa, hmmm. Chyba o czymś zapomłem, ale jeśli tego nie pamiętałem, to nie było ważne"
            $ stan2["Kris"] == 5
            

        elif stan2["Kris"] == 5:
            cr "Gratulacje [player_name], udało Ci się przeprowadzić inwigilację kasyna Benka i wyjść z tego cało"
            p "A dziękuję, jakaś nagroda mnie za to czeka?"
            cr "Tak, za swoje wyczyny dostajesz dietę w postaci edwardów"
            $ edki += 2000
            $ renpy.notify("Dostałeś 2000 edków")
            p "Jasna dupa ile pieniędzy! Wojskowe diety są aż tak duże?"
            cr "Robisz tajną misję dla nas, tu tylko są takie wypłaty"
            p "No to panie Krzysztofie, ja się piszę na kolejne zadanie"
            cr "Niepotrzebnie, po zakończeniu jajec z kasynem przestajemy się znać"
            p "AHA66"
            cr "No tak wygląda tak u nas. Nie musisz się martwić, z tego ci wiem, twoji starzy znajomi niedługo wracają z pierdla"
            p "Co ty pierdolisz? Wyrok im się już kończy?"
            cr "Nie, oni po prostu spierdalają. I tak nie ma już sensu w trzymaniu ich tam"
            p "A jaki był sens wcześniej?"
            cr "Gonili ich najemnicy i musieliśmy ich gdzieś schować. Najemników już nie ma, więc mogą wracać"
            p "I tak po prostu na to pozwalasz?"
            cr "Tak. Ta banda jest przydatna do uspokajania miasta w nasz sposób"
            p "Ta, pewnie, już w to wierzę"
            cr "Nie obchodzi mnie to za bardzo. Oni robią to, co im zagramy i tak powoli ustawiamy misto pod siebie"
            p "Jak niby? Oni robią to, co im głos w głowie (Robert) powie. Nie mają jakiś większych planów"
            cr "Dobra młody, ty się ogarnij lepiej. Nie wyciągniesz ze mnie żadnych wrażliwych informacji"
            p "Karwasz, miałem nadzieję, że mi się to uda"
            cr "Powiedziałbym, że warto próbować ale nie w tym przydaku. To ostatnie ostrzeżenie"
            p "Dobra szefunciu, kalmuj koka"
            cr "Weź mi znikaj z oczu, wróć potem, to może powiem Ci co masz dalej robić"
            p "TAJEST"
            $ stan2["Kris"] = 0
            $ bigquest = 4

    elif bigquest == 4:
        if stan2["Kris"] == 1:
            p "Co ty się tu tak prujesz?"
            cr "Wyobraź sobie kurwa, że ta twoja banda parapetów zrobiła największą przysłguę Benkowi"
            p "W sensie, że teraz?"
            cr "Nie kurwa, jeszcze nim trafili do Czyśćca, dostarczyli Benkowi cyberpsychola"
            cr "Ten psychol miał w sobie bardzo spocyficzny wszczep"
            p "A jakoś mniej tajemniczo?"
            cr "Zakładam, że wiesz jak działa sandevistan. Dodaj sobie do tego możliwość obsługi wielu kończyn"
            cr "W taki sposób, powstaje ośmioręki strzelec, którego nie możesz nawet trafić"
            cr "A znając Benka, to on to podłączy pod tą swoją babę i będzie napierdalał"
            cr "A taka broń w rękach fixera nie jest niczym dobrym"
            p "I co, będę musiał to teraz podpierdolić?"
            cr "Nie. Dostaniesz się znowu do środka i wgrasz specjalnego wirusa na jego soft"
            cr "Jeśli pójdzie dobrze, to część wszczepów zostanie uszkodzona"
            p "Będzie to jakieś ciężkie zadanie?"
            cr "W tą podróż ruszysz z kompanami, będziesz im dawał jeszcze dodatkowe taski"
            cr "Zacznę tutaj obmyślanie wykonania tego zadania. Idź się przygotuj, to będzie ciężka sprawa"
            p "Się zrobi szefie"
            $ stan2["Kris"] = 2

        if stan2["Kris"] == 2:
            jump tempend

    jump opor


label oporslep:
    scene pokoj
    show screen hud
    call bigunl from _call_bigunl_2
    if stan2["Bo"] == 2 and dzien > 19:
        show bocall
        bo "Te kurwa, dawaj tu"
        p "Spoczko foczko, jak mi się zachce to ruszę"
        $ stan2["Bo"] = 3

    if bigquest == 4 and stan2["Kris"] == 0:
        p "Dobra kurwa, udało mi się zrobić inwigilację. Jeśli dobrze liczę, to teraz czeka mnie ostatnie zadanie"
        p "Po tym, skończy się 2 akt i będzie coś nowego do roboty. Mam nadzieję na powrót do bazy"
        p "Baza estate powinno być już zrobione i będę mógł poprawić swoje warunki mieszkalne"
        p "Kurwa, mieć więcej możliwości spędzania czasu dnia, to jest cel życia"
        p "Jeszcze znając tego kutasa, to będę musiał ulepszać pokój bo będzie więcej zadań w czasie dnia i może jeszcze da jakieś limity czasowe"
        mg "Oj, nie mylisz się kolego"
        p "No, kurwa, właśnie"
        p "Pozostaje mi tylko trzymać kciuki, bym mógł w spokoju skończyć akt"
        "Po tych słowach, usłyszałeś głośny, wkurwiony krzyk Krisa z pomieszczenia obok"
        p "No tak, chuj mi w dupe"
        $ stan2["Kris"] = 1
        
    p "Pusto tu"
    menu:
        "Jesteś w swoim pokoju, co chcesz zrobić?"
        "Idę spać":
            $ czas = 20
            $ dzien += 1
            if HP < MaxHP:
                if inventory.has_item(Flaszka) == True and MaxHP>HP+4:
                    p "Flaszka, moja żono"
                    $ inventory.remove_item(Flaszka)
                    $ HP += 5

                elif edki > 19 and hunger == 1:
                    "Przed snem zjadłeś jeszcze coś z automatu"
                    $ edki -= 20
                    if atrefakty["Jaja"] == "Zbadane":
                        $ HP += (cechy["BC"] * 2 )
                    
                    else:
                        $ HP += cechy["BC"]

                    if HP > MaxHP:
                        $ HP = MaxHP

                else:
                    "Zasnąłeś z pustym brzuchem"

            elif HP == MaxHP:
                "Śpisz słodko, jak aniołek"

            $ hunger = 1
            return

        "Czy ja przypadkiem nie dostałem?":
            if HP < MaxHP:
                p "Faktycznie mam tylko [HP] na [MaxHP]."
                p "Pancerz ma [armor] punktów"
                jump oporslep

            else:
                p "Zdawało mi się."
                jump oporslep

        "Pora zająć się jajcami" if atrefakty["Jaja"] == "W sejfie":
            jump artcrack

        "Sprawdzam chipy" if chipy > 0:
            achieve Red
            menu:
                "Który chip?"
                "Pierwszy" if chipy > 0:
                    "Sprawdzasz pierwszy chip. Wszystko co było na nim zawarte to info o Benku"
                    "Jest on fixerem w Glenn. Otwarcie toczy wojnę z gangami"
                    "Jeśli nie udaje mu się ich przekonać do rozejmu wysyła na nich łowców"
                    "Prowadzi jeszcze poszukiwania pozostałości po Seckond handzie"
                    "Chuja Ci to mówi ale podobno daje tonę kapusty za protezy"
                    "Kto wie, może i tobie uda się coś znaleźć"
                    jump oporslep

                "Drugi" if chipy > 1:
                    p "No to lecimy"
                    "Niestety cip zawierał coś, czego świat nigdy nie powinien zobaczyć"
                    "5 nocy z Haliną"
                    p "Na chuja mego wuja! Zgiń przepadnij cipie zła"
                    "Zrobiłeś taktyczny format pistoletem"
                    jump oporslep

                "Trzeci" if chipy > 2:
                    "Przeglądasz znalezionego w żabce cipa"
                    p "A niech mnie dunder świśnie, ten cip jest pełen informacji o DH. Tak na 7 procent to są jakieś pamiętniki Cyphera"
                    p "Tu coś pierdoli o wakacjach. Instrukcja wróbla. 50 twarzy Młynarczyka"
                    p "Kurwica, robi się nieciekawie"
                    "Ale najbardziej niepokojący był ostatni plik. Było na nim zdjęcie Cyphera i dokładna twoja lokalizacja"
                    c "JA i DE"
                    p "Noi chuj noi cześć"
                    "Cypher już po Ciebie idzie"
                    jump oporslep

                "Czwarty" if chipy > 3:
                    if jajca == 0:
                        p "No dobra, co my tu mamy. O kurwica! (Robert taki)"
                        "Twoim oczom ukazuje się pełna kolekcja streamów Kody"
                        p "Słyszałem legendy o tym typie. Podobno jego jajca mogą zresetować uniwersum"
                        p "Jest tu lokacja warsztatu Fanta i Kanta. Muszę to sprawdzić"
                        $ jajca = 1

                    else:
                        p "No tu było pierdolenie o jajcach, nie wiem po chuj mam to znowu czytać."

                    jump oporslep

                "Piąty" if chipy > 4:
                    p "Ostatni cip, jak tu nic nie będzie to mnie popierdoli"
                    "I Cię popierdoliło"
                    p "Jakim kurwa prawem tu niczego nie ma? Powinny być tajne informacje na tego Benka"
                    p "A tu jest jakiś dziwny pornol z Vistami! Kris musi coś z tym zrobić"
                    jump oporslep
                    
        "Wyjść" if czas > 0:
            return

label anomalia:
    scene rozstaje
    if stan2["Bo"] == 0:
        show jax at left
        ja "Oj kurwa, brakowało mi tej dziury"
        p "Niby czemu?"
        ja "Tyle jajec się tu działo, tyle krwi się przelało"
        p "I za tym tak tęsknisz?"
        ja "No też nie do końca, brakuje mi ludzi"
        p "Tęsknisz za tymi pojebami?"
        ja "Trochę, jednak da się z nimi dogadać. Dzięki nim też zacząłem cokolwiek znaczyć w mieście"
        p "No dobra, trochę rozumiem"
        ja "Ale dobra, kończmy te pogadanki, jest i nasz gość"
        scene dziura
        show jax at left
        show bo at right
        bo "A kogo to moje oczenta widzą?"
        ja "Witaj Bo" 
        bo "Tożto Jaxini!"
        ja "Nom, to ja"
        bo "A co to za wywłoka obok Ciebie?"
        p "Jestem [player_name]"
        bo "Nawet mówić potrafi! Jaki zdolniacha! Bezi w końcu daje Ci jakiś odpowiednich ludzi?"
        p "Kim jest bezi?"
        ja "Bezi nie żyje"
        bo "Bruh"
        ja "Wypadł z helikoptera i zamienił się w gerberka"
        bo "Ha ha ha! To sam zostałeś fixerem, czy dalej zlecenia?"
        ja "Umowa zlecenie"
        bo "Czyli jesteś od Krisa?"
        ja "Bingo"
        bo "No, to kto będzie nurkował"
        p "Ja"
        bo "Oj szczylu, tak mi Cie szkoda, że aż w cale"
        p "Ale czemu"
        bo "Widzisz tę dziurę?"
        p "No widzę"
        bo "To wyobraź sobie, że jest w niej ekstrakt z Cyphera"
        p "O cholera"
        bo "A to jeszcze nie wszystko! Wyobraź sobie, że szczury Guna były z biotechu"
        bo "I część z nich wpadła do tego ścieku. Potem się wymieszała i się stały większe jaja"
        p "Co kurwa"
        ja "Wyobraź sobie, że tu była sobie wcześniej Arasaka"
        ja "Rozstawili tu jakieś swoje prototypowe nagrywaczki braindanców"
        ja "I ponagrywali co tylko się dało"
        bo "I tu wchodzi kolejny poziom spierdolenia! Bo sok z Cyphera rozjebał im kable"
        bo "Tak powstał tzw. Wyciek danych"
        p "Ale po chuj mi opowiadasz te całe backstory"
        bo "Bo będziesz musiał zejść do piwnicy wyłapywać dane"
        p "Co kurwa? Jak?"
        bo "Rozmieściliśmy tam zbieraczki danych i musisz wybrać z nich dane"
        p "A czemu ja?"
        bo "Bo jesteś kurwa protagonistą"
        p "No dobra, to ma sens"
        bo "To będziesz tam łaził i zbierał dane. Tylko musisz uważać na halucynacje"
        p "No dobra, to chyba jestem gotowy"
        p "Nie wiem tylko czy ta cała bomba lorowa była potrzebna"
        mg "Spierdalaj" 
        p "No to wskakuję"
        "I wskoczyłeś do dziury"
        play sound "fall.mp3"
        bo "Głupcze zaczekaj"
        scene podziemia
        p "Kurwa, gdzie to mnie wyjebało"
        p "I czego ja mam w sumie szukać"
        p "A chuj, ja se zrobię spacerek"
        show jaxcall
        ja "Aż tak Ci się spieszy?"
        p "No troszeczkę"
        ja "To słuchaj"
        ja "Masz tu kurwa natychmiast wracać, albo urwę Ci jaja wraz z kutasem"
        p "Czemu? Ja tu robię speedrun"
        ja "Za 5 minut zacznie się dekontaminacja! To Cie wymorbuje z całej gry"
        p "Dobra, teraz się wystraszyłem"
        "I grzecznie wróciłeś do reszty"
        scene dziura
        show jax at left
        show bo at right
        bo "Nie rób tak więcej"
        p "Sorki"
        ja "Czyli, jak rozumiem, jesteśmy tu za wcześnie"
        bo "Zaiste"
        ja "Dobra [player_name], spierdalamy"
        ja "Wrócimy za x czasu"
        bo "Siemson"
        $ stan2["Bo"] = 1
        $ stan2["Kris"] = 2
        $ czas = 0
        jump opor

    elif stan2["Bo"] == 1:
        scene dziura
        show bo at right
        bo "Siema [player_name]"
        p "Cześć Bo, wyjaśnisz mi o co dokładnie Ci chodzi z tym zadaniem?"
        bo "Tak jak mówiłem wcześniej, musisz zebrać esencję z innych bazowników"
        p "Nic nie rozumiem"
        bo "Wiesz czym jest braindance co nie?"
        p "No wiem"
        bo "To zrobili takie wykrywaczki, bez pojebanych czapek"
        bo "Oni tu kiedyś mieli fabrykę i badali tak swoich pracowników"
        bo "Ale nie opłacało się i zamknęli wszystko"
        bo "Potem wystawili miejsce na handel i dalej nagrywali ludzi"
        p "Aaaa to ma teraz trochę sensu"
        bo "No, teraz musisz połazić trochę po podziemiach i szukać ruterów"
        bo "Wyciąg z Cyphera rozjebał kable i teraz są w trybie nadawania"
        bo "Jak będziesz w okolicy to twój agent zacznie wibrować"
        p "Zajebałeś to z Wiedźmina"
        mg "Tak"
        bo "Idąc dalej, pobierasz dane na agenta i wracasz do mnie"
        bo "Ja to zgrywam na dvd i oglądamy"
        bo "Po pierwszej próbie zobaczymy kto będzie to dalej robił"
        p "A czemu wtedy dopiero?"
        bo "Bo jak chuj będziemy oglądać trupy"
        p "Fujka"
        bo "I czasami mózg tego nie wytrzymuje"
        bo "Ale to na spokojnie, jak skończymy odradzanie to dam Ci znać"
        p "Spoko, to ja spadam"
        bo "Bywaj"
        $ stan2["Bo"] = 2
        jump opor

    elif stan2["Bo"] == 2:
        scene dziura
        show bo at right
        bo "Czekaj na sms-a"
        jump opor

    elif stan2["Bo"] == 3:
        scene dziura
        show bo at right
        bo "Dobra, możemy brać się za robotę"
        p "A co to za robota?"
        bo "Ty jesteś głupi czy akustyczny?"
        p "Czasami mi się zdaje że oba"
        bo "Mogłem się domyślić"
        bo "Twoim celem jest wlecenie w dziurę, tam musisz wyłapać wspomnienie Kody"
        p "A po mojemu?"
        bo "Tu masz taki pierdolniczek do łapania sygnałów"
        bo "Jak będziesz chodził po strefie anomalii to zapisuje wszystko co złapie"
        bo "Jak jakaś tania kurwa"
        bo "Następnie moi technicy albo ty zajmiecie się odszyfrowywaniem"
        mg "Zależy czy mi się będzie chciało robić jakąś minigierkę"
        bo "I z odszyfrowanych danych "
        p "Jak wcześniej mi to opowiadałeś to było prostrze"
        bo "Sprawdzałem czy podstawy zrozumiesz"
        p "Czyli mam już wskakiwać"
        bo "Tak"
        "I Bo wepchnął Cię do dziury"
        play sound "fall.mp3"
        p "KURWAAAAAA"
        scene podziemia
        p "Ja pierdolę, jak tu jest ciemno"
        p "No to chuj, idziemy po ciemku"
        "Wędrujesz po tym ciemnym miejscu w poszukiwaniu sygnału i po godzince słyszysz pikanie"
        p "Dobra kurwa, to jest chyba to miejsce. Co ja mam teraz zrobić?"
        call testSkili("Myslenie", "INT", 9) from _call_testSkili_10
        if wynik == 1:
            p "Z tego co Bo opowiadał to mam zrobić skrinszota"
            "I to faktycznie zadziałało"

        else:
            p "Chuj kurwa, chuj. Brutforsuje to"
            "Niestety pierdolnął cie prąd"
            call checkHP(10) from _call_checkHP_34
            "Ale jakimś cudem Ci się to udało"

        p "Pogczamp pacjent, pora wracać"
        scene dziura
        show bo at right
        bo "Kurwa dzieciaku, nie spodziewałem się, że Ci się to uda"
        p "Ja też się trochę tego nie spodziewałem"
        bo "To znaczy, że możemy się teraz zabrać za przeglądanie tego gówna"
        p "Ja też muszę?"
        bo "TAK"
        $ czas = 0
        "Siedziałeś resztę dnia z Bo oglądając filmiki z życia Kody"
        p "Tu się kurwa tyle rzeczy nie klei, najpierw zdrada Wujka, potem solo kręcenie fixerów"
        p "Po kiego grzyba on w ogóle robił tyle głupich rzeczy?"
        bo "Koda był kretynem ale to nie jest jedyna jego zaleta"
        p "Chodzi Ci o ten fragment z Talibami?"
        bo "Uznałbyś, że to jest brud na Benka?"
        p "No ja nie ale inni mogą mieć mniej radykalne poglądy"
        bo "Dla bezpieczeństwa to zniszczymy"
        p "Ale czemu? Moglibyśmy na tym trochę zarobić"
        bo "Jeszcze raz mi coś takiego zaproponujesz to Ci jebne"
        p "Dobra, sorki. Ile Ci w ogóle Benek płaci że tak go bronisz?"
        bo "W pierdlu siedzi mój znajomy, twoi w sumie też. Znając ich to będą próbowali uciec jak tylko się da"
        bo "Mój kumpel z tego skorzysta a twoi pewnie nawet sobie nie zdadzą z tego sprawy"
        p "No dobra, to jest spoko plan. A kim jest ten twój kolega?"
        bo "Nazywa się Tar. To jest strzelec, konstruktor, dyplomata i najbardziej szczwany skurwysyn jakiego znam"
        p "Brzmi groźnie"
        bo "On jest groźny ale tylko jak go wkurwisz. Będzie dobrym kompanem do trudnych chwil"
        p "Dobra, dzięki za info, wracam do Krisa z wieściami"
        $ stan2["Kris"] = 3
        $ stan2["Bo"] = 4

    elif stan2["Bo"] == 4 and stan2["Kris"] == 5:
        scene dziura
        show bo at right
        bo "Witam ponownie [player_name]! Jak rozumiem wracamy do poszukiwań"
        p "Tja, Kris sprawdził dokładnie imprint, trzeba szukać kolejnego"
        bo "To tym razem lecisz szukać danych po CJ-u"
        p "Kodę jeszcze kiedyś na streamie widziałem a tego kasztana w ogóle nie kojarzę"
        bo "CJ był jednym z normalniejszych policjantów w NC, debil, kanibal, chyba wiesz co mam na myśli"
        p "Standardzik chyba"
        bo "Rng to straszne jest, czasami trafiają się u nich śmieszniejsze cechy"
        bo "Ale o tym sobie raczej później pogadamy, teraz pora na nurka"
        p "Za demokrację!"
        "I dzielnie wskoczyłeś do dziury"
        scene podziemia
        p "Kurwa, zapomniałem jak tu jest ciemno"
        "Przez kilka godzin wędrowałeś po podziemiach, aż nagle trafiłeś na skrzynkę"
        p "O jasny chuj, co w tym miejscu robi czest?"
        p "Pora na otwarcie"
        if inventory.has_item(Wytrych) == True:
            p "Dzięki wielkie wytryszku, zobaczmy co jest w środku"
            $ edki += 500
            p "JA PIERDOLĘ! 500 edków, bogactwo skurwysyny"

        else:
            p "Na mózg tego nie zrobię, jest za ciemno"
        
        "Łaziłeś dalej aż nie znalazłeś kolejnego sygnału"
        p "Pyk, zgrywamy dane na telefon i spierdalamy"
        $ stan2["Bo"] = 5
        "Nagle usłyszałeś dziwny krzyk gdzieś dalej"
        p "Jasny chuj, co to było?"
        menu:
            p "Iść to zbadać?"
            "Spierdalam stąd":
                jump opor

            "Ruszam dzielne":
                "Wędrujesz dalej w podziemiach NC"
                "Po jakimś czasie ponownie usłyszałeś dziwny krzyk"
                p "Popierdoli mnie zaraz, chyba się też zesram ze strachu"
                "Idziesz dalej i znalazłeś jakiegoś naprutego gangusa"
                sb "Te kurwa, spierdalaj stąd"
                p "Jesteś moim darmowym lootem, szykuj się na śmierć"
                call testSkili("Bron","ZW",7) from _call_testSkili_11
                if wynik == 1:
                    p "Słodkich snów, parówczaku"
                    p "Pora zebrać twoje itemki"
                    $ edki += 200
                    p "Darmowe edeczki, to się szanuje"

                else:
                    $ checkHP(10)
                    p "Kurwa chuj mnie trafił, z mi jeszcze chujowo siadło"
                    p "Nawet nie ma co zbierać"
                
                p "Przynajmniej nie umarłem, zawsze jakiś sukces"
                sb "Halo! jest tam kto?"
                p "Jestem, w dodatku uzbrojony"
                sb "A ja jestem tu uwięziona"
                p "Na jaja mojej matki, kobieta w opałach. Jako biały rycerz muszę ją uratować"
                "Podchodzisz bliżej i swoim oczom nie dajesz wiary"
                p "Zaraz, zaraz, ja cię chyba znam"
                achieve Wow
                ha "Niewykluczone"
                p "Jak ty w to wpadłaś"
                ha "Niestety moi klienci są czasami jebnięci"
                p "I co, mam cię teraz uwolnić?"
                ha "Byłoby bardzo miło z twojej strony"
                p "Jakie będę miał z tego korzyści?"
                ha "Postaram się panować nad sobą w środy"
                p "Coś jeszcze?"
                ha "Uspokoję blok demonów"
                p "Wiesz co, niech stracę"
                "Uwalniasz Halinę z więzów"
                ha "Dziękuję słoneczko"
                "Halina cichaczem wyszła z pomieszczenia"
                $ stan2["Halina"] == 1
                p "A ja powinienem wracać do bazy"
                jump opor

    elif stan2["Bo"] == 5:
        scene dziura
        show bo at right
        bo "Dobra, sprawdziłem chipa, nic nie znalazłem"
        p "Serio kurwa, to na chuj ja tam latam"
        bo "Czekaj chwilę debliu jebany. Nic na Bena ale coś co może Ci się spodobać"
        p "No co? Brudy na jakiegoś psa?"
        bo "Coś znacznie ciekawszego, wskazówkę do insygni"
        p "W sensie?"
        bo "Trupy zostawiają po sobie insygnie śmierci, my możemy je zbierać"
        bo "Każda daje potężną moc i zerową odpowiedzialność"
        p "Kurwa, podoba mi się to"
        bo "Po CJ-u została jego pała"
        p "Kinky jak King"
        bo "Nie ta pała debilu jebany. Jego policyjna pałeczka"
        bo "Z jej pomocą możesz znaleźć jego kajdanki"
        p "To jest jakiś pojebany qłest kurjerski z Jakuzy?"
        bo "Jeszcze raz mi przerwiesz i dostaniesz w mordę"
        p "Sorki"
        call checkHP(10) from _call_checkHP_35
        bo "Ostrzegałem"
        bo "Kajdanki pozwalają Ci na zakucie pierdalnych chłopów"
        bo "I tylko odpowiednio dochromowani mogą próbować się z nich uwolnić"
        bo "Masz jakieś pytania?"
        p "Gdzie mogę je znaleźć?"
        bo "Musisz się udać na komisariat, potem pokażę Ci gdzie on jest"
        p "Nie możesz mi teraz pokazać?"
        bo "To wymaga zbyt dużo pracy"
        p "Zrozumiałe"
        bo "Łap tego Cipa i wracaj do szefa z wieściami, prawdopodobnie to był ostatni"
        p "Serio? Myślałem, że to będzie dłuższy quest"
        bo "Jest wystarczająco długi, zdupcaj"
        $ stan2["Bo"] = 6
        $ stan2["Kris"] = 6
        jump opor

    else:
        scene dziura
        show bo at right
        bo "Zdupcaj, utrudniasz mi pracę"
        jump opor

    jump opor

label chipnik:
    if chipy == 0:
        scene black
        "Podchodzisz do randomowego bloku"
        p "Dobra, to tutaj wykrywa mi cipa"
        p "Pora dostać się do środka"
        "Co ciekawe, są one otwarte"
        p "No to wchodzimy"
        "Wesoło tuptasz po okolicy aż znajdujesz źródło sygnału"
        p "Co jest kurwa"
        p "Kto wsadził cipa do miktofalówki"
        sb "Ja"
        p "A przepraszam bardzo, kim ty jesteś"
        sb "Senior Ciri, Krejzi Konstruktor"
        p "A pan inżynier oddałby mi tego cipa?"
        sb "Ty na łep upadłeś chyba"
        menu:
            p "No to jak rozwiązujemy ten problem?"
            "Masz tu 500 edków i spierdalaj" if edki > 499:
                achieve Psy
                $ edki -= 500
                sb "No dobra, mi pasuje"
                p "No to dogadani"
                "Zabrałeś cipa z mikrofalówki"
                achieve Cip
                $ chipy = 1
                p "Bywaj Ciri"
                sb "Bywaj"

            "VIO, weź go zjedz!" if kompan == 1:
                vi "Vpoko"
                sb "Co kurwa"
                vi "Vrup"
                "I VIO tak serio opierdolił chłopa"
                p "Ja pierdolę"
                vi "Vtrasznie Verstwy"
                "Zabrałeś chipa i w ciszy wydzedłeś"
                achieve Cip
                $ chipy = 1
                vi "Va vewno vie vcesz vawałka?"

            "Jax? Możesz pomóc?" if kompan == 2:
                ja "Kolego, daj nam chipa albo będzie problem"
                "Zastraszanie JAX-a się udało"
                sb "Dobra kurwa, masz"
                "Dostałeś cipa"
                achieve Cip
                $ chipy = 1
                p "Dziękujemy za współpracę"
                ja "I polecamy się na przyszłość"

            "A ja Ci zaraz strzelę w łep":
                call testSkili("Bron","ZW",12) from _call_testSkili
                if  wynik == 1:
                    "Odstrzeliłeś mu łep nim zdążył cokolwiek zrobić"
                    if inventory.has_item(HuMeat) == False and inventory.has_space(Cap) == True:
                        "Zebrałeś jeszcze trochę mięsa"
                        $ inventory.add_item(HuMeat)

                else:
                    call checkHP(10) from _call_checkHP_24
                    "Oddał do Ciebie strzał przed śmiercią"

                p "Dobrej nocy panie Ciri"
                "Podnosisz cip i wychodzisz"
                achieve Cip
                $ chipy = 1

        p "Zadanie wykonane, wracam do bazy"
        jump opor

    elif chipy == 1:
        p "No popierdoli mnie"
        scene badblok
        p "Cip jest w bloku demonów"
        p "Obawiam się, że to może być za trudne zadanie dla mnie"
        p "Ale w sumie, chuj. Jak coś będzie źle to wczytam sejva"
        p "IDI"
        "Wchodzisz do środka"
        scene black
        p "Kurwa, ciemno tu jak w dupie u Cyphera"
        call cipflash from _call_cipflash
        p "Szkoda, że nie mam latatki"
        p "Mam nadzieję, że nie stanie mi się nic złego"
        "I kurwa deklu wykrakałeś"
        sb "Kurwa Mietek, dawaj na browara"
        sb "Spoko Waldek, żabka jest blisko"
        menu:
            "Jak unikniesz kłopotów?"
            "Jestem jak cień":
                call testSkili("Atletyka", "ZW", 10) from _call_testSkili_1
                if wynik == 1:
                    "Jesteś jak Cień, demony cie nie zauważyły"

                else:
                    call checkHP(12) from _call_checkHP_25
                    "Jeden z demonów cię kopnął"
                    p "Kurwa cosplay trupa nie był dobrym pomysłem"

            "Pora na buchowego potwora" if inventory.has_item(Smoke) == True:
                $ inventory.remove_item(Smoke)
                sb "Kierwa Waldek, Zbychu znowó pali to gówno"
                sb "No to dawaj mu najebiemy przed wyjściem"
                "Jakiś inny demon dostał agro"

            "Jax, śmigło" if kompan == 2:
                ja "Fyr fyr fyr"
                "Widzisz jak Jax wyśmiglił oponentów z pomieszczenia"
                p "Dobra robota"

            "Chuj kurwa, atak frontalny":
                call testSkili("Bron", "ZW", 15) from _call_testSkili_2
                if wynik == 1:
                    "Demony zostały pokonane (przynajmniej te dwa i to na pięć minut)"
                
                else:
                    call checkHP(15) from _call_checkHP_26
                    "Jeden z nich sprzedał Ci luja na łep i poszli dalej"

        p "Dobra, to było intensywne"
        p "Trza iść dalej"
        "Wesoło tuptasz dalej aż trafiasz do celu"
        p "No nie, NO KURWA NO NIE"
        p "Te skurwysyny dały chipa do automatu typu wending"
        menu:
            "Co mam robić?"
            "Niech stracę te 200 edków" if edki > 199:
                "Wpłaciłeś dwie stówy"
                $ edki -= 200
                p "Noi cip zdobyty"
                $ chipy = 2

            "VIO, możesz pomóc?" if kompan == 1:
                vi "Vaden vroblem"
                "Widzisz jak VIO zaczął trząść maszyną"
                "I dzięki temu wypadł cip"
                $ chipy = 2
                p "Dzięki VIO"

            "Rozkręcamy imprezę" if inventory.has_item(Srubo) == True:
                $ inventory.remove_item(Srubo)
                "Rozkręciłeś automat i wydobyłeś cip. Niestety, twój śrubokręt się rozwalił"
                $ exp += 2
                $ chipy = 2


            "Zacznę hackowanie":
                call testSkili("Myslenie", "INT", 10) from _call_testSkili_3
                if wynik == 1:
                    p "No i ez, cipek za friko"
                    $ chipy = 2

                else:
                    $ edki = 0
                    p "No kurwa bez jaj, zabrało mi wszystkie pieniądze"
                    $ chipy = 2
                    p "Oby ten cip był tego wart"

        p "Zadanie wykonane, wracam do bazy"
        jump opor
        
        
    elif chipy == 2:
        stop music
        play music "szop.mp3" volume 0.2
        scene black
        p "O proszę, ciekawe"
        p "Wygląda na to, że ten chip jest w żabce"
        scene frogszop
        if Frakcja == 6:
            fse "OMG Anon, ty wróciłeś!"
            p "Prawda żabeńko ale teraz nazywam się [player_name]"
            fse "Czemu?"
            p "Tajne przez poufne"
            fse "I jesteś tu pracować dalej czy co?"
            p "Chipa szukam, szef zgubił tu jakieś ważne dane"
            fse "To pomogę Ci szukać"
            "I razem szukaliście tylko chwilę"
            $ chipy = 3
            p "Zajebiście, wielkie dzięki"
            fse "Polecam się na przyszłość"
            jump opor

        else:
            fse "Dzień dobry, mogę w czymś pomóc?"
            p "Tak, czy ma pani gdzieś tu cip?"
            fse "Zboczeńcu!"
            p "Nie, nie, nie, taki z danymi"
            fse "Jeśli pan zaraz nie wyjdzie, to wezwę ochronę"
            p "Dobra dobra"
            menu:
                p "Czy mam jakiś pomysł jak go zdobyć"
                "Bomba dymna" if inventory.has_item(Smoke):
                    $ inventory.remove_item(Smoke)
                    p "ZADYMA"
                    "Zadymiłeś cały sklep, masz chwilę na szukanie"
                    $ czas -= 5
                    p "Dobra jest! Teraz trzeba spierdalać"
                    $ chipy = 3
                    $ exp += 2
                    jump opor

                "Spróbuje ją zagadać":
                    call testSkili("Gadanie", "CHAR", 10) from _call_testSkili_4
                    p "Droga babko w żabko, proszę wysłuchaj mnie"
                    if wynik == 1:
                        "Wyperswadowałeś babeczce swój dostęp do sklepu"
                        fse "No dobra, tylko bez napastowań w przyszłości"
                        p "Luzik arbuzik"
                    
                    else:
                        "Babeczka nie chciała słuchać"
                        fse "OCHRONA"
                        sb "A Ci jebne"
                        p "Ło nie"
                        call checkHP(15) from _call_checkHP_27
                        p "Ała, jak to mocno uderzyło"
                        sb "Dobra, teraz możesz znowu robić zakupy"

                "Przepraszam, przejęzyczyłem się, 200 edwardów załatwi sprawę?" if edki > 199:
                    $ edki -= 200
                    fse "No dobra, niech będzie"
                    fse "Ale proszę się pośpieszyć, bo zaraz tu będzie ochrona"
                    p "Myślałem że mamona rozwiąże sprawę"
                    fse "Ochrony to nie interesuje, a ja za szybko po nią zadzwoniłam"

            p "Czyli mogę wracać do zakupów"
            p "Mam jakieś pięć minut aby go znaleść"
            if kompan == 1:
                vi "Vobra, vnalazłem vo"
                p "Zajebiście VIO"
                $ chipy = 3
                p "Chyba możemy wracać"
            
            elif kompan == 2:
                ja "To jest to czego szukamy?"
                p "Bingo"
                $ chipy = 3
                p "No to wracamy"

            else:
                p "Kurwa, trochę mi zajęło szukanie tego gówna"
                fse "Jeśli pan nie wyjdze wezwę ochronę"
                $ czas = 0
                p "Dobra, dobra, już spierdalam"
                $ chipy = 3
                p "Ale przynajmniej mam cipa"

        stop music
        jump opor

    elif chipy == 3:
        $ nua = len(persistent._achievements)
        p "Kolejny cipek"
        p "I mi pokazuje, że jest w jednej z alejek"
        p "I to takiej dziwnej ciemnej"
        p "Chuj tam, robota to robota"
        scene black
        "Wchodzisz w ciemną alejkę i tak jak się mogłeś spodziewać"
        "Jakiś sus typus wyszedł, blokując Ci drogę"
        gkp "Witaj [old_pn]"
        p "Skąd znasz moje imię?"
        gkp "To nie jest istotne"
        gkp "Muszę sprawdzić  czy jesteś gotowy"
        if nua > 19:
            gkp "Tak, jesteś gotowy"
            p "Ale co to kurwa w ogóle znaczy?"
            "Ziomo zniknął, zostawiając po sobie tylko cip"
            $ chipy = 4
            p "No dobra, jakoś poszło"
            jump opor

        else:
            gkp "Musisz jeszcze pozdobywać osiągnięć"
            p "Serio kurwa? Nie masz innych pomysłów na wydłużenie gry?"
            "Ale ziomka już nie było"
            p "No i spermastycznie"
            jump opor

    elif chipy == 4:
        p "No dobra, ostatni cip"
        p "Obstawiam, że czeka mnie tutaj niesamowicie trudna walka"
        p "FInałowy boss, wyzwanie mojego życia"
        "I się niesamowicie myliłeś"
        p "Co jest kurwa"
        p "Ten cip literalnie leży na podłodze"
        "Podnosisz cip z podłogi"
        $ chipy = 5
        p "No dawaj kurwa, go pvp"
        "But nobody came"
        p "No dobra, to jest dziwne"
        "I tak czekałeś do końca dnia ale nikt się nie pojawił"
        p "No to chuj, wracam"
        achieve Zjw
        jump opor


    else:
        p "Mam już wszystko"

    jump opor

label pierdex:
    scene pierdex
    if bigquest == 2:
        if stan2["BB"] == 1:
            bb "Siema młody, witamy w Pierdex! Od teraz jesteś jednym z kurierów."
            p "I będę musiał jeździć po miejscach z paczkami?"
            bb "Szybko się uczysz. Dokładnie tak, będziesz miał paczki do przewozu z opcjonalnym strzelaniem do oponentów"
            bb "Czasami będzie niebezpieczna dostawa ale za to dostaniesz większą wypłatę"
            p "Chwila chwila, ty mi będziesz płacił za pracę?"
            bb "Witamy w normalnej pracy. Będziesz tu dostawał mamonę, psie pieniądze co prawda ale zawsze coś"
            p "Jasny gwint, wypłata w pracy. Chyba aż tu będę pracował dłużej"
            bb "Tak jak każdy normik. Zaraz dostaniesz już pierwszą dostawę."
            p "A niech mnie kule biją! Co będę musiał dostarczyć?"
            bb "Na start będzie Ciebie czekało proste zadanie. Przejedziesz się z pizzą do kilku miejsc"
            bb "Po dostawie, dostaniesz 60 edków wypłaty"
            p "O JA PIERDOLE! To chyba największa wypłata w moim życiu"
            bb "Nie przyzwyczajaj się, to taki bonus powitalny."
            bb "Przebieraj się w zestaw roboczy i lecisz"
            p "Się robi szefie!"
            "Przebrałeś się w outfit pierdexu i wskoczyłes na skuter"
            play music "idrive.mp3"
            scene dostawa
            "Zapierdalasz skuterkiem przez zakorkowane night city"
            p "Kurde balans, nie wiedziałem, że potrafię jeździć na skuterku"
            p "Za 50 metrów mam skręcić w prawo i będę na miejscu"
            "Parkujesz jak prawdziwy sigma"
            "Na klatce schodowej"
            p "Kolejne udane parkowanie, lepiej mi poszło, niż goonowi"
            p "Dobrze, że mnie nie słyszy, nasłałby pewnie na mnie szczury"
            stop music
            p "Pora kończyć wspominki, czas na robotę. Pizzka idzie na 6 piętro"
            p "Tup, tup, tup, tup, tup"
            "Po wejściu, zapukałeś do drzwi i otworzyła Ci gorąca milfica w szlafroku"
            p "Dzień dobry, kurier pierdex, z pizzą przyjechałem"
            sb "Kurcze, chyba nie mam portfela, mogę zapłacić w inny sposób?"
            menu:
                "Niech stracę":
                    "Wchodzisz z pizzą do środka"
                    sb "Pora sprawdzić, z czego jesteś zrobiony"
                    "Widzisz, jak ta ponętna samica wyciąga strapona"
                    achieve GOO
                    p "TO JEST WIĘKSZE OD MOJEJ RĘKI!"
                    sb "(:"
                    call testSkili("Atletyka", "ZW", 10) from _call_testSkili_12
                    if wynik == 1:
                        "Udało Ci się w porę uciec, przed napaloną samicą"
                        p "Dżisus, faken, koken, saken. Było zbyt blisko"
                        p "Jeszcze mi nawet lampucera nie zapłaciła. Kolosalnie zjebałem"
                        "Wróciłeś do firmy"
                        scene pierdex
                        bb "Dobra robota młody, zjebałeś"
                        bb "W nagrodę, nic nie dostaniesz, sam jesteś sobie winny"
                        bb "Tylko tym razem potraktuję Cię ulgowo. Jak inne zlecenia zjebiesz, sam płacisz"
                        bb "Przyjdź do mnie jeszcze za jakiś czas, następna robota będzie czekać"
                        $ czas = 0
                        $ stan2["BB"] = 2
                        jump opor

                "Domagam się wypłaty":
                    sb "No dobrze, się przejdę po edki"
                    "Samica zapłaciła, a ty wróciłeś do firmy"
                    scene pierdex
                    bb "Dobra robota młody, udało Ci się dostarczyć zamówienie"
                    bb "Masz tu swoją wypłatę"
                    $ edki += 60
                    bb "Przyjdź do mnie jeszcze za jakiś czas, następna robota będzie czekać"
                    $ czas = 0
                    $ stan2["BB"] = 2
                    jump opor

        elif stan2["BB"] == 2:
            bb "Kolejna robota na horyzoncie się pojawiła, szykuj się"
            p "Coś trudnijeszego tym razem?"
            bb "No proste że tak, pierwszy był tutorial. Teraz masz zabić boga"
            p "Co?"
            bb "Poproszono nas o przysłanie najładniejszego dostawcy i ty zostałeś wybrany"
            p "To mam być dostawcą czy szonem z roxy?"
            bb "Dostawcą"
            p "To po chuj taki opis? To jest groźba?"
            bb "Nah, tylko opis taska. Twoją paczkę mamy tutaj obok"
            "I to jest spory karton"
            p "Powiesz mi przynajmniej co jest w śroku?"
            bb "Nie mam zielonego pojęcia"
            p "Klasyk. To chuj, ruszam dzielnie."
            bb "Powodzenia"
            play music "idrive.mp3"
            scene dostawa
            p "Popierdoli mnie, ta firma śmierdzi mi seksem na zawołanie"
            p "Mam nadzieję, że w tej grze nie będzie nadmiernej seksualizacji"
            mg "Spokojnie nie będzie"
            achieve Bug
            p "Dzięki, to mnie uspokoiło"
            "Udało Ci się dojechać na miejsce"
            jump nowedh   

        elif stan2["BB"] > 2 and stan2["BB"] < 8:
            bb "Już Cie młody wysyłam do klienta"
            jump nowedh

        elif stan2["BB"] == 8:
            bb "Gładka robota młody, klient zadowolony, więc ja też jestem"
            $ edki += 1000
            bb "Masz tu wpłatę z bonusikiem za dobrą robotę"
            p "Czeka mnie jeszcze jakieś tu zadanie?"
            bb "Ostatnia przewidziana dla Ciebie dostawa. Jedziesz na badlandy z towarem"
            p "Towarem towarem?"
            bb "Bingo, jeden z lokalnych kucharzy to wysyła. Jedziesz, dajesz, uciekasz"
            p "Jak duża jest szansa, że mnie po drodze ktoś zaatakuje?"
            bb "50 procent, albo dostaniesz albo nie. Pure RNG"
            p "Dobra, no to chuj, ruszam dzielnie"
            play music "idrive.mp3"
            scene dostawa
            p "Dobra, ostatnia dostawa i będę miał wolne. Kurwa, oby to zadziałało"
            p "Jak po tym wszystkim Kris da mi coś głupiego na next taska to chyba spierdalam"
            p "Wydaje mi się, że to jest na tyle sus, że mu dam cynk po tym. Jeśli Blink nie napisał mu już"
            "Wyjechałeś poza teren NC"
            p "Popierdoli mnie, taka trasa do zrobienia. Dostawa po piasku powinna być nielegalna"
            stop music
            scene badchruch
            p "Kurwa to jest tu? Kto zamawia dragi na środek pustyni?"
            show alfonso at left 
            al "To ty jesteś tym kurierem?"
            p "Tajest, mam tu paczuszkę opłaconą z góry"
            al "Postaw ją na ziemi i spierdalaj stąd"
            p "Dobra szefie, bez takich nerwów"
            "Postawiłeś paczkę na ziemi, wskoczyłeś na skuter i zacząłeś uciekać"
            play sound "BOOM.mp3"
            p "Co tam się kurwa stało"
            "Się okazało, to paczkę wyjebało"
            p "Nie nie nie nie nie, ja się w to nie mieszam"
            "I błyskawicznie wróciłeś prosto do szefa"
            scene pierdex
            bb "Dobra robota młody, ostatnia paczka z głowy"
            p "CO TO KURWA MIAŁO BYĆ? PO CHUJ JA MIAŁEM ZAWIEŹĆ BOMBĘ"
            bb "Takie delikatne wyrównanie rachunków, nie musisz wiedzieć więcej"
            p "Mogłeś mi przynajmniej powiedzieć, jakbym się wjebał w tira, to z trzy bloki bym rozjebał"
            bb "Niestety, tak tu u nas wyglądają sprawy. Nie musisz się martwić, to było tylko ten jeden raz"
            p "Czy masz jeszcze jakieś paczki do transportu, czy mogę już iść w diabły"
            bb "Masz pełne prawo iść do diabła, możesz go ode mnie pozdrowić"
            p "To spierdalam, sajonara"
            achieve DTH
            $ stan2["BB"] = 9
            $ czas = 1
            jump opor


label nowedh:
    stop music
    play music "a2amb.mp3"
    scene bazadh
    if stan2["BB"] == 2:
        p "Co to kurwa jest? Czemu ktoś tu zamówił paczkę?"
        show cypher at left with moveinleft
        c "To byłem ja! HiHiHaHa"
        p "Co do kurwy? Ty nie powinieneś być w więzieniu"
        c "Słuchaj szczylu, ja mam swoje metody na unikanie konsekwencji swoich czynów"
        p "Na przykład?"
        c "Tym razem mój geniusz nawet mnie zaskoczył. Znalazłem maszynę klonującą i się zklonowałem"
        c "Następnie, wysłałem czterysta swoich klonów do więzienia a sam sobie tu chilluję bombę"
        p "Gdzie ty niby znalazłeś maszynę klonującą?"
        c "W magazynie wojskowym stała niepilnowana, tylko głupi by nie zabrał"
        p "A potem się dziwisz, że armia nie chce Ci dawać zadań"
        call cipflash from _call_cipflash_1
        c "Gnoju, nie pyskuj tu do mnie. Teraz będę twoim szefem!"
        p "Jak kurwa niby?"
        c "Pewnie BB nic Ci nie powiedział ale będziesz miał dla mnie kilka bojowych zadań do wypełnienia."
        p "Będą tak samo głupie jak w pierwszym akcie?"
        c "Lepiej! Będą ciut głupsze ale o to się nie powinieneś martwić."
        p "To powiedz mi, co mam zrobić"
        c "To ja tu wydaję rozkazy. Teraz słuchaj, bo powiem Ci co masz zrobić"
        p "Pojebie mnie"
        c "Twoje zadania to:"
        $ stan2["BB"] = 3
        c "Przywiezienie mi soczystego kawałka sera"
        c "Następnie, będę potrzebował 500 edków"
        c "Później, jak wydam te pieniądze, to się wybiorę na zakupy"
        c "To co tam kupię, będziesz musiał dać Jaxowi, on powie Ci dalej co będziesz miał zrobić"
        c "Po tym wszystkim, będzie ciebie czekać zadanie ostateczne ale o nim opowiem Ci później"
        p "I jak ja mam to niby wszystko zapamiętać?"
        c "Widziałem jak to notujesz w telefonie, nie rób mnie w chuja"
        p "Sorson, sprawdzałem czy widzisz co ty pierdolisz. Ja tu robię ważne tajne zadania a ty marnujesz mój czas"
        c "W NC żadne zadanie nie jest ważne, przyzwyczaj się, a poza tym, ja zawszę muszę mieć coś do powiedzeia"
        c "W porównaniu do Ciebie, więc kończ pierdolić i idź mi po ten ser. Tosty chcę sobie zjeść"
        p "Dobrze Cypher"
        c "A! I jeszcze jedno, nie przychodź tu do mnie mapą, tylko przez Pierdex."
        p "Nie chce Ci się robić nowej ikony?"
        mg "Tak"
        c "Nie debilu, to ma być tajna dostawa."
        p "Sranie w banie, a nie tajne dostawianie"
        $ czas = 0
        jump opor

    if stan2["BB"] == 3 and inventory.has_item(Ser) == True:
        show cypher at left with moveinleft
        c "Jeśli mój węch mnie nie myli, to chyba przyniosłeś ser. Wezmę go sobie."
        $ inventory.remove_item(Ser)
        $ stan2["BB"] = 4
        p "Powiesz mi po co Ci ten ser?"
        c "Znalazłem starą książkę kucharską jakiegoś anarchisty. Teraz będę robił sernik"
        p "Masz przynajmniej piekarnik w tej bazie?"
        c "Mam customowe cygaro z funkcją dopalacza ognia, to powinno wystarczyć"
        c "Tak z innej beczki, masz może już te 500 edków?"
        if edki > 499:
            p "Tak, udało mi się zdobyć trochę kapitału"
            c "To oddawaj"
            $ edki -= 500
            $ stan2["BB"] = 5
            c "Teraz mogę iść na zakupy, bywaj"
            hide cypher
            jump opor

        else:
            p "Nie, jeszcze muszę trochę popracować"
            c "No to idź do roboty lol"
            p "A może sam pójdziesz? A nie mnie tylko męczysz"
            c "Spierdalaj"
            jump opor

    elif stan2["BB"] == 4:
        show cypher at left with moveinleft
        c "Masz te 500 edków?"
        if edki > 499:
            p "Tak, udało mi się zdobyć trochę kapitału"
            c "To oddawaj"
            $ edki -= 500
            $ stan2["BB"] = 5
            c "Teraz mogę iść na zakupy, bywaj"
            hide cypher
            jump opor

        else:
            p "Nie, jeszcze muszę trochę popracować"
            c "No to idź do roboty lol"
            p "A może sam pójdziesz? A nie mnie tylko męczysz"
            c "Spierdalaj"
            jump opor

    elif stan2["BB"] == 5:
        show cypher at left with moveinleft
        c "Ah, uwielbiam chodzić na zakupy bez obstawy, najlepsze promocje mi się wtedy trafiają."
        p "No to pochwal się, co takiego udało Ci się kupić"
        c "Oj stary, nawet nie wiesz co można znaleźć w chińczykach"
        p "W sensie, że w sklepach chińskich?"
        c "To zostawię w twojej strefie domysłów"
        p "Kurwa Cypher, czy ty napadłeś jakiś żółtków?"
        c "Hi Hi Ha Ha"
        p "Dobra chuj, wracając, co masz takiego niesamowitego"
        $ inventory.add_item(Wytrych)
        c "Niesamowite ustrojstwo, potrafiące otwierać wszystkie zamki w okręgu trzech stanów"
        p "Cypher, zwykły wytrych możesz kupić w praktycznie każdym sklepie"
        c "Po pierwsze, to nie zwykły, tylko przeklęty i nie jest wytrych, tylko ustrojstwo"
        c "Przeklęty ustrojstwo"
        p "Jak to jest niby przeklęte? Rzuciłeś na niego strefę dobrych rzutów?"
        c "Nah, o klątwie mi powiedział taki dziwny cygan z cyckami"
        c "Teraz jego magiczne przeklęte zdolności będzie musiał Jax przetestować"
        p "I co takiego ma tym niby otworzyć?"
        c "Spółkę z ograniczoną odpowiedzialnością w trzy dni"
        p "Popierdoli mnie"
        c "Jaxa pewnie też w czasie jego prób, zanieś mu to i zobacz co zrobi"
        p "A on przynajmniej wie, że dostał takie zadanie bojowe?"
        c "Ty na łep chyba upadłeś, jakby wiedział, to nie byłoby takie śmieszne wtedy"
        p "Jeśli ten twój następny qłest będzie równie głupi, to nie wiem co zrobię"
        c "Pewnie nic lol. Znikaj już, muszę go wymyśleć"
        $ stan2["BB"] = 6
        jump opor

    elif stan2["BB"] == 7:
        c "I jak? Udało się wam otworzyć działalność?"
        p "Nah, zamiast tego udało nam się otworyć skrzynkę"
        call cipflash from _call_cipflash_2
        c "CO! Dałem Ci jasne zadanie bojowe a ty je całkowicie olałeś?"
        p "Bingo"
        c "Niesubordynacja u pracownika"
        c "jest"
        c "absolutnie"
        c "Dopuszczalna :), tego się po tobie spodziewałem [old_pn]. Dobra robota"
        p "Czyli podoba Ci się to co zrobiłem"
        call cipflash from _call_cipflash_3
        c "Tak."
        p "Wylkuczasz się z danymi w Hudzie"
        c "Nie wiem co do mnie mówisz ale klepie w chuj"
        p "Dobra klepaczu, ostatnie zadanie mi teraz dawaj"
        c "Nie mam już więcej zadań, żartowałem z tym ostatnim"
        p "To na chuj ja czas tracę!"
        c "Chciałem tylko trochę pogadać z ludźmi, strasznie pusto jest w tej bazie"
        menu:
            "Twoja reakcja?"
            "Niech stracę, pogadam z nim":
                stop music
                $ renpy.notify("Cypher to zapamięta")
                p "Niech stracę, co tam u ciebie Cypher"
                $ czas = 0
                c "A dziwnie dość, siedzę tu sobie praktycznie sam, całe DH lata teraz po Czyśćcu i szuka magicznego kamienia"
                p "Tak Ci brakowało kontaktu z ludźmi?"
                c "Oj [old_pn] żebyś wiedział, pusto tu jest strasznie, czasami gadam sam do siebie by jakoś wypełnić tę pustkę"
                p "Kurwa, to brzmi poważnie, nie chcesz może iść z tym do jakiegoś doktorka?"
                c "Na łep chyba upadłeś, da mi tylko jakieś proszki i każe spierdalać"
                p "Zawsze możesz spróbować, jest szansa, że to coś pomoże"
                c "Sztuczne ogłupianie siebie nie zabierze całego tego bólu ode mnie"
                p "A wiesz czemu cały czas odczuwasz cierpienie?"
                c "Izolacja mnie tak dobija, nienawidzę być sam ale boję się zbliżyć do kogoś. Sam dobrze wiesz jak to boli, gdy ktoś, do kogo się przywiązałeś nagle znika"
                p "Można powiedzieć że wiem"
                c "No właśnie, myślałem, że się do tego przyzwyczaiłem ale tylko oszukuję siebie. Cały czas chodzę uśmiechnięty, ukrywając ból"
                p "Mówiłeś może o tym kiedyś komuś wcześniej?"
                c "Raz się zdarzyło, zaczęło boleć tylko jeszcze bardziej. Ja nie potrafię tak zrzucić z siebie wszystkiego na kogoś"
                p "Kurwa, Cypher, od tego masz nas w końcu, tak długo jak się trzymamy jako drużyna, tak długo będziemy sobie pomagać"
                c "Łatwo Ci mówić, jak Ci coś nie wyjdzie, to wczytasz sobie zapis i lecisz dalej. Ja tak nie mogę"
                p "Nie do końca rozumiem o co Ci chodzi"
                c "Klasyk, coraz częściej tak się dzieje, mówię coś, co siedzi we mnie i nikt nie jest w stanie tego zrozumieć, latam tylko, by sprawiać pozory"
                p "Oj Cypher, tylko proszę, nie rób nic głupiego"
                c "Luzy rajtuzy [old_pn], jeszcze we mnie płynie diamentowa krew, będę walczył do samego końca"
                p "Cieszę się, bez Ciebie, byłoby tu bardzo pusto"
                $ renpy.notify("Cypher to docenia")
                c "Dzięki"
                achieve Dep
                "Ostatecznie, wieczorem wróciłeś do bazy"


            "Ja idę, mam świat do ratowania":
                c "Szkoda"
        
        $ stan2["BB"] = 8
        jump opor


    else:
        show cypher at left with moveinleft
        c "Kolego, ty chyba nie masz tego co mi jest potrzebne, powinieneś wrócić z odpowiednimi przedmiotami."
        jump opor

label jajquest:
    scene kfws
    p "Dobra kurwa, tu powinny być te jajca"
    "Spędziłeś trochę czasu na szukaniu jajec"
    p "Są kurwa!"
    achieve Egg
    "Tylko, że w sejfie"
    p "No kurwa, jak ja to otworzę?"
    p "Ten sejf nie jest jakiś giga duży, zabiorę go ze sobą"
    "Spakowałeś sejf do plecaka"
    p "Kod jest na 6 cyfr"
    p "Jak mnie pamięć nie myli to mam 1/10^6 szansy na trafienie"
    p "Chuj, coś wykombinuje"
    "Spakowałeś itemki i wróciłeś do domu"
    $ atrefakty["Jaja"] = "W sejfie"
    $ jajca = 2
    return


label cipfin:
    scene black
    p "Dobra, to chyba to miejsce"
    p "Mam nawiązać kontakt z jakimś randomem żeby zdobyć od niego inprinty mózgów"
    p "Nie mam zielonego pojęcia co to kurwa znaczy"
    p "Gdzie ta jego jebana kuźnia?"
    p "Tu chyba"
    "Wchodzisz to kuźni osobowości"
    p "Halo, kurwa, jest ktoś w domu?"
    au "Jestem"
    p "Przysyła mnie Czerownopolski, podobno masz dla mnie jakieś maski"
    au "Ta będę je miał, tylko daj mi te chipy i będzie można lecieć z tematem"
    "Przekazałeś cipy kowalowi"
    au "Teraz spierdalaj i czekaj na mój znak"
    p "Napiszesz do mnie sms-a?"
    au "Pojebało Cię, na telefonie nie ma miejsca na więcej aplikacji"
    p "Fuckt"
    au "Przyjdź do Krisa w odpowiednim czasie, on cie wysle do mnie"
    p "A nie mogę na mapce kliknąć?"
    au "Ty widzisz ile tam jest miejsca zabranego?"
    p "Czaje"
    au "Dobra, to spierdalaj mi stąd [player_name], muszę wracać do roboty"
    p "Dobra, dobra, już spierdalam"
    $ bigquest = 1
    $ stan2["Kris"] = 0
    jump opor

label artcrack:
    scene black
    p "Dobra, to czym się mogę zająć"
    menu:
        "Odblokuję jaja Kody" if atrefakty["Jaja"] == "W sejfie":
            p "Ok, prosty sejf, z 6 cyfrowym zamkiem"
            p "No to strzelamy kod"
            $ odp = renpy.input("Kod",length=6)
            if odp == "111221":
                p "Kurwa trafiłem"
                p "Ale jaja, i teraz one są moje"
                $ atrefakty["Jaja"] = "Do zbadania"
                p "Hihihaha"
                p "Teraz muszę je tylko zbadać"

            else:
                p "Kurde balans, to nie ten"
                p "Strzelanie nie ma sensu"
                p "Muszę się dowiedzieć jaki jest ten kod"

        "Badam jajuchy" if atrefakty["Jaja"] == "Do zbadania":
            p "No to dobra, pora zbacać jajuchy"
            $ dzien += 2
            "Spędziłeś dwa dni na badaniach"
            p "Skończone, kurwa, nareszcie"
            $ atrefakty["Jaja"] = "Zbadane"
            p "Wygląda na to, że teraz będę się szybciej regenerował"

    jump oporslep


label tempend:
    scene black
    mg "Gratulacje, skończyłeś aktualny progress 2 aktu cptg"
    mg "Kiedy następne updaty będą to zobaczę po robocie"
    mg "Jeśli udało Ci się skończyć ten moment historii, wyślij mi screena następnej wiadomości"
    mg "Jax i VIO mnie bijo"
    mg "Obfita nagroda Cię czeka"
    mg "Btw. wielkie dzięki dla Mandauskyego, Araba, Czajniga i Żyda za ich wielką pomoc w testach"
    mg "Wielkie dzięki za granie"
    mg "Pamiętaj poszukać nagród w galeri"
    mg "Papatki"
    $ session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
    $ persistent.czasGry += session_time
    $ MainMenu(confirm=False)()