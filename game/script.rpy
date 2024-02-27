
define c = Character(_("Cypher"), color="#00FFF7")
define g = Character(_("Gun"), color="03FEFA")
define h = Character(_("Hartmann"), color="1945FF")
define pl = Character(_("Łaskawca"), color="696969")
define k = Character(_("Kałach"),color="FF00FF")
define p = Character(_("[player_name]"))
define r = Character(_("Szczur"),color="123456")
define j = Character(_("Jhin"),color = "444444")
define v = Character(_("Vista"), color = "213769")
define kk = Character(_("Krateus"), color = "ABCDEF")
define t = Character(_("Toro"), color = "6969EE")
define gk = Character(_("Gen. Kennedy"), color = "098703")
define kr = Character(_("Krateus"), color = "#023a10")

init python:
    class Inventory():
        def __init__(self, items, quantity):
            self.items = items
            self.quantity = quantity

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


    class quest():
        def __init__(self,name,giver,reward,req):
            self.name = name
            self.giver = giver
            self.reward = reward
            self.req = req

        def add_quest(self,giver,reward,req):
            self.name = name
            self.giver = giver
            self.reward = reward
            self.req = req

        def finish_quest(self,giver,reward,req):
            pass


label checktime:
    if czas == 0:
        $dzien += 1
        jump sypialnia

    else:
        return

label checkHP(dmg):
    if armor > 10:
        if dmg < (armor+1) :
            $ HP = HP

    else:
        if armor != 0:
            $ HP -= -(armor - dmg)
            $ armor -= 1
        else:
            $ HP -= dmg

    if umieram == 1:
        jump gameover

    elif HP < 1:
        $ umieram = 1
        return

    else:
        return

label start:
    default postacie = {"Kalach":0, "Gun":0, "Cypher":0, "Laskawca":0, "Hartmann":0, "Jhin":0, "Visty":0, "Kennedy":0, "Krateus":0}
    #deklaracja inventory
    default inventory = Inventory([],0)

    #deklaracja przedmiotów
    default AR = InventoryItem("AR", "Fajny karabin")
    default Rat = InventoryItem("Szczur", "Grube bydle")
    default Flaszka = InventoryItem("Flacha", "Najlepszy przyjaciel Kałacha")
    default Kokos = InventoryItem("Kokos","Tak na prawdę to kokaina")
    default Pistolecik = InventoryItem("Pistolet","Prosta tania broń")
    default Granat = InventoryItem("Granat","Mały gadżet, robiący bum")
    default Klapek = InventoryItem("Klapek","Klapek z twarzą Cyphera. Nie dotykałbym tego")
    default MalyArmor = InventoryItem("Pancerz","Standardowy cyberowy armor")
    default Vron = InventoryItem("Vroń","Współczuję zakupu")
    default Wytrych = InventoryItem("Wytrych","Cudowny sprzęt do otwierania drzwi i nie tylko")
    default Vomba = InventoryItem("Bomba","Bomba, tylko produkcji Vist")
    default Vranat = InventoryItem("Vranat","Wabajack tego uniwersum")
    default Ser = InventoryItem("Ser","Strasznie cheesy, Gun musi go lubić")
    default THeal = InventoryItem("Turbouzdrawiacz","Turbo uzdrawia")

    #deklaracja cech
    default INT = 2
    default REF = 2
    default ZW = 2
    default TECH = 2
    default CHAR = 2
    default SW = 2
    default SZ = 2
    default RUCH = 2
    default BC = 2
    default EMP = 2

    #Stany posraci
    default gun_stan = 0
    default kalach_stan = 0
    default laskawca_stan = 0
    default hartmann_stan = 0
    default jhin_stan = 0
    default cypher_stan = 0
    default kibel_stan = 0
    default wojsko_stan = 0
    default krateus_stan = 0

    #deklaracja reszty
    default edki = 0
    default vdolce = 0
    default MaxHP = 10 + (5*((BC+SW)/2))
    default Fragi = 0
    default akt = 0
    default HP = 0
    $ HP = MaxHP
    default Frakcja = 0
    # 0 = Niezrzeszony
    # 1 = DH
    # 2 = DN
    # 3 = Visty
    # 4 = Uda
    # 5 = Wojsko
    default dzien = 1
    default armor = 0
    default umieram = 0
    default maxarmor = 0
    default czas = 20
    default veq = 0
    default psycha = 0
    $ psycha = [EMP] * 10
    default znajOkol = 0
    default lilquest = 0
    default vrrr = 0
    default bigquest = 0
    default vron = 0
    default helper = 1
    default part = 0

    play music "Bongo_Madness.mp3" volume 0.2
    while helper == 1:
        $ player_name = renpy.input("Nazywasz się")
        if player_name == "Gun":
            g "Prawa autorskie kurwa"

        elif player_name == "Kałach":
            k "Odpierdol się"

        elif player_name == "Cypher":
            c "Cypher może być tylko jeden"
            c "GIŃ"
            jump gameover

        elif player_name == "Łaskawca":
            pl "Koleżko, nie pozwalaj sobie"

        elif player_name == "Jhin":
            j "Obawiam się, że to imię jest już zajęte."

        elif player_name == "Hartmann":
            h "A Ci migomatem pierdolne"

        elif player_name == "Vista":
            v "Vtamy w koloni"
            $ Frakcja = 3
            $ helper = 0

        elif player_name == "Szczur":
            g "Na tym etapie jeszcze z tobą nie gadam"

        elif player_name == "Debil":
            g "To brzmi debilnie"

        elif player_name == "Bezi":
            p "Nie żyję lmao"
            jump gameover

        elif player_name == "Krateus":
            kr "Zaraz będziesz celem jew dzitsu"

        elif player_name == "Kretyneus":
            g "Faktycznie kretyn"

        elif player_name == "Chuj":
            g "Pewnie mały"
            $ helper = 0

        elif player_name == "Jan":
            g "Jebany dzban"
            $ helper = 0

        elif player_name == "Joon Goo":
            g "Jak ja Cię kurwa nienawidzę"
            $ postacie["Gun"] = -99
            $ helper = 0

        else:
            $ helper = 0

    "Nie miałeś edków"
    "Sensu życia"
    "Ani nawet broni"

    menu:
        "Więc postanowiłeś..."

        "Dołączyć do Cyberdzbanów.":

            scene baza

        "Spierdalać.":

            "Good ending, lol"
            return

    show cypher with dissolve

    c "Witamy w bazie młody."
    c "Pa ten trick!"

    "Zaczyna morbować"

    show gun at right
    show cypher at left

    g "Spokojnie kasztanie"
    "Gun katyńskim kopem wysłał Cyhpera na dach"
    c "DiamandHunde znowu błysnęło"
    play sound "CARTOON RICOCHET #2.mp3"
    hide cypher with fade

    g "Łap rata"
    play sound "THROWING.mp3"
    $ inventory.add_item(Rat)
    show grab

    g "Oto symbol twojej przynależności do Drako Nero"
    g "Znaczy, jeszcze nie jesteś jego członkiem"
    g "Ale na start masz rata. Ten chuj srał mi w kieszeni"
    g "Dawaj do środka"
    jump intro

