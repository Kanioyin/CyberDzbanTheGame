
init python:
    import os 
    class Inventory():
        def __init__(self, items, quantity):
            self.items = items
            self.quantity = quantity

        def has_space(self, max):
            if self.quantity < max:
                return True
            
            else:
                return False

        def add_item(self,item):
            self.items.append(item)
            self.quantity += 1
            p(f"Dostałem {item.name}")

        def remove_item(self, item):
            self.items.remove(item)
            self.quantity -= 1
            p(f"Straciłem {item.name}")

        def list_items(self):
            if self.quantity <= 0:
                p("Nie mam nic przy sobie")

            else:
                p("Mam w plecaku:")
                for item in self.items:
                    p(f"{item.name}, {item.desc}")

        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False

    class InventoryItem():
        def __init__(self, name, desc):
            self.name = name
            self.desc = desc


label yeet:
    scene black
    $ odp = renpy.input("Co chcesz wyjebać?")
    if (odp == "AR" or odp == "Ar" or odp == "ar") and inventory.has_item(AR) == True:
        achieve Eko
        $ inventory.remove_item(AR)
        window hide

    elif (odp == "Szczur" or odp == "Rat") and inventory.has_item(Rat) == True:
        achieve Eko
        $ postacie["Gun"] -= 1
        $ inventory.remove_item(Rat) 

    elif (odp == "Flaszka" or odp == "Flacha") and inventory.has_item(Flaszka) == True:
        achieve Eko
        $ postacie["Kalach"] -= 1
        $ inventory.remove_item(Flaszka)

    elif (odp == "Kokos" or odp == "Koks") and inventory.has_item(Kokos) == True:
        achieve Eko
        $ inventory.remove_item(Kokos)
        $ postacie["Laskawca"] -= 1

    elif (odp == "Pistolet" or odp == "Pistol" or odp == "Pistolecik") and inventory.has_item(Pistolecik) == True:
        achieve Eko
        $ inventory.remove_item(Pistolecik)

    elif (odp == "Granat") and inventory.has_item(Granat) == True:
        achieve Eko
        $ inventory.remove_item(Granat)

    elif (odp == "Wytrych") and inventory.has_item(Wytrych) == True:
        achieve Eko
        $ inventory.remove_item(Wytrych)

    elif (odp == "Ser") and inventory.has_item(Ser) == True:
        achieve Eko
        $ inventory.remove_item(Ser)

    else:
        "Nie masz tego"
        window hide
        
    if akt == 1:
        jump sypialnia
    
    elif akt == 2:
        jump oporslep


label updict(Who,dict):
        python:
            for key in dict.keys():
                if key != Who:
                    dict[key] = 0
                

label checktime:
    if akt == 1:
        call klontwakalacha from _call_klontwakalacha
    if czas < 1:
        p "Późno już, idę spać"
        if akt == 1:
            jump sypialnia
        
        elif akt == 2:
            jump oporslep

    else:
        return


# input call testSkili("Cecha", PT), nie fogoruj ""
label testSkili(skil,cecha, PT):
    if skil == "Bron":
        if inventory.has_item(AR):
            $ PT -= 3

        elif inventory.has_item(Granat):
            $ PT -= 2

        elif inventory.has_item(Pistolecik):
            $ PT -= 1

        else:
            pass

    $ exp += 1
    $ wynik = 0
    $ d10 = renpy.random.randint(1,10)
    if d10 == 1:
        $ d10 -= renpy.random.randint(1,10)

    if d10 == 10:
        $ d10 += renpy.random.randint(1,10)

    if skile[skil]+cechy[cecha]+d10 > PT-1:
        $ wynik = 1
        return

    else:
        $ wynik = 0
        return



label checkHP(dmg):
    $ wybrany_dzwiek = renpy.random.choice(buul)
    if inventory.has_item(Kokos):
        $ inventory.remove_item(Kokos)
        p "Pa ten unik szmato, Koks+L+Ratio"
        if renpy.random.randint(0,1) == 0:
            p "Essa, uniknięte"
            achieve Frik
            return
        else:
            pass

    if armor > dmg:
        p "Armor wszystko zablokował"
    
    elif armor == dmg:
        p "Armor wszystko zablokował"
    
    elif armor == 0:
        $ HP -= dmg
        play sound (wybrany_dzwiek)

    else:
        $ HP -= (dmg - armor)
        $ armor -= 1
        play sound (wybrany_dzwiek)

    if armor < 0:
        $ armor = 0
        
    if armor == 0 and inventory.has_item(MalyArmor) == True:
        $ inventory.remove_item(MalyArmor)
        p "Pancerz się rozsypał"

    if HP < 0:
        $ HP = 0

    if HP > MaxHP:
        $ HP = MaxHP

    if umieram == 1:
        if inventory.has_item(THeal) == True:
            achieve Clos
            $ inventory.remove_item(THeal)
            $ HP =  ["BC"] * 2
            $ umieram = 0
            p "Dobrze że miałem Turbo Uzrawiacz"
        else:
            jump gameover

    elif HP < 1:
        p "Dostałem straszny wpierdol, zaraz umrę"
        $ umieram = 1
        $ HP = 0
        return

    return


label klontwakalacha:
    if postacie["Kalach"] < 0:
        if inventory.has_item(Flaszka) == True:
            k "Wyczuwam flaszki, pora się napić"
            achieve Curs
            python:
                postacie["Kalach"] = 0
                while inventory.has_item(Flaszka) == True:
                    inventory.remove_item(Flaszka)
            return

        else:
            return

    else:
        return


transform bounce:
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat 2


label start:
    play music "Bongo_Madness.mp3" volume 0.2

    while helper == 1:
        $ player_name = renpy.input("Nazywasz się:")
        if player_name == "Gun":
            g "Prawa autorskie kurwa"

        elif player_name == "Kałach":
            k "Odpierdol się"

        elif player_name == "Cypher":
            c "Cypher może być tylko jeden"
            c "GIŃ"
            achieve Ttsd
            jump gameover

        elif player_name == "Łaskawca":
            pl "Koleżko, nie pozwalaj sobie"

        elif player_name == "Jhin":
            j "Obawiam się, że to imię jest już zajęte."
            j "Ale możesz zostać Jhin2"
            $ player_name = "Jhin2"
            $ helper = 0

        elif player_name == "Hartmann":
            h "A Ci migomatem pierdolne"

        elif player_name == "Vista" or player_name =="GenToo":
            v "Vitamy w koloni"
            $ Frakcja = 3
            $ helper = 0

        elif player_name == "Szczur":
            g "Na tym etapie jeszcze z tobą nie gadam"

        elif player_name == "Debil":
            g "To brzmi debilnie"

        elif player_name == "Bezi":
            p "Nie żyję lmao"
            achieve Ttsd
            jump gameover

        elif player_name == "Krateus":
            kr "Zaraz będziesz celem jew dzitsu"

        elif player_name == "Kretyneus":
            g "Faktycznie kretyn"

        elif player_name == "Chuj" or player_name =="Siur":
            g "Pewnie mały"
            $ helper = 0

        elif player_name == "Jan":
            g "Jebany dzban"
            $ helper = 0

        elif player_name == "Joon Goo":
            g "Jak ja Cię kurwa nienawidzę"
            $ postacie["Gun"] = -99
            $ helper = 0

        elif player_name == "Hubert":
            k "Spierdalaj"
            $ postacie["Kalach"] = -5
            $ helper = 0

        elif player_name == "Kennedy" or player_name == "Ken":
            gk "Szczylu, uspokuj się"

        elif player_name == "Sex" or player_name == "sex":
            "Kto jak kto ale ty raczej nie ruchasz"

        elif player_name == "Cycu":
            "Co jest kurde, to cyber jest kurde"

        elif player_name == "Czajnik":
            "A ty nie widziałeś już wszystkiego?"
            ha "Czekam słoneczko"
            $ helper = 0

        elif player_name == "Jax":
            ja "Wywiatracze cię zaraz"

        elif player_name == "Vio":
            vi "Vipierdalaj"

        elif player_name == "Kris":
            cr "Kolego nie pomyliło Ci się coś?"

        elif player_name == "Alfonso":
            k "Siema byku"
            $ postacie["Kalach"] += 5
            $ Frakcja = 4
            $ inventory.add_item(Flacha)
            $ helper = 0

        elif player_name == "Anon":
            achieve Owo
            fse "OMG, Anon-kun"
            fse "Nawet nie wiesz jak tęskniłam"
            fse "Pora wracać do roboty"
            $ Frakcja == 6
            $ helper = 0

        elif player_name == "Anton":
            mg "OMG, Anton-kun"
            mg "Hai Hai"
            $ helper = 0

        elif player_name == "XD2":
            $ atrefakty["Jaja"] = "W sejfie"
            jump artcrack

        elif player_name == "Zium":
            jump a2intro
            $ chipy = 5
            

        else:
            $ helper = 0

    
    "Nie miałeś edków"
    call bigunl from _call_bigunl
    "Sensu życia"
    "Ani nawet broni"
    menu:
        "Więc postanowiłeś..."

        "Dołączyć do Cyberdzbanów.":

            scene baza

        "Spierdalać.":
            achieve Msnc
            "Good ending, lol"
            return

    show cypher with dissolve
    c "Witamy w bazie młody."
    c "Pa ten trick!"
    "Zaczyna morbować"
    show gun at right
    show cypher at left
    g "Spokojnie kasztanie"
    show ciphate with dissolve
    "Gun katyńskim kopem wysłał Cyphera na dach"
    hide ciphate with dissolve
    c "DiamandHunde znowu błysnęło"
    play sound "CARTOON RICOCHET #2.mp3"
    hide cypher with fade
    g "Łap rata"
    play sound "THROWING.mp3"
    $ inventory.add_item(Rat)
    show grab
    g "Oto symbol twojej przynależności do Draco Nero"
    g "Znaczy, jeszcze nie jesteś jego członkiem ale na start masz rata. Ten chuj srał mi w kieszeni"
    g "Dawaj do środka"
    jump intro
# intro

label intro:
    $ helper = 1
    $ baba_name = "Babka from żabka"
    achieve Poczatek
    scene kuchnia
    show gun at right
    g "Więc nowy, witamy w bazie"
    g "Jak ty się w ogóle nazywasz?"
    p "[player_name]"
    g "Brzmi jak debil"
    g "Idź się przejdź, pogadaj z innymi, przywitaj się jak człowiek"
    jump rozstaje

label gameover:
    achieve GitGud
    "Przegrałeś lol"
    $ MainMenu(confirm=False)()

label rozstaje:
    play sound "scen.mp3"
    scene rozstaje
    stop music
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    $ renpy.block_rollback()
    $ config.rollback_enabled = True
    call checktime from _call_checktime
    menu:
        "Kaj leziesz?"

        "Kierunek kuchnia":
            play sound "scen.mp3"
            jump kuchnia

        "Może się pomodlę?":
            play sound "scen.mp3"
            jump kosciol

        "Przycisnęło mnie" if bigquest < 5:
            play sound "scen.mp3"
            jump kibel

        "Nie boję się śmierci":
            play sound "scen.mp3"
            jump dach

        "Co tam tak napierdala?":
            play sound "scen.mp3"
            jump warsztat

        "Ten czerwony krzyż wygląda obiecująco":
            play sound "scen.mp3"
            jump klinika

        "Dziupla Jhina" if bigquest > 2:
            play sound "scen.mp3"
            jump jhinownia

        "Lil Brazil" if bigquest > 4:
            play sound "scen.mp3"
            jump bruhzylia

        "Idę do siebie" if akt > 0:
            play sound "scen.mp3"
            jump sypialnia

        "Wychodzę stąd" if akt > 0:
            show screen map_screen
            window hide
            pause 1
            pause 1
            pause 1
            pause 1
            pause 1
            pause 1
            jump rozstaje


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
                g "Tak czy siak, nic dobrego to nie oznacza"
                g "Zdupcaj, muszę pomyśleć"
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
                g "Zostaniesz szpiegiem, może nie z krainy deszczowców"
                g "Tylko z bazy, wślizgniesz się w szeregi Vistów"
                g "Wyciągniesz tyle informacji ile się da i spierdolisz"
                g "Zadanie analnie proste"
                g "Zaczynasz bezzwłocznie"
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
                show cypher at left with moveinleft
                c "Dzień dobry [player_name]!"
                p "Co ty tu kurwa robisz? Guna ja tu szukam."
                c "Przykra sprawa ale mnie to nie obchodzi trzeba przeprowadzić Anschluss tej kuchni"
                p "Co to kurwa znaczy?"
                c "No patrz. Tu się zrobi dziurę tam się pierdolnie bunkier i okopy"
                c "Nad wejściem działka, może nawet z ammunicją"
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
                        g "Dokładnie"
                        g "Jeśli jeszcze raz zobaczę że myszkujecie mi w kuchni urwę jaja z kutasami"
                        hide gun with moveoutleft
                        $ postacie["Gun"] -= 2
                        p "Chyba się zdenerwował"
                        c "Chuj z nim"
                        $ stan["Cypher"] = 4
                        jump rozstaje

                    "Przyjmuję konsekwencje":
                        p "Przyszliśmy pooglądać kuchnie"
                        g "Po chuj"
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
                g "Czyli ze mną chcesz zacząć randkować?"
                g "Daniel Krej z!"
                g "No to zacznijmy rozmowę kwalifikacyjną"
                g "Pytanie pierwsze"
                $ config.rollback_enabled = False
                $ odp = renpy.input("Jaki jest twój ulubiony kolor?")
                if odp == "Szczurzy":
                    g "I to mi się podoba"
                    $ postacie["Gun"] += 1

                else:
                    g "Chuja się znasz"

                g "Pytanie numero dos"
                $ odp = renpy.input("Lubisz bigos?")
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
                if odp == "Prawdziwy":
                    g "Bardzo dobrze"
                    $ postacie["Gun"] += 1
                
                else:
                    g "Ten też dobry ale nie top"

                g "Pytanie piąte"
                $ odp = renpy.input("Gdzie leży prawo według BB?")
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
                g "No to witam ponownie, dziś zobaczysz Mączysława w akcji"
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
                g "Zobaczysz w środku"
                g "Ale najpierw. Raty aktywacja!"
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
                p "Panie Ganie, jak pan mógł, znowu całe gówno na mojej głowie"
                p "Jak znajdę pokój Cyphera? Ten budynek ma kilkanaście pięter"
                "Podszedłeś do pierwszych drzwi"
                "Widzisz pierdalny napis Cypher"
                p "No dobra, to nie było trudne"
                "Drzwi nie były nawet zakluczone"
                p "Zbyt łatwo"
                play sound "Dzwi.wav"
                "Wszedłeś do środka"
                p "Chuja widzę"
                p "Gdzie Cypher schowałby spodnie"
                show cypher
                c "W szafie"
                hide cypher with dissolve  
                p "No co ty kurwa nie powiesz"
                "Sprawdziłeś pierwszą szafę"
                "I były w niej spodnie"
                p "Kurwa jackpot"
                p "Zdecydowanie zbyt prosto to idzie"
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
                k "Nie, ciężko ranny ale żywy"
                k "O! Jest i moja flaszka! He, to zaraz będzie jeszcze jedna"
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
                g "Spokojnie szczylu, to jest zaklęty obiekt"
                g "Nie możesz sobie tak po prostu go zabrać"
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
                    g "Chciałem pojechać z Jhinem na zadanie bojowe ale mu się zdechło"
                    g "Więc to mamy już z głowy"
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
                    scene idrive
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
                    "Odwróciłeś się aby sprawdzić co z Jhinem"
                    "A Jhin leży na ziemi nieprzytomny"
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
                    g "Ta, dokładnie. Kretynus znalazł bombę. Ja ją podstawie i spierdalamy"
                    g "Twoim zadaniem będzie stanie na czatach"
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

