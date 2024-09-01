label a2intro:
    $ akt = 2
    $ bigquest = 0
    default stan2 = {"Vio":0, "Jax":0, "Kris":0}
    sb "Aj karamba, bolało"
    sb "Mam nadzeję, że jesteś cały"
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
    sb "Faktycznie, wypada się przedstawić"
    sb "Krzysztof Czerownopole"
    cr "Do usług"
    p "Dobra kurwa ale skąd ty wiesz jak ja się nazywam?"
    cr "Mam swoje źródła"
    cr "Oto przed tobą: Jax"
    show jax at left
    ja "Witam"
    cr "I VIO"
    show vio at right
    vi "Vitam"
    p "On nie jest kurwa Vistą?"
    vi "Jestem, takim udomowionym"
    p "Ok, zrozumiałe"
    p "To powiesz mi co ty ode mnie chcesz?"
    cr "Ano tak. Mamy jeden prosty plan."
    cr "Drużyna już o tobie zapomniała"
    $ old_pn = [player_name]
    $ player_name = "Zbigniew"
    cr "Od teraz jesteś Zbigniew"
    p "Co kurwa?"
    cr "Spokojnie, mamy zapisane twoje dawne imię"
    cr "Jak nie zapomnę to kiedyś wróci"
    p "I co mam teraz zrobć?"
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
    cr "No nie. Masz tu dwóch dzielnych wojowników."
    cr "Będą mogli Ci pomagać w trudnych chwilach"
    cr "Ale wracając do roboty, po całym mieście są chipy z danymi."
    cr "Musisz je zdobyć a ja je sprawdzę czy są właściwe"
    p "A co się będzie na nich znadować?"
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
    call checktime
    show screen oportalk
    show screen hud
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

            "Idę questować solo" if kompan == 2:
                ja "Żaden prblem mordeczko"
                $ kompan = 0
                "JAX wraca do swoich zajęć"
            
            "Co powiesz na mały trening?" if exp > 9:
                ja "Jasne mordeczko"
                $ exp -= 10
                menu:
                    ja "Co chciałbyś ulepszyć?"
                    "Wytłumacz mi o co chodzi":
                        ja "Jak sprawdzasz swoje umiejętności, zdobywasz doświadczenie"
                        ja "Gdy zdobędziesz go wystarczająco dużo, to przychodzisz do mnie"
                        ja "Ja Ci pokażę jak wykożystać to doświadczenie w praktyce"
                        ja "A tobie następne testy idą łatwiej"
                        p "Wow, to takie proste?"
                        ja "Proste że tak!"

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
                    vi "Vuzik vrbuzik"
                    $ HP = MaxHP
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
            cr "To nie jest aż takie proste"
            cr "Masz tu wykrywacz"
            cr "Jak będziesz w okolicy to będzie brzęczeć"
            p "WOW! I co wtedy?"
            cr "Wtedy ruszasz dzielnie tam gdzie pika"
            cr "Może tam być niebezpiecznie, więc radzę iść z kimś"
            cr "VIO i JAX się polecają do napierdalania"
            p "A nie mogę wziąć ich obu?"
            cr "W sensie że do walki tak?"
            p "Tak"
            cr "Uf, nie możesz bo:"
            cr "a) To by było zbyt proste"
            cr "b) Jak walczą razem to wpadają w dziki szał"
            cr "I potrafi im czasem odjebać aż za bardzo"
            cr "Ostatnio prawie rozjebali pół osiedla"
            cr "A ja nie wiem jak to powstrzymać"
            cr "Odkąd Arasaka porwała JAX-a to jest z nim coraz gorzej"
            cr "Ale dobra, czas kończyć ten Ted tok"
            cr "Ruszaj dzielnie do roboty"
            p "Tajest!"
            $ stan2["Kris"] = 1
            jump opor

        elif stan2["Kris"] == 1 and chipy == 1:
            cr "O! Widzę że udało Ci się zdobyć pierwszego Chipa"
            cr "Gratulacje [player_name]"
            cr "Nie wiem czy widziałeś ale dodałem Ci do pokoju możliwość czytania tych danych"
            p "Wow, po chuj mi to?"
            cr "Jakby cię lore interesował to możesz sobie przeczytać"
            p "Fantastycznie, czy coś"
            cr "Dobra, nei truj mi dupy"
            $ stan2["Kris"] = 2

        else:
            cr "Zajęty jestem, przyjdź jak zrobisz jakieś postępy"
            jump opor

    elif bigquest == 1:
        pass

    elif bigquest == 2:
        pass

    elif bigquest == 3:
        pass

    jump opor


label oporslep:
    scene pokoj
    show screen hud
    call bigunl
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

        "Sprawdzam chipy" if chipy > 0:
            achieve Red
            menu:
                "Który chip?"
                "Pierwszy" if chipy > 0:
                    "Sprawdzasz pierwszy chip"
                    "Wszystko co było na nim zarawte to info o Benku"
                    "Jest on fixerem w Glenn"
                    "Otwarcie toczy wojnę z gangami"
                    "Jeśli nie udaje mu się ich przekonać do rozejmu wysyła na nich łowców"
                    "Prowadzi jeszcze poszukiwania pozostałości po Seckond handzie"
                    "Chuja Ci to mówi"
                    "Ale podobno daje tonę kapusty za protezy"
                    "Kto wie, może i tobie uda się coś znaleźć"

                "Drugi" if chipy > 1:
                    "Bla bla bla"

                "Trzeci" if chipy > 2:
                    "Ble Ble ble"

                "Czwarty" if chipy > 3:
                    "Blo blo blo"

                "Piąty" if chipy > 4:
                    "Bli bli bli"
                    
        "Wyjść" if czas > 0:
            return

