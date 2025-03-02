label dach:
    scene dach
    show cypher
    if akt == 0:
        if stan["Cypher"] == 0:
            "Cypher skończył morbowanie"
            c "Chcesz zostać najemnikiem? A może wolisz wynająć najemników?"
            c "Wykonujemy każde zadanie, nawet niemożliwe damy radę zrobić za odpowiednią opłatę oczywiście"
            g "Te młody, dawaj na dół"
            hide cypher
            scene kuchnia
            show gun
            g "Lepiej nie zawieraj żadnych umów z Cypherem, to nigdy nie kończy się dobrze"
            g "Pamiętaj też, jak raz dołączysz do DH to już nie ma wyjścia. Cypher nie może Cię z niego wyjebać"
            $ stan["Gun"] += 1
            $ stan["Cypher"] += 1
            jump rozstaje

        elif stan["Cypher"] == 1:
            "Widzisz że Cypher nad czymś pracuje"
            c "Nie przeszkadzaj mi, przygotowuję coś niesamowitego"
            c "Jeśli dołączysz do DH, to dostaniesz bojowe zadanie"
            $ stan["Cypher"] += 1
            jump rozstaje

        elif stan["Cypher"] == 2:
            c "Czy ty chcesz usłyszeć każdy dialog z mną?"
            c "Czy może stwierdziłeś że chcesz truć mi dupę"
            c "Powiedz mi kasztanie, wierzysz w kobiety?"
            c "Zastanów się nad odpowiedzią"
            $ stan["Cypher"] += 1
            jump rozstaje

        elif stan["Cypher"] == 3:
            c "No pierdolne Ci"
            c "Literalnie Ci pierdolnę"
            c "Jeszcze raz tu kurwa przyjdź a poszczuję Cię Młynarczykiem"
            $ stan["Cypher"] += 1
            jump rozstaje

        elif stan["Cypher"] == 4:
            show ciphate with dissolve
            c "No to masz przepierdolone. Młynarczyk! Bierz go!"
            play sound "Bestia.mp3" 
            "I coolawy mściciel postanowił pozbyć się szkodnika"
            hide ciphate with dissolve
            achieve Mill
            "Git Gud"
            jump gameover

    elif akt == 1:
        if bigquest == 0:
            $ czas -= 1
            c "Co tam [player_name]?"
            if Frakcja == 1 and postacie["Cypher"] == 4 and inventory.has_item(Klapek) == False:
                c "Dobra, robotę masz"
                play sound "THROWING.mp3"
                $ inventory.add_item(Klapek)
                c "Zanieś to Gunowi, jako symbol naszej przyjaźni"
                jump rozstaje

            elif postacie["Cypher"] == 5:
                c "Witaj mój najodważniejszy wojowniku"
                c "Nie mam teraz dla ciebie nowego zadania ale nie martw się, DH jeszcze zabłyśnie"
                jump rozstaje

            elif Frakcja != 1:
                c "Jakbyś dołączył do DH to miałbyś teraz niesamowicie ciekawego kłesta"
                c "Tak to możesz spierdalać"
                jump rozstaje

            if dzien > 4:
                c "Dzielny wojowniku, idź do guna robotę ma wróć potem do mnie, opowiem Ci więcej"

        elif bigquest == 3 and stan["Cypher"] == 0:
            $ czas -= 1
            c "Czekaj, wróciłeś właśnie od Vistów co nie? Jak tam było? Dobrze się bawiłeś?"
            c "Powiem Ci w sekrecie, który jednak każdy zna kiedyś, za czasów swojej światłości, polowałem na Visty"
            c "Ale moja umowa z wojskiem poszła się jebać gdy ten chuj Kennedy nie dał mi wsparcia"
            c "Jakby ta Av-ka wleciała do metra, byłbym niepokonany"
            c "A tak to Jhin prawie się zabił tnąc kable. Mówiłem mu, trakcja to śmierć. Tory! To jest przyszłość"
            c "To tyle z mojej audiencji teraz idź w chuj."
            $ stan["Cypher"] = 1
            jump rozstaje

        elif bigquest == 3 and stan["Cypher"] == 1:
            $ czas -= 3
            c "No co ty kurwa ode mnie chcesz? Nie chce mi się z tobą gadać"
            c "Spierdalaj"
            jump rozstaje

        if bigquest == 5:
            if stan["Cypher"] < 1:
                if Frakcja == 1:
                    p "Dzień dobry szefie"
                    c "Witaj mój ulubiony najemniku! Czego ode mnie potrzebujesz?"
                    p "Kennedy dał mi misję"
                    c "Oho, to będą jaja, mam do niego zadzwonić?"
                    p "Muszę być twoim przyjacielem"
                    c "To tyle?"
                    p "Tak"
                    c "No to kurwa, zrobione"
                    p "Tak po prostu?"
                    c "Zawszę pomogę swoim pracownikom"
                    p "Cholibka milutko"
                    c "RICHTIG"
                    achieve Cippp
                    $ stan["Cypher"] = 5
                    jump rozstaje
                
                else:
                    c "Czego chcesz?"
                    p "Mam misję od Kennedy'ego"
                    c "Zaciekawiłeś mnie, mów dalej"
                    p "No to musimy zostać przyjaciółmi"
                    c "Oj, nie wiesz na co się piszesz"
                    p "To prawda, nie mam zielonego pojęcia"
                    c "A więc, dostaniesz doomstack bojowych zadań. Będę je wymyślał bardzo wolno, chyba"
                    c "Wtedy dostaniesz fragment mojej afekcji. Możemy uznać że pierwsze zadanie już wykonałeś"
                    p "No, to było szybkie"
                    c "Nie ciesz się zbyt szybko, następne będą trudniejsze"
                    c "Będą wymagały od Ciebie masy sprzętu i trochę umysłu. Dobra, spierdalaj. Wyruszam myśleć"
                    $ stan["Cypher"] = 1
                    jump rozstaje

            if stan["Cypher"] == 1:
                c "No dobra mam pomysł, przelećmy się"
                p "Kurwa cypher, popierdoliło Cie? Dlaczego ty taki rogaty jesteś?"
                c "Źle mnie zrozumiałeś [player_name]. Widzisz ten helikopter? Lecimy na zadanie"
                p "Jakie zadanie?"
                c "Bojowe"
                c "Czeczeni się buntują i musimy ich zbombardować"
                p "No dobra, to lecimy"
                scene cypherkopter
                play sound "heli.mp3"
                "W czasie lotu Cypher spał jak zabity"
                "Strasznie Cię korciło by taki został ale ostatecznie dolecieliście na miejsce"
                "I to było 10 metrów od waszej bazy"
                show cypher
                c "Ale się wyspałem"
                p "Czemu my pół dnia lecieliśmy 10 metrów"
                c "Droga w remoncie, trzeba było lecieć na około"
                p "Pojebie mnie"
                c "Najpierw bierz się za robotę"
                p "Dobrze szefie"
                c "I to mi się podoba"
                p "Czemu Ci czeczeni wyglądają jak Gun i Łaskawca?"
                c "Kamuflaż. Przestań myśleć i ciąg"
                $ config.rollback_enabled = False
                menu:
                    "Ciągniesz za wajchę?"
                    "Cypher kazał ja robię":
                        "Zkronkowałeś wajchę i napalm spadł"
                        show ciphate with dissolve
                        $ postacie["Cypher"] += 2
                        hide ciphate with dissolve
                        achieve Pyro
                        "Okazało się, że to nie był kamuflaż"
                        play sound "3yell1.wav"
                        g "Ty debilu jebany"
                        pl "ALE SIĘ PODJARAŁEM"
                        $ postacie["Gun"] -= 1
                        $ postacie["Laskawca"] -= 1
                        c "HI HI HA HA"
                        c "Zadanie wykonane, możemy wracać"
                    
                    "Nie zranię ziomków":
                        p "Pierdol się Cypher, nie zrobię tego"
                        show ciphate with dissolve
                        c "Pizda jesteś nie wojownik"
                        hide ciphate with dissolve
                        $ postacie["Cypher"] -= 2
                        c "Dobra wracamy, nie ma z tobą zabawy"
                
                $ renpy.block_rollback()
                $ config.rollback_enabled = True
                "I kolejne pół dnia wracaliście"
                $ czas = 0
                $ stan["Cypher"] = 2
                jump rozstaje

            if stan["Cypher"] == 2:
                $ config.rollback_enabled = False
                c "Tym razem zadanie będzie dość proste, musimy odwiedzić fantastyczną fabrykę"
                p "Jaką kurwa fabrykę?"
                c "Zaraz zobaczysz"
                scene dhfak
                show cypher at left
                p "DH ma swoją własną fabrykę w NC"
                c "To prawda, zajebista co?"
                p "No troszeczkę"
                c "A zaraz zobaczysz co jest w środku"
                scene fakins
                show cypher at left
                c "Tada!"
                show gun
                g "Nienawidzę chuja"
                hide gun
                p "I co ty tu niby produkujesz?"
                c "Klapki"
                p "Serio?"
                c "A czego ty się spodziewałeś? Merch DH musi zalać zachodniotajwański rynek"
                p "Ale to jest wszystko?"
                c "Nie no co ty. Drukuję tu jeszcze broń"
                p "I też to idzie na handel"
                c "W taki sposób finansuję swoje bizzarne przygody"
                c "Młynarczyk siedzi i opycha to za gruby pitos ale trzeba teraz przejść do głównego dania"
                c "Kierunek piwnica"
                scene dhpiw
                show cypher at left
                c "I tu się drukują pistoleciki średnio po dwóch strzałach się rozpierdala"
                c "Czasami potrafi działać do twojej śmierci, czyli do trzeciego strzału"
                p "Sprowadziłeś mnie tu tylko by mi to pokazać?"
                c "Nie, to by było zbyt proste. Jedna z drukarek przestała działać"
                c "Napraw mi to"
                p "O ja pierdolę"
                menu:
                    "Jak to naprawić"
                    "Może walne w to hita?":
                        "Jebłeś w drukarkę, niestety przebiłeś się przez obudowę"
                        show ciphate
                        c "NIEEEE! GŁUPCZE!"
                        hide ciphate
                        $ postacie["Cypher"] -= 2
                        c "To kosztowało z 200 edków"
                        c "Nigdy się z tego nie pozbieram"
                        c "Chujowy z ciebie fixer, zupełnie jak Gun"

                    "Dodam kokainy do filamentu" if inventory.has_item(Kokos):
                        $ inventory.remove_item(Kokos)
                        "Wcierasz koks w filament"
                        "Nagle drukarka zaczęła działać"
                        c "Jesteś pierdolonym geniuszem"
                        $ postacie["Cypher"] += 1
                        c "Aż bym Cie znowu zaprosił do DH ale niestety komuś nie chce się tego kodować"
                        c "Więc tak zwany chuj, możemy wracać"
                        "I z Cypherem wróciliście do bazy"
                        $ stan["Cypher"] = 3
                        jump rozstaje

                    "Nie wiem":
                        c "No to szkoda"

                c "Giga sadge, chyba będę musiał kupić nową"
                c "Chuj pora wracać"
                "I z Cypherem wróciliście do bazy"
                $ stan["Cypher"] = 3
                jump rozstaje

            if stan["Cypher"] == 3:
                "Cyphera tu nie ma, powinien być gdzieś w bazie"
                jump rozstaje
            
            if stan["Cypher"] == 4:
                c "Dobra, lecimy z kolejnym bojowym zadaniem"
                c "W dzisiejszym odcinku wysokiego trybu: wyruszymy do sklepu po zakupy"
                scene owocniak
                show cypher
                c "Ah, uwielbiam plastikowe truskawki"
                play sound "EAT OR MUNCH.mp3"
                c "Przepyszne ale jesteśmy tu w innym celu niż zdrowe jedzenie"
                c "Jesteśmy tu na przesłuchanie"
                p "Kogo?"
                c "Ciebie"
                c "Pytanie pierwsze"
                $ config.rollback_enabled = False
                menu:
                    c "Ile chlebów w życiu zjadłeś?"
                    "Kurwa, nie liczę tego":
                        show ciphate with dissolve
                        c "I to był błąd"
                        hide ciphate with dissolve
                        show krateus at right
                        kr "To prawda, liczenie makro oddaje. Wiesz, że jeden bochenek ma 2001 kalorii"
                        kr "363 węgli, 66 białka i 24 fatu. Warto kontrolować te wartości"
                        hide krateus
                        c "No właśnie"
                        $ postacie["Cypher"] -= 1

                    "Biedny jestem, z trzy":
                        c "Oj rozumiem twój ból. Jak byłem małym szczylem"
                        c "To my na platformie jedliśmy plastik z solą"
                        c "A na pierwszej wojnie korporacyjnej jedzono zieloną sałatę"
                        p "A ona nie zawsze była zielona?"
                        c "No od wojny jest"
                        $ postacie["Cypher"] += 1

                    "Nienawidzę chleba":
                        c "W sensie że bochenków?"
                        p "Kromek też"
                        c "A, bo już myślałem, że twardego nie lubisz"
                        p "No też, kto kurwa lubi twardy chleb"
                        c "Oj i teraz mnie wkurwiłeś"
                        $ postacie["Cypher"] -= 1

                c "Kwestię gastro mamy za sobą, teraz kolejne pytanie"
                menu:
                    c "Widziałeś gdzieś moje spodnie?"
                    "Fredi ich pilnuje" if stan["Gun"] > 2:
                        c "Karamba, myślałem że zostały już uratowane"
                        p "A ty nie masz innych spodni?"
                        c "Mam ale w tamtych jest coś ważnego"
                        p "OK"
                        $ postacie["Cypher"] += 1

                    "Na dupie je masz":
                        c "Się kurwa dowcipniś znalazł"
                        c "Jak taki jesteś śmieszny to co byś powiedział na granat w odbycie?"
                        p ":czacha"
                        c "HiHiHaHa"

                    "Nie wiem Cypher":
                        c "Same"

                c "No i ostatnie pytanie"
                menu:
                    c "Ufasz mi?"
                    "Tak":
                        c "Więc udawaj, że gadamy i idź za mną"
                        p "Ok"
                        "Spacerkiem szliście dalej, aż do ślepego zaułka"
                        c "No, czego od nas chcecie"
                        "Para zbirów wyłoniła się zza rogu"
                        "Guten Morgen, Großer Manager"
                        c "Guten Morgen"
                        "Wir haben eine wichtige Frage an Sie"
                        c "Komm schon"
                        "Wir können Autogramme bekommen, wir sind große Fans"
                        c "Natürlich"
                        "Widzisz jak Cypher podchodzi do tej pary i pisze im coś na kartkach"
                        "Następnie parka odchodzi"
                        p "Cypher, co to było?"
                        c "Fałszywy alarm młody, wracamy do domu"
                        p "Ile masz jeszcze dla mnie zadań?"
                        c "Wiesz co? Jak mi ufasz, to ja zaufam tobie. Możesz mnie liczyć jako sojusznika"
                        p "Klawo"
                        achieve Cippp
                        $ stan["Cypher"] = 5
                        $ postacie["Cypher"] += 2
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje


                    "Nie":
                        c "To spierdalaj"
                        show ciphate with dissolve
                        achieve Foch
                        "I bez słowa zaczął uciekać"
                        hide ciphate with dissolve
                        $ postacie["Cypher"] -= 9999
                        $ stan["Cypher"] = 9
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje

            if stan["Cypher"] == 5 or stan["Cypher"] == 6:
                scene disko
                show cypher at left
                stop music
                play music "inba.mp3"
                p "Co tu się kurwa dzieje?"
                c "Witam na imperzie"
                p "Ale czemu? Zrobiłem z tobą kłesty!"
                c "To jest bonus! Całkiem za friko!"
                p "Serio?!"
                c "No ta, nie wiem po chuj tu wchodziłeś"
                p "Gra mi pozwoliła"
                c "Tu powinni być tylko ludzie z DH ale chuj, niech zyskam"
                p "To co, będzie jeszcze jakiś bonus?"
                c "Będzie tylko dla posiadaczy Cibuch Premium Premium"
                p "Co to znaczy?"
                c "Nie mogę Ci powiedzieć, to załamie kontinuum czasoprzestrzenne, a to będę mógł robić dopiero w następnym arku"
                p "To może dasz mi jakieś zadanie specjalne?"
                c "A spierdalaj, tańcz kurwa"
                "I zacząłeś tańczyć z Cypherem"
                $ stan["Cypher"] = 7
                achieve Fri
                jump rozstaje

            if stan["Cypher"] == 7:
                c "Ja tu czekam na zadanie i przybędę jak zawołasz na nie"
                jump rozstaje

            if stan["Cypher"] == 9:
                c "Spierdalaj"
                jump rozstaje 

    jump rozstaje          