label kosciol:
    scene kosciul
    show kalach at right
    if akt == 0:
        if inventory.has_item(Flaszka) == True:
            k "Wyczuwam flachę"
            k "Wezmę sobie"
            $ postacie["Kalach"] += 1
            $ inventory.remove_item(Flaszka)
            $ stan["Gun"] += 1
            jump rozstaje

        if postacie["Kalach"] == 0:
            k "Kim ty kurwa jesteś?"
            k "Wypierdalaj"
            $ stan["Gun"] += 1
            jump rozstaje

        else:
            play sound "BURP.mp3"
            k "Pijesz?"
            jump rozstaje

    if akt == 1:
        if bigquest == 0:
            $ czas -= 1
            if stan["Kalach"] == 0:
                k "Jak tam poszło?"
                k "Postrzelałeś?"
                k "Poruchałeś?"
                k "Może coś popiłeś?"
                if wojownik == True:
                    p "Było Pif Paf robione"
                    k "Czyli coś postrzelałeś, milutko"
                    $ postacie["Kalach"] += 1

                else:
                    k "Jedyne co strzeliłeś to foch, Ciper moment"
                    show cypher with moveinleft
                    c "Falsch"
                    hide cypher with moveoutright
                    k "Spierdalaj syfer"
                    $ postacie["Kalach"] -= 1

                $ stan["Kalach"] = 1
                k "Zdupcaj, wracam do picia"
                jump rozstaje

            if stan["Kalach"] == 1:
                "Kałach alkoholizuje się, lepiej mu nie przeszkadzaj"
                jump rozstaje

        elif bigquest == 3:
            if stan["Kalach"] == 1:
                k "Niech mnie uda i zimna wóda"
                k "Wróciłeś żywy z siedliska Vist"
                $ postacie["Kalach"] += 1
                k "Masz nagrodę"
                if inventory.has_space(Cap) == True:
                    play sound "THROWING.mp3"
                    $ inventory.add_item(Flaszka)
                    k "Zachowaj na specjalną okazję, albo chlej teraz"
                
                else:
                    k "Albo jednak nie"
                $ stan["Kalach"] = 2
                jump rozstaje

            else:
                "Kałach alkoholizuje się, lepiej mu nie przeszkadzaj"

        elif bigquest == 4:
            if stan["Kalach"] != 3:
                if dzien < 10:
                    "Kościół jest zamknięty, wróć później"
                    jump rozstaje

                elif dzien > 9:
                    $ stan["Kalach"] = 3
                    k "Wróciłem z krucjaty."
                    k "I niech mnie dunder świśnie, tak mnie w krzyżu napierdala."
                    k "Jeśli kiedykolwiek dołączysz do fanów stópek."
                    k "To zostaniesz zgilotynowany."
                    k "I granie Briar też się liczy."
                    if Frakcja == 0:
                        k "Może chcesz dołączyć do kościoła?"
                        k "Dostaniesz błogosławienie i coś jeszcze"
                        k "Co konkretnie, to jeszcze nie wiem"
                        k "Ale na 69 procent coś będzie."
                        $ config.rollback_enabled = False
                        menu:
                            k "To co, piszesz się?"

                            "Proste że tak, Umen":
                                $ Frakcja = 4
                                $ postacie["Kalach"] += 4
                                achieve Holy
                                k "Niech wszystko Ci się teraz UDA!"
                                jump rozstaje

                            "Sorry Kałach, jestem ateistą":
                                k "Dobrze więc."
                                k "Ale pamiętaj, nigdy stopy."
                                jump rozstaje

                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                    jump rozstaje

        elif bigquest == 5:
            if stan["Kalach"] == 9:
                k "Hubert spierdalaj"
                jump rozstaje

            k "No witam witam"
            k "Przyszedłeś po przebaczenie grzechów?"
            p "Nie Kałachu, muszę zostać twoim przyjacielem"
            k "Co kurwa?"
            p "Kennedy szuka ludzi na misję"
            p "A ja muszę się z wami zakumplować"
            if [player_name] == "Hubert":
                k "Kurwa Hubert, spierdalaj"
                $ stan["Kalach"] = 9
                jump rozstaje

            k "Łe dobra, nie strasz mnie kurwa"
            k "Już myślałem że Hubert gra"
            k "A wiesz, on jest fanem Yaoj"
            k "A to nie jest dating sim"
            k "Tylko CPTG"
            k "Ale no dobra, nie chce mi się z tobą gadać"
            k "Powiedzmy, że jak będziemy musieli się napierdalać"
            k "To masz mój karabin"
            achieve Kalpp
            if Frakcja == 1:
                show cypher with moveinright
                c "Ale on już ma twój sprzęt"
                k "Spierdalaj"
                hide cypher with moveoutright

            $ postacie["Kalach"] += 1
            $ czas -= 2
            $ stan["Kalach"] = 5

        else:
            k "Czego ty kurwa chcesz?"
            k "Nie mam teraz czasu na gadanie"
            k "Spierdalaj"
            jump rozstaje

    jump rozstaje

label kibel:
    scene kibel
    if akt == 0:
        show grat at left
        "Ić stont"
        $ stan["Gun"] += 1
        jump rozstaje

    elif akt == 1 and bigquest == 0:
        $ czas -= 1
        if kibel_stan == 0:
            "Spokojnie tu, zbyt spokojnie"
            "Ciekawe gdzie podziały się wszystkie szczury?"
            if inventory.has_item(Rat):
                menu:
                    "Mam jednego w kieszeni"
                    "Wracaj do rodziny słoneczko":
                        show ciphate with dissolve
                        "Zostawiłeś szczura w kiblu"
                        hide ciphate with dissolve
                        $ inventory.remove_item(Rat)
                        show grat at left
                        r "Dziękuje, dobry człowieku"
                        $ postacie["Gun"] += 1
                        $ kibel_stan = 1
                        jump rozstaje

                    "Kontynuuj sranie w kieszeni":
                        p "Tu będzie Ci bezpieczniej"
                        jump rozstaje
            jump rozstaje

        elif kibel_stan == 1:
            show grat
            r "Witaj dobry człowieku"
            r "Pozwól mi egzystować w tym niebezpiecznym środowisku samotnie"
            show gun at right
            g "Kurwa, gadasz ze szczurami"
            g "Będą z Ciebie ludzie"
            achieve Shizo
            $ postacie["Gun"] += 1
            $ kibel_stan += 1
            jump rozstaje

        elif kibel_stan == 2:
            "Raty ratują"
            jump rozstaje

    elif akt == 1 and bigquest > 2:
        $ czas -= 1
        "Raty ratują"
        jump rozstaje

    else:
        jump rozstaje

label dach:
    scene dach
    show cypher
    if akt == 0:
        if stan["Cypher"] == 0:
            "Cypher skończył morbowanie"
            c "Chcesz zostać najemnikiem?"
            c "A może wolisz wynająć najemników?"
            c "Wykonujemy każde zadanie, nawet niemożliwe damy radę zrobić za odpowiednią opłatę oczywiście"
            g "Te młody, dawaj na dół"
            hide cypher
            scene kuchnia
            show gun
            g "Lepiej nie zawieraj żadnych umów z Cypherem, to nigdy nie kończy się dobrze"
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
            c "No to masz przepierdolone"
            c "Młynarczyk! Bierz go!"
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
            c "Czekaj, wróciłeś właśnie od Vistów co nie?"
            c "Jak tam było? Dobrze się bawiłeś?"
            c "Powiem Ci w sekrecie, który jednak każdy zna kiedyś, za czasów swojej światłości, polowałem na Visty"
            c "Ale moja umowa z wojskiem poszła się jebać gdy ten chuj Kennedy nie dał mi wsparcia"
            c "Jakby ta Av-ka wleciała do metra, byłbym niepokonany"
            c "A tak to Jhin prawie się zabił tnąc kable. Mówiłem mu, trakcja to śmierć. Tory! To jest przyszłość"
            c "To tyle z mojej audiencji teraz idź w chuj."
            $ stan["Cypher"] = 1
            jump rozstaje

        elif bigquest == 3 and stan["Cypher"] == 1:
            $ czas -= 3
            c "No co ty kurwa ode mnie chcesz?"
            c "Nie chce mi się z tobą gadać"
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
                    c "Wtedy dostaniesz fragment mojej afekcji"
                    c "Możemy uznać że pierwsze zadanie już wykonałeś"
                    p "No, to było szybkie"
                    c "Nie ciesz się zbyt szybko, następne będą trudniejsze"
                    c "Będą wymagały od Ciebie masy sprzętu i trochę umysłu"
                    c "Dobra, spierdalaj. Wyruszam myśleć"
                    $ stan["Cypher"] = 1
                    jump rozstaje

            if stan["Cypher"] == 1:
                c "No dobra mam pomysł, przelećmy się"
                p "Kurwa cypher, popierdoliło Cie? Dlaczego ty taki rogaty jesteś?"
                c "Źle mnie zrozumiałeś [player_name]"
                c "Widzisz ten helikopter? Lecimy na zadanie"
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
                c "A czego ty się spodziewałeś?"
                c "Merch DH musi zalać zachodnitajwański rynek"
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
                c "Nie, to by było zbyt proste"
                c "Jedna z drukarek przestała działać"
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
                        c "Aż bym Cie znowu zaprosił do DH"
                        c "Ale niestety komuś nie chce się tego kodować"
                        c "Więc takzwany chuj, możemy wracać"
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
                        kr "To prawda, liczenie makro oddaje"
                        kr "Wiesz, że jeden bochenek ma 2001 kalorii"
                        kr "363 węgli, 66 białka i 24 fatu"
                        kr "Warto kontrolować te wartości"
                        hide krateus
                        c "No właśnie"
                        $ postacie["Cypher"] -= 1

                    "Biedny jestem, z trzy":
                        c "Oj rozumiem twój ból"
                        c "Jak byłem małym szczylem"
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
                        c "Wiesz co? Jak mi ufasz, to ja zaufam tobie"
                        c "Możesz mnie liczyć jako sojusznika"
                        p "Klawo"
                        achieve Cippp
                        $ stan["Cypher"] = 5
                        $ postacie["Cypher"] += 2
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje


                    "Nie":
                        c "To spierdalaj"
                        achieve Foch
                        "I bez słowa zaczął uciekać"
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
                c "To jest bonus!"
                c "Całkiem za friko!"
                p "Serio?!"
                c "No ta, nie wiem po chuj tu wchodziłeś"
                p "Gra mi pozwoliła"
                c "Tu powinni być tylko ludzie z DH"
                c "Ale chuj, niech zyskam"
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
                c "Ja tu czekam na zadanie"
                c "Przybędę jak zawołasz na nie"
                jump rozstaje

            if stan["Cypher"] == 9:
                c "Spierdalaj"
                jump rozstaje 

    jump rozstaje            

label warsztat:
    scene warsztat
    show hartmann at right
    $ czas -= 1
    if akt == 0:
        play sound ["Budowa.wav","Pila.wav"]
        $ stan["Gun"] += 1
        "Wchodząc do pokoju słyszysz agresywne napierdalanie młotkiem, a w tle leci niemiecki metal"
        h "Kim ty kurwa jesteś? Dlaczego mi kurwa przeszkadzasz w robocie?"
        h "Spierdalaj, albo Ci migomatem przypierdolę"
        stop sound
        jump rozstaje

    elif akt == 1:
        if inventory.has_item(MalyArmor) == False and stan["Hartmann"] != 1:
            h "Co tam [player_name]?"
            h "Chcesz kupić jakiś pancerz? Tylko 100 edków i nie padniesz na pierda"
            menu:
                "Czy potrzebny mi jest pancerz?"

                "Kurwa biorę" if edki > 99 and inventory.has_space(Cap) == True:
                    if edki > 100:
                        $ inventory.add_item(MalyArmor)
                        $ edki -= 100
                        $ armor = 11
                        h "Jak Ci się rozpierdoli, to wiesz gdzie mnie szukać"

                    else:
                        p "Nie stać mnie"

                "A spierdalaj, unikać będę":
                    h "Jak dostaniesz wpierdol, to wiesz gdzie mnie szukać"

        elif armor < 11 and stan["Hartmann"] != 1:
            h "Już ci się armor rozjebał?"
            h "Co jak co ale do wpierdolu to jesteś pierwszy. Zespawać Ci to, 10 za punkcik"
            menu:
                "Naprawiać mam: [armor]/11 pancerza"
                "Spawaj" if edki > (11-armor)*10:
                    $ edki -= (11-armor)*10
                    $ armor = 11
                    h "Get spawed"

                "Cholpika, nie stać mnie":
                    h "To idź do roboty lol"
                    
        if bigquest > 2:
            if stan["Hartmann"] == 0:
                $ stan["Hartmann"] = 1
                h "Powiedz mi przetrwańcze"
                h "Czy Visty mają migomat na stanie?"
                h "Bo słyszałem że vigomat podobno spawa tylko gówno"
                menu:
                    "Czym jest kurwa migomat?":
                        h "Ty pierdolony betoniarzu"
                        h "Migomat to popularna nazwa spawarki, służącej do spawania metodą MIG-MAG."
                        h "Technologia MIG umożliwia spawanie w osłonie gazów obojętnych (argon lub hel), natomiast technologia MAG w osłonie gazów aktywnych (dwutlenek węgla)."
                        h "Spawanie migomatem jest efektywne, wydajne i precyzyjne."
                        h "Uzyskanie spoiny charakteryzują się wysoką jakością wykonania."
                        h "A teraz powiem Ci jak to działa"
                        h "Spawanie MIG (Metal Inert Gas) to metoda 131, natomiast spawanie MAG (Metal Active Gas) to metoda 135. "
                        h "Migomaty to urządzenia półautomatyczne. Najważniejsze elementy układu to źródło prądu, połączone z układem sterującym;"
                        h "podajnik drutu (jeżeli umieszczony jest na zewnątrz, to łączy się go ze źródłem prądu za pomocą przewodu zespolonego); przewód masowy, łączący przedmiot spawany ze źródłem prądu"
                        h " butla z gazem osłonowym; uchwyt doprowadzający prąd do drutu."
                        h "Proces spawania rozpoczyna się od naciśnięcia przycisku na uchwycie MIG-MAG. Uchwyt spawalniczy przemieszczany jest równomiernie w stosunku do spoiny."
                        h "Należy określić prędkość wysuwania się drutu. Wysuwający się drut ulega stopieniu w łuku elektrycznym."
                        h "Tworzy się on pomiędzy drutem (elektrodą topliwą), a materiałem spawanym. Długość łuku utrzymywana jest na stałym poziomie."
                        h "Łuk elektryczny i stopiony metal (jeziorko) ochraniane są przez gaz osłonowy przed oddziaływaniem atmosfery. Krzepnące jeziorko spawalnicze tworzy trwałe złącze."
                        h "I to chyba tyle"
                        h "Teraz ić se w chuj, muszę ochłonąć"
                        $ czas -= 1
                        jump rozstaje

                    "Nie widziałem żadnego Vigomatu":
                        h "Scheise"
                        h "Albo jesteś ślepy, albo to vigomat jest mitem"
                        h "Tak czy siak, daj mi trochę czasu, muszę to przemyśleć"
                        jump rozstaje

                    "Opowiem Ci kawał, Vista gówno spawał":
                        h "KURWA WIEDZIAŁEM"
                        h "MUSZĘ GO ZDOBYĆ"
                        h "WYRUSZAM BEZZWŁOCZNIE"
                        jump rozstaje

            elif stan["Hartmann"] == 1 and dzien > 10:
                h "Pyk Pyk, jako tako i do Cyphera"
                p "Cześć Hartmann!"
                h "O Gluten morgen [player_name]! Potrzebujesz czegoś, jestem trochę zajęty"
                p "A przyszedłem pogadać trochę"
                p "Ale jak pracujesz to nie przeszkadzam"
                h "Typie, robię brońkę dla Cyphera"
                h "To nie jest jakkolwiek ważne"
                show cypher with moveinleft
                c "Wrrrr"
                hide cypher with moveoutright
                h "No widzisz, nic istotnego"
                h "O czym chcesz pogadać?"
                p "A tak, po prostu. Lubię znać swoich współpracowników"
                h "No to siadaj, opowiem Ci zwykłą historię"
                h "Byłem szczylem, spawałem złom"
                h "Romansowałem sobie trochę ale baby nie były gotowe na potężnego prawicowca"
                h "Później pewna zajebana korporacja się pojawiła"
                h "Rozstrzelała mój gang i w taki sposób trafiłem tu"
                p "No to było szybkie"
                h "A co ja mam Ci opowiadać historię mojego życia?"
                h "Biografię chcesz mi pisać?"
                p "No nie no, tyle mi wystarczy"
                h "No i dobra, get pogadaned"
                p "Tja, to ja spierdalam"
                h "I słusznie"
                h "Spawu, spawu, spawu"
                $ stan["Hartmann"] = 2
                $ czas -= 1
                jump rozstaje

            elif stan["Hartmann"] == 2 and bigquest == 5:
                h "Czemu ty mi znowu dupę zawracasz?"
                p "Dostałem bojowe zadanie od Generała"
                h "No i co? Chyba jesteś w stanie sam to zrobić."
                p "Zadanie polega na zebraniu drużyny"
                h "No i?"
                p "Czy nie chcesz może dołączyć do mojego party?"
                h "Na łeb upadłeś"
                p "AHA ):"
                h "Wypłata jak wysoka?"
                p "Nie wiem ):"
                h "No to z czym do ludzi panie"
                h "Jak mi powiesz ile zarobię to może się zastanowię"
                h "Możesz też mi kupić nową spawarkę"
                h "Wyjebane, muszę coś dostać"
                $ config.rollback_enabled = False
                menu:
                    "Co robisz?"
                    "(Kłamstwo) Żartowałem, dostaniemy 3k na głowę":
                        h "No i to jest zysk"
                        h "Wchodzę w to jak w albatrosa"
                        p "No to witamy na pokładzie"
                        $ helper2 = 1
                        $ stan["Hartmann"] = 5
                        "Zadowolony z siebie wyszedłeś"
                        achieve Harpp
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje

                    "Znajdę Ci tę spawarkę":
                        show ciphate with dissolve
                        h "Nie, Nie, Nie kochanieńki"
                        hide ciphate with dissolve
                        h "Idziemy teraz na market i Ci powiem jaką chcę"
                        scene nocny
                        show hartmann
                        "Wędrowaliście sobie między kramami"
                        h "O! Patrz ten model ale ma parametry"
                        p "Wiesz że ja chuja z tego rozumiem"
                        h "Zdaję sobie z tego sprawę"
                        p "Powiedz mi jaka cena"
                        if edki > 499:
                            h "Pięć stówek, uczciwie"
                            p "Ała, mój portfel płacze"
                            $ edki -= 500
                        
                        else:
                            h "Promocja jest tylko [edki]!"
                            p "Czyli dokładnie tyle ile mam w portfelu"
                            $ edki = 0
                        
                        h "No, to ja jestem kontent."
                        p "A ja jestem biedny"
                        h "Ale masz kolejnego wojownika dzielnego"
                        p "Przynajmniej tyle"
                        achieve Harpp
                        $ stan["Hartmann"] = 5
                        $ czas -= 5
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje

            else:
                h "Nie mam Ci nic do powiedzenia"
                jump rozstaje
        else:
            h "Nie mam Ci nic do powiedzenia"
            jump rozstaje

    
    jump rozstaje