# intro

label intro:
    scene kuchnia
    show gun at right
    g "Więc nowy, witamy w bazie"
    g "Jak ty się w ogóle nazywasz"
    g "[player_name], brzmi jak debil"
    g "Idź się przejdź, pogadaj z innymi"
    g "Przywitaj się jak człowiek"
    jump rozstaje

label gameover:
    "Przegrałeś lol"
    return

label rozstaje:
    scene black
    call checktime
    menu:
        "Kaj leziesz?"

        "Kierunek kuchnia":
            jump kuchnia

        "Może się pomodlę?":
            jump kosciol

        "Przycisło mnie":
            jump kibel

        "Nie boję się śmierci":
            jump dach

        "Co tam tak napierdala?":
            jump warsztat

        "Ten czerwony krzyż wygląda obiecująco":
            jump klinika

        "Dziupla Jhina" if bigquest > 2:
            jump jhinownia

        "Lil Brazil" if bigquest > 4:
            jump bruhzylia

        "Idę do siebie" if akt > 0:
            jump sypialnia

        "Wychodzę stąd" if akt > 0:
            jump miasto

label kuchnia:
    scene kuchnia
    show gun
    if akt == 0:
        g "Szybko Ci poszło"
        if gun_stan < 4:
            if inventory.has_item(Flaszka) == True:
                g "To pomoże Ci z kałachem"
                g "Daj mu tę flachę"
                jump rozstaje
            else:
                g "Masz, to Ci pomoże zdobyć zaufanie księdza"
                play sound "THROWING.mp3"
                $ inventory.add_item(Flaszka)
                g "Daj mu to, powinien Cię polubić"
                jump rozstaje
        elif gun_stan > 2:
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
                    return

    elif akt == 1 and bigquest == 0:
        $ czas -= 1
        g "Ser dobry, [player_name]"
        g "Daj mi trochę czasu roboty szukam"
        if inventory.has_item(Klapek) == True:
            p "Mam przesyłkę od Cyphera"
            g "Co on znowu chce?"
            p "Mam dla Ciebie... klapka?"
            $ inventory.remove_item(Klapek)
            $ postacie["Gun"] -= 2
            $ postacie["Cypher"] += 1
            g "Obawiam się że to jest wypowiedzenie wojny"
            g "Albo gorzej"
            g "Zaczął produkcję merchu z DH"
            g "Tak czy siak, nic dobrego to nie oznacza"
            g "Zdupcaj, muszę pomysleć"
            jump rozstaje
        else:
            jump rozstaje

        if dzien > 3 and bigquest == 0:
            show jhin at right
            g "Robota się znalazła"
            j "Zostaniesz naszym tajnym agentem"
            j "Będziesz inwigilował wrogie społeczeństwo"
            j "Niczym Dżejms Bond"
            g "Nie zesraj się ten taki"
            g "Ale wracając do roboty, od dzisiaj nazywasz się Vładek"
            g "Zostaniesz szpiegiem, może nie z krainy deszczowców"
            g "Tylko z bazy, wślizgniesz się w szeregi Vistów"
            g "Wyciągniesz tyle informacji ile się da i spierdolisz"
            g "Zadanie analnie proste"
            g "Zaczynasz bezzwłocznie"
            jump amongthev

    elif akt == 1 and bigquest == 3:
        if dzien < 10:
            g "Daj mi trochę czasu, vista ma chujowy charakter pisma."
        
        else:
            g "Dobra [player_name], powiem Ci że jesteśmy w piździe."
            g "Jeśli dobrze rozumiem te papiery."
            g "To Visty wypuszczają jakąś nową broń."
            g "Polecisz teraz do naszego kontaktu, generała Kenediego"
            g "On da Ci broń do walki z Vinfekcją"
            $ bigquest = 4
            jump rozstaje

    elif akt == 1 and bigquest == 5 :
        if gun_stan == 0:
            g "No to mów, co Ci ten Kennedy powiedział ciekawego"
            p "Musimy zostać przyjaciółmi"
            g "Ja pierdole"
            g "Ale my że my, czy my że ty i inni?"
            p "Ja i inni"
            g "Ser z serca. No to do robory żołnierzu"
            g "Mocą przyjaźni zdobądź serca innych dzbanów"
            $ gun_stan = 1
            jump rozstaje 

        elif gun_stan == 1:
            g "Czyli ze mną chcesz zacząć randkować?"
            g "Daniel Krej z!"
            g "No to zacznijmy rozmowę kwalifikacyjną"
            g "Pytanie pierwsze"
            menu:
                "Jaki jest twój ulubiony kolor?"
                "Zielony":
                    g "Ok"
                "Ciorny":
                    g "Niepozorny"
                "Fioletowy":
                    g "Trochę gejowy"
                "Żółty":
                    g "2137"
                "Szczurzy":
                    g "I to mi się podoba"
                    $ postacie["Gun"] += 1

            g "Pytanie numero dos"
            menu:
                "Lubisz bigos"
                "Co kurwa?":
                    g "Pstro"
                "Tak":
                    g "To chujowo"
                    $ postacie["Gun"] -= 1

                "Nie":
                    g "To dobrze"
                    $ postacie["Gun"] += 1

            g "To chyba tyle z pytań"
            p "I co to kurwa niby znaczy?"
            g "Dowiesz się w swoim czasie"
            $ gun_stan = 2
            jump rozstaje

        elif gun_stan == 2:
            g "Kolego, to jest jeszcze wczesna alfa"
            g "Nie spodziewaj się że wszystko już będzie"
            g "Wróć za x updatów"
            g "(2)"


    if inventory.has_item(Ser) == True:
        p "Mam coś dla Ciebie gun"
        $ inventory.remove_item(Ser)
        g "Hmmm, tajemniczy mysi sprzęt."
        g "To mi się przyda."
        g "Dzięki"
        $ postacie["Gun"] += 1

    else:
        jump rozstaje

