label a2intro:
    sb "Aj karamba, bolało"
    sb "Mam nadzeję, że jesteś cały"
    sb "Zobaczmy z czego jesteś zbudowany"
    menu:
        "Co jest moją mocną stroną?"
        "Siła":
            if helper == 0:
                $ cechy["BC"] = 6
                $ MaxHP = 10 + (5*((cechy["BC"])))

            elif helper > 50:
                $ cechy["BC"] = 4
                $ MaxHP = 10 + (5*((cechy["BC"])))

            elif helper > 0:
                $ cechy["BC"] = 5
                $ MaxHP = 10 + (5*((cechy["BC"])))

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
            $ cechy["Bron"] = 4

        "Spierdalam":
            $ cechy["Atletyka"] = 4

        "Perswaduje":
            $ cechy["Gadanie"] = 4

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