label klinika:
    scene klinika
    show laskawca at right
    if akt == 0:
        $ stan["Gun"] += 1
        pl "Siema, chcesz kokosa kurwa ten?"
        if inventory.has_item(Kokos) == True:
            pl "No wciągnij no"
            jump rozstaje

        else:
            pl "Łap, pierwszy za darmoszkę"
            play sound "THROWING.mp3"
            $ inventory.add_item(Kokos)
            pl "Korzystaj do woli, nic złego się nie stanie"
            pl "Papatki"
            jump rozstaje

    elif akt > 0:
        $ czas -= 1
        pl "Co tam [player_name]?"
        if HP != MaxHP and edki > 49:
            pl "Może Cię uleczyć?"
            pl "Tylko 50 edków"
            menu:
                "Potrzebuje leczenia? [HP]/[MaxHP]"
                "Lecz mnie" if edki > 49:
                    $ HP = MaxHP
                    $ umieram = 0
                    $ edki -= 50
                    $ czas -= 5
                    "Zostałeś Healnięty"

                "Podziękuje":
                    pass

        if inventory.has_item(Kokos) == False and edki > 19:
            pl "Chcesz kupić kokosa kurwa ten?"
            menu:
                "Dawaj tego kokosa":
                    if edki > 20 and inventory.has_space(Cap) == True:
                        $ postacie["Laskawca"] += 1
                        play sound "THROWING.mp3"
                        $ inventory.add_item(Kokos)
                        $ edki -= 20

                    else:
                        p "Nie stać mnie"

                "Podziękuje":
                    pass

        if inventory.has_item(THeal) == False and edki > 199:
            pl "Może chcesz zakupić turbouzdrawiacz?"
            pl "Uratuje cię przed dedem"
            menu:
                "Bardzo chętnie" if edki > 199 and inventory.has_space(Cap) == True:
                    play sound "THROWING.mp3"
                    $ inventory.add_item(THeal)
                    $ edki -= 200

                "Nie mam kapitału":
                    pl "No to szkoda" 

    if akt == 1:
        if bigquest < 5:
            if stan["Laskawca"] == 0:
                pl "No to opowiadaj, jak Ci życie mija"
                pl "Powiem Ci, u mnie jest dość ciężko. Szukam serwera dla baby"
                pl "Kiedyś w bazie mieliśmy cały czas jakiegoś netrunnera"
                pl "Ale przez cały ten konflikt z Vistami"
                pl "To mało kto chce się pojawić"
                pl "Raz mieliśmy taki zajebisty serwer"
                pl "To się okazało że pali ludzi, jak się do niego wpięli"
                pl "Przez trzy tygodnie się kłócili co z nim zrobić"
                pl "I kurwa nawet nie pamiętam co się z nim stało"
                pl "Jakbyś znalazł jakiś fajny serwerek"
                pl "To daj mi cynk, wynagrodzę cię"
                $ config.rollback_enabled = False
                menu:
                    "Mam nadzieję, że w naturze ( ͡° ͜ʖ ͡°)":
                        show ciphate with dissolve
                        pl "Kto wie kotku."
                        hide ciphate with dissolve
                    
                    "Mam nadzieję, że w edkach":
                        pl "Pitos się znajdos"

                    "Dla Ciebie, poszukam za friko":
                        pl "No to mam u Ciebie dług"
                        $ postacie["Laskawca"] += 2

                $ renpy.block_rollback()
                $ config.rollback_enabled = True
                pl "No to czekam na info z niecierpliwością"
                $ stan["Laskawca"] = 1
                jump rozstaje

            else:
                jump rozstaje

        elif bigquest == 5:
            if stan["Laskawca"] == 1:
                pl "Czekam dalej"
                p "To przestań czekać i ruszamy na poszukiwania"
                pl "Karamba, jesteś dobrym mówcą"
                scene szop
                show laskawca at right
                "Wyruszyliście do lokalnego sklepiku"
                "I poznaliście miejsce następnego nocnego"
                pl "Nocny market w Night City"
                p "No, delikatny cringe"
                pl "Ale chuj, potrzebuję kobiety"
                p "Co?"
                pl "Dowiesz się w swoim czasie, pierdol się"
                p "Skąd ta agresja?"
                pl "Sorki, poniosło mnie"
                "I wyruszyliście na nocny"
                scene nocny
                show gun at left
                show laskawca at right
                pl "O! Witaj Gunie"
                g "Ser dobry panowie"
                pl "Czego tu szukasz"
                g "Dobry towar gorgonzola"
                pl "Jakieś gówno pewnie, nie słyszałem o tym"
                g "Chuja się znasz skośnooki"
                hide gun
                p "Wy zawsze się tak gryziecie?"
                pl "Co jak co ale Gunowi nie ufam"
                p "Dlaczego?"
                pl "Nie wiem w sumie, tak dla jajec, bardzo chętnie bym go zabił"
                p "Ok, zostawmy ten temat"
                "Sprawdziliście kilka straganów"
                "I pojawił się sprzedawca sieciowy"
                pl "Szanowny panie, 5 koła za to!? Literalnie cie popierdoliło"
                if edki > 4999:
                    p "Spokojnie Łaskawca, mnie na to stać"
                    $ edki -= 5000
                    pl "Jesteś pojebany! Gigantyczne czołgi człowieku"
                    pl "Masz mój miecz, pistolet i co tylko zapragniesz"
                    achieve Laspp
                    achieve Bogol
                    $ czas -= 5
                    $ postacie ["Laskawca"] += 20
                    $ stan["Laskawca"] = 2
                    jump rozstaje

                p "No plus jeden, to pewnie nawet tetrisa nie uciągnie"
                show ciphate with dissolve
                "Ale wasze gadanie nic nie dało"
                hide ciphate with dissolve
                pl "Dobra, chuj z tym, wracamy do bazy"
                scene klinika
                show laskawca at right
                pl "5000 edków, to jest mała fortuna"
                "Nie, nie chodzi mu o piwo"
                pl "Musielibyśmy napaść na bank"
                p "Kennedy ma robotę dla nas"
                pl "Ile płaci?"
                p "Dobre pytanie"
                pl "Popierdoli mnie. Jakieś wymagania ma do roboty?"
                p "Musimy zostać przyjaciółmi"
                pl "Ja pierdolę"
                pl "Dobra, możemy być?"
                pl "To musimy iść na jakąś randkę?"
                p "Pomińmy to, powiedzmy, że my ziomki"
                pl "No i dobra, fren"
                p "Fren"
                pl "To daj mi znać jak będzie akcja"
                p "Luzik arbuzik"
                scene black
                p "Dobra, jeden z głowy"
                achieve Laspp
                $ czas -= 5
                $ postacie ["Laskawca"] += 1
                $ stan["Laskawca"] = 2
                jump rozstaje

            else:
                jump rozstaje

        else:
            pl "U mnie po staremu, wracaj do siebie"
            jump rozstaje

    jump rozstaje

label jhinownia:
    $ czas -= 1
    scene takiten
    if stan["Jhin"] == 9:
        "Chłop nie żyje"
        "Spoczywaj w tym pokoju"
        jump rozstaje
        

    if akt == 1:
        if stan["Jhin"] == 0:
            show jhin
            j "Hejka naklejka jestem Jhin Taki-Ten"
            j "To nazwisko zawdzięczam swoim rodzicom"
            j "Czyli udało Ci się nakraść w gnieździe Vist"
            j "Powiem Ci, jestem pod wrażeniem"
            $ postacie["Jhin"] += 1
            j "Powiedz mi jak tam było?"
            j "Czy to prawda że Visty rozmnażają się przez pączkowanie?"
            j "Czy może po śmierci dzielą się na pół?"
            $ config.rollback_enabled = False
            menu:
                "Zdecydowanie pączkowanie":
                    show ciphate with dissolve
                    j "O cholibka, wiedziałem"
                    hide ciphate with dissolve
                    $ postacie["Jhin"] += 1
                    j "To oznacza że trzeba zabić każdego piekarza w mieście"
                    j "Wyruszam natychmiast"
                    "I se poszedł"
                    $ stan["Jhin"] = 1
                    jump rozstaje

                "Dzielą się na pół":
                    j "A niech to dunder świśnie"
                    j "To oznacza że przegrałem zakład z Cypherem"
                    show cypher with moveinleft
                    c "RICHTIG"
                    hide cypher with moveoutright
                    j "On już tu jest, uciekam"
                    "I spierdolił"
                    $ stan["Jhin"] = 1
                    jump rozstaje

                "Co ty pierdolisz Ken-Taki?":
                    j "Ej to nie było miłe"
                    j "Staram się napisać książkę o Vistach"
                    j "I mam teraz rozdział o rozmnażaniu"
                    j "3.14rdol się chamie"
                    $ postacie["Jhin"] -= 1
                    $ stan["Jhin"] = 1
                    jump rozstaje

        if stan["Jhin"] == 1 and dzien > 4:
            "Pokój jest pusty, Jhin gdzieś wybył"
            if dzien > 9:
                $ stan["Jhin"] = 2

            jump rozstaje

        if stan["Jhin"] == 2:
            show jhin
            j "No hejka, dokonałem badań do mnożenia Vist"
            j "Źródłem jest strona internetowa"
            j "Krejzi.braindance.cum"
            j "Niestety nie mam pozwolenia od rodziców"
            j "Więc nie mogłem sprawdzić"
            $ config.rollback_enabled = False
            menu:
                j "Może ty jesteś na tyle odważny żeby to zrobić?"

                "Aż taki głupi nie jestem":
                    j "Bardzo dobrze, to był tylko test"
                    $ postacie["Jhin"] += 1
                    j "Jednak jesteś mądrzejszy od ośmioklasisty"
                    j "A to nie jest typowa sytuacja w tej bazie"
                    j "To dobry znak, nie będzie jeszcze z Ciebie insygni"
                    $ stan["Jhin"] = 3

                    j "Przyjdź później, będę miał kolejne pytania"
                
                "Sprawdzę":
                    j "Jesteś głupi, nie rób tego"
                    j "Powiem Gunowi i zapierdolą Cię"
                    j "Skończysz w sarnie"
                    show gun at left
                    g "SKOŃCZYSZ MARNIE DEBILU"
                    hide gun
                    j "Ano tak, skończysz marnie"
                    j "Weź się prześpij i przemyśl swoje zachowanie"
                    $ stan["Jhin"] = 3

                "Ja już jestem jednym z nich" if Frakcja == 3:
                    j "Pierdolisz"
                    p "Nie, masz przejebane"
                    j "aaaaa"
                    menu:
                        "Co chcesz zrobić z Jhinem?"
                        "Aloha Jhinocha":
                            p "Słodkich snów, Ten Taki"
                            j "Pls no kill"
                            p "Za późno Jhin, Vózg rozkazuje"
                            p "Ja pociągam za spust"
                            "Wystrzał z broni, sprzątnął tentakiego"
                            achieve Impostor
                            $ postacie["Jhin"] = -9999
                            $ stan["Jhin"] = 9
                            jump rozstaje

                        "Spokojnie, jestem dobrym Vistom":
                            j "Bo mój borze"
                            p "Bór Ci tu nie pomorze"
                            j "No dobra, to dlaczego jesteś przyjazny"
                            p "Integer overflow, słyszałeś o Gandhim w Civ?"
                            j "A dobra, teraz to ma sens"
                            j "No to dobra, zrobię potem z tobą wywiad"
                            j "Pomożesz mi się stać głównym charakterem"
                            p "No ok? Czytałem twoje backstory"
                            p "To przypadkiem nie jesteś nim już?"
                            j "No niestety nie, trochę fantazja mnie poniosła"
                            p "No dobra, to ma sans"
                            p "Odwiedzę cię potem, bywaj Vhin"
                            j "Bywaj [player_name]!"
                            $ postacie["Jhin"] += 1
                            $ stan["Jhin"] = 3

            "Wychodzisz z pokoju"
            jump rozstaje

        if stan["Jhin"] == 3 and bigquest == 5:
            show jhin
            j "Siemaneczko [player_name], co tam chcesz?"
            p "Jest robota od Kennedy'ego"
            j "O cholibka, pewnie coś niebezpiecznego"
            p "Masz rację"
            p "Musimy się zaprzyjaźnić"
            j "I co w tym jest takiego niebezpiecznego?"
            p 'To że muszę to zrobić z całym teamem'
            j "W sensie że przyjaźń tak?"
            p "No ta"
            j "A, ok, no to ten, fren?"
            p "Tak po prostu?"
            j "A czego ja mogę więcej wymagać?"
            p "No nie wiem, reszta ma doomstack bojowych zadań"
            j "Rozmawiałeś już ze mną przynajmniej dwa razy"
            j "W tej bazie czasem szybko można znaleźć cumpla"
            p "Pewnie zależy to od osoby"
            j "No ta"
            p "No to bywaj Jhin, ruszam siać przyjaźń z innymi"
            achieve Jhipp
            $ stan["Jhin"] = 4
            jump rozstaje

        elif stan["Jhin"] == 4:
            show jhin
            j "Idź pogadaj z Kennedym"
            jump rozstaje

        elif stan["Jhin"] == 6:
            show jhin
            j "To czekam na resztę i ruszamy"
            jump rozstaje

    jump rozstaje