label kosciol:
    scene kosciul
    show kalach at right
    if akt == 0:
        if inventory.has_item(Flaszka):
            k "Wyczuwam flachę"
            k "Wezmę sobie"
            $ postacie["Kalach"] += 1
            $ inventory.remove_item(Flaszka)
            $ gun_stan += 1
            jump rozstaje

        if postacie["Kalach"] == 0:
            k "Kim ty kurwa jesteś?"
            k "Wypierdalaj"
            $ gun_stan += 1
            jump rozstaje

        else:
            play sound "BURP.mp3"
            k "Pijesz?"
            jump rozstaje

    if akt == 1 and bigquest == 0:
        $ czas -= 1
        if kalach_stan == 0:
            k "Jak tam poszło?"
            k "Postrzelałeś?"
            k "Poruchałeś?"
            k "Może coś popiłeś?"
            if wojownik == True:
                k "Czyli coś postrzelałeś, milutko"
                $ postacie["Kalach"] += 1

            else:
                k "Jedyne co strzeliłeś to foch, Ciper moment"
                show cypher at left
                c "Falsh"
                hide cypher with dissolve
                k "Spierdalaj syfer"
            $ kalach_stan += 1
            k "Zdupcaj, wracam do picia"
            jump rozstaje

        if kalach_stan == 1:
            "Kałach alkoholizuje się, jepiej mu nie przeszkadzaj"
            jump rozstaje

    elif akt == 1 and bigquest == 3:
        $ czas -= 1
        if kalach_stan == 0:
            k "Niech mnie uda i zimna wóda"
            k "Wróciłeś żywy z siedliska Vist"
            $ postacie["Kalach"] += 1
            k "Masz nagrodę"
            play sound "THROWING.mp3"
            $ inventory.add_item(Flaszka)
            k "Zachowaj na specjalną okazję, albo chlej teraz"
            $ kalach_stan += 1

        elif kalach_stan == 1 and dzien < 10:
            "Kościół jest zamknięty, wróc później"

        elif kalach_stan == 1 and dzien > 9:
            k "Wróciłem z krucjaty."
            k "I niech mnie dunder świśnie, tak mnie w krzyżu napierdala."
            k "Jeśli kiedykolwiek dołączysz do fanów stupek."
            k "To zostaniesz zgilotynowany."
            k "I granie Briar też się liczy."
            if Frakcja == 0:
                k "Może chcesz dołączyć do kościoła?"
                k "Dostaniesz błogosławienie i coś jeszcze"
                k "Co konkretnie, to jeszcze nie wiem"
                k "Ale na 69% coś będzie."
                menu:
                    k "To co, piszesz się?"

                    "Proste że tak, Umen":
                        $ Frakcja = 4
                        $ postacie["Kałach"] += 2
                        k "Niech wszystko Ci się teraz UDA!"

                    "Sory Kałach, jestem ateistą":
                        k "Dobrze więc."
                        k "Ale pamiętaj, nigdy stopy."
            $ kalach_stan = 2

    jump rozstaje

label kibel:
    scene kibel
    if akt == 0:
        show grat at left
        "Ić stont"
        $ gun_stan += 1
        $ kibel_stan += 1
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
                        "Zostawiłeś szczura w kiblu"
                        $ inventory.remove_item(Rat)
                        show grat at left
                        r "Dziękuje, dobry człowieku"
                        $ postacie["Gun"] += 1
                        jump rozstaje

                    "Kontynuuj sranie w kieszeni":
                        p "Tu będzie Ci bezpieczniej"
                        jump rozstaje
            jump rozstaje

        elif kibel_stan == 1:
            show grat
            r "Witaj dobry człowieku"
            r "Pozwól mi egzystować w tym niebezpiecznym środowisku samotnie"
            g "Kurwa, gadasz ze szczurami"
            g "Będą z Ciebie ludzie"
            $ postacie["Gun"] += 1
            $ kibel_stan += 1
            jump rozstaje

        elif kibel_stan == 2:
            "Raty raują"
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
        if cypher_stan == 0:
            "Cypher skończył morbowanie"
            c "Chcesz zostać najemnikiem?"
            c "A może wolisz wynająć najemników?"
            c "Wykonujemy każde zadanie, nawet niemożliwe damy radę zrobić"
            c "Za odpowiednią opłatę oczywiście"
            g "Te młody, dawaj na dół"
            hide cypher
            scene kuchnia
            show gun
            g "Lepiej nie zawieraj żadnych umów z Cypherem, to nigdy nie kończy się dobrze"
            $ gun_stan += 1
            $ cypher_stan += 1
            jump rozstaje

        elif cypher_stan == 1:
            "Widzisz że Cypher nad czymś pracuje"
            c "Nie przeszkadzaj mi, przygotowuję coś niesamowitego"
            c "Jeśli dołączysz do DH, to dostaniesz bojowe zadanie"
            $ cypher_stan += 1
            jump rozstaje

        elif cypher_stan == 2:
            c "Czy ty chcesz usłyszeć każdy dialog z mną?"
            c "Czy może stwierdziłeś że chcesz truć mi dupę"
            c "Powiedz mi kasztanie, wierzysz w kobiety?"
            c "Zastanów się nad odpowiedzią"
            $ cypher_stan += 1
            jump rozstaje

        elif cypher_stan == 3:
            c "No pierdolne Ci"
            c "Literealnie Ci pierdolnę"
            c "Jeszcze raz tu kurwa przyjdź a poszczuję Cię Młynarczykiem"
            $ cypher_stan += 1
            jump rozstaje

        elif cypher_stan == 4:
            c "No to masz przepierdolone"
            c "Młynarczyk! Bierz go!"
            play sound "Bestia.mp3" 
            "I coolawy mściciel postanowił pozbyć się szkodnika"
            "Git Gud"
            jump gameover

    elif akt == 1:
        if bigquest == 0:
            $ czas -= 1
            c "Co tam [player_name]?"
            if Frakcja == 1 and postacie["Cypher"] == 4:
                c "Dobra, robotę masz"
                play sound "THROWING.mp3"
                $ inventory.add_item(Klapek)
                c "Zanieś to Gunowi, jako symbol naszej przyjaźni"
                jump rozstaje

            elif postacie["Cypher"] == 5:
                c "Witaj mój najodważniejszy wojowniku"
                c "Nie mam teraz dla ciebie nowego zadania"
                c "Ale nie martw się, DH jeszcze zabłyśnie"
                $ cypher_stan = 1
                jump rozstaje

            elif Frakcja != 1:
                c "Jakbyś dołączył do DH to miałbyś teraz niesamowicie ciekawego kłesta"
                c "Tak to możesz spierdalać"
                jump rozstaje

        elif bigquest == 3:
            $ czas -= 1
            c "Czekaj, wróciłeś właśnie od Vistów co nie?"
            c "Jak tam było? Dobrze się bawiłeś?"
            c "Powiem Ci w sekrecie, który jednak każdy zna"
            c "Kiedyś, za czasów swojej światłości, polowałem na Visty"
            c "Ale moja umowa z wojskiem poszła się jebać gdy ten chuj Kennedy nie dał mi wsparcia"
            c "Jakby ta Avałka wleciała do metra, byłbym niepokonany"
            c "A tak to Jhin prawie się zabił tnąc kable"
            c "Mówiłem mu, trakcja to śmierć. Tory! To jest przyszłość"
            c "To tyle z mojej audiencji teraz idż w chuj."
            $ cypher_stan = 1
            jump rozstaje

