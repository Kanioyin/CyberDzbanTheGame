label spacerek:
    scene spacer
    $ czas -= 5
    $ cel = renpy.random.randint(1, 100)
    if stan["Kasia"] == 3:
        jump frogsimp
        
    if cel > 0 and cel < 11:
        if akt == 1:
            "Znalazłeś jakieś drobniaki"
            $ zysk = renpy.random.randint(1, 50)
            $ edki += zysk
            p "Znalazłem [zysk] edków"

        else:
            "Znalazłeś jakieś drobniaki"
            $ zysk = renpy.random.randint(20, 90)
            $ edki += zysk
            p "Znalazłem [zysk] edków"

    elif cel > 10 and cel < 21:
        if Frakcja == 0:
            "Ni chuja, same nudy"

        elif Frakcja == 1:
            "Wędrując znalazłeś skrzynkę z symbolem DH"
            p "Ciperowe śmieci, wezmę sobie"
            call cipflash
            $ helper = renpy.random.randint(1,200)
            "Znalazłeś [helper] edków"
            $ edki += helper
            p "Kurde balans, zawsze coś"
            $ helper = 0

        elif Frakcja == 3:
            "Wędrując, znalazłeś dziwny słoik, który postanowiłeś otworzyć"
            $ vdolce += 2
            p "Vajnie, vnalazłem 2 vdolce"

        elif Frakcja == 4:
            "Na mieście spotkałeś Kałacha. Dostałeś od niego flachę"
            $ inventory.add_item(Flacha)

        elif Frakcja == 6:
            "Na mieście znalazłeś kupon na darmowego monsterka (frogsy)"
            $ frogsy += 225

        else:
            "Ni chuja, same nudy"

    elif cel > 20 and cel < 31:
        if akt == 1:
            "Przez przypadek wszedłeś do Bloku Władcy Demonów"
            $ wpierdol = renpy.random.randint(4, 18)
            call checkHP(wpierdol) from _call_checkHP_4

        elif akt == 2:
            "Przez przypadek wszedłeś do Bloku Władcy Demonów"
            "Ale teraz nadszedł czas działać"
            menu:
                "Co robisz?"
                "Atak na suki":
                    call testSkili("Bron","ZW",7) from _call_testSkili_5
                    if wynik == 1:
                        "Demony zostały pokonane, natenczas"
                        p "Szach mat frajery"
                        $ edki += 250
                        p "Wszystkie wasze portfele są teraz moje"
                        if inventory.has_item(HuMeat) == False and inventory.has_space(Cap) == True:
                            $ inventory.add_item(HuMeat)
                            p "Wezmę trochę boczku dla VIO"
                    
                    else:
                        p "Ło nie, są silniejsi"
                        call checkHP(renpy.random.randint(4, 18)) from _call_checkHP_28

                "Ted Talk":
                    call testSkili("Gadanie","CHAR",7) from _call_testSkili_6
                    "Powiedziałeś demonom żeby spierdalali"
                    if wynik == 1:
                        "I nawet Ci się udało"
                        p "Krowy doić! He he"
                        "Kolejny sukces Night Citiowskich punków"

                    else:
                        "Niestety, nikt Cie nie zrozumiał"
                        call checkHP(renpy.random.randint(4, 18)) from _call_checkHP_29

                "Ucieczka":
                    call testSkili("Atletyka","ZW",7) from _call_testSkili_7
                    "Gdy tylko ich zobaczyłeś zacząłeś uciekać"
                    "Te pojeby otworzyły ogień"
                    if wynik == 1:
                        "Uniknąłeś części pocisków"
                        call checkHP(renpy.random.randint(1, 10)) from _call_checkHP_30

                    else:
                        "Skurwysyny chyba mają snipera"
                        call checkHP(renpy.random.randint(4, 18)) from _call_checkHP_31


        else:
            "Coś się zjebało"

    elif cel > 30 and cel < 47:
        if znajOkol == 0:
            "Udało Ci się odkryć fajny osiedlowy sklepik"
            $ znajOkol = 1

        elif znajOkol == 1:
            p "Ty kurwa, żabka jest obok, zapamiętam to sobie"
            $ znajOkol = 2

        elif znajOkol == 2:
            p "Ten ziomek przypadkiem nie powiększa wora?"
            p "Muszę to sprawdzić"
            $ znajOkol = 3

        else:
            p "Jaki fajny plasterek"
            if HP < MaxHP:
                p "A se przykleję"
                $ HP += 1
            else:
                p "Ta? To zajebiście."
                "Plasterek trafił do kosza."

    elif cel > 46 and cel < 57:
        "Wszedłeś do bloku furrasów"
        if stan2["Halina"] == 0:
            if dzien % 7 == 4:
                "Futrzana domina Cię dopadła"
                achieve Futa
                $ HP = 1
                $ czas = 0
            else:
                "Masz farta, był zamknięty"

        elif stan2["Halina"] == 1:
            "Halina dotrzymała obietnicy, blok jest spokojny"

    elif cel > 56 and cel < 66:
        "Chodząc widzisz fagasa którego możesz obrabować"
        menu:
            "Co robisz?"
            "Napadańsko":
                if akt == 1:
                    "Atakujesz kasztana"
                    call checkHP(renpy.random.randint(8, 18)) from _call_checkHP_21
                    $ zysk = renpy.random.randint(50, 150)
                    $ edki += zysk
                    p "Trochę dostałem ale udało mi się zarobić [zysk] edków!"

                elif akt == 2:
                    call testSkili("Bron","ZW",renpy.random.randint(8, 12)) from _call_testSkili_8
                    if wynik == 1:
                        "Ziomo dostał wpierdol"
                        p "A ja wypłatę"
                        $ zysk = renpy.random.randint(100, 300)
                        $ edki += zysk
                        p "Trochę dostałem ale udało mi się zarobić [zysk] edków!"

                    else:
                        p "Oj kurwa, typ jest silny"
                        call checkHP(20) from _call_checkHP_33
                        p "Następnym razem muszę się lepiej uzbroić"

            "Lepiej nie":
                pass

    elif cel == 66:
        show evilc
        achieve Zns
        ec "Witaj [player_name]!"
        p "O kierwa! To zły Cypher"
        ec "Tak, to ja"
        p "Proszę, nie rób mi krzywdy!"
        ec "Nawet nie chcę"
        $ HP = MaxHP
        "Magiczna moc złego Cyphera cię uleczyła"
        p "Cholera Cypher, dzięki"
        hide evilc with dissolve
        ec "Hi Hi Ha Ha..."


    elif cel > 66 and cel < 78:
        if inventory.has_item(Kokos) == True:
            "Znalazły Cię ćpuny"
            "Niestety mięli przewagę liczebną (było ich 3)"
            $ inventory.remove_item(Kokos)

        elif inventory.has_item(AR) == True:
            "Chodząc po ulicy czujesz, że jest Ci jakoś lekko"
            "Obracasz się za siebię i widzisz że czegoś brakuje"
            p "Kurwa"
            $ inventory.remove_item(AR)

        elif inventory.has_item(Ser) == True:
            "W twoim kierunku leci chmara (5) szczurów"
            p "Na chuja mego wuja, tylko nie to"
            $ inventory.remove_item(Ser)
            "Po chwili pojawia się też Gun"
            show gun at left
            g "Serson [player_name], nie mogę ich złapać"
            if akt == 2:
                p "Ty nie powinieneś być w pierdlu?"
                g "Faktycznie, to ja znikam"
                hide gun with dissolve
        
        else:
            p "Dziwne, nic się nie stało. Jakbym miał itemki to pewnie ktoś by mnie okradł."
            
    elif cel > 77 and cel < 81:
        p "Na chuja mego wuja, ktoś tu zostawił skrzynkę!"
        p "Ciekawe czy mam jak ją otworzyć?"
        if inventory.has_item(Wytrych) == True:
            p "Jest i wytryszek, pogczamp"
            p "Opening time!"
            $ helper = renpy.random.randint(1, 4)
            if renpy.random.randint(1, 5) == 5:
                $ inventory.remove_item(Wytrych)

            if helper == 1:
                p "O proszę! Hajsiwo"
                $ edki += renpy.random.randint(50, 300)

            elif helper == 2 and inventory.has_space(Cap) == True:
                p "Ktoś tu kurwa wsadził szczura!"
                $ inventory.add_item(Rat)
                p "Może mi się do czegoś przyda"

            elif helper == 3:
                p "Kurwa! TU JEST BOMBA!"
                call checkHP(10) from _call_checkHP_23
                p "Jebać trapy"
            
            elif helper == 4:
                p "O proszę, powiększenie ekwipunku"
                $ Cap += 1
                p "Zawsze jeden przedmio więcej"

        elif akt == 2:
            call testSkili("Myslenie","INT",10) from _call_testSkili_9
            if wynik == 1:
                p "Mój giga mózg pomógł mi to otworzyć"
                $ helper = renpy.random.randint(1, 4)
                if helper == 1:
                    p "O proszę! Hajsiwo"
                    $ edki += renpy.random.randint(50, 300)

                elif helper == 2 and inventory.has_space(Cap) == True:
                    p "Ktoś tu kurwa wsadził szczura!"
                    $ inventory.add_item(Rat)
                    p "Może mi się do czegoś przyda"

                elif helper == 3:
                    p "Kurwa! TU JEST BOMBA!"
                    call checkHP(10) from _call_checkHP_32
                    p "Jebać trapy"
                
                elif helper == 4:
                    p "O proszę, powiększenie ekwipunku"
                    $ Cap += 1
                    p "Zawsze jeden przedmiot więcej"

        else:
            p "Kurwa nie, przydał by się wytrych"

    elif cel > 80 and cel < 100:
        if akt == 1:
            p "Nic tu nie ma"

        elif akt == 2:
            if chipy == 0:
                p "Pierdolnik drży, to miejsce cipa"
                $ chiplok = 1

            elif chipy == 1:
                p "Pierdolnik drży, to miejsce cipa"
                $ chiplok = 2

            elif chipy == 2:
                p "Pierdolnik drży, to miejsce cipa"
                $ chiplok = 3

            elif chipy == 3:
                p "Pierdolnik drży, to miejsce cipa"
                $ chiplok = 4

            elif chipy == 4:
                p "Pierdolnik drży, to miejsce cipa"
                $ chiplok = 5   

            elif chipy == 5:
                if inventory.has_item(HuMeat) == False and inventory.has_space(Cap) == True:
                    p "Ty kurwa, tu jest ludzkie mięso, wezme sobie"
                    $ inventory.add_item(HuMeat)

                else:
                    p "Nic tu nie ma"

            else:
                p "Znalazłem chyba wszystko" 

    elif cel > 99:
        p "Nic tu nie ma"

    else:
        "Print dupa, nie powinno Cię tu być."

    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    return