label bruhzylia:
    scene brazil
    show krateus at right
    if akt == 1:
        if stan["Krateus"] == 0:
            kr "Czyli to ty jesteś nowy."
            kr "Witaj, jestem Krateus, a ty?"
            p "Jestem [player_name]."
            kr "No to zajebiście, formalności za nami"
            kr "Teraz tylko jedna drobnostka została"
            kr "Uściśnij mi dłoń"
            $ config.rollback_enabled = False
            menu:
                "No dobra":
                    "Widzisz że Krateus wyjął siekierę"
                    kr "No to za znajomość"
                    "I zamachnął się w kierunku twojego ramienia"
                    p "Pojebało CIĘ"
                    kr "WIEM"
                    "I siekiera zatrzymała się kilka centymetrów od celu"

                "Spierdalaj":
                    kr "Aha66"
                    "Krateus wyjął strzelbę"
                    kr "Może teraz zmienisz zdanie"
                    p "Na chuj chcesz uścisnąć mi dłoń?"
                    kr "Tak mnie nauczyli w KGB"
                    kr "Ale i tak"
                    
            kr "W Brazyli było gorzej"
            p "A czy tu będzie gorzej?"
            kr "Proste, że tak"
            "Nagle usłyszeliście krzyk dziecka"
            kr "Jebane mutanty"
            kr "Dobra, bywaj [player_name]. Idę polować"
            $ stan["Krateus"] = 1

        if stan["Krateus"] == 1:
            if dzien < 14:
                "No chłop poluje"
                "Daj mu trochę czasu"

            elif dzien > 14:
                kr "Kałabanga"
                kr "Wróciłem z polowania"
                p "Ta, to zajebiście"
                kr "Co nie? Chcesz iść następnym razem ze mną?"
                p "Mogę ale jeśli mi potem pomożesz"
                kr "Pojebało cię chyba"
                kr "Ja ci oferuję rozrywkę"
                kr "A ty chcesz żebym Ci coś jeszcze zrobił"
                kr "Wkurwiasz mnie"
                kr "Zaraz Ci pokaże Brazylijskie sztuki walki"
                p "CZEKAJ KURWA"
                kr "TO MNIE ZATRZYMAJ"
                p "ARMIA MA ROBOTĘ"
                kr "O, to aż posłucham"
                p "Musimy zostać kumplami"
                kr "No to będziemy musieli iść na polowanie"
                p "No dobra, kiedy?"
                kr "Jutro"
                $ stan["Krateus"] = 2
                jump rozstaje

        elif stan["Krateus"] == 2:
            scene fiszop at right
            show krateus
            "Wraz z Kreteusem wyruszyliście do miejskiej dżungli"
            kr "Nasze polowania zaczniemy od tamtego burdelu"
            p "A na co my będziemy w ogóle polować?"
            kr "Głupie pytanie. Na ludzi oczywiście"
            kr "Mam marzenie, które mnie napędza do działania"
            kr "Gdyby mnie przyjęli do ASP to nie byłoby problemu"
            kr "A tak to będą jaja jak sam skurwysyn"
            p "Dlaczego akurat na ludzi chcesz polować?"
            kr "Potrzebuję pracowników do nowego interesu"
            kr "Ale o tym opowiem Ci później"
            p "Pewnie w następnym..."
            kr "Sklej, cele idą"
            "Zatkaliście obaj mordy i przygotowaliście broń"
            p "Kto strzela pierwszy"
            show cypher with moveinleft
            c "Ja, hihi haha"
            "I widzicie jak ten debil jebany strzelił z bazooki"
            c "HI HI HA HA"
            hide cypher with moveoutright
            play sound "BOOM.mp3"
            "Rakieta przeleciała obok ludzi i eksplodowała fajerwerkami"
            c "Hi....HI......HA......HA"
            kr "Uwielbiam tego człowieka"
            p "A to przypadkiem nie utrudniło nam polowania?"
            kr "No gdzie, patrz! Lecą prosto w moją pułapkę."
            p "Czyli?"
            "Widzisz jak uciekający w panice ludzie wbiegają do sklepu wędkarskiego"
            "Następnie w sklepie zamykają się wszystkie rolety antywłamaniowe"
            kr "Jak szczury w pułapce"
            show gun
            g "Spierdalaj"
            hide gun with dissolve
            p "Dobra, co teraz?"
            kr "Musimy się tam włamać"
            p "Pierdolisz"
            kr "Tylko twoją matkę"
            p "Czyli ta cała akcja była po to żeby zamknąć ludzi w sklepie?"
            kr "No ta, teraz ich uwolnimy i będą robić co im powiemy"
            kr "Tak to działa w brazylii więc tu też powinno"
            p "To jak tam się dostaniemy?"
            if inventory.has_item(Wytrych) == True:
                p "Może tam się włamię wytrychem?"
                $ postacie["Krateus"] += 1
                kr "Dobry pomysł ale nie teraz"
                p "Czemu niby?"
                kr "Niech trochę głodują to będą bardziej skłonni do słuchania"
                p "Jesteś jebnięty"
                kr "Dziękuję"

            elif inventory.has_item(Vranat) == True or inventory.has_item(Vomba) == True or inventory.has_item(Granat) == True:
                p "Mam trochę materiałów wybuchowych"
                kr "Tylko to rzuć a upierdolę Ci ręce"
                p "Daj spokój, to tylko kilka cywili"
                kr "Koło chuja mi to lata, idziemy do domu"

            else:
                show ciphate with dissolve
                p "No nie mam nic przy sobie"
                hide ciphate with dissolve
                kr "No ja też"
                p "To po 10"
                kr "Co?"
                p "Jajco"
                kr "A ci zaraz pierdolne"
                p "To mnie złap"
                "I zacząłeś uciekać w kierunku bazy"

            "Zostawiliście cywili na tymczasową (oby) głodówkę"
            $ stan["Krateus"] = 3 
            $ czas -= 4
            $ postacie["Krateus"] += 1
            jump rozstaje

        elif stan["Krateus"] == 3:
            if dzien > 19:
                kr "Dobra, chyba tyle czasu wystarczy"
                p "No, trochę ich tam trzymaliśmy, myślisz że jeszcze żyją?"
                kr "Jeśli silni zjedli słabych, to raczej tak"
                kr "Jeśli mają moralność to będzie doomstack trupów"
                p "No to lećmy sprawdzić"
                scene fiszop
                show krateus
                kr "No to robimy opening"
                if inventory.has_item("AR"):
                    "Wyjąłeś AR dla bezpieczeństwa"
                kr "Na trzy otwieram drzwi, gotowy?"
                p "Tajest"
                kr "Trzy"
                "Kreteus szybkim ruchem otworzył drzwi"
                "I w środku widzicie trzy osoby"
                kr "FBI NC! Na ziemię skurwysyny"
                "Trzy osoby rzuciły się na was z prowizoryczną bronią"
                if inventory.has_item("AR"):
                    "Szybką serią z AR ich zdjąłeś"
                    $ postacie["Krateus"] += 1

                elif inventory.has_item("Pistolet"):
                    "Udało Ci się zastrzelić jednego ale dostałeś z dzidy"
                    call checkHP(9) from _call_checkHP_13

                else:
                    "Potężna gazrurka trafiła w twoją twarz"
                    call checkHP(16) from _call_checkHP_14

                "Widzisz jak Krateus zajmuje się resztą"
                kr "Waleczne skurwiele"
                kr "Kurwa szkoda, byliby dobrymi wojownikami"
                kr "Chuj tam, za dwa dziki pewnie znajdę nowych"
                p "Co?"
                kr "Co?"
                p "Jakie dziki"
                kr "Nie zadawaj głupich pytań, głośno myślałem"
                p "To co teraz robimy?"
                kr "Wracamy do domu i zacznę knuć znowu"
                $ stan["Krateus"] = 4
                $ czas = 0
                jump rozstaje

            else:
                kr "Daj im głodować jeszcze trochę"

        elif stan["Krateus"] == 4:
            if stan["Laskawca"] < 2:
                kr "Pogadaj z Łaskawcą"
                kr "Jak zrobisz co on chce to wróć"
                jump rozstaje

            else:
                kr "No to dzień dobry"
                show laskawca at left
                pl "Siemaneczko"
                p "Ale bojowa ekipa się zebrała"
                kr "Plan mamy prosty, obecny tu Łaskawca robi Call of Bitches"
                kr "Następnie usypia to co dopadnie, a my skalpujemy"
                pl "Nom, plan w teorii prosty"
                p "To zabieramy się za robotę?"
                kr "Poczekaj chwilę"
                "I pół dnia siedzieliście u krateusa"
                kr "Teraz jest odpowiednia pora"
                pl "Ruszam dzielnie"
                "Kilka minut później"
                $ helper = 10
                if stan["Kalach"] < 4:
                    "Niczym nie zajęty kałach porwał kilka nowych zakonnic"
                    $ helper -= 3

                if stan["Gun"] < 4:
                    "Schizofremia jest zawsze kusząca dla altek"
                    $ helper -= 1 

                if stan["Jhin"] < 4:
                    "Urok Jhina odgonił jedną z babeczek"
                    $ helper -= 2

                if stan["Cypher"] < 4:
                    c "Hi Hi Ha Ha"
                    "I na ten odgłos dwie samice uciekły"
                    $ helper -= 4

                if helper == 10:
                    achieve Alesex

                if helper < 4:
                    kr "Kurwa, te bestie odgoniły kobiety"
                    $ postacie["Krateus"] -= 2
                    $ postacie["Laskawca"] -= 2
                    $ stan["Krateus"] = 5
                    kr "Chuja dało radę zrobić"
                    kr "Dawaj na Kennedy'ego, może się odkujemy"
                
                else:
                    kr "Dobra, trochę się ostało"
                    p "I co z nimi teraz będzie?"
                    kr "Mięso, włosy, organy itp."
                    pl "Panowie zapraszam"
                    scene klinika
                    show laskawca at left
                    show krateus at right
                    p "I co, mam teraz kroić te baby"
                    kr "Jakie kebaby"
                    p "No te tu na stole"
                    pl "No ta, masz pokroić baby"
                    $ czas = 0
                    "Wieczorem"
                    pl "Dawno tyle bab nie kroiłem"
                    kr "Ale jaki pitos będzie potem"
                    pl "A gdzie to niby opchniesz?"
                    kr "Mam swoje źródła"
                    kr "Spokojna twoja rozczochrana"
                    p "To jesteś gotowy na zadanie Kenowe"
                    kr "Kurwa brachu, pewex"
                    kr "Daj tylko znać i się pojawię"
                    achieve Krapp
                    $ stan["Krateus"] = 5
                    $ postacie["Krateus"] += 2
                    $ postacie["Laskawca"] += 2
                    jump rozstaje


    jump rozstaje

label sypialnia:
    scene pokoj
    show screen hud
    call bigunl from _call_bigunl_1
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

        "Wyjebie gówno przez okno":
            jump yeet

        "Czy ja przypadkiem nie dostałem?":
            if HP < MaxHP:
                p "Faktycznie mam tylko [HP] na [MaxHP]."
                p "Pancerz ma [armor] punktów"
                jump sypialnia

            else:
                p "Zdawało mi się."
                jump sypialnia

        "Wyjść" if czas > 0:
            jump rozstaje

#akt 1
label akt1:
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    scene akt1
    $ stan = {"Kalach":0, "Gun":0, "Cypher":0, "Laskawca":0, "Hartmann":0, "Jhin":0, "Visty":0, "Kennedy":0, "Krateus":0}
    $ akt = 1
    $ wojownik = False
    "A więc zostałeś w tej bazie pełnej degeneratów"
    "Wybrałeś życie śmiecia za marne pieniądze"
    "Chujowy wybór, jak mam być szczery, no ale niech zyskam"
    "Miałeś może z pięć minut spokoju, aż Gun nie znalazł roboty"
    scene kuchnia
    show gun
    g "Panowie, robota jest"
    show cypher at left
    c "Płacą dobrze?"
    g "Nie wiem jeszcze"
    c "To nie zawracaj mi dupy"
    hide cypher with dissolve
    "Cypher opuszcza scenę"
    show gun at left with move
    show hartmann at right
    show laskawca
    g "Skoro problem wyszedł, to możemy zacząć rozmowy"
    h "To co to za robota?"
    g "Idziemy, strzelamy, spierdalamy"
    pl "Podoba mi się to"
    g "A ty [player_name]? Piszesz się?"
    $ config.rollback_enabled = False
    menu:
        "Piszę się?"
        "Kurwa no pewex":
            show ciphate with dissolve
            $ postacie["Gun"] += 1
            hide ciphate with dissolve
            g "To mi się podoba"
            $ wojownik = True
            jump akcja

        "Ja wracam, bo się trochę cykam":
            $ postacie["Gun"] -= 1
            $ postacie["Cypher"] += 1
            g "Pizda jesteś nie wojownik"
            $ wojownik = False
            scene dach
            show cypher
            c "Cenisz sobie zysk?"
            c "Może chcesz dołączyć do Diamandhunde?"
            c "Oferujemy sporo korzyści, na twoim miejscu bym dołączył"
            menu:
                "Czy chcesz dołączyć do DH?"
                "W sumie czemu nie" if Frakcja == 0:
                    achieve Damm
                    $ Frakcja = 1
                    $ czlonekFrakcji = True
                    $ postacie["Cypher"] += 3
                    c "Witamy w szeregach, później powiem Ci więcej. Muszę iść trollować Ciper."
                    jump podsumowanie1
                "Podziękuje":
                    c "Pamiętaj, oferta jest ważna do śmierci"
                    jump podsumowanie1

label akcja:
    stop music
    scene combat1
    play music "klepa.ogg" volume 0.2
    show gun at left
    g "Plan jest prosty, strzelamy, lootujemy"
    show laskawca at right
    pl "Nie musisz mnie namawiać"
    hide laskawca with dissolve
    "Łaskawca zaczął eksterminację oponentów"
    hide gun
    $ config.rollback_enabled = False
    menu:
        "A co ty robisz?"
        "Zaczynam strzelać":
            play sound ["Pif.wav","Pif.wav","Pif.wav","hit1.mp3"]
            call checkHP(7) from _call_checkHP
            "Udało Ci się zdjąć jednego ale do Ciebie strzelili"
            $ Fragi += 1
            $ postacie["Gun"] += 1
        "Zbieram co mogę":
            $ inventory.add_item(AR)
            $ edki += 15
            call checkHP(5) from _call_checkHP_1
        "Cykam się trochę":
            "Przeczekałeś część ostrzału"

    "Wrogowie padali jak muchy"
    show laskawca
    pl "JESTEM PIERDOLONYM BOGIEM WOJNY"
    hide laskawca
    "Słyszysz krzyk z daleka"
    h "KTO KURWA SPAWA CIENKĄ BLACHĘ ELEKTRODOWĄ"
    "Seria pocisków rozsmarowała biedne kurwinoxy"
    menu:
        "Masz kolejną szansę się wykazać, co robisz?"
        "ZOSTAJĘ PIERDOLONYM BOGIEM WOJNY":
            play sound ["Pif.wav","Pif.wav","Pif.wav","Pif.wav","Pif.wav"]
            $ Fragi += 3
            call checkHP(10) from _call_checkHP_2
            "I trzech Vistów zostało zdjętych"
            $ postacie["Laskawca"] += 2
        "Zbieram jeszcze więcej":
            $ inventory.add_item(Pistolecik)
            $ inventory.add_item(Granat)
            $ edki += 50
            call checkHP(5) from _call_checkHP_3
        "Czekam aż reszta nabije sobie fragi":
            show ciphate with dissolve
            "Kitrałeś się do końca"
            hide ciphate with dissolve

    show gun
    g "Dobra robota panowie"
    show laskawca at right with moveinleft
    pl "KREW DLA BOGA KRWI"
    g "Ta, pewnie... pora wracać do bazy"
    jump podsumowanie1

label podsumowanie1:
    stop music
    scene kuchnia
    show gun
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    if wojownik == True:
        g "Nie poszło najgorzej, masz zasłużyłeś"
        $ edki += 200
        "Dostałeś 200 edków"

    else:
        g "Szkoda że Cię nie było, zarobiłbyś coś"
        g "Mówiłem, nie gadaj z Cypherem"
        g "Następnym razem postaraj się bardziej"
        $ postacie["Gun"] -= 2

    "Nadszedł czas chwilowego odpoczynku"
    g "Daj mi kilka dni to może znajdę jakąś robotę"
    g "Na piętrze masz pokój, czuj się jak w gościach"
    $ czas = 0
    jump rozstaje


label trader:
    $ czas -= 2
    stop music
    play music "szop.mp3" volume 0.2
    scene szop
    p "A se coś kupię"
    p "Ile mam mamony? [edki] edków, mogło być mniej"
    $ helper = 1
    while helper == 1:
        menu:
            "Szopping tajm"
            "Hazmat" if edki > 999 and inventory.has_item(RadArm) == False and inventory.has_space(Cap) == True:
                $ inventory.add_item(RadArm)
                $ edki -= 1000

            "Tajemniczy energol?" if edki > 999 and inventory.has_item(NRG) == False and inventory.has_space(Cap) == True:
                $ inventory.add_item(NRG)
                $ edki -= 1000

            "Ale fajna Aerka" if edki >= 600 and inventory.has_item(AR) == False and inventory.has_space(Cap) == True:
                $ inventory.add_item(AR)
                $ edki -= 600

            "Bomba dymna" if edki > 199 and inventory.has_item(Smoke) == False and inventory.has_space(Cap) == True and akt > 1:
                $ inventory.add_item(Smoke)
                $ edki -= 200

            "Wytrych? " if edki >= 100 and inventory.has_space(Cap) == True:
                $ inventory.add_item(Wytrych)
                $ edki -= 100

            "Kurwa ser?" if edki >= 50 and inventory.has_space(Cap) == True:
                $ inventory.add_item(Ser)
                $ edki -= 50

            "Na nic więcej mnie nie stać":
                p "Get zakuped"  
                $ helper = 0

    stop music
    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    jump trader


label frogszop:
    stop music
    play music "szop.mp3" volume 0.2
    $ czas -= 1
    scene frogszop
    fse "Dzień dobry"
    $ helper = 1
    while helper == 1:
        menu:
            fse "Co chciałby pan kupić?"
            "Dej mnie hot doga" if (edki > 9 or frogsy > 89) and HP < MaxHP:
                fse "To będzie 10 edków"
                if frogsy > 89:
                    achieve Frg
                    p "Zapłacę frogsami"
                    $ frogsy -= 90

                else:
                    p "Proszę"
                    $ edki -= 10
                    $ frogsy += 40

                "Chwilę poczekałeś i jadło otrzymałeś"
                fse "Smacznego"
                play sound "EAT OR MUNCH.mp3"
                $ HP += 5
                if HP > MaxHP:
                    $ HP = MaxHP

            "Dupnę sobie monsterka" if (edki > 24 or frogsy > 224) and czas < 30:
                fse "To będzie 25 edków"
                if frogsy > 224:
                    achieve Frg
                    p "Zapłace frogsami"
                    $ frogsy -= 225

                else:
                    p "Proszę"
                    $ edki -= 25
                    $ frogsy += 100
                
                "Wypiłeś potwora"
                p "Czuję, że mogę dziś zrobić więcej"
                $ czas += 10


            "Zdrapeczka" if edki > 24:
                $ edki -= 25
                $ frogsy += 100
                fse "25 edków"
                p "Proszę"
                p "Dobra, zobaczymy czy wygrałem"
                if renpy.random.randint(0, 100) == 0:
                    p "O CHUJ WYGRAŁEM"
                    $ edki += 1000
                    p "Prosze pani, chciałbym tę zdrapkę wymienić"
                    fse "Gratulacje"
                    fse "Proszę pańskie 1000 edków"

                else:
                    p "Kurwa, nie siadło"

            "Przewalutowanie" if vdolce > 0:
                fse "Już, oto normalne edki"
                $ edki += (vdolce*50)
                $ vdolce = 0
                p "Dziękuję"

            "Szukacie może pracowników?" if Frakcja == 0 and dzien > 11:
                fse "Mamy jeszcze wolny wakat"
                fse "Byłby pan zainteresowany pracą?"
                menu:
                    "Dołączam do żabki?"
                    "PEWEX":
                        $ Frakcja = 6
                        fse "Witamy na pokładzie"
                        fse "Jestem Kasia btw"
                        $ baba_name = "Kasia"

                    "Podziękuję":
                        fse "Wakat nie będzie wiecznie wolny!"

            "Ja do roboty przyszedłem" if Frakcja == 6 and czas > 0:
                fse "To dawaj za kasę"
                $ edki += czas * 8
                $ czas = 0
                "Przepracowałeś cały dzień"
                $ helper = 0
                
            "To tyle, dziękuję, dowidzenia":
                fse "Dowidzenia, zapraszam ponownie"
                $ helper = 0

    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    jump frogszop


label vradeZewn:
    $ czas -= 3
    scene vshop
    menu:
        v "Co chciałbyś zakupić?"

        "Wymiana edków na vdolce" if edki > 99:
            $ vdolce += 1
            $ edki -= 100

        "Wymiana vdolców na edki" if vdolce > 0:
            $ vdolce -= 1
            $ edki += 100

        "Ale fajna Aerka" if vdolce >= 5 and inventory.has_item(AR) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(AR)
            $ vdolce -= 5
            $ veq += 1
            "Wydałeś 5 vdolcy na AR-kę"

        "Wytrych? " if vdolce >= 2 and inventory.has_item(Wytrych) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(Wytrych)
            $ vdolce -= 2
            $ veq += 1
            "Wydałeś 2 vdolce na Wytrych"

        "Flaszka?" if vdolce >= 1 and inventory.has_item(Flaszka) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(Flaszka)
            $ vdolce -= 1
            $ veq += 1
            "Wydałeś 1 vdolca na Flaszkę"

        "Varmor" if vdolce >= 3 and inventory.has_item(MalyArmor) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(MalyArmor)
            $ armor = 11
            $ vdolce -= 3
            $ veq += 1
            "Wydałeś 3 vdolce na lil varmor"

        "Nie potrzebuję twoich towarów":
            jump rozstaje

    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    jump vradeZewn