label warsztat:
    scene warsztat
    show hartmann at right
    $ czas -= 1
    if akt == 0:
        $ gun_stan += 1
        "Wchodząc do pokoju słyszysz agresywne napierdalanie młotkiem, a w tle leci niemiecki metal"
        h "Kim ty kurwa jesteś?"
        h "Dlaczego mi kurwa przeszkadzasz w robocie?"
        h "Spierdalaj, albo Ci migomatem przypierdolę"
        jump rozstaje

    elif akt == 1:
        if bigquest == 0:
            c "Co tam [player_name]?"
            if armor == 0:
                h "Chcesz kupić jakiś pancerz? Tylko 100 edków"
                h "Nie padniesz na pierda"
                menu:
                    "Czy potrzebny mi jest pancerz?"

                    "Kurwa biorę":
                        if edki > 100:
                            $ inventory.add_item(MalyArmor)
                            $ edki -= 100
                            $ armor = 11
                            h "Jak Ci się rozpierdoli, to wiesz gdzie mnie szukać"

                        else:
                            p "Nie stać mnie"

                    "A spierdalaj, unikać będę":
                        h "Jak dostaniesz wpierdol, to wiesz gdzie mnie szukać"
            jump rozstaje

        elif bigquest == 3:
            if hartmann_stan == 0:
                $ hartmann_stan += 1
                h "Powiedz mi przetrwańcze"
                h "Czy Visty mają migomat na stanie?"
                h "Bo słyszałem że vigomat podobno spawa tylko gówno"
                menu:
                    "Czym jest kurwa migomat?":
                        h "Ty pierdolony betoniarzu"
                        h "Migomat to popularna nazwa spawarki, służącej do spawania metodą MIG-MAG."
                        h "Technologia MIG umożliwia spawanie w osłonie gazów obojętnych (argon lub hel), natomiast technologia MAG w osłonie gazów aktywnych (dwutlenek węgla)."
                        h "Spawanie migomatem jest efektywne, wydajne i precyzyjne."
                        h "Uzyskiwane spoiny charakteryzują się wysoką jakością wykonania."
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
                        $ hartmann_stan += 1
                        jump rozstaje
    else:
        jump rozstaje

label klinika:
    scene klinika
    show laskawca at right
    if akt == 0:
        $ gun_stan += 1
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
        if HP != MaxHP:
            pl "Może Cię uleczyć?"
            pl "Tylko 50 edków"
            menu:
                "Potrzebuje leczenia? [HP]/[MaxHP]"
                "Lecz mnie":
                    $ HP = MaxHP
                    $ umieram = 0
                    $ edki -= 50
                    $ czas -= 5
                    "Zostałeś Healnięty"

                "Podziękuje":
                    pass

        if inventory.has_item(Kokos) == False:
            pl "Chcesz kupić kokosa kurwa ten?"
            menu:
                "Dawaj tego kokosa":
                    if edki > 20:
                        play sound "THROWING.mp3"
                        $ inventory.add_item(Kokos)
                        $ edki -= 20

                    else:
                        p "Nie stać mnie"

                "Podziękuje":
                    pass

        if laskawca_stan == 0:
            pl "No to opowiadaj, jak Ci życie mija"
            pl "Powiem Ci, u mnie jest dość ciężko. Szukam servera dla baby"
            pl "Kiedyś w bazie mieliśmy cały czas jakiegoś netrunnera"
            pl "Ale przez cały ten konflikt z Vistami"
            pl "To mało kto chce się pojawić"
            pl "Raz mieliśmy taki zajebisty serwer"
            pl "To się okazało że pali ludzi, jak się do niego wpięli"
            pl "Przez trzy tygodnie się kłócili co z nim zrobić"
            pl "I kurwa nawet nie pamiętam co się z nim stało"
            pl "Jakbyś znalazł jakiś fajny serwerek"
            pl "To daj mi cynk, wynagrodzę cię"
            menu:
                "Mam nadzieję że w naturze ( ͡° ͜ʖ ͡°)":
                    pl "Kto wie kotku."
                
                "Mam nadzieję że w edkach":
                    pl "Pitos się znajdos"

                "Dla Ciebie, poszukam za friko":
                    pl "No to mam u Ciebie dług"
                    $ postacie["Laskawca"] += 2
            pl "No to czekam na info z niecierpliwością"
            $ laskawca_stan = 1

        if laskawca_stan == 1:
            pl "Czekam dalej"
        
        jump rozstaje

    else:
        jump rozstaje

label jhinownia:
    $ czas -= 1
    scene takiten
    if akt == 1:
        if jhin_stan == 0:
            show jhin
            j "Hejka naklejka jestem Jhin Taki-Ten"
            j "To nazwisko zawdzięczam swoim rodzicom"
            j "Czyli udało Ci się nakraść w gnieździe Vist"
            j "Powiem Ci, jestem pod wrażeniem"
            $ postacie["Jhin"] += 1
            j "Powiedz mi jak tam było?"
            j "Czy to prawda że Visty rozmnażają się przez pączkowanie?"
            j "Czy może po śmierci dzielą się na pół?"
            menu:
                "Zdecydowanie pączkowanie":
                    j "O cholipka, wiedziałem"
                    $ postacie["Jhin"] += 1
                    j "To oznacza że trzeba zabić każdego piekarza w mieście"
                    j "Wyruszam natychmiast"
                    "I se poszedł"
                    $ jhin_stan = 1
                    jump rozstaje

                "Dzielą się na pół":
                    j "A niech to dunder świśnie"
                    j "To oznacza że przegrałem zakład z Cypherem"
                    show sypher at left
                    c "RICHTIG"
                    hide cypher with dissolve
                    j "On już tu jest, uceikam"
                    "I spierdolił"
                    $ jhin_stan = 1
                    jump rozstaje

                "Co ty pierdolisz Ken-Taki?":
                    j "Ej to nie było miłe"
                    j "Staram się napisać książkę o Vistach"
                    j "I mam teraz rozdział o rozmnażaniu"
                    j "3.14rdol się chamie"
                    $ postacie["Jhin"] -= 1
                    $ jhin_stan = 1
                    jump rozstaje

        if jhin_stan == 1 and dzien < 10:
            "Pokój jest pusty, Jhin gdzieś wybył"
            if dzien > 9:
                $ jhin_stan = 1

            jump rozstaje

        if jhin_stan == 2:
            j "No hejka, dokonałem badań do mnożenia Vist"
            j "Źródłem jest strona internetowa"
            j "Krejzi.braindance.cum"
            j "Niestety nie mam pozwolenia od rodziców"
            j "Więc nie mogłem sprawdzić"
            menu:
                j "Może ty jesteś na tyle odważny żeby to zrobić?"

                "Aż taki głupi nie jestem":
                    j "Bardzo dobrze, to był tylko test"
                    $ postacie["Jhin"] += 1
                    j "Jednak jesteś mądrzejszy od ośmioklasisty"
                
                "Sprawdzę":
                    j "Jesteś głupi, nie rób tego"
                    j "Powiem Gunowi i zapierdolą Cię"
                    j "Skończysz w sarnie"
                    show gun at left
                    g "SKOŃCZYSZ MARNIE DEBILU"
                    hide gun
                    j "Ano tak, skończysz marnie"

                "Ja już jestem jednym z nich" if Frakcja == 3:
                    j "Pierdolisz"
                    p "Nie, masz przejebane"
                    j "aaaaa"

            j "No to ten, finito"
            $ jhin_stan = 3

        if jhin_stan == 3:
            "No jhin?"


