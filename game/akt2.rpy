label a2intro:
    play music "a2amb.mp3"
    $ akt = 2
    $ bigquest = 0
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
    $ old_pn = [player_name]
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
    while talkloop == 0:
        menu:
            ja "Co tam chcesz [player_name]?"
            "Potrzebuję Cię w moim składzie!" if kompan == 0:
                ja "Spoczko foczko"
                $ kompan = 2
                "JAX dołącza jako kompan"

            "Wyskakujesz może na piwko?" if kompan == 2:
                ja "Spoczko, da się zrobić"
                jump piwko

            "Idę questować solo" if kompan == 2:
                ja "Żaden problem mordeczko"
                $ kompan = 0
                "JAX wraca do swoich zajęć"
            
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
                        ja "No to lecimy, czas trenować cardio"
                        $ skile["Atletyka"] += 1
                        "Spędziłeś trochę czasu na bieganiu"
                        $ czas -= 10

                    "Strzelanie" if skile["Bron"] < 7:
                        ja "Kierunek strzelnica!"
                        $ skile["Bron"] += 1
                        "Udało Ci się trafić nawet 10"
                        $ czas -= 10

                    "Rozmawianie" if skile["Gadanie"] < 7:
                        ja "No to opowiadaj, jak Ci życie mija"
                        $ skile["Gadanie"] += 1
                        "Opowiedziałeś JAX-owi o swoich problemach"
                        $ czas -= 10

                    "Rozmyślanie" if skile["Myslenie"] < 7:
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
            $ chipy = 0
            p "Ale co w sumie z tego, jak na tych cipach gówno jest o Benku"
            cr "To dobry omen"
            p "Ale jak kurwa"
            cr "To znaczy, że nasi informatorzy to gówno ale na spokojnie"
            cr "Zaraz ruszysz na misje, która nam wszystko wyjaśni"
            cr "Ten ostatni chip jaki znalazłeś będzie naszym kluczem"
            cr "Idziesz teraz do kowala, on może coś ci wyjaśni"
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
        cr "Czekaj na dalsze updaty"
        jump tempend

    elif bigquest == 3:
        pass

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

                elif edki > 19:
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

            return

        "Czy ja przypadkiem nie dostałem?":
            if HP < MaxHP:
                p "Faktycznie mam tylko [HP] na [MaxHP]."
                p "Pancerz ma [armor] punktów"
                jump oporslep

            else:
                p "Zdawało mi się."
                jump oporslep

        "Wyjebie gówno przez okno":
            jump yeet

        "Pora zająć się jajcami" if atrefakty["Jaja"] == "W sejfie":
            jump artcrack

        "Sprawdzam chipy" if chipy > 0:
            achieve Red
            menu:
                "Który chip?"
                "Pierwszy" if chipy > 0:
                    "Sprawdzasz pierwszy chip. Wszystko co było na nim zarawte to info o Benku"
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
                    p "No dobra, co my tu mamy. O kurwica! (Robert taki)"
                    "Twoim oczom ukazuje się pełna kolekcja streamów Kody"
                    p "Słyszałem legendy o tym typie. Podobno jego jajca mogą zresetować uniwersum"
                    p "Jest tu lokacja warsztatu Fanta i Kanta. Muszę to sprawdzić"
                    $ znajOkol = 4
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
        ja "Trochę, jednak da się z nimi dogadać"
        ja "Dzięki nim też zacząłem cokolwiek znaczyć w mieście"
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
        bo "Nawet mówić potrafi! Jaki zdolniacha"
        bo "Bezi w końcu daje Ci jakiś odpowiednich ludzi?"
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
        ja "Wyobraź sobie, że tu była sobie wcześniej arasaka"
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
        bo "To będziesz tam łaził i zbierał dane"
        bo "Tylko musisz uważać na halucynacje"
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
        ja "Za 5 minut zacznie się dekontaminacja"
        ja "To Cie wymorbuje z całej gry"
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
        bo "Czekaj na sms-a"
        jump opor

    elif stan2["Bo"] == 3:
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
        bo "Następnie moi technicy alby ty zajmiecie się odszyfrowywaniem"
        mg "Zależy czy mi się będzie chciało robić jakąś minigierkę"
        bo "I z odszyfrowanych danych "
        p "Jak wcześniej mi to opowiadałeś to było prostrze"
        bo "Sprawdzałem czy podstawy zrozumiesz"
        p "Czyli mam już wskakiwać"
        bo "Tak"
        "I Bo wepchnął Cię do dziury"
        play sound "fall.mp3"
        p "KURWAAAAAA"
        scene black
        p "Ja pierdolę, jak tu jest ciemno"
        p "To to chuj, idziemy po ciemku"
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
        p "Tu się kurwa tyle żeczy nie klei, najpierw zdrada Wujka, potem solo kręcenie fixerów"
        p "Po kiego grzyba on w ogóle robił tye głupich rzeczy?"
        bo "Kody był kretynem ale to nie jest jedyna jego zaleta"
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
        p "Dobra, dzięki za info, wracam do Sójeczki z wieściami"
        $ stan2["Kris"] = 3
        $ stan2["Bo"] = 4

    elif stan2["Bo"] == 4 and stan2["Kris"] == 5:
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
        scene black
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
                p "Popierdoli mnie zaraz, chyba się też zestam ze strachu"
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

    else:
        bo "Zdupcaj, utrudniasz mi pracę"
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
        show ciphate
        p "Szkoda, że nie mam latatki"
        hide ciphate
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

                "Przepraszam, przejęzyczyłem się, 200 załatwi sprawę?" if edki > 199:
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
        p "Kolejny chipek"
        p "I mi pokazuje, że jest w jednej z alejek"
        p "I to takiej dziwnej ciemnej"
        p "Chuj tam, robota to robota"
        scene black
        "Wchodzisz w ciemną alejkę i tak jak się mogłeś spodziewać"
        "Jakiś sus typus wyszedł, blokując Ci drogę"
        gkp "Witaj [player_name]"
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
        p "No dobra, ostatni chip"
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
        if postacie2["BB"] == 0
            show bbb
            bb "Siema młody, witamy w Pierdex! Od teraz jesteś jednym z kurierów."
            p "I będę musiał jeździć po miejscach z paczkami?"
            bb "Szybko się uczysz. Dokładnie tak, będziesz miał paczki do przewozu z opcjonalnym strzelaniem do oponentów"
            bb "Czasami będzie niebezpieczna dostawa ale za to dostaniesz większą wypłatę"
            p "Chwila chwila, ty mi będziesz płacił za pracę?"
            bb "Witamy w normalnej pracy. Będziesz tu dostawał mamonę, psie pieniądze co prawda ale zawsze coś"
            p "Jasny gwint, wypłata w pracy. Chyba aż tu będę pracował dłużej"
            bb "Tak jak każdy normik."


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
    $ znajOkol = 3
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
    p "Przysyła mnie Czerwonopolski, podobno masz dla mnie jakieś maski"
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