label workowiec:
    scene bager
    $ czas -= 2
    menu:
        p "Czy chcę powiększyć wora?"
        "Pewex" if edki > (Cap+1)*100:
            $ edki -= (Cap) * 100
            achieve Mocz
            p "Zwiększaj"
            $ Cap += 1
            if akt == 1:
                jump rozstaje

            elif akt == 2:
                jump opor

        "Lepiej nie":
            show screen map_screen
            window hide
            pause 1
            pause 1
            pause 1
            pause 1
            pause 1
            pause 1
            jump workowiec

label wojsko:
    $ czas -= 5
    scene wojsko
    if wojsko_stan == 0:
        show genken at right
        gk "Witamy w armii młody"
        gk "Jestem Generał Kennedy, przywódca tego pierdolnika"
        if Frakcja == 0 or Frakcja == 3:
            gk "I jesteś tu z woli Guna"

        elif Frakcja == 1:
            gk "Jasna cholera, jesteś od Cyphera"

        gk "To co masz ogarnąć to destrukcja Vist"
        gk "Jakaś kurwa z Arasaki chce przejąć nad nimi kontrolę"
        p "Ależ to skurwysyn musi być"
        gk "To prawda, każdy pracownik korpo to skurwysyn"
        gk "Ale ten skurwysyn, to taki super skurwysyn"
        gk "Będziesz musiał zebrać drużynę"
        gk "I razem wyruszycie pozbyć się kutasa"
        p "Ja pierdolę"
        p "Ty na prawdę wymagasz ode mnie, żebym się dogadał z tymi debilami"
        p "Przecież to jest kurwa niewykonalne"
        gk "Dlatego to zadanie będzie dla ciebie wyzwaniem"
        gk "Jeśli je wykonasz, to dostaniesz potężną wypłatę"
        p "Już trzeci raz słyszę o ogromnej wypłacie"
        p "Opowiedz mi dokładnie, co JA KURWA DOSTANĘ"
        gk "Wypłatę"
        show cypher with moveinleft
        c "Hi Hi ha ha"
        hide cypher with moveoutright
        gk "O nie, ta kreatura się tu materializuje"
        gk "Potem Ci wyjaśnię, teraz muszę się ukryć"
        gk "Pamiętaj, musisz się zaprzyjaźnić z CyberDzbanami"
        show cypher with moveinleft
        c "The Game ©"
        hide cypher with moveoutright
        gk "To jest coraz mocniejsze"
        gk "Znikam"
        hide genken with dissolve
        p "No i zniknął"
        p "Jak zwykle kurwa"
        p "I wyjdzie, że dostanę 7,50 edka"
        p "Nienawidzę NC, Nienawidzę NC"
        $ wojsko_stan = 1
        $ bigquest = 5
        p "No to wracam do bazy"
        jump rozstaje

    elif wojsko_stan > 0:
        "Opowiedziałeś Kenowi o swoim progresie"
        if stan["Laskawca"] == 2:
            "Pochwaliłeś się przyjaźnią z Łaskawcą"
            gk "Czyli Łaskawca jest gotowy Ci pomóc"
            gk "Healer zawsze się przyda"
            $ wojsko_stan += 1
            $ stan["Laskawca"] = 6

        if stan["Gun"] == 5:
            "Pochwaliłeś się przyjaźnią z Gunem"
            gk "Gun chce wykonać zadanie dla mnie"
            gk "Nie wiem czy to dobry znak"
            gk "Kiedyś jak dostał zadanie, to do teraz go nie skończył"
            gk "Na szczęście kapitan Sójeczka był w okolicy"
            gk "Tak im namieszał w papierach, że sami nam pojazd oddali"
            $ wojsko_stan += 1
            $ stan["Gun"] = 6

        if stan["Kalach"] == 5:
            "Pochwaliłeś się przyjaźnią z Kałachem"
            gk "Jeśli Kałach leci z tobą, musisz go pilnować"
            gk "Jeśli znajdę jakiegokolwiek dildosa na terenie akcji"
            gk "To Ciebie złapią konsekwencje"
            $ wojsko_stan += 1
            $ stan["Kalach"] = 6

        if stan["Hartmann"] == 5:
            "Pochwalileś się przyjaźnią z Hatrmannem"
            gk "Twardy zawodnik dołączył do Ciebie?"
            gk "Tylko musisz uważać, jak Gun dostanie auto w ręce"
            gk "Mogą być straty w cywilach"
            $ wojsko_stan += 1
            $ stan["Hartmann"] = 6

        if stan["Jhin"] == 4:
            "Pochwalileś się przyjaźnią z Jhinem"
            gk "Ten Taki idzie z Tobą?"
            gk "Szalone jak sam skurwysyn ale to jego decyzja"
            $ wojsko_stan += 1
            $ stan["Jhin"] = 6

        if stan["Cypher"] == 5 or stan["Cypher"] == 6:
            "Dumnie ogłosiłeś dołączenie Cyphera"
            gk "Dlaczego?"
            $ wojsko_stan += 1
            $ stan["Cypher"] = 9

        if stan["Krateus"] == 5:
            "Pochwaliłeś się przyjaźnią z Krateusem"
            gk "Krateus też tam jest?"
            gk "Powinien wykonywać zadanie bojowe"
            gk "Oj, będę musiał z nim pogadać"
            $ wojsko_stan += 1
            $ stan["Krateus"] += 1


    if wojsko_stan > 4: 
        if wojsko_stan > 7:
            achieve Full
            mg "Gratulacje, zebrałeś całą drużynę"
            mg "Wasze szanse na przetrwanie są zwiększone"

        gk "Dobra robota szczylu."
        gk "Udało Ci się zdobyć przyjaźń z innymi dzbanami"
        menu:
            gk "Jesteście gotowi na tajną misję?"
            "Kurwa no pewex":
                gk "Git"
            
            "Daj mi jeszcze trochę czasu":
                gk "Spoczko"
                jump rozstaje

        gk "Więc lecicie na super tajną misję"
        gk "Siłą przyjaźni musicie wysadzić jedno z vniazd"
        gk "Prowadzą tam badania nad ściśle tajnym projektem Vezuwiusz"
        gk "Niech bóg was przyjmie"
        if inventory.has_item(Pistolecik) == False and  inventory.has_space(Cap) == True:
            gk "Masz przyda Ci się"
            $ inventory.add_item(Pistolecik)
            
        jump wojowezadanie

    jump rozstaje