label bruhzylia:
    scene brazil
    show krateus at right
    if krateus_stan == 0:
        kr "Czyli to ty jesteś nowy."
        kr "Witaj, jestem Krateus, a ty?"
        p "Jestem [player_name]."
        kr "No to zajebiście, formalności za nami"
        kr "Teraz tylko jedna drobnostka została"
        kr "Uściśnij mi dłoń"
        menu:
            "No dobra":
                "Widzisz że Krateus wyjął siekierę"
                kr "No to za znajomość"
                "I zamachnął się w kierunku twojego ramienia"
                p "Pojebało CIE"
                kr "WIEM"
                "I siekiera zatrzymała się kilka centymetrów od celu"

            "Spierdalaj":
                kr "Aha66"
                "Krateus wyjął strzelbę"
                kr "Może teraz zmienisz zdanie"
                p "Na chuj chcesz uścisnąć mi dłoń?"
                kr "Tak mnie nauczyli w KGB"
                kr "Ale i tak"
                
        kr "W brazyli było gorzej"
        p "A czy tu będzie gorzej?"
        kr "Proste że tak"
        "Nagle usłyszeliście krzyk dziecka"
        kr "Jebane mutanty"
        kr "Dobra, bywaj [player_name]. Idę polować"
        $ krateus_stan = 1
    if krateus_stan == 1:
        "No chłop poluje"
    jump rozstaje

label sypialnia:
    scene pokoj
    show screen hud
    p "Pusto tu"
    menu:
        "Jesteś w swoim pokoju, co chcesz zrobić?"
        "Idę spać":
            $ dzien += 1
            $ czas = 20
            if HP < MaxHP and  edki > 10:
                "Przed snem zjadłeś jeszcze coś z automatu"
                $ edki -= 10
                $ HP += BC
                if HP > MaxHP:
                    $ HP = MaxHP

            elif HP == MaxHP:
                "Śpisz słodko, jak aniołek"

            else:
                "Zasnąłeś z pustym brzuchem"

            jump rozstaje

        "Czy ja przypadkiem nie dostałem?":
            if HP != MaxHP:
                p "Faktycznie mam tylko [HP] na [MaxHP]."
                p "Pancerz ma [armor] punktów"
                jump sypialnia

            else:
                p "Zadawało mi się."
                jump sypialnia

        "Wyjść" if czas > 0:
            jump rozstaje

#akt 1
label akt1:
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    scene akt1
    $ cypher_stan = 0
    $ gun_stan = 0
    $ hartmann_stan = 0
    $ kalach_stan = 0
    $ jhin_stan = 0
    $ laskawca_stan = 0
    $ akt = 1
    $ wojownik = False
    "A więc zostałeś w tej bazie pełnej degeneratów"
    "Wybrałeś życie śmiecia za marne pieniądze"
    "Chujowy wybór, jak mam być szczery, no ale niech zyskam"
    "Miałeś może z pięć minut spokoju, aż Gun nie znalazł roboty"
    scene kuchnia
    show gun
    g "Panowie, robota jest"
    hide gun
    show cypher
    c "Płacą dobrze?"
    hide cypher
    show gun
    g "Nie wiem jeszcze"
    hide gun
    show cypher with dissolve
    c "To nie zawracaj mi dupy"
    hide cypher with dissolve
    "Cypher opuszcza scenę"
    show gun at left
    show hartmann at right
    show laskawca
    g "Skoro problem wyszedł, to możemy zacząć rozmowy"
    h "To co to za robota?"
    g "Idziemy, strzelamy, spierdalamy"
    pl "Podoba mi się to"
    g "A ty [player_name]? Piszesz się?"
    menu:
        "Piszę się?"
        "Kurwa no pewex":
            $ postacie["Gun"] += 1
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
            c "Może chcesz dołączyć do Diamand Hunde?"
            c "Oferujemy sporo kozyści, na twoim miejscu bym dołączył"
            menu:
                "Czy chcesz dołączyć do DH?"
                "W sumie czemu nie" if Frakcja == 0:
                    $ Frakcja = 1
                    $ czlonekFrakcji = True
                    $ postacie["Cypher"] += 3
                    c "Witamy w szeregach, później powiem Ci więcej. Muszę iść trollować Ciper."
                    jump podsumowanie1
                "Podziękuje":
                    c "Pamiętaj, oferta jest ważna do śmierci"
                    jump podsumowanie1

label akcja:
    scene combat1
    show gun at left
    g "Plan jest prosty, strzelamy, lootujemy"
    show laskawca at right
    pl "Nie musisz mnie namawiać"
    hide laskawca with dissolve
    "Łaskawca zaczął eksterminację oponentów"
    hide gun
    menu:
        "A co ty robisz?"
        "Zaczynam strzelać":
            call checkHP(7)
            "Udało Ci się zdjąć jednego ale sam też oberwałeś"
            $ Fragi += 1
            $ postacie["Gun"] += 1
        "Zbieram co mogę":
            $ inventory.add_item(AR)
            $ edki += 15
            call checkHP(5)
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
            $ Fragi += 3
            call checkHP(10)
            $ postacie["Laskawca"] += 2
        "Zbieram jeszcze więcej":
            $ inventory.add_item(Pistolecik)
            $ inventory.add_item(Granat)
            $ edki += 50
            call checkHP(5)
        "Czekam aż reszta nabije sobie fragi":
            "Kitrałeś się do końca"

    show gun
    g "Dobra robota panowie"
    show laskawca at right
    pl "KREW DLA BOGA KRWI"
    g "Ta, pewnie... pora wracać do bazy"
    jump podsumowanie1

