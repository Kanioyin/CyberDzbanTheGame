label kuchnia:
    scene kuchnia
    show gun
    if akt == 0:
        g "Szybko Ci poszło"
        if stan["Gun"] < 4:
            if inventory.has_item(Flaszka) == True:
                g "To pomoże Ci z kałachem"
                g "Daj mu tę flachę"
                jump rozstaje

            elif postacie["Kalach"] == 0:
                g "Masz, to Ci pomoże zdobyć zaufanie księdza"
                play sound "THROWING.mp3"
                $ inventory.add_item(Flaszka)
                g "Daj mu to, powinien Cię polubić"
                jump rozstaje

        elif stan["Gun"] > 2:
            g "Skończyłeś już pogaduszki?"
            menu:
                "Skończyłem?"

                "Ta, lecimy dalej":
                    stop music fadeout 1.0
                    jump akt1

                "Jeszcze chwilka":
                    jump rozstaje

                "Po gadaniu z takimi deklami, jednak spierdalam":
                    "Good Ending"
                    $ MainMenu(confirm=False)()

    elif akt == 1:
        if bigquest == 0:
            $ czas -= 1
            g "Ser dobry, [player_name]"
            if dzien < 3:
                g "Daj mi trochę czasu roboty szukam"

            if inventory.has_item(Klapek) == True:
                p "Mam przesyłkę od Cyphera"
                g "Co on znowu chce?"
                p "Mam dla Ciebie... klapka?"
                achieve Fedex
                $ inventory.remove_item(Klapek)
                $ postacie["Gun"] -= 2
                $ postacie["Cypher"] += 1
                g "Obawiam się, że to jest wypowiedzenie wojny albo gorzej zaczął produkcję merchu z DH"
                g "Tak czy siak, nic dobrego to nie oznacza. Zdupcaj, muszę pomyśleć"
                jump rozstaje

            else:
                pass

            if dzien > 3:
                g "Robota się znalazła"
                show jhin at right 
                with moveinright
                j "Zostaniesz naszym tajnym agentem, będziesz inwigilował wrogie społeczeństwo"
                j "Niczym Dżejms Bond"
                g "Nie zesraj się ten taki ale wracając do roboty, od dzisiaj nazywasz się Vładek"
                g "Zostaniesz szpiegiem, może nie z krainy deszczowców, tylko z bazy, wślizgniesz się w szeregi Vistów"
                g "Wyciągniesz tyle informacji ile się da i spierdolisz. Zadanie analnie proste. Zaczynasz bezzwłocznie"
                jump amongthev

        elif bigquest == 3:
            if dzien < 10:
                g "Daj mi trochę czasu, vista ma chujowy charakter pisma."
                g "Tak jeszcze z [10-dzien] dni"
            
            else:
                g "Dobra [player_name], powiem Ci, że jesteśmy w piździe."
                g "Jeśli dobrze rozumiem te papiery, to Visty wypuszczają jakąś nową broń."
                g "Polecisz teraz do naszego kontaktu, generała Kennedy'ego on da Ci broń do walki z Vinfekcją"
                $ bigquest = 4
                jump rozstaje

        elif bigquest == 5:
            if inventory.has_item(Rat) == True:
                menu:
                    "Mam w eq szczura, dać go Gunowi?"
                    "Ta":
                        p "Te Gun, chcesz może szczura?"
                        g "Pewnie"
                        $ inventory.remove_item(Rat)
                        g "Dzięki"

                    "Nah":
                        "Niech posra jeszcze w kieszeni"
                        
            if stan["Cypher"] == 3:
                hide gun
                show cypher at left with moveinleft
                c "Dzień dobry [player_name]!"
                p "Co ty tu kurwa robisz? Guna ja tu szukam."
                c "Przykra sprawa ale mnie to nie obchodzi trzeba przeprowadzić Anschluss tej kuchni"
                p "Co to kurwa znaczy?"
                c "No patrz. Tu się zrobi dziurę tam się pierdolnie bunkier i okopy. Nad wejściem działka, może nawet z ammunicją"
                p "I co? Mam Ci pomóc to przynieść?"
                c "Nie rozpędzaj się kasztanie musiałem z kimś pogadać, wiesz, oczyszczenie umysłu itp"
                p "Fantastycznie, mogę już iść?"
                show gun at right with moveinright
                g "A co wy tu kurwa robicie?"
                c "O karamba, on wrócił!"
                menu:
                    c "[player_name]! Co robimy?"
                    "Spierdalamy":
                        "Z Cypherem wybiegliście z kuchni"
                        scene rozstaje
                        "Biegniecie przez bazę"
                        g "Skurwysyny"
                        show laskawca at right with moveinright
                        pl "A co tu się dzieje?"
                        p "O fak szybki dodge"
                        "Ale ten dodge zabrał Ci cenne sekundy"
                        g "Jestem bliżej"
                        "Wbiegacie na dach"
                        scene dach
                        show gun at left
                        show cypher at right
                        g "No dobra gagatki, co macie na swoją obronę?"
                        if inventory.has_item(Ser) == True:
                            p "Ser"
                            g "Akceptuję"
                            $ inventory.remove_item(Ser)
                            hide gun with moveoutleft
                            c "Łał, to było szybkie"
                            p "Aż za szybkie"
                            "Gun to zje"
                            $ stan["Cypher"] = 4
                            jump rozstaje
                        
                        p "No my tylko chcieliśmy zobaczyć co jest w lodówce"
                        g "I co znaleźliście?"
                        p "Szczury"
                        g "Dokładnie! Jeśli jeszcze raz zobaczę że myszkujecie mi w kuchni urwę jaja z kutasami"
                        hide gun with moveoutleft
                        $ postacie["Gun"] -= 2
                        p "Chyba się zdenerwował"
                        c "Chuj z nim"
                        $ stan["Cypher"] = 4
                        jump rozstaje

                    "Przyjmuję konsekwencje":
                        p "Przyszliśmy pooglądać kuchnie"
                        show ciphate with dissolve
                        g "Po chuj"
                        hide ciphate with dissolve
                        c "A bo ja chcę zrobić mały Re."
                        g "NIE MÓW TEGO SŁOWA"
                        c "A, faktycznie"
                        g "A teraz wypierdalać mi stąd zamierzam gorgonzolić Mączysława"
                        c "Fuj, [player_name], wychodzimy"
                        "I wyszliście"
                        $ stan["Cypher"] = 4
                        jump rozstaje

            if stan["Gun"] == 0:
                g "No to mów, co Ci ten Kennedy powiedział ciekawego"
                p "Musimy zostać przyjaciółmi"
                g "Ja pierdole ale my że my, czy my że ty i inni?"
                p "Ja i inni"
                g "Ser z serca. No to do roboty żołnierzu mocą przyjaźni zdobądź serca innych dzbanów"
                $ stan["Gun"] = 1
                jump rozstaje 

            elif stan["Gun"] == 1:
                g "Czyli ze mną chcesz zacząć randkować? Daniel Krej z!"
                g "No to zacznijmy rozmowę kwalifikacyjną"
                g "Pytanie pierwsze"
                $ config.rollback_enabled = False
                $ odp = renpy.input("Jaki jest twój ulubiony kolor?")
                $ odp = odp.capitalize()
                if odp == "Szczurzy":
                    g "I to mi się podoba"
                    $ postacie["Gun"] += 1

                else:
                    g "Chuja się znasz"

                g "Pytanie numero dos"
                $ odp = renpy.input("Lubisz bigos?")
                $ odp = odp.capitalize()
                if odp == "Tak":
                    g "To chujowo"
                    $ postacie["Gun"] -= 1

                elif odp == "Nie":
                    show ciphate with dissolve
                    g "To dobrze"
                    $ postacie["Gun"] += 1
                    hide ciphate with dissolve

                else:
                    g "Chyba źle zrozumiałeś pytanie"

                g "Pytanie trzecie"
                $ odp = renpy.input("Jaka jest prędkość lotu nieobciążonej jaskółki w metrach na sekundę?")
                if odp == "10":
                    g "Tak, takiej europejskiej"

                elif odp == "14":
                    g "Tak, takiej z afryki"

                else:
                    "Tak to lata twój stary"

                g "Pytanie czwarte"
                $ odp = renpy.input("Jaki rodzaj sera jest najlepszy?")
                $ odp = odp.capitalize()
                if odp == "Prawdziwy":
                    g "Bardzo dobrze"
                    $ postacie["Gun"] += 1
                
                else:
                    g "Ten też dobry ale nie top"

                g "Pytanie piąte"
                $ odp = renpy.input("Gdzie leży prawo według BB?")
                $ odp = odp.capitalize()
                if odp == "Na południe":
                    g "DOBRZE!"

                else:
                    g "Źle"

                $ renpy.block_rollback()
                $ config.rollback_enabled = True
                g "To chyba tyle z pytań"
                p "I co to kurwa niby znaczy?"
                g "Dowiesz się w swoim czasie"
                $ stan["Gun"] = 2
                $ czas -= 2
                jump rozstaje

            elif stan["Gun"] == 2:
                g "No to witam panownie, dziś zobaczysz Mączysława w akcji"
                p "Kim jest kurwa Mączysław?"
                g "To najlepszy telefon EUNE polecany przez instytut RATki z dzieckiem"
                p "No dobra ale co to za tricki?"
                g "Zaraz zobaczysz młody, ruszamy dzielnie"
                scene black
                "Gun zabrał cię do nowego miejsca"
                "Zaskoczyło Cię to że pojechaliście tam autem"
                scene idrive
                play music "idrive.mp3" volume 0.2
                p "JA PIERDOLĘ, KTO CI DAŁ PRAWO JAZDY?"
                g "Paczka cheetosów serowych"
                p "Mogłem się tego spodziewać"
                g "Skończ pierdolić i powiedz mi gdzie jechać"
                p "ALE TO TY KURWA MIAŁEŚ WIEDZIEĆ"
                g "Zapomłem"
                show laskawca
                pl "Jeden token mniej (4)"
                hide laskawca with dissolve
                g "Popierdoli mnie z tym pedantem, każdego trolla mi liczy"
                p "O chuj chodzi w tej waszej relacji"
                g "Nie mam zielonego pojęcia"
                p "KURWA uważaj, baba na pasach"
                g "Którym się hamuje"
                play sound "hit.mp3"
                "Baba poleciała"
                g "Będzie padać, nisko latają"
                p "Nawet kurwa nie pytam"
                g "To dobrze, bo i tak bym nie odpowiedział"
                p "Pewnie dlatego że nie wiesz co ty pierdolisz"
                g "Nie. Dlatego że jesteśmy na miejscu"
                stop music
                play music "Monkeys Spinning Monkeys.mp3" volume 0.2
                scene badblok
                p "O cholera"
                g "Dokładnie, Fredi Fazber"
                p "Co?"
                g "Zobaczysz w środku ale najpierw. Raty aktywacja!"
                "Gun wyjął worek z plecaka i wypuścił 83 szczury."
                show gun at left
                g "W tym miejscu mieszkał jeden z większych zbrodniarzy"
                p "Hitler?"
                g "Pojebało Cię, Cypher"
                p "To po chuj tu przyjechaliśmy? Wyprowadza się od nas?"
                g "Nie, zostawił tu swoje spodnie"
                p "I to jest ten cały bojowy kłest"
                g "Tak"
                p "Dobra, chuj, miejmy to za sobą"
                scene black
                stop music
                play music "spook.ogg"
                "Weszliście do środka"
                p "Kurwa jak tu ciemno"
                g "A to była jego matka"
                p "Co?"
                g "No bo było ciemno"
                play sound "FrediFnaf.mp3"
                p "CO TO KURWA BYŁO"
                g "To jest właśnie niebezpieczeństwo, ten słynny Fryderyk FazNiedźwiedź"
                p "I ON CHRONI SPODNI?"
                g "Jak się nie będziesz darł to nas nie znajdzie"
                p "Sorka"
                g "Luz marki arbuz, rozdzielamy się, nie daj się zabić"
                "I poszedł w pizdu"
                p "Panie Ganie, jak pan mógł, znowu całe gówno na mojej głowie. Jak znajdę pokój Cyphera? Ten budynek ma kilkanaście pięter"
                "Podszedłeś do pierwszych drzwi i widzisz pierdalny napis Cypher"
                p "No dobra, to nie było trudne"
                "Drzwi nie były nawet zakluczone"
                p "Zbyt łatwo"
                play sound "Dzwi.wav"
                "Wszedłeś do środka"
                p "Chuja widzę. Gdzie Cypher schowałby spodnie"
                show cypher
                c "W szafie"
                hide cypher with dissolve  
                p "No co ty kurwa nie powiesz"
                "Sprawdziłeś pierwszą szafę"
                "I były w niej spodnie"
                p "Kurwa jackpot! Zdecydowanie zbyt prosto to idzie"
                "I nagle coś cię ugryzło"
                achieve Aboes
                play sound "EAT OR MUNCH.mp3"
                call checkHP(15) from _call_checkHP_10
                p "AŁA KURWA SPIERDALANDO"
                "Zacząłeś uciekać ale Fryderyk stanął Ci na drodze"
                p "JA PIERDOLĘ"
                "W tak zwanym międzyczasie"
                scene badblok
                show gun at left
                g "Stawiam 10 że zdechnie"
                show kalach at right
                k "Stawiam flachę że ucieknie"
                g "Stoi"
                k "Stanął"
                scene black
                "Wracając"
                "Walczyłeś dzielnie ale Fryderyk był zbyt silny"
                "Nagle, jak Filip z konopi wyskoczył goblin z pościeli"
                "Usłyszałeś głośne GOBELIN BLAST"
                play sound "blast.wav"
                "I straciłeś przytomność"
                scene badblok
                show gun at left
                g "Coś długo go nie ma"
                show kalach at right
                k "To go poszukaj lol"
                g "Nie chce mi się"
                k "To ja idę"
                g "Nie spodziewałem się tego po Tobie"
                k "Chcę sprawdzić, czy Fredi wypił flaszkę"
                scene black
                k "Kurwa, jak tu ciemno"
                k "Zaraz kurwa, czy on zdechł?"
                k "Nie, ciężko ranny ale żywy. O! Jest i moja flaszka! He, to zaraz będzie jeszcze jedna"
                "Kałach wyciągnął twoje ciało z bloku"
                k "Znalazłem go"
                g "Czyli wygrałem"
                k "Chuja prawda bananowcu, on żyje"
                g "Pierdolisz"
                k "No sprawdź se puls"
                g "Kurwa, masz rację ale pa ten trick"
                "Gun przystawił topór to twojej głowy"
                g "Ja to wygram, raz już przegrałem zakład"
                "A ty odzyskałeś przytomność"   
                scene badblok
                show gun at left
                show kalach at right
                p "POJEBAŁO CIĘ"
                g "No i dupa"
                "Gun schował broń"
                g "Masz te gacie?"
                "Sprawdziłeś po kieszeniach"
                p "Kurwa, miałem je, przysięgam"
                g "Spokojnie szczylu, to jest zaklęty obiekt. Nie możesz sobie tak po prostu go zabrać"
                p "Ale skam"
                g "To to prawda ale zadanie wykonałeś. Wskakuj do auta, wracamy"
                k "Ale ja prowadzę"
                p "Popierdoli mnie"
                "I w rodzinnej atmosferze wróciliście do domu"
                $ postacie["Gun"] += 1
                $ postacie["Kalach"] += 1
                $ stan["Gun"] = 3
                $ czas = 0
                jump rozstaje
            
            if stan["Gun"] == 3:
                if stan["Jhin"] == 9:
                    g "Chciałem pojechać z Jhinem na zadanie bojowe ale mu się zdechło. Więc to mamy już z głowy"
                    $ stan["Gun"] = 4
                    "Wychodzisz z kuchni"
                    jump rozstaje
                
                elif stan["Jhin"] < 4:
                    g "Pogadaj z Jhinem, jak zrobisz z nim trochę roboty to zapraszam"
                    jump rozstaje

                else:
                    show jhin at left
                    g "Dzień dobry [player_name]"
                    j "Siemaneczko"
                    p "Czołem, co to za zebranie?"
                    g "Wyruszamy na wycieczkę tosteroznawczą"
                    p "Co kurwa?"
                    g "Zaraz zobaczysz"
                    scene idrivewtt
                    play music "idrive.mp3" volume 0.2
                    p "Nie rozjedź żadnej baby tym razem"
                    j "Jak to tym razem?"
                    j "Czy ja o czymś nie wiem?"
                    g "O wielu sprawach ken taki"
                    "Ale tym razem szybka podróż była bezpieczna"
                    stop music
                    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
                    scene tostblok
                    show gun at left
                    show jhin at right
                    g "Panowie, tu macie papiery, wchodzicie do środka i wyłudzacie hajs"
                    j "Gunie, to chyba nie jest legalne"
                    p "Kurwa, jesteśmy w Night City"
                    j "Co fakt, to fakt"
                    g "To do pracy rodacy"
                    scene klatka
                    show jhin at right
                    j "Dziwna robota się trafiła"
                    p "Chłopie, ja to robię tylko dla main questa"
                    j "Czyli?"
                    p "Potem Ci opowiem"
                    "Zapukaliście do pierwszych drzwi"
                    "Okazało się że na pierwszym piętrze mieszkają sebixy"
                    "W taki sposób rozpoczął się kombat"
                    play sound "hit.mp3"
                    call checkHP(10) from _call_checkHP_11
                    "Dostałeś potężnego luja ale oddałeś pięknym za nadobne"
                    "Odwróciłeś się aby sprawdzić co z Jhinem a Jhin leży na ziemi nieprzytomny"
                    p "O MÓJ BOŻE JHIN"
                    g "Co się tak tam prujesz"
                    p "Chodź tu szybko Gun, Jhin dostał w cymbał"
                    g "Szczur zjadł mojego agenta, zrób mu zdjęcie"
                    p "Pomóż mi przenieść go do auta"
                    g "No dobra"
                    "Przenieśliście nieprzytomnego Jhina do kara i ruszyliście do bazy"
                    scene idrive
                    play music "idrive.mp3" volume 0.2
                    g "Co tam się w ogóle stało?"
                    p "Sebixy wyklęte"
                    g "O w mordę strzelił"
                    p "A to było potem"
                    g "To było bardzo niemiłe z ich strony, powinniśmy ich wysadzić"
                    p "No to jest dobry plan ale gdzie dostanę bombę?"
                    g "Pozwól mi gotować"
                    "I w atmosferze skandalu wróciliście do bazy"
                    $ stan["Gun"] = 4
                    $ postacie["Gun"] += 1
                    $ postacie["Jhin"] += 1
                    $ czas = 0
                    jump rozstaje

            if stan["Gun"] == 4:
                if stan["Krateus"] < 3:
                    g "Brazylijczyk coś od Ciebie chce, idź do niego"
                    jump rozstaje

                else:
                    g "No to lecimy, zadanie ostateczne"
                    show krateus at left
                    kr "Dokładnie kurwa! Pora rozpierdolić sebixów"
                    g "Ta, dokładnie. Kretynus znalazł bombę. Ja ją podstawie i spierdalamy. Twoim zadaniem będzie stanie na czatach"
                    p "Powinienem dać sobie radę"
                    g "No to w drogę"
                    scene idrivewk
                    play music "idrive.mp3" volume 0.2
                    kr "Powiedz Gun, kiedy nauczyłeś się prowadzić?"
                    g "Nigdy"
                    play sound "hit.mp3"
                    "I w tym momencie uderzyliście w lampę"
                    call checkHP(5) from _call_checkHP_12
                    stop music
                    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
                    kr "Ała"
                    g "A mówiłem, nie kraczemy jak prowadzę"
                    kr "Spoko, w Brazyli było gorzej"
                    p "A mnie siur boli"
                    g "Spokojnie, od bólu się powiększa"
                    kr "To dlatego walisz non stop ball breakerem?"
                    g "Pojebało cię?"
                    p "Panowie, co to tak pika?"
                    g "NA RATY CHRYSTUSA"
                    kr "Pierdolisz"
                    g "Bomba się uzbroiła"
                    "Otworzyliście bagaja i faktycznie bomba pika"
                    g "Wypierdol to z auta"
                    kr "Się robi"
                    play sound "THROWING.mp3"
                    "Krateus yeetnął bombę"
                    g "Będzie padać, nisko latają"
                    "Ładunek trafił do sklepu z narzędziami"
                    kr "To za brak promocji Kurwo"
                    play sound "BOOM.mp3" volume 0.2
                    "I pierdolło"
                    g "No to ponowie, chyba po robocie"
                    kr "Kurwa serio, ja chciałem bijatykę! No i ta bomba była na wynajem"
                    p "To ty miałeś to oddać"
                    kr "No, teraz będę miał problem"
                    g "Straszna chujnia, anyway. Panowie wracamy, do Gunmobilu"
                    "I po niesamowicie sukcesywnym queście wróciliście do bazy"
                    g "To chyba tyle z syzyfowych prac, możemy się zając zadaniem Kennedy'ego"
                    p "Kurwa w końcu"
                    achieve Gunpp
                    $ stan["Gun"] = 5
                    "Zadowolony wyszedłeś"
                    $ czas = 0
                    jump rozstaje

            if stan["Gun"] == 5:
                g "Idź do tego Kena"
                jump rozstaje

            if stan["Gun"] == 6:
                g "To czekam aż dasz znać i idziemy na kłest"
                jump rozstaje            

    if inventory.has_item(Ser) == True:
        p "Mam coś dla Ciebie gun"
        $ inventory.remove_item(Ser)
        achieve Smrut
        g "Hmmm, tajemniczy mysi sprzęt."
        g "To mi się przyda. Dzięki"
        $ postacie["Gun"] += 1
        jump rozstaje

    else:
        jump rozstaje