label wojowezadanie:
    stop music
    play music "CMS.mp3"
    $ helper == 100
    $ config.rollback_enabled = False
    if Frakcja == 0:
        scene vniazdo
        "Poprowadziłeś punków prosto w vniazdo"
        p "Panowie, Kennedy wybrał mnie jako szefa tej operacji, więc proszę słuchajcie się mnie"
        "O dziwo nikt nie miał z tym problemu"
        "Teraz jako szef, czeka Cię wyzwanie kierowania swoją ekipą"
        "Wskaźnik zagrożenia jest na poziomie 100"
        "Jeśli spadnie do 0 to osiągniesz giga sukces"
        "Nie spodziewaj się tego wyniku"
        "To jakie masz możliwości zależy od ludzi w ekipie"
        "I od tego jaki masz sprzęt"
        "Wracając do wyroku śmierci"
        "Macie kilka opcji na wykonanie tej roboty"
        menu:
            "Po Cichu":
                "Brak w tobie cyberowego ducha walki"
                p "Panowie, robimy to tak Cicho jak się tylko da"
                p "I to będzie bardzo trudne"
                p "Trzeba teraz dostać się do środka"
                p "Co my mamy do wyboru"
                menu:
                    "Jak wchodzisz?"
                    "Drzwi główne":
                        "Dostaliście się do środka głównymi drzwiami"
                        "Najgorsze możliwe wejście"
                        "Ale okazało się niestrzeżone"

                    "Okno" if stan["Krateus"] > 5:
                        p "Krateus, wskakuj oknem i nam pomożesz"
                        kr "Tajest kierowniku"
                        kr "Chopaky, to jest schowek na miotły"
                        kr "Wskakujcie, macie tu linę"
                        $ helper -= 15
                        hide krateus
                        "A po nim wskoczyła cała reszta"

                    "Drzwi dla personelu" if inventory.has_item(Wytrych) == True:
                        p "Na szczęście mam wytrych przy sobie"
                        p "Fiku foku picku loku"
                        $ inventory.remove_item(Wytrych)
                        "Zręczne palce koniobijcy pomogły Ci otworzyć drzwi"
                        "Panowie, zapraszam"
                        $ helper -= 20

                    "Wentylacja" if stan["Gun"] > 5:
                        p "Gun, możesz wentować?"
                        show gun
                        g "Dlaczego ja?"
                        p "W kombosach do KTG jesteś w spiskowcach"
                        p "A to jednak jest trochę sus"
                        g "To ma sers"
                        $ helper -= 25
                        hide gun
                        scene agunus
                        g "Kurwa, ciemno tu"
                        g "O, jest chyba wyjście"
                        "Gun skończył wentować"
                        g "Przycisk z napisem tajne vejście"
                        g "A se kliknę"
                        "I dzięki temu, reszta drużyny dostała się do środka"

                scene vards
                "Jesteście przy drzwiach 2"
                "Zbliżając się, usłyszeliście vrażników"
                v "Vrombał bym coś"
                v "Vejm"
                v "Vo voviesz na vot-voga?"
                v "Vybornie"
                p "Trzeba się ich pozbyć"
                p "Tylko jak to zrobię?"
                menu:
                    "Atak frontalny":
                        p "Za hordę"
                        "AAAAAAAA"
                        call checkHP(10) from _call_checkHP_20
                        "Dzielnie szturmowaliście parę Vist"
                        "Niestety jeden z vist miał przy sobie terminal"
                        $ edki = 0
                        "I w taki sposób zabrał Ci wszystkie pieniądze"
                        
                    "Chessy akcja" if inventory.has_item(Ser) == True:
                        p "Żryjcie to kutafony"
                        "Rzuciłeś serem w Visty"
                        $ inventory.remove_item(Ser)
                        v "Ty viekki, akurat byłem głodny"
                        p "Luzik arbuzik, smacznego"
                        v "Dawaj Varek, idziemy na obiad"
                        play sound "EAT OR MUNCH.mp3"
                        $ helper -= 10

                    "Granat" if inventory.has_item(Granat) == True:
                        $ inventory.remove_item(Granat)
                        $ helper -= 15
                        "Poturlałeś granat w kierunku Vist"
                        v "Vo Volera!"
                        v "Darmowy granat"
                        v "Jest mój"
                        v "Nie jest mój"
                        "Dzika bijatyka się zaczęła"
                        "I Visty wybiły się ze sceny"


                    "Kałach, dywersja" if stan["Kalach"] > 5:
                        show kalach
                        k "Hej seksiaki"
                        v "O, siemka Kałach, co tam"
                        k "A vista z hot-dogami przyjechał"
                        v "VO VOLERA"
                        v "VUSZAMY VIELNIE"
                        "I dzielnie vybiegli"
                        $ helper -= 25
                        p "Dobra robota Kałach"
                        k "Wiem"
                        hide kalach

                scene vezuwiusz
                "Przeszliście przez straż"
                "Idziecie dalej przez gniazdo"
                "Dzielnie dostrzegasz znak vaboratorium"
                p "Chopaky, jesteśmy na miejscu"
                p "Pora zrobić rozpierdol"
                menu:
                    "Jak spacyfikuję laba"
                    "Atak frontalny":
                        call checkHP(5) from _call_checkHP_19
                        "Wbiegliście do środka atakując każdego Vistę w okolicy"

                    "Pora na blackout" if stan["Jhin"] > 5:
                        p "Ten taki, odetnij im kable"
                        show jhin
                        j "Spoczko foczko"
                        "Widzisz że Jhin wyjmuję katane"
                        p "Nie tak deklu, prąd cię jebnie"
                        j "Fakt"
                        "Schował kanatę i wyjął broń z ręki"
                        p "NIEEEEEE"
                        "Jhin przeciął kable ostrzem z dłoni"
                        "I tak jak przwidywałeś, jebnął go prąd"
                        j "Oj karamba"
                        p "Jhin, jesteś cały?"
                        j "Powiedz mojej żonie, że jej nie mam"
                        if inventory.has_item(THeal) == True:
                            p "Spokojnie kentaki"
                            "Dałeś Jhinowi Turbo uzdrawiacz"
                            $ inventory.remove_item(THeal)
                            $ postacie["Jhin"] += 3
                            achieve Hero
                            j "Dzięki stary"
                        "Reszta dostała się do środka i po ciemku i cichu wybiła resztę"
                        hide jhin
                        $ helper -= 15

                    "Brazylijska sztuka walki" if stan["Krateus"] > 5:
                        show krateus
                        kr "Ni Chu Ja"
                        kr "Hadong"
                        kr "Boom szakalaka"
                        kr "Walę Vistę prosto w ptaka"
                        play sound "hit1.ogg"
                        "Brazylijska sztuka walki rozgromiła Visty"
                        "Ale sam Krateus też trochę oberwał (głównie od siebie)"
                        hide krateus
                        $ helper -= 10

                    "Łaskawca, anestezja bojowa" if stan["Laskawca"] > 5:
                        show laskawca
                        pl "Się robi"
                        "Łaskawca podszedł pod szyb i dał trochę gazu"
                        v "Vopaki, vide vpać"
                        v "Vamimir"
                        pl "Słodkich snów chuje"
                        p "Jeszcze cukrzycy dostaną"
                        pl "Jakieś minusy?"
                        $ helper -= 25
                        hide laskawca

                "Laboratorium jest wasze"
                "Badając dokumenty odkryłeś vistowy plan"
                p "Oni są tak głupi że ja pierdolę"
                p "Próbowali wrzucić Guna do wulkanu"
                p "I tak chcieli przywołać boga gniewu"
                p "No debile"
                "Po przeszukiwaniu postanowiliście wysadzić laba"
                "Szybki trik i cały lab się wyjebie za pięć minut"
                p "Spierdalamy"
                "Zaczęliście biec do wyjścia"
                "Ale na waszej drodze stanął VPrime"
                scene vinalvoss
                stop music
                play music "bossa.mp3"
                v "Vavava"
                p "Spierdalaj"
                v "NIE"
                p "A powiesz o chuj wam chodzi z tymi klaunami?"
                v "Taki vress vode"
                p "Mogłem się domyślić"
                menu:
                    "Ostatni przeciwnik"
                    "Let mi solo him":
                        v "Oh? You're approaching me? Instead of running away, you're coming right to me?"
                        p "I can't beat the shit out of you without getting closer."
                        v "Oh ho! Then come as close as you like."
                        p "Ora"
                        v "Too slow, too slow! The Vorld is the ultimate Stand."
                        "ora ora ora ora vs vuda vuda vuda vuda"
                        p "It's over VMax. I have a high ground"
                        v "Vurwa"
                        p "GIŃ"
                        play sound "hit.mp3"
                        "Dostałeś srogi wpierdol ale pokonałeś wroga"
                        call checkHP(20) from _call_checkHP_15
                        v "To jeszcze nie jest koniec"
                        p "Panowie wychodzimy"
                        " I w taki sposób wyszliście z vazy"
                        $ helper -= 10
                        jump akt1pods
                    
                    "Pora na spawanie" if stan["Hartmann"] > 5:
                        p "Hartmann, bier migomat"
                        show hartmann
                        h "PORA NA SPAWANIE WORA"
                        v "Nieeeeeeeee"
                        "Szybkim ruchem Hartmann zespawał Vprima"
                        v "Moje kochones"
                        p ":czacha"
                        h ":czacha"
                        p "Panowie wychodzimy"
                        " I w taki sposób wyszliście z vazy"
                        $ helper -= 15
                        hide hartmann
                        jump akt1pods

                    "Góra, prawo, dół dół dół" if stan["Cypher"] > 5:
                        show hellciper
                        p "Cypher, pora na nalot"
                        c "Cypher łan w drodze"
                        v "Co kurwa?"
                        v "Jak ty niby chcesz zrzucić bombę w budynku?"
                        v "Jakby, tu nie ma jak wlecieć"
                        v "A jak spadnie na dach to chuja mi zrobić"
                        v "Kurwa, przecież Cypher stoi obok"
                        v "To nie ma prawa działać"
                        c "To pa ten trick"
                        "Cypher wziął potężnego bucha i nad v prime pojawiła się chmura"
                        v "I to wszystko?"
                        c "Hi Hi Ha Ha"
                        "Z chmury wypadła mała bomba"
                        v "Co do kurwy"
                        "I ta bomba wybombowała vprima"
                        p "Nie wierzę że to mówię ale dobra robota Cypher"
                        c "DH poleca się"
                        p "Panowie wychodzimy"
                        " I w taki sposób wyszliście z vazy"
                        $ helper -= 25
                        hide hellciper
                        jump akt1pods

                    "Zielone światło" if stan["Gun"] > 5:
                        scene idrive
                        play music "idrive.mp3" volume 0.2
                        g "Ja jadę"
                        v "Ale jak, ty nawet nie masz auta"
                        g "Brum Brum"
                        play sound "BOOM.mp3"
                        "No i Vista zrobił boom"
                        p "Jak ty to zrobiłeś? "
                        g "Kupiłem szczurom RC autko"
                        g "I Hartmann podczepił minę p.piech"
                        p "Sprytne"
                        stop music
                        play music "CMS.mp3" volume 0.2
                        $ helper -= 20
                        jump akt1pods

            "Na głośno":
                p "Kurwa chłopaki, nie pierdolimy się w tańcu"
                p "Zapierdalamy na nich"
                "Dzielenie ruszacie szturmować vazę"
                menu:
                    "Jak się teraz dostaniecie do środka?"
                    "Zapukam":
                        p "Puk Puk"
                        v "Vto vam?"
                        p "Dzień dobry. Nazywam się [player_name]. Jestem nowym V"
                        v "O! Klawo! Zapraszamy."
                        "Vista otworzył drzwi"
                        v "Zaraz, zaraz, ja was chyba znam"
                        p "To prawda"
                        "I zastrzeliłeś Vistę"
                        p "Hasta la vista, vista"
                        "Dostaliście się do środka"

                    "Kałach bazooka" if stan["Kalach"] > 5:
                        show kalach at left
                        k "Boom, boom, boom, boom"
                        k "I'm going to Coom"
                        "I Kałach wystrzelił"
                        "Ale rakieta wybuchła fajerwerkami"
                        k "Co jest kurwa"
                        show cypher
                        c "Hi Hi Ha Ha"
                        hide cypher with dissolve
                        p "To co teraz?"
                        k "Chuj"
                        "Kałach podszedł bliżej i kopnął drzwi"
                        k "Tada!"
                        "Możecie teraz wejść"
                        $ helper -= 10

                    "Krateus, Los pollos hermanos" if stan["Krateus"] > 5:
                        show krateus at left
                        kr "Los españoles necesitan ayuda"
                        kr "Cavador, tienes que cavar"
                        kr "Artillero, nos están cubriendo"
                        kr "I teraz atak ostateczny"
                        kr "Ekspansja domeny: KRATA DZIKA"
                        mg "Przyjmuję twoją ofertę"
                        kr "Otwarte"
                        "I drzwi się otworzyły"
                        p "Jak ty to zrobiłeś?"
                        kr "Battle pass słonko"
                        $ helper -= 25

                    "Gun, miej fun" if stan["Gun"] > 5:
                        show gun at left
                        g "Tajest"
                        g "Ale zaskoczę was wszystkich, tym razem nie prowadzę"
                        p "Faktycznie plottwist"
                        g "Spokojnie [player_name], Mączysław prowadzi"
                        p "Co kurwa?"
                        r "Skłik Skłik"
                        "Widzisz jak rozpędzony tir jedzie prosto w drzwi"
                        g "Pamiętaj o hamulcach"
                        r "Skłik?"
                        g "NIEEEEE MĄCZYSŁAW!!!"
                        "Tir jebnął"
                        g "MÓJ AGENT"
                        p "Nie martw się Gun, pewnie trafił do ratowego nieba"
                        g "Gówno, on był diabłem wcielonym"
                        r "Skłik Skłik!"
                        g "O CHOLERA, ON ŻYJE"
                        g "RATTER POTTER"
                        "Ominąłeś chwilę czułości i poszedłeś dalej"
                        $ helper -= 20 

                "Jesteście w środku"
                scene vrogi
                "Biegnie na was z dziesięć rozsierdzonych vist"
                menu:
                    "Co teraz?"
                    "Pif Paf słoneczko":
                        "Rozpocząłęś strzelanie, a drużyna strzelała wraz z tobą."
                        call checkHP(15) from _call_checkHP_22
                        "Troszeczkę oberwałeś ale udało Ci się zostać bogiem gniewu i wojny"
                        "Możesz dzielnie iść dalej"
                        "Ale nie możesz zapomnieć o lootowaniu"
                        $ edki += 150
                        "Trochę mamony się znalazło"
                        $ inventory.add_item(AR)
                        $ inventory.add_item(Vron)
                        $ vdolce += 3
                        "I trochę Vidolcy"

                    "Pora Geentować" if stan["Laskawca"] > 5:
                        show laskawca at left
                        pl "Się robi"
                        "Łaskawca zaczął strzelać na oślep"
                        "Trafił wszystkie 11 strzałów"
                        "Spytasz się, jak 11 strzałów na 10 vist"
                        "Odpowiedź jest bardzo prosta"
                        "Jeśli kiedykolwiek będzie kombat w którym Gun nie dostanie rykoszetu"
                        "To się chyba posram."
                        g "Aua ):"
                        $ helper -= 15

                    "Hartmann! Spaw bojowy" if stan["Hartmann"] > 5:
                        show hartmann at left
                        h "No to spawamy"
                        h "Ja nie wiem co to jest rzecz niemożliwa"
                        h "Fach w ręku, tak bywa"
                        h "Czasem beton, cementem się spawa"
                        h "Czasem, Visty się doprawia"
                        "Vięso Vist topiło się pod wpływem spawarki do ludzi"
                        "Czujesz się strasznie,jesteś niczym więcej niżeli potworem"
                        "Kreatura twojego rodzaju nie powinna mieć kontaktu z ludźmi"
                        "Szczęśliwie to jest tylko gra i nie będziesz chciał powtarzać tego irl?"
                        "Prawda"
                        menu:
                            "Prawda?"
                            "Prawda":
                                "To dobrze"
                                "Wiedźmin 3: kamień z serca"
                                $ helper -= 10
                            
                            "Fałsz":
                                "Ty chory pojebie"
                                $ renpy.quit()

                    "Czy moc pay to play też na mnie działa?" if edki > 199:
                        achieve Bug
                        mg "TAK"
                        p "O jasna dupa, to Wielki Dzik"
                        mg "To prawda, jestem więc myślę"
                        p "Czy możesz mi pomóc w walce z Vistami?"
                        mg "Mogę zrobić wszystko ale ile jesteś gotowy za to zapłacić?"
                        menu:
                            "Ilę chcę dać?"
                            "Może dziczeg?" if inventory.has_item(NRG) == True:
                                mg "Oj kolego, kupiłeś mnie tym jak paczkę żelków"
                                mg "Oto moje błogosławieństwo"
                                p "Dziękuję wielki dziku"
                                $ helper -= 25

                            "Masz tu 200 edków i spierdalaj":
                                mg "Przyjmuję tę ofertę"
                                p "Fr fr?"
                                mg "Tak"
                                mg "Vistus znikus"
                                "I tyle było z Vist"
                                p "Dziękuję wielki dziku"
                                "Ale dzika już tu nie było"
                                $ helper -= 25

                            "Dusza Kałacha":
                                mg "Ambitnie"
                                mg "Przyjmuję tę ofertę"
                                show kalach at right
                                k "Co kurwa?"
                                mg "bywaj Kałachu"
                                k "KURWAAAAAAAAAAAAAAAAAAAAAAAA"
                                hide kalach with dissolve
                                $ stan["Kalach"] = -1
                                $ postacie["Kalach"] = -9999
                                mg "Paskudny w smaku"
                                "Wielki dzik potężnym beknięciem wystrzelił Visty poza czwartą ścianę"
                                p "Dziękuję wielki dziku"
                                "Ale dzika już tu nie było"
                                achieve Ocult
                                $ helper -= 15
                            
                            "Jednak nie, spierdalaj":
                                mg "Teraz mnie wkurwiłeś"
                                p "O nie, tylko nie to, JESTEŚ TYLKO WYTWOREM MOJEJ WYOBRAŹNI"
                                mg "Kłamstwo"
                                scene vibechec
                                play sound "skokostrach.mp3"
                                $ MainMenu(confirm=False)()

                "Idąc dalej widzisz laboratorium"
                scene vab
                "Visty planują zbudować wielki wulkan"
                "Masz rację, pojebało ich"
                "Ich głównymi składnikami są ocet i soda kuchenna"
                "Oznacza to zagrożenie poziomu Demon"
                "Całe NC może zostać zalane wulkanową wydzieliną"
                p "Pora ich powstrzymać"
                p "Hujsaria"
                menu:
                    "Wybierz styl dewastacji"
                    "Bombka" if inventory.has_item(Granat):
                        p "Przeciwpiechotny granat sromotny!"
                        p "A teraz. SPIERDALAMY!"
                        play sound "BOOM.mp3"
                        "Granat wybuchając wymieszał składniki granatu"
                        "Ta bojowa mieszanka zaczęła reagować"
                        "Nie minęła chwila jak to gówno zaczęło wypełniać vazę"
                        p "Szybciej panowie, szybciej!"
                        "Resztkami sił udało wam się wybiec z placówki"
                        $ helper -= 25
                    
                    "Ocet jest smaczny, wypiję":
                        show ciphate with dissolve
                        mg "Obrzydzasz mnie"
                        hide ciphate with dissolve
                        "Wypiłeś cały ocet jaki mieli"
                        "Dzięki twojej brawurze visty poniosły straty finansowe"
                        "Całe 4,50 w plecy"
                        play sound "BURP.mp3"
                        p "To chyba tyle"
                        p "Misja wykonana"
                        p "Możemy wychodzić"
                        "I spokojnym krokiem wyszliście z pomieszczenia"
                        achieve Dis
                        $ helper -= 10

                    "Łaskawca, obczaj ten proszek" if stan["Laskawca"] > 5:
                        show laskawca at left
                        pl "Wydaje mi się że to jest kreda"
                        p "Jak kurwa kreda?"
                        pl "No normalnie"
                        p "A wulkan nie powinien działać z sodą?"
                        pl "Powinien ale to jest Vista dynamicks"
                        p "No dobra, punkt dla Ciebie"
                        p "To wychodzi na to, że żadnego zagrożenia nie ma"
                        p "Spermastycznie. Wychodzimy!"
                        "I spokojnym krokiem wyszliście z pomieszczenia"
                        $ helper -= 15

                    "Zrobię delikatny trolaż" if inventory.has_item(Kokos):
                        p "Mam taki śmieszny pomysł"
                        "Podszedłeś do stołu i zamieniłeś sodę na koks"
                        p "Co prawda wychodzę przez to na minus"
                        p "Ale będzie śmiesznie jak im to nie zadziała"
                        "Po delikatnym sabotażu wyszliście z vazy"
                        $ helper -= 20

                p "Kurwa panowie, to było zajebiście łatwe"
                v "Vie Vwal vnia vprzed vachodem vłońca"
                p "Co kurwa"
                scene vinalvoss
                stop music
                play music "bossa.mp3"
                v "Vestem V-Max"
                v "Vopowa vakość V"
                p "Oj nie zesraj się"
                v "Va vóźno"
                "Widzisz jak V-Max się powiększa"
                p "No tak, chuj mi w dupę"
                v "Va Va Va"
                v "Vykuj vię va vmierć"
                p "No to pvp"
                menu:
                    "No to jak cię zabiję?"
                    "Stary dobry pistolet" if inventory.has_item(Pistolecik):
                        p "Giń Visto"
                        "Wystrzeliłeś z pistoletu ale vista podszedł do Ciebie bliżej"
                        v "V vasz"
                        call checkHP(19) from _call_checkHP_16
                        p "Kurwa bolało"
                        v "V veraz vrugi vtak"
                        p "Ej kurwa, to jest nie fair"
                        p "Musisz poczekać na swoją turę"
                        v "V viździe vo vam"
                        call checkHP(2) from _call_checkHP_17
                        "Potężny atak Visty tylko cię drasnął"
                        p "Ja też"
                        play sound "Paf.mp3"
                        v "Vkurwysyn"
                        p "Spoczywaj w koszu v"
                        p "Misja ukończona"
                        $ helper -= 25
                        jump akt1pods
                        
                    "Pora na kręcienie wora" if stan["Krateus"] > 5:
                        show krateus
                        kr "Chodź tu kurewko"
                        v "Vde"
                        kr "Zostaniesz świadkiem brazylijskich eggzekucji"
                        p "W sensie?"
                        v "Vlus veden"
                        kr "No bo chodzi o to, że w brazyli jest dużo eunuchów"
                        kr "Bo tam terroryści strzelali w jaja"
                        p "To dobrego cela mają"
                        kr "Właśnie nie, oni celują w głowę"
                        kr "Ale tam jest ciężka amunicja"
                        p "Ale głupota"
                        kr "No. Dlatego ja polegam na pięściach"
                        v "Vo vo vo ven ved-valk?"
                        kr "Dla jajec"
                        v "V vensie"
                        "Przez całą pogadankę Kreteus zbliżał się do V-Maxa"
                        kr "Egg stiler"
                        v "Vvaaaaaaaaaa"
                        kr "Turbo kręcenie wora!"
                        kr "I teraz finiszer, cios prosto w prostatę"
                        play sound "Bonk.mp3"
                        scene black
                        "Ze względu na brutalną naturę tej sceny zastąpiłem ją opisem jajec"
                        "Wielkie i czerwone jak pomidory"
                        "Dziękuję za uwagę"
                        show krateus
                        kr "Kurwa, chyba przesadziłem"
                        p "Chłopie, tortury Trewora były bardziej ludzkie"
                        kr "Serio"
                        p "No, chodźmy stąd, muszę chyba iść na terapię"
                        kr "No sorson, ale jak to pisze jest miesiąc geja, przez to nie mam hamulców"
                        $ helper -= 10
                        jump akt1pods

                    "Volololo" if stan["Kalach"] > 5:
                        k "Niech będą pochwalone uda."
                        k "I jak powiedział kiedyś prorok:"
                        k "„Błogosławione uda, które nie postępują w radzie bezbożnych, ani nie stoją na drodze bonera,"
                        k "ani nie siedzą na tronie simpów. Ale jego upodobanie jest w prawie THICC Ud!"
                        v "Vo vy vierdolisz?"
                        k "Twoją matkę"
                        v "Vooooo"
                        v "Vylko vie voją vamusie"
                        v "Varża"
                        k "Vistolo volololo"
                        v "Vo vaj vad"
                        "Takim dziwnym sposobem V-Max dołączył do drużyny"
                        v "Vitam vanowie"
                        v "Vychodzimy?"
                        p "Wychodzimy"
                        "Wychodzicie z vazy"
                        v "Vo vo vak vikło?"
                        p "VMax nieee"
                        "I Vistę vysadziło"
                        "Vista opuszcza drużynę"
                        $ helper -= 15
                        jump akt1pods
                        


    elif Frakcja == 1:
        show cypher
        c "Hihi ha ha"
        c "Pozwól młody że ja zajmę się dowodzeniem"
        p "No spoko, szefie"
        c "Szybko się uczysz, będą z Ciebie psy"
        c "Diamentowe takie"
        scene cypherkopter
        play sound "heli.mp3"
        "Pyr pyr pyr"
        p "Gdzie my lecimy?"
        c "To jest ważna misja"
        c "Lecimy do żabki"
        stop sound
        scene frogszop
        stop music
        play music "chill.mp3"
        show cypher at right
        c "Dzień dobry szanowny pracowniku tego sklepi"
        fse "Dzień dobry? Pomóc w czymś?"
        c "Tak młody, potrzebuję knura, najlepiej z dwa"
        fse "W sensie, że dzika, tego energetyka?"
        c "Czytasz mi w myślach brachu"
        fse "To są one w lodówce, tam"
        c "Wielkie dzięki szanowny kawalerze"
        hide cypher
        p "Przepraszam za niego, Szef nie wierzy w kobiety"
        fse "To i tak nie jest najdziwniejszy klient"
        p "Bywali gorsi?"
        fse "Bywali tacy co chcieli hot-doga dwie minuty przed zamknięciem"
        fse "Są mochery płacące rachunki"
        fse "Są żule i w ogóle"
        fse "Dramat wielki"
        p "Faktycznie brzmi strasznie"
        fse "No. Cieszę się że mam tu ochronę"
        fse "Jest dzielny Kacperek, siedzi tam z tyłu"
        fse "Cały dzień obstawia mecze ale jak jest potrzeba to przychodzi"
        c "Szajse ale tu jest duży wybór"
        c "Ponętne towary, chciałbym nabyć je wszystkie" 
        fse "Tylko proszę tam nic nie rozwalić!"
        c "Spokojnie młody, jestem ostrożny"
        p "Nie, on nie jest ostrożny"
        fse "Właśnie widzę"
        show cypher at right
        c "Dobra, mam wszystko"
        fse "No dobrze, to będzie razem 40 edków"
        c "Karamba drogo"
        "Cypher wyjął cygaro i je zapalił"
        fse "Proszę pana, tu nie wolno palić"
        c "To pa ten trick"
        "Cypher wziął giga bucha i zadymił cały sklep"
        hide cypher with dissolve
        fse "OCHRONA"
        p "Nie będzie potrzebna, ja zapłacę"
        $ edki -= 40
        fse "Macie kurwa szczęście, grubcio zaczął już wstawać"
        p "Przepraszam za kłopot"
        "Wróciłeś do DH koptera"
        stop music
        scene cypherkopter
        play sound "heli.mp3"
        p "Co to kurwa miało być"
        c "Portfela zapomniałem ):"
        p "Nie mogłeś powiedzieć?"
        c "Honor mi zabrania"
        p "Powiedz mi że masz to co chciałeś"
        c "Nie"
        p "TO CO TY KURWA KUPIŁEŚ?"
        c "Panini"
        play sound "EAT OR MUNCH.mp3"
        c "Całkiem smaczne"
        p "Popierdoli mnie"
        c "Cichaj tam, najedzony punk to gotowy punk"
        p "To mogłeś coś mi kupić"
        c "Kupiłem ale zjadłem"
        p "Niby kiedy?"
        c "Jak rozmawiałeś z typem"
        p "Szef roku kurwa jego mać"
        c "A dziękuję"
        "Resztę drogi lecieliście w ciszy"
        c "To to jest ta cała vaza?"
        p "Nie wiem, ty nastawiłeś nawigację"
        c "No to mamy czeski remis"
        c "Chuj, Młynarczyk! Pora na bombę!"
        p "Na randomowy budynek chcesz zrzucić bombę?"
        c "Jeszcze jak"
        "Bomba spadła, niestety nie trafiła"
        c "To mi się podoba, kolejny sukces"
        p "Ale ty nie trafiłeś"
        c "To był zrzut ostrzegawczy"
        p "Masz więcej bomb?"
        c "Nie"
        p "To co teraz robimy?"
        c "Wchodzimy"
        play music "CMS.mp3"
        p "W sensie?"
        "Ciper kopter zaczął lecieć prosto w budynek"
        stop sound
        play sound "BOOM.mp3"
        scene black
        c "Kolejne udane lądowanie (2 martwych, 14 rannych)"
        scene wonsuwiusz
        show cypher
        c "Proszę proszę, tożto laboratorium"
        c "Sprawdźmy to"
        p "Dobrze Cypher"
        c "Kurwa, oczekiwałem jakiegoś entuzjazmu"
        c "Dobra jebać. Dawaj do środka"
        "Weszliście do środka"
        c "CO TO KURWA JEST"
        p "W sensie?"
        c "CZY TY TEGO KURWA NIE WIDZISZ?"
        c "TE SKURWYSYNY DOMALOWAŁY MI WĄSY"
        p "Zabawne"
        c "A CI PIERDOLNE"
        c "TO JEST ATAK NA MÓJ WIZERUNEK"
        c "PRZYSTOJNEGO PATRIOTY"
        c "I WYCHODZI JAKIŚ CHUJ Z WĄSEM"
        c "ABSOLUTNIE NIEWYBACZALNE"
        p "Spokojnie"
        c "JAK JA MAM BYĆ KURWA SPOKOJNY?"
        p "O patrz"
        "Podszedłeś do plakatu i oderwałeś wąs"
        scene vezuwiusz
        show cypher
        c "No dobra, uspokoiłem się"
        p "Serio?"
        c "NIE KURWA. JEDYNYM WEZUWIUSZEM TU JESTEM JA"
        c "ROZPIERDOLĘ ICH"
        hide cypher
        "Rozsierdzony wyszedł z labu"
        "I po chwili zawył alarm"
        play sound "alarm.ogg"
        p "Pojebie mnie"
        p "Ale dobra, jestem tu sam, muszę skończyć misję"
        if inventory.has_item(Granat):
            p "Siepię granatem"
            "Granat poleciał"
            p "A ja spierdalam"

        elif inventory.has_item(Vomba):
            p "Ty kurwa, ja mam Vombe"
            p "Rozpierdolę ich ich własną bronią"
            "Bomb has been planted"
            p "Pora wiać"

        else:
            p "Jasny chuj, nic nie mam"
            p "Proces autodestrukcji, Visty muszą to mieć"
            p "A ten wielki przycisk nie klikać chyba będzie od tego"
            p "I tak nie mam innego wyjścia"
            "Nacisnąłeś przycisk i zacząłeś uciekać"
            "Niestety Visty zaczęły strzelać"
            call checkHP(15) from _call_checkHP_18

        p "Jasna dupa, zaraz tu umrę"
        "Vistowa grupa bojowa jest tuż za tobą"
        p "KURWA CYPHER"
        show cypher at bounce
        c "Jestem"
        p "Co!"
        c "Pa na to"
        "Cypher zaczął strzelać w kierunku Vist"
        "Cały magazynek wystrzelił"
        "Niestety miał tylko 4 pociski"
        p "Serio kurwa?"
        c "Sorka, kontrola rodzicielska od Ocelota"
        c "Ale mam jeszcze granatnik"
        "Z ręki Cyphera wysuwa się granatnik"
        c "Ciekawe czy działa"
        "Po strzale, z granatnika leci strumień ognia"
        c "Ło kurwa"
        p "Niezły ten granatnik"
        c "Customowy"
        "Okazało się, że Visty są słabe na ogień"
        c "Przed Cypherem udeż czołem, Cypher górą, chociaż dołem"
        p "A to co kurwa jest"
        c "A se wymyśliłem, śmiesznie brzmi"
        p "Cypher, jesteśmy we wrogiej bazie"
        c "No i?"
        p "Możemy zaraz umrzeć"
        c "Ja nie. Ja mam plot armor"
        p "Aha 66"
        c "Koniec smęcenia, wychodzimy"
        p "I teraz nagle chcesz wychodzić?"
        c "Nom, nowy helikopter jest"
        p "Jak to? Przecież zawsze miałeś tylko jeden"
        c "Magia dzika młody"
        p "Nic już nie rozumiem"
        c "Same"
        "Skończyliście rozmawiać i wyszliście z laba"
        "Ale na waszej drodze stanął V-Max"
        scene vinalvoss
        stop music
        play music "bossa.mp3"
        v "Vrrr"
        c "Spierdalaj ziomo, śpieszy nam się"
        v "Vozjebaliście vi vazę"
        v "Vniszczyliście vasze vadania"
        v "Vrujnowaliście vój vom"
        v "V vabiliście voich vrzyjaciół"
        v "Vlaczego viałbym Vię vie vabić v vej vwili?"
        c "Bo ja będę pierwszy"
        hide cypher
        show hellciper
        c "Góra, prawo, dół, dół, dół"
        v "Vo?"
        c "Półtonowa bomba Młynarczykowa"
        "Precyzyjnie udeżyła w Vistę"
        p "Kurwa Cypher, od kiedy masz takie skile?"
        c "Od zawsze w sumie"
        p "To czemu tego wcześniej nie wezwałeś?"
        c "Nie byłoby takich emocji"
        c "Mogliśmy sobie jak rodzinka postrzelać"
        p "Ja prawie umarłem"
        c "Ale nie umarłeś"
        c "I to się liczy"
        c "Zaczynam cię lubić [player_name]"
        hide hellciper
        show cypher
        $ postacie["Cypher"] += 3
        p "Wracajmy już do domu"
        show ciphate
        c "Tak wcześnie?"
        hide ciphate
        p "No zrobiliśmy to co mieliśmy"
        c "Nudziaż"
        c "Jednak mi się nie podobasz"
        c "Wracasz z buta"
        c "Ja lecę do żabki"
        c "Jak to mówimy w niemczech, Adios"
        "I Cypher odleciał"
        p "Adios jest po Hiszpańsku"
        jump akt1pods

    elif Frakcja == 3:
        p "Dobra kurwa, jestem Vista"
        p "Nie mogę pozwolić aby nasze tajne projekty zostały zniszczone"
        p "Ale z drugiej strony"
        p "Nikt mi za obronę nie płaci"
        p "Co powinienem zrobić?"
        menu:
            "Pozostań V":
                p "Dobra kurwa, co ja teraz zrobię"
                p "Zawsze jest opcja kulki w łep"
                p "Ale to zostawię sobię na potem"
                p "Wiem kurwa!"
                p "Zadzwonię do Vistów i powiem im żeby spierdalali"
                p "Następnie ściągniemy tam VMaxów"
                p "Jak oni tam wejdom to sie zestają"
                p "Hihihaha"
                "Dzwonisz do Vist"
                v "Halo"
                p "Za halo w morde walo"
                v "Vrzepraszam"
                p "Vo v vit"
                "Opowiedziałeś V swój plan"
                v "Vurwa vądry vesteś"
                p "Viem"
                v "Vykonajmy vo"
                "I zaczęliście wykonywać swój genitalny plan"
                scene vniazdo
                show kalach at right
                k "Kurwa, pusto tu"
                show laskawca at left
                pl "Kurde blaszka masz rację"
                k "Ja zawsze mam rację"
                pl "Dobra spokojnie, wchodzimy"
                pl "Ciekawe czemu [player_name] nie jest z nami"
                p "Oj zaraz się dowiesz"
                scene vaxy
                v "Viespovianka"
                "Słyszałeś bardzo brutalne dźwięki walki"
                p "Słodkich snów chuje"
                scene black
                "Chillowałeś sobie w spokoju, do pewnego momentu"
                show kalach at right
                show laskawca at left
                pl "Pobudka słoneczko"
                p "Vo vest vurwa"
                k "Sprzedałeś nas kurwisynu"
                p "Vo? Va vigdy!"
                pl "Słyszymy jak mówisz, sorki stary"
                p "Vie, vanowie, va vie vhciałem"
                k "Koło chuja mi to lata"
                k "Wypierdalasz na tamagoczi"
                "Dostałeś taktycznym paralizatorem"
                k "Idziemy do bazy, czeka Ciebie przesłuchanie"
                scene bev
                achieve Tam
                "GG byczku"
                $ MainMenu(confirm=False)()


            "Wróć do normalności":
                p "Koniec z Vistami"
                p "SV-vists: off"
                $ Frakcja = 0
                jump wojowezadanie


    elif Frakcja == 4:
        scene vniazdo
        show kalach
        k "Dobra, ja szefuje"
        p "Dobrze Kałach"
        k "Plan jest prostrzy niż budowa uda"
        k "Robimy krucjatę"
        p "Nic mi to nie mówi"
        k "Bo w dupie byłeś i gówno widziałeś"
        k "Krok 1: piszę posta o wojnie"
        k "Krok 2: wyznawcy się pojawiają"
        k "Krok 3: ???"
        k "Krok 4: Profit"
        p "Czemu nie znasz kroku trzeciego?"
        k "Ja wtedy chleję"
        p "I to jest cały twój plan, wezwać ludzi niech to zrobią za Ciebie?"
        k "Ta, to tylko Visty, nie chce mi się marnować ammo"
        k "Plus, Vista jest śmieszny"
        p "Jakim cudem ty jesteś jeszcze głową tego kościoła?"
        k "Niebotyczna charyzma"
        k "Inteligencja Ejnsztajna"
        k "I wątroba z tytanu"
        p "Tylko tyle wystarczy?"
        k "Jakie kurwa tylko tyle? Chopie, to jest w chuj pracy"
        k "Raz na dwa dni muszę wrzucać zdjęcie na stronę"
        k "Skurwysyńsko męcząca praca"
        p "Się znalazł influenser po chuju"
        k "TO PATRZ I SIĘ KURWA UCZ"
        "Kałach sam poszedł prosto do gniazda"
        p "Popierdoliło go"
        p "Albo promile nie są już procentami"
        "Słyszysz tonę strzałów z vniazda"
        p "Zobaczę jak mu idzie, jeśli zdechł to free itemy"
        scene vniazdo
        p "Jasna dupa, jaka rzeź"
        "A Kałach cały czas strzela"
        p "Co on, w boga wojny się zmienił?"
        k "A żebyś kurwa wiedział"
        show kalach
        k "Jak jestem wkurwiony"
        k "To nie troluje i napierdalam"
        p "No to dobrze Ci idzie"
        k "Spokojnie, ja dopiero się rozkręcam"
        scene vinalvoss
        stop music
        play music "bossa.mp3"
        show kalach at left
        k "Ło kurwa, VMax się pojawił"
        v "Vrrrr"
        k "[player_name] zajmiesz się nim?"
        p "Popierdoliło Cię, jak ja mam chujowe staty"
        k "No to patrz na to"
        scene stand
        k "W imię ojca, i syna i uda wielkiego"
        k "Niech wpierdol dosięgnie jego"
        v "Vo Vhuj Vi vodzi?"
        k "Specjalny atak Alfonsowy"
        k "Pora na udowy atak krzyżowy"
        v "Vo vie"
        "I VMax dostał wpierdol"
        p "Cholipka Kałach"
        k "Widzisz? Tak się kończy jak mnie wkurwisz"
        p "No dobra, przepraszam"
        k "A spierdalaj"
        p "Aha 66"
        "I Kałach poszedł sobie w pizdu"
        jump akt1pods

    elif Frakcja == 6:
        scene frogszop
        fse "Siema [player_name], mam wiadomość od szefa"
        p "O kierwa, co on takiego chce?"
        fse "Powiedział, że jak pójdziesz na tą robotę od wojska to Cie wyjebie z roboty"
        p "Pojebało go"
        fse "Dokładnie to samo mu powiedziałam"
        fse "I co masz teraz w planach"
        menu:
            "Co ja teraz zrobię?"
            "Żegnaj żabko":
                p "Odchodzę, to jednak nie dla mnie"
                fse "Tylko nie daj się zabić"
                p "Pa teraz"
                $ Frakcja = 0
                jump wojowezadanie

            "Zapłacę mu za czas mojej nieobacności" if edki > 1999:
                fse "Bardzo to ambitne z twojej strony, raczej to mu się spodoba"
                $ edki -= 2000
                p "Oto moje pieniądze, bywaj natenczas"
                fse "Żegnaj, adios"
                jump wojowezadanie

            "Może uciekniemy stąd razem?":
                fse "OMG anon, myślałam o tym odkąd Cię zobaczyłam"
                p "No to klawo, spierdalaj"
                scene bew
                achieve Crg
                "CRINGE DETEKTED"
                $ MainMenu(confirm=False)()

    return