label piwko:
    if kompan == 2:
        scene japiwko
        if postacie2["Jax"] == 0:
            ja "Kurwa, przyjemnie tak sobie skoczyć na browca"
            p "Ciężko się z tobą nie zgodzić"
            ja "To opowiadaj [old_pn], co tam u Ciebie"
            p "Pamiętasz moje imię nawet, jestem pełen podziwu"
            ja "No słuchaj, to jest tylko zmienna"
            mg "(Jeśli się nie wyjebało)"
            p "Tak czy siak, podziwko."
            ja "Wracajmy do tematu, jak tam Ci życie mija?"
            p "No powoli to jakoś leci, wiesz, questy się robi, edki zarabia"
            ja "Czyli po staremu"
            p "Gadaj lepiej jak u Ciebie"
            ja "No co, czekam aż koledzu wyjdą z pierdla i staram nie dać się zabić"
            p "To jest już klasyk"
            ja "Nom, jak już wrócą to czeka nas bojowe zadanie"
            p "O kurwens, brzmi poważnie. Co to za robota"
            ja "Ty jeszcze szczylem jesteś w mieście, nie mieszaj się w to"
            p "Kurwa, teraz to mnie zainteresowałeś, opowiadaj"
            ja "VIO znalazł jednego z ziomków którzy mnie porwali. Musimy go teraz dopaść"
            p "Jak VIO dał radę coś takiego w ogóle znaleźć?"
            ja "On ma swoje sposoby, tak Ci powiem w tajemnicy, on nie jest tak głupi na jakiego się wydaje"
            p "Ciekawe, cały czas siedzi pod taką przykrywką?"
            ja "To jest bardziej jak Doktor Jekyll i pan Hyde"
            p "Takie pojebane rozdwojenie jaźni, ciekawe. Tak miał od startu czy od niedawna"
            ja "Jak drużyna trafiła do więzienia zaczął przesiadywać w labie Łaskawcy"
            ja "Prawdopodobnie udało mu się zrobić szczepionke na Visty"
            p "Pierdolisz"
            ja "Serio, poszedł testować to na dzikich Vistach i się sam przeraził, to zadziałało ale odkrył coś jeszcze gorszego"
            p "Visty zaczęły szczekać?"
            ja "Powstała nowa generacja Vist. V5 zaczyna wchodzić do obiegu. Mają zwiększone limity inta"
            p "Do jakiego stopnia?"
            ja "Teraz mogą mieć max 4"
            p "To serio jest niebezpieczne i tam się dowiedział o agentach?"
            ja "Coś w tym rodzaju. Jakiś korpos był na miejscu, potem wpadł w ręce VIO"
            p "Jak bardzo groźnie tam może być?"
            ja "Sami agenci nie są niebezpieczni, jest ich chyba trzech, z czego jeden robił to tylko dla awansu"
            p "Jebane korposzczury"
            ja "Złapiemy jakiegoś z nich i znajdziemy szefa. Potem będę mógł się zemścić i spierdalać z tego miasta"
            p "Znudziło Ci się bycie gangusem?"
            ja "Żonka z dzieckiem na mnie czekają"
            p "Kurwa Jax, czy ty chcesz zrobić sobie dobre zakończenie?"
            ja "Przelałem już wystarczająco dużo krwi"
            p "Kurwa.... głębokie"
            "I tak spędziłeś wieczorek na piwerku z Jaxem"
            achieve Bir
            $ postacie2["Jax"] = 1

        elif postacie2["Jax"] == 1:
            "Na ten moment Jax nie chce więcej gadać"

    elif kompan == 1:
        vi "Pije solo"

    else:
        "Wyjebali Cię z baru"

    jump opor

label tempend:
    mg "Gratulacje, skończyłeś to zacząłem z 2 aktu cptg"
    mg "Kiedy następne updaty będą to studia ocenią"
    mg "Jeśli udało Ci się skończyć ten moment historii, wyślij mi screena następnej wiadomości"
    mg "Jax i VIO mnie bijo"
    mg "Obfita nagroda Cię czeka"
    mg "Btw. wielkie dzięki dla Mandauskyego, Araba, Czajniga i Żyda za ich wielką pomoc w testach"
    mg "Wielkie dzięki za granie"
    mg "Pamiętaj poszukać nagród w galeri"
    mg "Papatki"
    $ MainMenu(confirm=False)()