label anomalia:
    jump opor

label chipnik:
    if chipy == 0:
        scene black
        p "Dobra, to tutaj wykrywa mi cipa"
        p "Pora dostać się do środka"
        "Co ciekawe, są one otwarte"
        p "No to wchodzimy do środka"
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
                $ edki -= 500
                sb "No dobra, mi pasuje"
                p "No to dogadani"
                "Zabrałeś cipa z mikrofalówki"
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
                $ chipy = 1
                vi "Va vewno vie vcesz vawałka?"

            "Jax? Możesz pomóc?" if kompan == 2:
                ja "Kolego, daj nam chipa albo będzie problem"
                "Zastraszanie JAX-a się udało"
                sb "Dobra kurwa, masz"
                "Dostałeś cipa"
                $ chipy = 1
                p "Dziękujemy za współpracę"
                ja "I polecamy się na przyszłośc"

            "A ja Ci zaraz strzelę w łep":
                call testSkili("Bron","ZW",12)
                if  wynik == 1:
                    "Odstrzeliłeś mu łep nim zdążył cokolwiek zrobić"
                    if inventory.has_item(HuMeat) == Flase and inventory.has_space(Cap) == True:
                        "Zebrałeś jeszcze trochę mięsa"
                        $ inventory.add_item(HuMeat)

                else:
                    call checkHP(10)
                    "Oddał do Ciebie strzał przed śmiercią"

                p "Dobrej nocy panie Ciri"
                "Podnosisz cip i wychodzisz"
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
        p "Szkoda, że nie mam laratki"
        hide ciphate
        p "Mam nadzieję, że nie stanie mi się nic złego"
        "I kurwa deklu wykrakałeś"
        sb "Kurwa Mietek, dawaj na browara"
        sb "Spoko Waldek, żabka jest blisko"
        menu:
            "Jak unikniesz kłopotów?"
            "Jestem jak cień":
                call testSkili("Atletyka", "ZW", 10)
                if wynik == 1:
                    "Jesteś jak Cień, domony cie nie zauważyły"

                else:
                    call checkHP(12)
                    "Jeden z demonów cię kopnął"
                    p "Kurwa cosplay trupa nie był dobrym pomysłem"

            "Pora na buchowego potwora" if inventory.has_item(Smoke):
                $ inventory.remove_item(Smoke)
                sb "Kierwa Waldek, Zbychu znowó pali to gówno"
                sb "No to dawaj mu najebiemy przed wyjściem"
                "Jakiś inny demon dostał agro"

            "Jax, śmigło" if komapn == 2:
                ja "Fyr fyr fyr"
                "Widzisz jak Jax wyśmiglił oponentów z pomieszczenia"
                p "Dobra robota"

            "Chuj kurwa, atak frontalny":
                call testSkili("Bron", "ZW", 15)
                if wynik == 1:
                    "Demony zostały pokonane (przynajmniej te dwa i to na pięć minut)"
                
                else:
                    call checkHP(15)
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
                call testSkili("Myslenie", "INT", 10)
                if wynik == 1:
                    "No i ez, cipek za friko"
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
        p "O proszę, ciekawe"
        p "Wygląda na to, że ten chip jest w żabce"
        scene frogszop
        fse "Dzień dobry, mogę w czymś pomóc?"
        p "Tak, czy ma pani gdzieś tu cip?"
        fse "Zobczeńcu!"
        p "Nie, nie, nie, taki z danymi"
        fse "Jeśli pan zaraz nie wyjdzie, to wezwę ochronę"
        p "Dobra dobra"
        menu:
            p "Czy mam jakiś pomysł jak go zdobyć"
            "spróbuje ją zagadać":
                call testSkili("Gadanie", "CHAR", 10)
                p "Droga babko w żabko, proszę wysłuchaj mnie"
                if wynik == 1:
                    "Wyperswadowałeś babeczce swój dostęp do sklepu"
                    fse "No dobra, tylko bez napaswowań w przyszłości"
                    p "Luzik arbuzik"
                
                else:
                    "Babeczka nie chciała słuchać"
                    fse "OCHRONA"
                    sb "A Ci jebne"
                    p "Ło nie"
                    call checkHP(15)
                    p "Ała, jak to mocno uderzyło"
                    sb "Dobra, teraz możesz znowu robić zakupy"

        p "Czyli mogę wracać do zakupów"
        p "Mam jakieś pięć minut aby go znaleść"
        if komapn == 1:
            vi "Vobra, vnalazłem vo"
            p "Zajebiście VIO"
            $ chipy = 3
            p "Chyba możemy wracać"
        
        elif komapn == 2:
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
        p "Kolejny chipek"
        p "I mi pokazuje, że jest w jednej z alejek"
        p "I to takiej dziwnej ciemnej"
        p "Chuj tam, robota to robota"
        scene black
        "Wchodzisz w ciemną alejkę i tak jak się mogłeś spodziewać"
        "Jakiś sus typus wyszedł, blokując Ci drogę"
        gk "Witaj [player_name]"
        p "Skąd znasz moje imię?"
        gk "To nie jest istotne"
        gk "Muszę sprawdzić  czy jesteś gotowy"
        if nua > 19:
            gk "Tak, jesteś gotowy"
            p "Ale co to kurwa w ogóle znaczy?"
            "Ziomo zniknął, zostawiając po sobie tylko cip"
            $ chipy = 4
            p "No dobra, jakoś poszło"
            jump opor

        else:
            gk "Musisz jeszcze pozdobywać osiągnięć"
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
        jump opor


    else:
        p "Mam już wszystko"

    jump opor