label akt1pods:
    if helper == 0:
        achieve Musk
    stop music
    scene black
    play music "final.ogg" volume 0.2
    mg "No to zobaczmy jak Ci poszło"
    mg "Ło karamba, mogło być lepiej"
    mg "Wracaliście z misji i usłyszeliście strzał ze snajperki"
    mg "Jak mogłeś się spodziewać, to ty dostałeś"
    mg "Drużyna zrobiła to czego też się spodziewałeś"
    mg "Zostawili Cię"
    mg "Powoli się wykrwawiałeś na pustyni"
    p "Kurwa, chyba tu umrę"
    p "Powiedz mojej żonie, że jej nie mam"
    p "Karamba, całe życie przeleciało mi przed oczami"
    p "Chyba za dużo grałem na kompie"
    "Podszedł do Ciebie jakiś mężczyzna ubrany na czarno"
    sb "A kogo my tu mamy [player_name] jak na talerzu"
    sb "To nie jest pora jeszcze umierać mam co do Ciebie plany"
    achieve GG1
    jump a2intro

label amongthev:
    stop music fadeout 1.0
    scene black
    if Frakcja != 1:
        p "Wysłali mnie prosto do wypizdowa"
        p "Nie dali jakichkolwiek wytycznych"
        p "Wiem że mam wykraść coś z archiw"
        p "Przyjaciele po chuju ale chuj, podobno dostanę 2k edków"
    
    elif Frakcja == 1:
        scene dach
        show cypher
        c "No to młody, robota jest Fun pewnie Ci już powiedział ale tak dla przypomnienia"
        c "Visty to debile cienkie pizdeczki"
        c "Musisz zabrać im dokumenty z archiw, dasz sobie radę ale dla pewności"
        if inventory.has_item(AR) == True and inventory.has_space(Cap) == True:
            c "Widzę że jakąś broń już masz, to masz ode mnie inny gadżet"
            play sound "THROWING.mp3"
            $ inventory.add_item(THeal)
            c "Zajebałem Łaskawcy"
            c "Tylko nie zjedz od razu"

        else: 
            c "Dostaniesz ode mnie śmieszną zabaweczkę"
            play sound "THROWING.mp3"
            $ inventory.add_item(AR)
            c "Zajebałem Kałachowi"
            c "W sensie"
            c "Wyrzucał go do śmieci a 500 edków piechotą nie chodzi"

    scene vland
    play music "dickdisco.mp3" volume 0.1
    show vista
    $ config.rollback_enabled = False
    v "Vitam v vlubie"
    v "Vestem Viesiek vędę vwoim vrzewodnikiem"
    v "Vprowadzę Vię vo vokolicy"
    show vechnik
    v "Vutaj vamy vechnika vie vrzeszkadzaj vu vepiej"
    v "Jak go wkurwisz, to Ci jeszcze Vpierdoli"
    hide vechnik
    v "Vobra, przejdź się po okolicy, poszukaj dla siebie roboty"
    v "Vajo"
    $ bigquest = 1
    hide vista
    jump vtimefri

# VISTY
# deklaracje co do V
default vechnik_stage = 0
default voktor_stage = 0
default varchiva_stage = 0
default valki = 5

label vtimefri:
scene vland
menu:
    "Gdzie chcesz iść?"

    "A obczaję vechnika" if vechnik_stage != 7:
        jump vechnik_wst

    "Voktor nie brzmi źle" if voktor_stage != 7:
        jump voktor_wst

    "Może po prostu zakradnę się do archiwów?":
        jump varchiwa

    "Zostanę vojownikiem":
        jump varena

    "Vmiana vrofeum?":
        jump vrade

    "Zdrzemnę się trochę":
        if HP < MaxHP:
            $ dzien += 1
            $ HP += 2
            p "Kilka ran mi się zasklepiło"
            $ umieram = 0
            if HP > MaxHP:
                $ HP = MaxHP
        if vrrr < 4:
            $ valki = 5

        jump vtimefri

    "A poczytam sobie dokumenty Vist" if bigquest == 2:
        jump vokum

    "Vpierdalam od pojebów" if bigquest == 2:
        jump amongthevpods

