
label heistprogsc:
    scene black
    mg "Takie delikatne info teraz dla Ciebie"
    mg "Teraz będziesz dawał polecenia swoim ziutkom"
    mg "W trakcie akcji, będzie się zwiększać ich poziom przypału"
    mg "Jak się nabije duży, to będą mięli problem"
    mg "Więc postaraj się dobrze decydować"
    scene spacer
    show jax at left
    show vio at right
    p "Dobra panowie, jedziemy z tym zadaniem"
    vi "Vasz vuż vakiś vlan vrzygotowany?"
    p "Na spokojnie, wszystko już sobie obmyślałem"
    vi "vo viech vędzie, vszyscy va vączach?"
    ja "Pewnie, że tak"
    p "Dobrze was słychać, możemy zaczynać powoli"
    p "Pamiętajcie, nie możemy panikować. Ben jest czujny jak pies podwójny"
    ja "I ma bardzo dobrych strażników przy sobie"
    vi "V va vego vafirynda vbserwuje vawsze vo vię vzieje"
    p "Będzie trzeba ich oślepić nim coś zrobimy"
    ja "Dobre podejście"
    scene kasyno
    p "Podejście pod miejście akcji"
    menu:
        p "Jak podchodzimy to tego zadania?"
        "Na przypale":
            p "Dobra panowie, plan jest prosty, wbijamy sobie głównym wejściem"
            vi "Vho, vobrze vię vapowiada"
            p "Cicho, nie zapeszaj"
            p "Po wejściu, pogramy sobie trochę a później się rozdzielimy"
            p "Powoli będziemy progresować do pomieszczenia ze wszczepem"
            p "Tylko będzie trzeba się pozbyć tych jebanych kamer"
            menu:
                p "Kto wyłączy kamery?"
                "VIO":
                    p "Będziesz w stanie się ich pozbyć?"
                    vi "Vasna vprawa"
                    $ stan2["Vio"] = 1
                    $ stan2["Jax"] = 1

                "JAX":
                    p "Będziesz w stanie się ich pozbyć?"
                    ja "Jasna sprawa"
                    $ stan2["Jax"] = 2
                    $ stan2["Vio"] = 2

            p "Przed wyłączeniem, ten drugi zrobi zamieszanie"
            p "Jak będą ślepi, to zobaczymy co nas dalej czeka"
            p "Spotkamy się w środku i zobaczymy co nas czeka"
            p "Zrozumiały plan?"
            ja "Tajest"
            scene kasyno
            p "Panowie, rozproszyć się"
            "I tak, każdy z was poszedł do własnego stołu"
            menu:
                "Na jakie stawki chcesz grać?"
                "Wysokie" if edki > 4999:
                    $ zakład = 5000

                "Średnie" if edki > 2499:
                    $ zakład = 2500

                "Niskie" if edki > 999:
                    $ zakład = 1000

                "Minimalne":
                    $ zakład = 50

            $ edki -= zakład
            p "Dobra, let's go gambling"
            "Teraz zobaczmy jak Ci poszło"
            $ helper = renpy.random.randint(25, 100)
            if helper < fart:
                "Ciemna cipa, udało Ci się wygrać"
                $ edki += zakład * 2

            else:
                "Jasny chuj, nic nie siadło"

            p "Dobra, pora powolutku zmieniać miejsce"
            p "Mój wybraniec poszedł już wyłączyć kamery"
            sb "Ej patrz tam, ziomek robi salto jak wygrywa"
            p "Ten drugi zrobił delikatne zamieszanie"
            p "Mogę się powolutku udawać do strefy dla pracowników"
            $ heistprog["Main"] = 1
            scene korytarzCasino
            $ helper = 0
            while helper == 0:
                menu:
                    "Gdzie idę?"
                    "Pierwsze drzwi" if heistprog["D1"] == 0:
                        "Przechodzisz przez pierwsze drzwi"
                        "Trafiasz prosto do składzika na miotły"
                        "Nie ma tu zbytnio nic ciekawego"
                        $ heistprog["D1"] = 1

                    "Drugie drzwi" if heistprog["D2"] == 0:
                        "Sprawdzasz drugie drzwi, jest tu szyb wentylacyjny"
                        if inventory.has_item(Srubo) == True:
                            "Odkręcasz szyb i wskakujesz do środka"
                            "Trochę sobie tuptasz i wychodzisz w innym pomieszczeniu"
                            "W taki sposób otwierasz sobie koeljne drzwi"
                            $ heistprog["D4"] = 1
                        
                        "Bez śrubokrętu nic tu nie wskórasz"
                        $ heistprog["D2"] = 1

                    "Trzecie drzwi" if heistprog["D3"] == 0:
                        "Przechodzisz przez trzecie drzwi"
                        "W środku czekali na Ciebie twoi kompani"
                        show jax at left
                        show vio at right
                        ja "Siemaneczko"
                        p "Witam"
                        p "Dobrze nam poszło, szkoda, że się tutaj schowaliście, mógłbym was nie znaleźć"
                        vi "Vie vartw vię, va vglądam vorytarz vrzez vizjer"
                        p "No dobra, to było całkiem szczwane"
                        p "Dobra, wyskakujemy i sprawdzamy dalej"
                        $ heistprog["D3"] = 1
                    
                    "Czwarte drzwi" if heistprog["D4"] == 1:
                        "Sprawdzasz ostatnie drzwi, tutaj jest sejf naścienny"
                        if heistprog["D3"] == 1:
                            p "VIO, możesz otworzyć?"
                            vi "Vasna vprawa vzefie"
                            "Raz dwa VIO zhackował zabezpieczenia"
                            vi "Vasna vupa, vajny viniądz vrodku"
                            p "Fifti-fifty?"
                            vi "Vewex"
                            $ edki += 2500
                            $ renpy.notify("Dostałeś 2500 edków")

                        else:
                            p "Dupa, nie otworzę tego"

                        "Poza tym, jest tu jeszcze pistolecik"
                        if inventory.has_space(Cap) == True:
                            $ inventory.add_item(Pistolecik)
                            p "A wezmę sobie"

                        "I to tyle z tego pomieszczenia"
                        $ heistprog["D4"] = 2

                    "Wyjście":
                        $ helper = 1

            "Wychodzisz z pomieszczeń technicznych"
            "Po chwili dołączają do Ciebie twoi towarzysze"
            vi "Vo vo veraz vobimy?"
            p "Musimy się dostać do pomieszczenia ze wszczepami, powinno ono gdzieś tu być"
            ja "Wiesz w ogóle które to?"
            p "Będę strzelał"
            vi "Va vierdole"
            "Nagle, dostałeś tajemniczą wiadomośc na swojego agenta"
            sb "Idąc dalej zginiecie, lepiej zawróćcie"
            ja "Co tam Ci przyszło?"
            p "A jakaś napalona mamuśka pewnie"
            "Nagle, widzisz lufę z drona obronnego na suficie"
            p "HALT, mają ochronę"
            vi "Vkurvysyny"
            menu:
                "Co teraz zrobić?"
                "VIO, zhackuj to proszę":
                    $ stan2["Vio"] += 1
                    vi "Vię vobi"
                    "VIO sprawnie wyłączył drona"
                    vi "Vrobione"

                "JAX, pora pięści":
                    $ stan2["Jax"] += 1
                    ja "Przyjąłem"
                    "JAX zakrada się pod działko i błyskawicznie je wyrywa"
                    ja "Jak pójdziemy z tym na złom, to będziemy bogaci"
                    p "Plan dobry, okoliczności chujowe"
                    ja "Ah, fair point"

                "Zastrzelę tego gnoja":
                    call testSkili("Bron", "ZW", 15)
                    if wynik == 1:
                        "Celnym strzałem zdjąłeś drona"
                        ja "Dobra robota"

                    else:
                        call checkHP(15)
                        p "Kurwa, dostałem"
                        "I dopiero drugim strzałem do pokonałeś"

            p "Dobra robota, chodźmy sprawdzić co trzymają w środku"
            "Delikatnie otworzyłeś drzwi"
            p "Ty, fajne to"
            ja "A co to jest?"
            p "Jax, ty nie widzisz tego?"
            ja "Mordziaty, ja mam ponad dwa metry, drzwi są mniejsze ode mnie i zasłaniają mi wizję"
            p "Przykra sprawa"
            "W środku jest magazyn kończyn, część z nich oznaczono jako niebezpieczne"
            vi "Vo Volera, viezłe vkarby"
            p "Wiecie co, ja sobie chyba wezmę jedną sztukę"
            menu:
                "A wezmę sobie"
                "Zwykłą cyberkończynę":
                    $ Inventory.add_item("CyberK")

                "Niebezpieczną kończynę":
                    $ Inventory.add_item("NCyberK")

                "Chyba nic":
                    p "Głupio tak kraść w trakcie napadu"

            ja "Dobry wybór"
            p "Wiem, nie robię złych wyborów"
            vi "V vo veraz?"
            p "Odkręcamy płytę w podłodze i przejdziemy tunelem technicznym do dziupli"
            ja "Mamy się szykować na walkę?"
            p "Ty, to się szykuj do pilnowania i późniejszego spierdalania"
            ja "Nie wcisnę się do tunelu?"
            p "Ty kurwa ledwo przez drzwi przeszedłeś"
            ja "Fair point"
            vi "V vo ve vną?"
            p "Ty, mój drogi VIO, masz tu pendrajwa, wgrasz Benkowi jakiegoś wirusa od Krisa"
            vi "Vo volera, vo vie vniszczy vu vasyna?"
            p "Zniszczy, tylko powolutku, kawałek po kawałku jego imperium się rozpadnie"
            vi "V vkąd vo viesz?"
            p "Tak strzelam, nie wysłałby nas z bombą bez zapowiedzi"
            vi "Vogiczne"
            p "Dobra, to wskakujemy, trzymaj się Jax"
            ja "Narka"
            "Wskoczyliście do tunelu"
            scene black
            p "Kurwica, ciasno tutaj i jeszcze kurwa ciemno"
            vi "Vrawda vobrze ve vax vutaj vie vszedł"
            p "Słyszysz te wszystkie kroki nad nami? Chyba ochrona przyszła robić swoje"
            vi "Vam vadzieję, ve vobie voradzi"
            p "Tja, dobra, tutaj będziemy wskakiwać"
            scene jena
            show vio at left
            p "CO TO KURWA JEST?!"
            vi "Vo vest vhyba vobieta"
            p "I my to mamy zawirusować chyba"
            show ben at left
            be "Nie tak szybko chłopacy"
            p "A niech mnie chuj strzeli"
            vi "Voż vo vzybki Ven"
            be "To prawda, teraz mi powiedzcie, co wy tu knujecie?"
            menu:
                p "Co mu mówimy"
                "My tu tylko sprzątamy":
                    be "Ta, jakoś w to nie wierzę"
                    p "Jak nie, a ta miotła to do czego może być?"
                    be "[old_pn], ty nawet nie masz miotły"
                    p "O kurwica, skąd ty posiadasz takie dane wywiadowcze?"

                "A nie interesuj się (zaatakuj)":
                    "Nim zdążyłeś wyciągnąć spluwę, automatyczne działko do Ciebie strzeliło"
                    "I to w dodatku kilkanaście razy"
                    jump gameover

                "Tajną misję":
                    be "A zdradzisz mi kto zlecił Ci to zadanie?"
                    p "Kris, nie wiem w sumie jak on się nazywa"
                    be "Krzysztof Czerownopolski?"
                    p "Jasny chuj, skąd wiesz?"

            be "Jestem pierdolonym fixerem, mówi Ci to coś, czy mam Ci to kurwa przeliterować?"
            p "To znaczy, że szukasz informacji po mieście co nie?"
            be "Ja wiem więcej, niż Ci się wydaje"
            be "Wiem, że przysłał Cię tu Kris. Wiem, że chesz sabotować moje interesy"
            p "Strasznie dużo informacji"
            be "Nie powinno Cię to dziwić, taka moja praca"
            be "A z samego faktu, że mieszkasz w mojej dzielnicy, to już na mnie wymusza śledzenie Ciebie"
            be "I tak każdego, bardziej rzucającego się w oczy dzbana"
            p "To po kiego się mnie o cokolwiek pytasz, jak już znasz odpowiedzi?"
            be "Sprawdzałem, czy będziesz leciał fair. Dostałem odpowiedź na to pytanie"
            p "I co teraz ze mną zrobisz?"
            vi "Vic Vi vię vie vtanie vłody, vszystko vdzie vedle vlanu"
            p "Co? Jakiego planu? O czym ty do mnie VIO mówisz?"
            be "Jakby Ci to powiedzieć, gra była ustawiona od samego początku"
            be "Vio i Jax są moimi agentami, pomagali mi przy czyszczeniu"
            be "Bo w sumie też, nie mięli zbytnio innego wyjścia"
            be "Krzysiowi nie można ufać, jak w sumie każdemu z FAoNUSA"
            p "Pierwszy raz słyszę ten skrót"
            be "Jakoś mnie to nie dziwi, Federalna Agencja Nowego USA, specjalna rządowa jednostka"
            be "Mają jakieś bardzo dziwne plany a my nie chcemy im w tym pomagać"
            vi "Ven va v vękawie vartę vrzetargową"
            vi "Va vaba v vłoiku va vuper votężną VI"
            

        "Na skradaka":
            "Tit"