label podsumowanie1:
    scene kuchnia
    show gun
    if wojownik == True:
        g "Nie poszło najgorzej, masz zasłużyłeś"
        $ edki += 200
        "Dostałeś 200 edków"

    else:
        g "Szkoda że Cię nie było, zarobił byś coś"
        g "Mówiłem, nie gadaj z Cypherem"
        g "Następnym razem postaraj się bardziej"
        $ postacie["Gun"] -= 2

    "Nadszedł czas chwilowego odpoczynku"
    g "Daj mi kilka dni to może znajdę jakąś robotę"
    g "Na piętrze masz pokój, czuj się jak w gościach"
    $ czas = 0
    jump rozstaje

label vniazdo:
    scene vland
    "Jesteś u Vist"
    menu:
        "Co chcesz zrobić?"
        "Wymiana edków na vdolce" if ekdi > 99:
            $ vdolce += 1
            $ edki -= 100

        "Wymiana vdolców na edki" if vdolce > 0:
            $ vdolce -= 1
            $ edki += 100

        "Vracam":
            jump miasto

label miasto:
    scene miasto
    menu:
        "Wyruszyłem do:"
        "Bazy":
            jump rozstaje

        "Sklepiku" if znajOkol == 1 and czas > 2:
            $ czas -= 2
            jump trader

        "Wojsko" if bigquest > 3:
            jump wojsko

        "Dziupli Vist" if Frakcja == 3:
            jump vniazdo

        "Nikąd, pospaceruje sobię" if czas > 0:
            $ czas -= 5
            $ cel = renpy.random.randint(1, 5)
            if cel == 1:
                "Znalazłeś jakieś drobniaki"
                $ zysk = renpy.random.randint(1, 100)
                $ edki += zysk
                p "Znalazłem [zysk] edków"

            elif cel == 2:
                "Ni chuja, same nudy"

            elif cel == 3:
                "Przez przypadek wszedłeś do Bloku Władcy Demonów"
                $ wpierdol = renpy.random.randint(4, 18)
                call checkHP(wpierdol)

            elif cel == 4:
                if znajOkol == 0:
                    "Udało Ci się odkryć fajny osiedlowy sklepik"
                    $ znajOkol = 1

                else:
                    p "Jaki fajny plasterek"
                    if HP < MaxHP:
                        p "A se przykleję"
                        $ HP += 1
                    else:
                        p "Ta? To zajebiście."
                        "Plasterek trafił do kosza."

            elif cel == 5:
                "Wszedłeś do bloku furrasów"
                if dzien % 3 == 0:
                    "Futrzana domina Cię dopadła"
                    $ HP = 1
                    $ czas = 0
                else:
                    "Masz farta, był zamknięty"
            else:
                "Print dupa, nie powinno Cię tu być."

    jump rozstaje

label trader:
    scene szop
    p "A se coś kupię"
    p "Ile mam mamony? [edki] edków, mogło być mniej"
    menu:
        "Szopping tajm"
        "Ale fajna Aerka" if edki >= 500:
            $ inventory.add_item(AR)
            $ edki -= 500

        "Wytrych? " if edki >= 200:
            $ inventory.add_item(Wytrych)
            $ edki -= 200

        "Kurwa ser?" if edki >= 50:
            $ inventory.add_item(Ser)
            $ edki -= 50

        "Na nic więcej mnie nie stać":
            p "Get zakuped"
    jump miasto


label wojsko:
    if wojsko_stan == 0:
        scene wojsko
        show genken at left
        gk "Witamy w armi młody"
        gk "Jestem Generał Kennedy, przywódca tego pierdolnika"
        if Frakcja == 0 or Frakcja == 3:
            gk "I jesteś tu z woli Guna"
        elif Frakcja == 1:
            gk "Jasna cholera, jesteś od Cyphera"
        gk "To co masz ogarnąć to destrukcja Vist"
        gk "Jakaś kurwa z Arasaki chce przejąć nad nimi kontrolę"
        p "Ależ to skurwysyn musi być"
        gk "To prawda, każdy pracownik kopro to skurwysyn"
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
        show cypher at right
        c "Hi Hi ha ha"
        hide cypher with dissolve
        gk "O nie, ta kreatura się tu materializuje"
        gk "Potem Ci wyjaśnie, teraz muszę się ukryć"
        gk "Pamiętaj, musisz się zaprzyjaźnić z CyberDzbanami"
        show cypher at right
        c "The Game ©"
        hide cypher with dissolve
        gk "To jest coraz mocniejsze"
        gk "Znikam"
        hide genken
        p "Mo i zniknął"
        $ wojsko_stan = 1
        $ bigquest = 5
        p "No to wracam do bazy"
        jump rozstaje

    elif wojsko_stan > 5: 
        jump tempend

    
    elif wojsko_stan > 0:
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1
        if postacie["Laskawca"] > 5:
            $ wojsko_stan += 1