label vechnik_wst:
    scene vechnik
    if vechnik_stage == 0:
        v "Vitam, jestem vechnikiem. Vogę Ci zaoferować potężne vposażenie."
        v "Ale oczyViście, jeśli vasz odpowiednią ilość Vdolców."
        $ vechnik_stage = 1
        menu:
            "Zdobądź potężne Vposażenie"

            "Będę przyszłym Vogiem Vojny" if vdolce == 1:
                $ veq += 2
                v "Volecam się na vrzyszłość"
                $ vron = 1
                jump vtimefri

            "Kurde balans, nie posiadam kapitału":
                v "Vbacz, młody. Nie dostaniesz vorzyczki! Vróc później kiedy będziesz... MMMMMMM... VOGATRZY!"
                jump vtimefri



    if vechnik_stage == 1:
        v "Vitam znowu"
        if vron < 1:
            v "Chcesz vupić vrońkę?"
            menu:
                "Zdobądź potężne Vposażenie"

                "Będę przyszłym Vogiem Vojny" if vdolce >= 1:
                    $ veq += 2
                    $ vdolce -= 1
                    $ vron = 1
                    $ veq += 1
                    v "Volecam się na vrzyszłość"

                "Kurde balans, nie posiadam kapitału":
                    v "Vbacz, młody. Nie dostaniesz vorzyczki! Vróc później kiedy będziesz... MMMMMMM... VOGATRZY!"

        if lilquest == 1 and inventory.has_item(Vomba) == True:
            menu:
                "W swoim eq znajduje się vomba, co z nią robisz?"

                "Vsadzam technika":
                    $ inventory.remove_item(Vomba)
                    p "Pora vpierdalać"
                    $ vechnik_stage = 7
                    $ lilquest = 2
                    play sound "BOOM.mp3"
                    "Vomba vybuchła"
                    "Siła eksplozji wystrzeliła cię aż pod warzywniak"
                    jump vtimefri

                "Ja się trochę cykam, potem zdecyduję":
                    pass

                "A powiem vechnikowi":
                    p "Te panie vechnik, mam dla ciebie rozrywkę"
                    v "O vuj Ci chodzi?"
                    p "Bo voktor kazał mi cię vysadzić"
                    v "Voo ma ga, ale z niego vjut ale kalmuj koka i wysadź tego fjuta"
                    v "Vostaniesz vifta"
                    $ lilquest = 3
                    jump vtimefri

        if lilquest == 4:
            v "Vobra robota! Masz tu dwa vidolce"
            $ vdolce += 2
            v "Tylko nie przepierdol na głupoty"
            $ lilquest = 5
            jump vtimefri

        if lilquest == 5:
            v "Co ty jeszcze chcesz?"
            jump vtimefri

    jump vtimefri

label voktor_wst:
    scene voktor
    if voktor_stage == 0:
        v "Viema variacie! Chcesz vokosa kurde ten?"
        v "Nie no, yaycuję. W tym obozie nic nie ma za darmo."
        v "Możesz wykonać dla mnie bojowe zadanie"
        if lilquest == 0:
            menu:
                "Chcesz kolejne bojowe zadanie?"
                "Vevnie lmao":
                    play sound "THROWING.mp3"
                    $ inventory.add_item(Vomba)
                    $ veq += 1
                    v "Vpierdol w vovietrze varsztat"
                    $ lilquest +=1
                    $ voktor_stage +=1

                "Vole nie":
                    v "To mnie nie vkurwiaj"
                    $ voktor_stage +=1
        else:
            jump vtimefri

    elif voktor_stage == 1:
        if lilquest == 0:
            v "Uleczyć cię?"
            menu:
                "Medycyna?"
                "Lecz mnie voktorze!" if HP != MaxHP and vdolce > 0:
                    $ HP = MaxHP
                    $ vdolce -= 1

                "A ić pan w chuj":
                    jump vtimefri

        elif lilquest == 1:
            if inventory.has_item(Vomba) == True:
                v "Veź się za vobotę"

        if lilquest == 2:
            v "Vobra vobora, oto twoja naroda:"
            $ HP = MaxHP
            "Zostałeś uleczony"
            p "I co? To tyle?"
            v "A czego się vpodziewałeś? Miliarda edków i miliona avałek? Lmao"
            $ voktor_stage = 2
            $ lilquest = 7

        if lilquest == 3:
            if inventory.has_item(Vomba) == True:
                p "Mogę teraz vsadzić voktora"
                menu:
                    "Vpierdolić go v vovietrze?"
                    "Vypierdalam":
                        $ inventory.remove_item(Vomba)
                        $ lilquest = 4
                        $ voktor_stage = 7
                        play sound "BOOM.mp3"
                        p "Pora na eksplodatora"
                        p "Nigerundajo!"

                    "A w piździe mam to zadanie":
                        $ lilquest = 7

                    "Jeszcze się muszę zastanowić":
                        pass

    elif voktor_stage == 2:
        v "Uleczyć cię?"
        menu:
            "Medycyna?"
            "Lecz mnie voktorze!" if HP != MaxHP and vdolce > 0:
                $ HP = MaxHP
                $ vdolce -= 1

            "A ić pan w chuj":
                jump vtimefri

    jump vtimefri

label varchiwa:
    scene drzv
    if varchiva_stage == 0:
        "Trafiając do varchiw stają Ci na drodze drzwi"
        if Frakcja == 3:
            p "Jestem pewnien, że nikt tego nie zamykał"
            "I faktycznie miałeś racje"
            $ varchiva_stage = 1
            jump varchiwa

        if inventory.has_item(Wytrych) == True:
            p "Essa mam wytrycha"
            $ inventory.remove_item(Wytrych)
            "Udało Ci się dostać do środka"
            $ varchiva_stage = 1
            jump varchiwa

        elif inventory.has_item(Vomba) == True:
            p "Ty kurwa, wysadzę to ich własną bronią"
            achieve Bomb
            $ inventory.remove_item(Vomba)
            $ varchiva_stage = 1
            play sound "BOOM.mp3"
            p "Ała kurwa, cóż za siła eksplozji."
            call checkHP(10) from _call_checkHP_5
            p "Get bombed, lmao"
            jump varchiwa

        else:
            p "Dupa sraka Arasaka, nie wejdę. Przydałby mi się wytrych"
            jump vtimefri

    elif varchiva_stage == 1:
        scene vard
        "Dostałeś się do środka"
        "Ale na twojej drodze staje vrażnik"
        v "Vrrrr Vpierdalaj stond albo ci vpierdole"
        menu:
            "Co zrobić?"
            "Rozpoczynam pvp!":
                call checkHP(15) from _call_checkHP_6
                $ Fragi += 1
                p "essa wariacie"
                $ varchiva_stage = 2
                jump varchiwa

            "Pa te trick" if inventory.has_item(AR) == True:
                "Wyciągasz AR"
                v "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                "vochroniaż opuszcza scenę, vygrałeś valkę"
                $ varchiva_stage = 2
                jump varchiwa

            "Variusz, nie poznajesz mnie?" if Frakcja == 3:
                v "Vo va vag, Vista"
                p "Vo va"
                v "Vo vy vu vobisz?"
                p "Vusze vać vokumenty vo varchiv"
                v "Vo va vens, vapraszam"
                p "Vięki"
                $ varchiwa_stago = 2
                jump varchiwa
                
            "Vpierdalam":
                jump vtimefri

    elif varchiva_stage == 2:
        scene varch
        "Varchiva stoją przed tobą otworem (Nie będę mówił którym)"
        "Pozostaje Ci spędzić resztę swych dni szukając dokumentu"
        "Zobaczyłeś że w rogu pomieszczenia stoi automat"
        "Gdy zbliżyłeś się do niego widzisz, że ma nawet nagrody"
        "Rozglądasz się dalej po pomieszczeniu"
        "Na ścianie visi plakat vupermena, na podłodze jest dyvan i jest nawet 1 (słownie jedno) pudełko"
        $ helper = 2
        $ varchiva_stage = 3
        jump varchiwa

    elif varchiva_stage == 3:
        scene varch
        while helper > 1:
            menu:
                "Co teraz robisz?"
                "Tracę swój czas szukając papierku" if bigquest < 2:
                    if renpy.random.randint(0,3) == 2:
                        $ bigquest = 2
                        p "No i się udało, lmao"
                    else:
                        "Chuja znalazłem"
                        $ dzien += 1
                        jump varchiwa

                "Vautomat???":
                    jump vending

                "Vlakat?":
                    "Podchodzisz bliżej tego arcydzieła graficznego"
                    "Z każdym kolejnym krokiem chcesz valnąć ten głupi ryj"
                    menu:
                        "Znów bijatyka?"
                        "Bijatyka cały dzień":
                            "Sprzedałeś vupermanowi hita"
                            "Niestety za plakatem były kolce"
                            "Straciłeś trochę hp"
                            call checkHP(5) from _call_checkHP_7
                            jump varchiwa

                        "Nie mam problemów z agresją":
                            "Zostawiłeś plakat w spokoju"
                            jump varchiwa

                "Dyvan?":
                    "Podchodzisz do dyvanu. Vygląda dość normalnie na pierwszy rzut voka"
                    "Po kolejnym rzucie vokiem, skończyły Ci się voczy ale jest to najzwyklejszy dyvan"
                    jump varchiwa

                "Pudełeczko" if helper == 2:
                    "Normalnie jedno pudełeczko"
                    "Po chuj ktoś je tu zostawił?"
                    menu:
                        "Otwierasz?"
                        "Kurwa no pewex":
                            "Znalazłeś 4 vdolce"
                            $ vdolce += 4
                            $ helper = 3
                            jump varchiwa

                        "A chuj z tym":
                            "To pewnie pułapka"
                            jump varchiwa

                "Vychodzę":
                    jump vtimefri

label vending:
    scene vautom
    p "Vistowe specjały, kuszące i pociągające"
    menu:
        "Czy kusi mnie hazard?"
        "Kurwa no pewex" if vdolce > 0 :
            $ vdolce -= 1
            $ vagroda = renpy.random.randint(0,4)
            if vagroda == 0 and inventory.has_space(Cap) == True:
                p "Dostałem vranat"
                $ inventory.add_item(Vranat)
                jump vending

            elif vagroda == 1 :
                p "Cukierek, szkoda że wylizany"
                jump vending 

            elif vagroda == 2 :
                p "Jakaś dziwna vigółka"
                menu:
                    "Czy mam psychę by łyknąć?"
                    "Pewex!":
                        call checkHP(3) from _call_checkHP_8
                        play sound "EAT OR MUNCH.mp3"
                        p "Kurde balans, lukrecja"
                        jump vending

                    "Nie jestem vebilem":
                        p "Takie tabsy tylko po konsultacji z Łaskawcą lub farmaceutą"
                        jump vending

            elif vagroda == 3 :
                p "Guma vurbo, a se opierdole"
                play sound "EAT OR MUNCH.mp3"
                jump vending

            else:
                p "Spermastycznie, nic nie vypadło"
                jump vending

        "Szanuję swoje vdolce":
            jump varchiwa

    jump varchiwa

label vrade:
    scene vshop
    menu:
        v "Co chciałbyś zakupić?"
        "Ale fajna Aerka" if vdolce >= 5 and inventory.has_item(AR) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(AR)
            $ vdolce -= 5
            $ veq += 1
            "Wydałeś 5 vdolcy na AR-kę"

        "Wytrych? " if vdolce >= 2 and inventory.has_item(Wytrych) == False:
            $ inventory.add_item(Wytrych)
            $ vdolce -= 2
            $ veq += 1
            "Wydałeś 2 vdolce na Wytrych"

        "Flaszka?" if vdolce >= 1 and inventory.has_item(Flaszka) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(Flaszka)
            $ vdolce -= 1
            $ veq += 1
            "Wydałeś 1 vdolca na Flaszkę"

        "Varmor" if vdolce >= 3 and inventory.has_item(MalyArmor) == False and inventory.has_space(Cap) == True:
            $ inventory.add_item(MalyArmor)
            $ armor = 11
            $ vdolce -= 3
            $ veq += 1
            "Wydałeś 3 vdolce na lil varmor"

        "Nie potrzebuję twoich towarów":
            jump vtimefri

    jump vtimefri

label varena:
    scene vare
    show vista
    if valki == 0:
        v "Nie możesz już walczyć, przeciwnicy się skończyli"
        jump vtimefri

    else:
        v "Velo, vitam na varenie"
        v "Jeśli chcesz valczyć, to zapraszam. Możesz walczyć tylko [valki] razy"
        menu:
            "Zostaję vojownikiem?"

            "Vewnie":
                jump vlepa

            "Volę nie":
                v "Varena nie ucieknie, vracaj kiedy chcesz"
                jump vtimefri

label vlepa:
    scene black
    "Zobaczmy jak Ci poszło"
    if vron == 1 and vrrr < 4:
        "Jesteś popierdolony, że przyszedłeś z vronią na arenę"
        "Vygrałeś, reszta się Vstraszyła"
        $ valki = 0
        $ vdolce += 5
        $ vrrr += 1
        jump vtimefri

    elif vrrr > 4:
        "Nikt już nie chce z tobą walczyć"

    if valki > 0:
        $ cel = renpy.random.randint(1,3)
        if cel == 1:
            "Chujowo jak zwykle"
            $ wpierdol = renpy.random.randint(1,7)
            call checkHP(wpierdol) from _call_checkHP_9
            $ valki -= 1

        elif cel == 2:
            "Remis bałwany"
            $ valki -= 1

        else:
            "Jebaniec, udało Ci się wygrać"
            $ vdolce +=1
            $ valki -= 1

    if valki == 0:
        $ vrrr += 1
        
    jump vtimefri

label vokum:
    scene black
    p "To co ciekawego skrywają vistowe vokumenty"
    "Czytasz pierwszą kartkę"
    "Raport V nr 45672"
    v "Vedykamenty są napravde pomocne, moje umiejętności umysłowe zwiększyły się."
    v "Vózg v vłynie jest skuteczny, muszę vodziękować Vanowi"
    v "Vestem viekav, co jeszcze ugotuje"
    p "Kinda sus, ngl. Co oni tu jeszcze mają?"
    "Kolejny dokument"
    v "Vroń testowa jest strasznie vujowa"
    v "Vechnikowi powinienem urwać yaya i yondra!"
    v "Vstrzeliłem i nic się nie stało. Vkurwiam się, vopierdoli mnie"
    p "Lmao rip"
    p "O coś jeszcze ciekawego"
    v "Populacja V vnosi około 20 tysięcy. Mnożymy się jak świeże bułeczki"
    v "Jeszcze pół roku i Arasaka straci nad nami vładzę ale my musimy jeszcze czekać jak karaczany"
    v "Va szczęście dołączenie do naszej społeczności nie jest trudne"
    v "Vstarczy vpisać vardcorevorn.vom"
    p "O kurde balans, to jest aż tak proste?"
    menu:
        "Czy mam psychę sprawdzić tę stronę?"
        "Co może być złego w pornografi":
            $ Frakcja = 3
            "Vo volera"
            jump vtimefri

        "Nigdy nie zostanę V":
            jump vtimefri
 

label amongthevpods:
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    call updict("Laskawca",stan) from _call_updict
    $ kibel_stan = 0
    $ bigquest = 3
    achieve Iabk

    if Frakcja != 1:
        scene kuchnia
        "Wróciłeś do bazy po analizie Vist"
        if Frakcja == 3:
            $ bigquest == 4
            "A nawet dołączyłeś do nich"
            "Teraz, jako Vista, czy na pewno chcesz dawać wasze dokumenty?"
            menu: 
                "Fejkujemy ":
                    "Delikatnie pozmieniałeś papiery, raczej Gun się nie połapie"
                    "Wszedłeś do kuchni"
                    show gun
                    g "Na raty chrystusa, ty żyjesz!"
                    g "Znaczy ten, gRATulacje, udało Ci się"
                    g "Zobaczmy co tam przyniosłeś ciekawego"
                    "Oddałeś podrobione papiery"
                    g "Oj karamba, grube dowody"
                    g  "Prawie zapomłem, oto twoja nagroda"
                    $ helper = 2 * renpy.random.randint(1,10)
                    $ edki += helper
                    "Dostałeś [helper] edków"
                    $ helper = 0
                    p "Miało być 2K"
                    g "No i masz 2K10"
                    p "Ale skam"
                    g "Dobra, nie pierdol"
                    g "Od teraz jesteś prawdziwym bazownikiem"
                    show cypher with moveinleft
                    c "RICHTIG (:"
                    hide cypher with moveoutright
                    g "Zamknij się Cypher"
                    g "Dobra, idź do siebie, potrzebuje trochę czasu"
                    jump rozstaje

                "Boję się fałszerstwa":
                    v "Ale z Ciebie vipa"

        "Wszedłeś do kuchni"
        show gun
        g "Na raty chrystusa, ty żyjesz!"
        g "Znaczy ten, gRATulacje, udało Ci się"
        g "Zobaczmy co tam przyniosłeś ciekawego"
        "Oddałeś znaleziska"
        $ postacie["Gun"] += vron
        $ vron = 0
        g "Oj karamba, grube dowody"
        g "Prawie zapomłem, oto twoja nagroda"
        $ helper = 2 * renpy.random.randint(1,10)
        $ edki += helper
        "Dostałeś [helper] edków"
        $ helper = 0
        p "Miało być 2K"
        g "No i masz 2K10"
        p "Ale skam"
        g "Dobra, nie pierdol"
        g "Od teraz jesteś prawdziwym bazownikiem"
        show cypher with moveinleft
        c "RICHTIG (:"
        hide cypher with moveoutright
        g "Zamknij się Cypher"
        g "Dobra, idź do siebie, potrzebuje trochę czasu"
        jump rozstaje   

    if Frakcja == 1:
        scene dach
        show cypher
        c "Dzień dobry, mój ulubiony kurierze! Pokazuj co tam zajebałeś Vistom"
        c "Scheiße, ciekawe dokumenty"
        c "Chuja rozumiem ale na spokojnie, zrobię sobie kopie a Gun dostanie resztę"
        c "Masz, trochę drobniaków"
        $ edki += 400
        p "Nie spodziewałem się, że dasz mi pieniądze Cypher"
        c "Masz mnie za żyda, proszę Cię, ja nie Gajda, doceniam swoich oddanych pracowników"
        c "Zmykaj do siebie, należy Ci się odpoczynek"
        "Zacząłeś iść do siebie"
        c "Jednak czekaj, mam już kopie, zanieś je Gunowi"
        p "A nie możesz ty ich odnieść?"
        c "Pojebało się"
        hide cypher with dissolve
        jump kuchnia
