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
    window hide
    pause 10

label bufor:
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

            jump rozstaje

        "Czy ja przypadkiem nie dostałem?":
            if HP < MaxHP:
                p "Faktycznie mam tylko [HP] na [MaxHP]."
                p "Pancerz ma [armor] punktów"
                jump sypialnia

            else:
                p "Zdawało mi się."
                jump sypialnia

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
                call checkHP(10)
                "Oddał do Ciebie strzał przed śmiercią"
                p "Dobrej nocy panie Ciri"
                "Podnosisz cip i wychodzisz"
                $ chipy = 1

    elif chipy == 1:
        mg "in dev"
        
    elif chipy == 2:
        mg "in dev"

    elif chipy == 3:
        mg "in dev"

    elif chipy == 4:
        mg "in dev"

    else:
        p "Mam już wszystko"

    jump opor