label amongthev:
    stop music fadeout 1.0
    scene black
    if Frakcja != 1:
        p "Wysłali mnie prosto do wypizdowa"
        p "Nie dali jakichkolwiek wytycznych"
        p "Wiem że mam wykraść coś z archiw"
        p "Przyjaciele po chuju"
        p "Ale chuj, podobno dostanę 2k edków"
    
    elif Frakcja == 1:
        scene dach
        show cypher
        c "No to młody, robota jest"
        c "Fun pewnie Ci już powiedział"
        c "Ale tak dla przypomnienia"
        c "Visty to debile"
        c "Cienkie pizdeczki"
        if inventory.has_item(AR) == True:
            c "Widzę że jakąś broń już masz"
            c "To masz ode mnie inny gadżet"
            play sound "THROWING.mp3"
            $ inventory.add_item(THeal)
            c "Zajebałem Łaskawcy"
            c "Tylko nie zjedz od razu"

        else: 
            c "Dostaniesz ode mnie śmieszną zabaweczkę"
            play sound "THROWING.mp3"
            $ inventory.add_item(AR)
            c "Zajabałem Kałachowi"
            c "W sensie"
            c "Wyrzucał go do śmieci"
            c "A 500 edków piechotą nie chodzi"

    scene vland
    play music "dickdisco.mp3" volume 0.2
    show vista
    v "Vitam v vlubie"
    v "Jestem Viesiek"
    v "Będę twoim vrzewodnikiem"
    v "Oprowadzę Cię po vokolicy"
    show vechnik
    v "Tutaj mamy vechnika"
    v "Nie przeszkadzaj mu lepiej"
    v "Jak go wkurwisz, to Ci jeszcze Vpierdoli"
    hide vechnik
    v "Vobra, przejdź się po okolicy, poszukaj dla siebie roboty"
    v "Vajo"
    $ bigquest = 1
    hide vista
    jump vtimefri

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

    "Zostanę wojownikiem":
        jump varena

    "Vmiana vrofeum?":
        jump vrade

    "Zdrzemnę się trochę":
        if HP < MaxHP:
            $ HP += 2
            p "Kilka ran mi się zasklepiło"
            $ umieram = 0
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
        v "Vtam, jestem vechnikiem."
        v "Vogę Ci zaoferować potężne vposażenie."
        v "Ale oczyViście, jeśli vasz odpowiednią ilość Vdolców."
        $vechnik_stage = 1
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
        v "Vtam znowu"
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
                    "Vomba vybuchła"
                    "Siła eksplozji wystrzeliła cię aż pod warzywniak"

                "Ja się trochę cykam, potem zdecyduję":
                    pass

                "A powiem vechnikowi":
                    p "Te panie vechnik, mam dla ciebie rozrywkę"
                    v "O vuj Ci chodzi?"
                    p "Bo voktor kazał mi cię vsadzić"
                    v "Voo ma ga, ale z niego vjut"
                    v "Ale kalmuj koka i wysadź tego fjuta"
                    v "Vostiesz gifta"
                    $ lilquest = 3

        if lilquest == 4:
            v "Vobra robota"
            v "Masz tu dwa vidolce"
            $ vdolce += 2
            v "Tylko nie przepierdol na głupoty"

    jump vtimefri

label voktor_wst:
    scene voktor
    if voktor_stage == 0:
        v "Viema variacie!"
        v "Chcesz vokosa kurde ten?"
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
                "Lecz mnie voktorze!" if HP != MaxHP AND vdolce > 0:
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
            v "A czego się vpodziewałeś? Miliarda edków i miliona avałek?"
            v "Lmao"
            $ voktor_stage = 2
            $ lilquest = 7

        if lilquest == 3:
            if inventory.has_item(Vomba) == True:
                p "Mogę teraz vsadzić voktora"
                menu:
                    "Vpierdolić go v vovietrze?"
                    "Vpierdalam":
                        $ inventory.remove_item(Vomba)
                        $ lilquest = 4
                        $ voktor_stage = 7
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
            "Lecz mnie voktorze!" if HP != MaxHP AND vdolce > 0:
                $ HP = MaxHP
                $ vdolce -= 1

            "A ić pan w chuj":
                jump vtimefri

    jump vtimefri

label varchiwa:
    scene drzv
    if varchiva_stage == 0:
        "Trafiając do varchiw stają Ci na drodze drzwi"
        if inventory.has_item(Wytrych) == True:
            p "Essa mam wytrycha"
            $ inventory.remove_item(Wytrych)
            "Udało Ci się dostać do środka"
            $ varchiva_stage = 1
            jump varchiwa

        elif inventory.has_item(Vomba) == True:
            p "Ty kurwa, wysadzę to ich własną bronią"
            $ inventory.remove_item(Vomba)
            $ varchiva_stage = 1
            p "Ała kurwa, cóż za siła eksplozji."
            call checkHP(10)
            p "Get bombed, lmao"
            jump varchiwa

        else:
            p "Dupa sraka Arasaka, nie wejdę. Przydałby mi się wytrych"
            jump vtimefri

    elif varchiva_stage == 1:
        scene vard
        "Dostałeś się do środka"
        "Ale na twojej drodze staje vrażnik"
        v "vrrrr"
        v "vpierdalaj stond"
        v "albo ci vpierdole"
        menu:
            "Co zrobić?"
            "Rozpoczynam pvp!":
                call checkHP(15)
                $ Fragi += 1
                p "essa wariacie"
                $ varchiva_stage = 2
                jump varchiwa

            "Pa te trick" if inventory.has_item(AR) == True:
                "Wyciągasz AR"
                v "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                "vochroniaż opuszcza scenę, vgrałeś valkę"
                $ varchiva_stage = 2
                jump varchiwa

            "Vpierdalam":
                jump vtimefri

    elif varchiva_stage == 2:
        scene varch
        $ helper = 0
        "Varchiva stoją przed tobą otworem"
        "Nie będę mówił którym"
        "Pozostaje Ci spędzić resztę swych dni szukając dokumentu"
        "Zobaczyłeś że w rogu pomieszczenia stoi automat"
        "Gdy zbliżyłeś się do niego widzisz że ma nawet nagrody"
        "Rozglądasz się dalej po pomieszczeniu"
        "Na ścianie vsi platat vupermena"
        "Na podłodze jest dyvan"
        "I jest nawet 1 (słownie jedno) pudełko"
        while helper == 0:
            menu:
                "Co teraz robisz?"
                "Tracę swój czas szukając papierku":
                    if renpy.random.randint(0,3) == 2:
                        $ bigquest = 2
                        p "No i się udało, lmao"
                    else:
                        "Chuja znalazłem"
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
                            call checkHP(5)

                        "Nie mam problemów z agresją":
                            "Zostawiłeś plakat w spokoju"
                            jump varchiwa

                "Dyvan?":
                    "Podchodzisz do dyvanu"
                    "Vgląda dość normalnie na pierwszy rzut voka"
                    "Po kolejnym rzucie vokiem, skończyły Ci się voczy"
                    "Ale jest to najzwyklejszy dyvan"
                    jump varchiwa

                "Pudełeczko" if helper == 0:
                    "Normalnie jedno pudełeczko"
                    "Po chuj ktoś je tu zostawił"
                    menu:
                        "Otwierasz?"
                        "Kurwa no powex":
                            "Znalazłeś 4 vdolce"
                            $ vdolce += 4
                            $ helper = 1

                        "A chuj z tym":
                            "To pewnie pułapka"

                "Vchodzę":
                    $ helper = 1
                    jump vtimefri

label vending:
    scene vautom
    p "Vistowe specjały, kuszące i pociągające"
    menu:
        "Czy kusi mnie hazard?"
        "Kurwa no pewex" if edki > 0 :
            $ vagroda = renpy.random.randint(0,4)
            if vagroda == 0:
                p "Dostałem vranat"
                $ inventory.add_item(Vranat)

            elif vagroda == 1 :
                p "Cukierek, szkoda że wylizazny"

            elif vagroda == 2 :
                p "Jakaś dziwna vigółka"
                menu:
                    "Czy mam psychę by łyknąć?"
                    "Pewex!":
                        call checkHP(3)
                        play sound "EAT OR MUNCH.mp3"
                        p "Kurde balans, lukrecja"

                    "Nie jestem vebilem":
                        p "Takie tabsy tylko po konsultacji z Łaskawcą lub farmaceutą"

            elif vagroda == 3 :
                p "Guma vurbo, a se opierdole"
                play sound "EAT OR MUNCH.mp3"

            else:
                p "Spermastycznie, nic nie vypadło"

        "Szanuję swoje vdolce":
            jump varchiwa


label vrade:
    scene vshop
    menu:
        v "Co chciałbyś zakupić?"
        "Ale fajna Aerka" if vdolce >= 5 :
            $ inventory.add_item(AR)
            $ vdolce -= 5
            $ veq += 1
            "Wydałeś 5 vdolcy na AR-kę"

        "Wytrych? " if vdolce >= 2:
            $ inventory.add_item(Wytrych)
            $ vdolce -= 2
            $ veq += 1
            "Wydałeś 2 vdolce na Wytrych"

        "Flaszka?" if vdolce >= 1:
            $ inventory.add_item(Flaszka)
            $ vdolce -= 1
            $ veq += 1
            "Wydałeś 1 vdolca na Flaszkę"

        "Varmor" if vdolce >= 3:
            $ inventory.add_item(MalyArmor)
            $ vdolce -= 3
            $ veq += 1
            "Wydałeś 3 vdolce na lil varmor"

        "Nie potrzebuję twoich towarów":
            jump vtimefri

label varena:
    scene vare
    show vista
    v "Velo, vtam na vaernie"
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
        "Vgrałeś, reszta się Vstraszyła"
        $ valki = 0
        $ vdolce += 5
        $ vrrr += 1
        jump vtimefri

    elif vrrr > 4:
        "Nikt już nie chce z tobą walczyć"

    else:
        $ cel = renpy.random.randint(1,3)
        if cel == 1:
            "Chujowo jak zwykle"
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
    p "Kinda sus, ngl"
    p "Co oni tu jeszcze mają?"
    "Kolejny dokument"
    v "Vroń testowa jest strasznie vujowa"
    v "Vechnikowi powinienem urwać yaya i yondra!"
    v "Vstrzeliłem i nic się nie stało."
    v "Vkurwiam się, vopierdoli mnie"
    p "Lmao rip"
    p "O coś jeszcze ciekawego"
    v "Populacja V vnosi około 20 tysiący"
    v "Mnożymy się jak świerze bułeczki"
    v "Jeszcze pół roku i Arasaka straci nad nami vładzę"
    v "Ale my musimy jeszcze czekać jak karaczany"
    v "Va szczęście dołączenie do naszej społeczności nie jest trudne"
    v "Vstarczy vpisać vardcorevorn.vom"
    p "O kurde balans, to jest aż tak proste?"
    menu:
        "Czy mam psychę sprawdzić tę stronę?"
        "Co może być złego w pornografi":
            $ Frakcja = 3
            "Vo volera"

        "Nigdy nie zostanę V":
            jump vtimefri

    

label amongthevpods:
    $ gun_stan = 0
    $ kalach_stan = 0
    $ laskawca_stan = 0
    $ hartmann_stan = 0
    $ jhin_stan = 0
    $ cypher_stan = 0
    $ kibel_stan = 0
    $ bigquest = 3

    if Frakcja != 1:
        scene kuchnia
        "Wróciłeś do bazy po analizie Vist"
        if Frakcja == 3:
            "A nawet dołączyłeś do nich"
            "Teraz, jako Vista, czy na pewno chcesz dawać wasze dokumenty?"
            menu: 
                "Fejkujemy ":
                    "Delikatnie pozmieniałeś papiery, raczej Gun się nie połapie"
                    "Wszedłeś do kuchni"
                    show gun
                    g "Na raty chrystusa, ty żyjesz!"
                    g "Znaczy ten, gratulacje, udało Ci się"
                    g "Zobaczmy co tam przyniosłeś ciekawego"
                    "Oddałeś podrobione papiery"
                    g "Oj karamba, grube dowody"
                    g  "Prawie zapomłem, oto twoja nagroda"
                    $ edki += 2 * renpy.random.randint(1,10)
                    p "Miało być 2K"
                    g "No i masz"
                    g "2K10"
                    p "Ale skam"
                    g "Dobra, nie pierdol"
                    g "Od teraz jesteś prawdziwym bazownikiem"
                    show cypher at left
                    c "RICHTIG (:"
                    hide cypher with dissolve
                    g "Zamknij się Cypher"
                    g "Dobra, idź do siebie, potrzebuje trochę czasu"
                    jump rozstaje

                "Boję się fałszerstwa":
                    v "Ale z Ciebie vipa"

        "Wszedłeś do kuchni"
        show gun
        g "Na raty chrystusa, ty żyjesz!"
        g "Znaczy ten, gratulacje, udało Ci się"
        g "Zobaczmy co tam przyniosłeś ciekawego"
        "Oddałeś znaleziska"
        $ postacie["Gun"] += vron
        $ vron = 0
        g "Oj karamba, grube dowody"
        g  "Prawie zapomłem, oto twoja nagroda"
        $ edki += 2 * renpy.random.randint(1,10)
        p "Miało być 2K"
        g "No i masz"
        g "2K10"
        p "Ale skam"
        g "Dobra, nie pierdol"
        g "Od teraz jesteś prawdziwym bazownikiem"
        show cypher at left
        c "RICHTIG (:"
        hide cypher with dissolve
        g "Zamknij się Cypher"
        g "Dobra, idź do siebie, potrzebuje trochę czasu"
        jump rozstaje   

    if Frakcja == 1:
        scene dach
        show cypher
        c "Dzień dobry, mój ulubiony kurierze"
        c "Pokazuj co tam zajebałeś Vistą"
        c "Scheiße, ciekawe dokumenty"
        c "Chuja rozumiem"
        c "Ale na spokojnie, zrobię sobie kopie a Gun dostanie reszte"
        c "Masz, trochę drobniaków"
        $ edki += 400
        p "Nie spodziewałem się że dasz mi pieniądze Cypher"
        c "Masz mnie za żyda, proszę Cię, ja nie Gajda"
        c "Doceniam swoich oddanych pracowników"
        c "Zmykaj do siebie, należy Ci się odpoczynek"


label tempend:
    "Doszedłeś do końca tej historii"
    "Na ten moment nie ma nic więcej do odkrycia"
    "Możesz dumnie wypierdalać"
    "Albo czekaj"
    "Zrób ss następnego okienka i wyślij mi"
    "Ogarnij chhoja i idź do woja"
    "Dostaniesz kartę do KTG i 40 exp do cybera"
    "A teraz czekaj na następny update i wypierdalaj"
    return
