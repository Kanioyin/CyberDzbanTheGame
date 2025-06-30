
init python:
    import os 

    def after_load():
        session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
        persistent.czasGry += session_time
        persistent.session_start_time = renpy.get_game_runtime()
        if persistent.czasGry > 300:
            bobcachievement_grant("Tim") 

        while persistent.czasGry > 60:
            persistent.czasGry -= 60
            persistent.godzinyGry += 1

    def save_playtime():
        session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
        persistent.czasGry += session_time
        if persistent.czasGry > 300:
            bobcachievement_grant("Tim")

        while persistent.czasGry > 60:
            persistent.czasGry -= 60
            persistent.godzinyGry += 1

    def drop_item(item):
        if item in inventory.items:
            inventory.remove_item(item)
            if item == Klapek:
                bobcachievement_grant("DHW")
                postacie['Cypher'] = -9999
                renpy.notify("Cypher to zapomni")
            renpy.notify(f"Wyrzucono {item.name}")
            bobcachievement_grant("Eko")
        else:
            renpy.notify("Nie masz tego przedmiotu!")
    
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
            renpy.notify(f"Dostałem {item.name}")

        def remove_item(self, item):
            renpy.notify(f"Straciłem {item.name}")
            self.items.remove(item)
            self.quantity -= 1

        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False

    class InventoryItem():
        def __init__(self, name, desc, image):
            self.name = name
            self.desc = desc
            self.image = image


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


# input call testSkili("Skil","Cecha", PT), nie fogoruj ""
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

    $ exp += 2
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
            $ HP = cechy["BC"] * 2
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

label cipflash:
    show ciphate with dissolve
    pause 1
    hide ciphate with dissolve
    return


label start:
    $ start_time = renpy.get_game_runtime()
    play music "Bongo_Madness.mp3" volume 0.2
    $ baba_name = "Babka from żabka"
    $ HP = MaxHP
    if nua > 9:
        $ edki += 500

    if nua > 19:
        $ znajOkol = 1
    
    if nua > 29:
        $ Cap = 5

    if nua > 39:
        $ znajOkol = 2

    if nua > 49:
        $ edki += 2000

    while helper == 1:
        $ player_name = old_pn = renpy.input("Nazywasz się:")
        $ player_name = player_name.capitalize()
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
            $ chipy = 5

        elif player_name == "Kasia":
            mg "Nie pozwalaj sobie kurwa"

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
    call cipflash from _call_cipflash_4
    "Gun katyńskim kopem wysłał Cyphera na dach"
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
    achieve Poczatek
    scene kuchnia
    show gun at right
    g "Więc nowy, witamy w bazie! Jak ty się w ogóle nazywasz?"
    p "[player_name]"
    g "Brzmi jak debil"
    g "Idź się przejdź, pogadaj z innymi, przywitaj się jak człowiek"
    jump rozstaje

label gameover:
    scene gameover
    $ session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
    $ persistent.czasGry += session_time
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
                        call cipflash from _call_cipflash_5
                        "Zostawiłeś szczura w kiblu"
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
            g "Kurwa, gadasz ze szczurami! Będą z Ciebie ludzie"
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
                h "Powiedz mi przetrwańcze czy Visty mają migomat na stanie?"
                h "Bo słyszałem że vigomat podobno spawa tylko gówno"
                menu:
                    "Czym jest kurwa migomat?":
                        h "Ty pierdolony betoniarzu"
                        h "Migomat to popularna nazwa spawarki, służącej do spawania metodą MIG-MAG."
                        h "Technologia MIG umożliwia spawanie w osłonie gazów obojętnych (argon lub hel), natomiast technologia MAG w osłonie gazów aktywnych (dwutlenek węgla)."
                        h "Spawanie migomatem jest efektywne, wydajne i precyzyjne."
                        h "Uzyskanie spoiny charakteryzują się wysoką jakością wykonania. A teraz powiem Ci jak to działa"
                        h "Spawanie MIG (Metal Inert Gas) to metoda 131, natomiast spawanie MAG (Metal Active Gas) to metoda 135. "
                        h "Migomaty to urządzenia półautomatyczne. Najważniejsze elementy układu to źródło prądu, połączone z układem sterującym;"
                        h "podajnik drutu (jeżeli umieszczony jest na zewnątrz, to łączy się go ze źródłem prądu za pomocą przewodu zespolonego); przewód masowy, łączący przedmiot spawany ze źródłem prądu"
                        h " butla z gazem osłonowym; uchwyt doprowadzający prąd do drutu."
                        h "Proces spawania rozpoczyna się od naciśnięcia przycisku na uchwycie MIG-MAG. Uchwyt spawalniczy przemieszczany jest równomiernie w stosunku do spoiny."
                        h "Należy określić prędkość wysuwania się drutu. Wysuwający się drut ulega stopieniu w łuku elektrycznym."
                        h "Tworzy się on pomiędzy drutem (elektrodą topliwą), a materiałem spawanym. Długość łuku utrzymywana jest na stałym poziomie."
                        h "Łuk elektryczny i stopiony metal (jeziorko) ochraniane są przez gaz osłonowy przed oddziaływaniem atmosfery. Krzepnące jeziorko spawalnicze tworzy trwałe złącze."
                        h "I to chyba tyle. Teraz ić se w chuj, muszę ochłonąć"
                        $ czas -= 1
                        jump rozstaje

                    "Nie widziałem żadnego Vigomatu":
                        h "Scheise albo jesteś ślepy, albo to vigomat jest mitem"
                        h "Tak czy siak, daj mi trochę czasu, muszę to przemyśleć"
                        jump rozstaje

                    "Opowiem Ci kawał, Vista gówno spawał":
                        call cipflash from _call_cipflash_6
                        h "KURWA WIEDZIAŁEM MUSZĘ GO ZDOBYĆ"
                        h "WYRUSZAM BEZZWŁOCZNIE"
                        jump rozstaje

            elif stan["Hartmann"] == 1 and dzien > 10:
                h "Pyk Pyk, jako tako i do Cyphera"
                p "Cześć Hartmann!"
                h "O Gluten morgen [player_name]! Potrzebujesz czegoś, jestem trochę zajęty"
                p "A przyszedłem pogadać trochę"
                p "Ale jak pracujesz to nie przeszkadzam"
                h "Typie, robię brońkę dla Cyphera. To nie jest jakkolwiek ważne"
                show cypher with moveinleft
                c "Wrrrr"
                hide cypher with moveoutright
                h "No widzisz, nic istotnego. O czym chcesz pogadać?"
                p "A tak, po prostu. Lubię znać swoich współpracowników"
                h "No to siadaj, opowiem Ci zwykłą historię. Byłem szczylem, spawałem złom"
                h "Romansowałem sobie trochę ale baby nie były gotowe na potężnego prawicowca"
                h "Później pewna zajebana korporacja się pojawiła. Rozstrzelała mój gang i w taki sposób trafiłem tu"
                p "No to było szybkie"
                h "A co ja mam Ci opowiadać historię mojego życia? Biografię chcesz mi pisać?"
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
                h "No to z czym do ludzi panie. Jak mi powiesz ile zarobię to może się zastanowię"
                h "Możesz też mi kupić nową spawarkę. Wyjebane, muszę coś dostać"
                $ config.rollback_enabled = False
                menu:
                    "Co robisz?"
                    "(Kłamstwo) Żartowałem, dostaniemy 3k na głowę":
                        h "No i to jest zysk. Wchodzę w to jak w albatrosa"
                        p "No to witamy na pokładzie"
                        $ helper2 = 1
                        $ stan["Hartmann"] = 5
                        "Zadowolony z siebie wyszedłeś"
                        achieve Harpp
                        $ renpy.block_rollback()
                        $ config.rollback_enabled = True
                        jump rozstaje

                    "Znajdę Ci tę spawarkę":
                        call cipflash from _call_cipflash_7
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
            pl "Może Cię uleczyć? Tylko 50 edków"
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
            pl "Może chcesz zakupić turbouzdrawiacz? Uratuje cię przed dedem"
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
                pl "No to opowiadaj, jak Ci życie mija. Powiem Ci, u mnie jest dość ciężko. Szukam serwera dla baby"
                pl "Kiedyś w bazie mieliśmy cały czas jakiegoś netrunnera ale przez cały ten konflikt z Vistami"
                pl "To mało kto chce się pojawić. Raz mieliśmy taki zajebisty serwer"
                pl "To się okazało że pali ludzi, jak się do niego wpięli. Przez trzy tygodnie się kłócili co z nim zrobić"
                pl "I kurwa nawet nie pamiętam co się z nim stało. Jakbyś znalazł jakiś fajny serwerek"
                pl "To daj mi cynk, wynagrodzę cię"
                $ config.rollback_enabled = False
                menu:
                    "Mam nadzieję, że w naturze ( ͡° ͜ʖ ͡°)":
                        call cipflash from _call_cipflash_8
                        pl "Kto wie kotku."
                    
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
                    call cipflash from _call_cipflash_9
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
                call cipflash from _call_cipflash_10
                "Ale wasze gadanie nic nie dało"
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
                pl "Ja pierdolę. Dobra, możemy być?"
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
        "Chłop nie żyje. Spoczywaj w tym pokoju"
        jump rozstaje
        

    if akt == 1:
        if stan["Jhin"] == 0:
            show jhin
            j "Hejka naklejka jestem Jhin Taki-Ten. To nazwisko zawdzięczam swoim rodzicom"
            j "Czyli udało Ci się nakraść w gnieździe Vist. Powiem Ci, jestem pod wrażeniem"
            $ postacie["Jhin"] += 1
            j "Powiedz mi jak tam było?. Czy to prawda że Visty rozmnażają się przez pączkowanie?"
            j "Czy może po śmierci dzielą się na pół?"
            $ config.rollback_enabled = False
            menu:
                "Zdecydowanie pączkowanie":
                    call cipflash from _call_cipflash_11
                    j "O cholibka, wiedziałem"
                    $ postacie["Jhin"] += 1
                    j "To oznacza że trzeba zabić każdego piekarza w mieście! Wyruszam natychmiast!"
                    "I se poszedł"
                    $ stan["Jhin"] = 1
                    jump rozstaje

                "Dzielą się na pół":
                    j "A niech to dunder świśnie! To oznacza że przegrałem zakład z Cypherem"
                    show cypher with moveinleft
                    c "RICHTIG"
                    hide cypher with moveoutright
                    j "On już tu jest, uciekam"
                    "I spierdolił"
                    $ stan["Jhin"] = 1
                    jump rozstaje

                "Co ty pierdolisz Ken-Taki?":
                    j "Ej to nie było miłe! Staram się napisać książkę o Vistach"
                    j "I mam teraz rozdział o rozmnażaniu. 3.14rdol się chamie"
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
            j "No hejka, dokonałem badań do mnożenia Vist. Źródłem jest strona internetowa"
            j "Krejzi.braindance.cum"
            j "Niestety nie mam pozwolenia od rodziców. Więc nie mogłem sprawdzić"
            $ config.rollback_enabled = False
            menu:
                j "Może ty jesteś na tyle odważny żeby to zrobić?"

                "Aż taki głupi nie jestem":
                    j "Bardzo dobrze, to był tylko test"
                    $ postacie["Jhin"] += 1
                    j "Jednak jesteś mądrzejszy od ośmioklasisty a to nie jest typowa sytuacja w tej bazie"
                    j "To dobry znak, nie będzie jeszcze z Ciebie insygni"
                    $ stan["Jhin"] = 3

                    j "Przyjdź później, będę miał kolejne pytania"
                
                "Sprawdzę":
                    j "Jesteś głupi, nie rób tego! Powiem Gunowi i zapierdolą Cię"
                    j "Skończysz w sarnie"
                    show gun at left
                    g "SKOŃCZYSZ MARNIE DEBILU"
                    hide gun
                    j "Ano tak, skończysz marnie. Weź się prześpij i przemyśl swoje zachowanie"
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
                            p "Za późno Jhin, Vózg rozkazuje. Ja pociągam za spust"
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
                            j "A dobra, teraz to ma sens. No to dobra, zrobię potem z tobą wywiad"
                            j "Pomożesz mi się stać głównym charakterem"
                            p "No ok? Czytałem twoje backstory. To przypadkiem nie jesteś nim już?"
                            j "No niestety nie, trochę fantazja mnie poniosła"
                            p "No dobra, to ma sans. Odwiedzę cię potem, bywaj Vhin"
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
            p "Masz rację. Musimy się zaprzyjaźnić"
            j "I co w tym jest takiego niebezpiecznego?"
            p 'To że muszę to zrobić z całym teamem'
            j "W sensie że przyjaźń tak?"
            p "No ta"
            j "A, ok, no to ten, fren?"
            p "Tak po prostu?"
            j "A czego ja mogę więcej wymagać?"
            p "No nie wiem, reszta ma doomstack bojowych zadań"
            j "Rozmawiałeś już ze mną przynajmniej dwa razy. W tej bazie czasem szybko można znaleźć cumpla"
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
            kr "Czyli to ty jesteś nowy. Witaj, jestem Krateus, a ty?"
            p "Jestem [player_name]."
            kr "No to zajebiście, formalności za nami. Teraz tylko jedna drobnostka została"
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
                    kr "Tak mnie nauczyli w KGB ale i tak"
                    
            kr "W Brazyli było gorzej"
            p "A czy tu będzie gorzej?"
            kr "Proste, że tak"
            "Nagle usłyszeliście krzyk dziecka"
            kr "Jebane mutanty! Dobra, bywaj [player_name]. Idę polować"
            $ stan["Krateus"] = 1
            jump rozstaje

        if stan["Krateus"] == 1:
            if dzien < 10:
                "No chłop poluje"
                "Daj mu trochę czasu"

            elif dzien > 9:
                kr "Kałabanga! Wróciłem z polowania"
                p "Ta, to zajebiście"
                kr "Co nie? Chcesz iść następnym razem ze mną?"
                p "Mogę ale jeśli mi potem pomożesz"
                kr "Pojebało cię chyba! Ja ci oferuję rozrywkę a ty chcesz żebym Ci coś jeszcze zrobił"
                kr "Wkurwiasz mnie! Zaraz Ci pokaże Brazylijskie sztuki walki!"
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
            kr "Głupie pytanie. Na ludzi oczywiście. Mam marzenie, które mnie napędza do działania"
            kr "Gdyby mnie przyjęli do ASP to nie byłoby problemu a tak to będą jaja jak sam skurwysyn"
            p "Dlaczego akurat na ludzi chcesz polować?"
            kr "Potrzebuję pracowników do nowego interesu ale o tym opowiem Ci później"
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
            kr "No ta, teraz ich uwolnimy i będą robić co im powiemy. Tak to działa w brazylii więc tu też powinno"
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
                call cipflash from _call_cipflash_12
                p "No nie mam nic przy sobie"
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
            if dzien > 15:
                kr "Dobra, chyba tyle czasu wystarczy"
                p "No, trochę ich tam trzymaliśmy, myślisz że jeszcze żyją?"
                kr "Jeśli silni zjedli słabych, to raczej tak. Jeśli mają moralność to będzie doomstack trupów"
                p "No to lećmy sprawdzić"
                scene fiszop
                show krateus
                kr "No to robimy opening"
                if inventory.has_item("AR"):
                    "Wyjąłeś AR dla bezpieczeństwa"
                kr "Na trzy otwieram drzwi, gotowy?"
                p "Tajest"
                kr "Trzy"
                "Kreteus szybkim ruchem otworzył drzwi i w środku widzicie trzy osoby"
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
                kr "Waleczne skurwiele. Kurwa szkoda, byliby dobrymi wojownikami"
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
                kr "Pogadaj z Łaskawcą. Jak zrobisz co on chce to wróć"
                jump rozstaje

            else:
                kr "No to dzień dobry"
                show laskawca at left
                pl "Siemaneczko"
                p "Ale bojowa ekipa się zebrała"
                kr "Plan mamy prosty, obecny tu Łaskawca robi Call of Bitches, następnie usypia to co dopadnie, a my skalpujemy"
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
                    kr "Chuja dało radę zrobić! Dawaj na Kennedy'ego, może się odkujemy"
                
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
                    kr "Kurwa brachu, pewex! Daj tylko znać i się pojawię"
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
            if dzien > 7:
                $ dzien = 1
                $ tydzien += 1
            
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
            jump rozstaje

#akt 1
label akt1:
    play music "Monkeys Spinning Monkeys.mp3" volume 0.2
    scene akt1
    $ stan = {"Kalach":0, "Gun":0, "Cypher":0, "Laskawca":0, "Hartmann":0, "Jhin":0, "Visty":0, "Kennedy":0, "Krateus":0, "Kasia":0}
    $ akt = 1
    $ wojownik = False
    "A więc zostałeś w tej bazie pełnej degeneratów. Wybrałeś życie śmiecia za marne pieniądze"
    "Chujowy wybór, jak mam być szczery, no ale niech zyskam. Miałeś może z pięć minut spokoju, aż Gun nie znalazł roboty"
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
            call cipflash from _call_cipflash_13
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
            c "Cenisz sobie zysk? Może chcesz dołączyć do Diamandhunde?"
            c "Oferujemy sporo korzyści, na twoim miejscu bym dołączył"
            menu:
                "Czy chcesz dołączyć do DH?"
                "W sumie czemu nie" if Frakcja == 0:
                    achieve Damm
                    $ Frakcja = 1
                    $ czlonekFrakcji = True
                    $ postacie["Cypher"] += 3
                    c "Witamy w szeregach, później powiem Ci więcej. Muszę iść trollować."
                    $ inventory.add_item(Odznaka)
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
            call cipflash from _call_cipflash_14
            "Kitrałeś się do końca"

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
        g "Szkoda że Cię nie było, zarobiłbyś coś. Mówiłem, nie gadaj z Cypherem"
        g "Następnym razem postaraj się bardziej"
        $ postacie["Gun"] -= 2

    "Nadszedł czas chwilowego odpoczynku"
    g "Daj mi kilka dni to może znajdę jakąś robotę. Na piętrze masz pokój, czuj się jak w gościach"
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

            "Śrubokręt" if edki >= 100 and inventory.has_item(Srubo) == False and inventory.has_space(Cap) == True:
                $ inventory.add_item(Srubo)
                $ edki -= 100

            "Kurwa ser?" if edki >= 50 and inventory.has_space(Cap) == True:
                $ inventory.add_item(Ser)
                $ edki -= 50

            "Sztuczne kwiaty" if edki >= 20 and inventory.has_space(Cap) == True:
                $ inventory.add_item(Kwiat)
                $ edki -= 20

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
    if stan["Kasia"] < 8:
        scene frogszop
    
    else:
        scene frogkacp
        $ baba_name = "Kacperek"

    $ czas -= 1

    if stan["Kasia"] == 1:
        jump frogsimp

    
    if stan["Kasia"] == 2 and dzien % 2 == 0:
        jump frogsimp

    if stan["Kasia"] == 4 or stan["Kasia"] == 6:
        jump frogsimp

    if Frakcja == 6 or stan["Kasia"] > 0:
        fse "Cześć [old_pn]"
    
    else:
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
                    $ persistent.frgout += 90

                else:
                    p "Proszę"
                    $ edki -= 10
                    $ frogsy += 40

                "Chwilę poczekałeś i jadło otrzymałeś"
                fse "Smacznego"
                play sound "EAT OR MUNCH.mp3"
                $ hunger = 0
                $ HP += 5
                if HP > MaxHP:
                    $ HP = MaxHP

            "Malborasek?" if frogsy > 999 and fajki < 1:
                p "Daj mnie malboraska"
                fse "Się robi"
                $ frogsy -= 1000
                $ fajki += 1

            "Dupnę sobie monsterka" if (edki > 24 or frogsy > 224) and czas < 30:
                fse "To będzie 25 edków"
                if frogsy > 224:
                    achieve Frg
                    p "Zapłace frogsami"
                    $ frogsy -= 225
                    $ persistent.frgout += 225

                else:
                    p "Proszę"
                    $ edki -= 25
                    $ frogsy += 100
                
                "Wypiłeś potwora"
                p "Czuję, że mogę dziś zrobić więcej"
                $ zawal += 1
                $ persistent.monsters += 1
                if zawal >= renpy.random.randint(0,99):
                    p "A niech to, chyba mam zawał"
                    $ HP = 0
                    $ zawal = 0
                    $ umieram = 1

                $ czas += 10

            "Perła Import" if edki > 49:
                fse "To będzie 50 edków"
                p "Prosze"
                $ edki -= 50
                $ fart += 2

            "Zdrapeczka" if edki > 24:
                $ edki -= 25
                $ frogsy += 100
                $ persistent.skracz += 1
                fse "25 edków"
                p "Proszę"
                p "Dobra, zobaczymy czy wygrałem"
                if renpy.random.randint(0, 200) < fart:
                    $ fart = 1
                    p "O CHUJ WYGRAŁEM"
                    achieve Mak
                    $ edki += 1000
                    p "Prosze pani, chciałbym tę zdrapkę wymienić"
                    fse "Gratulacje"
                    fse "Proszę, pańskie 1000 edków"

                else:
                    p "Kurwa, nie siadło"
                    $ fart += 1

            "Przewalutowanie" if vdolce > 0:
                fse "Już, oto normalne edki"
                $ edki += (vdolce*50)
                $ vdolce = 0
                p "Dziękuję"

            "Szukacie może pracowników?" if Frakcja == 0 and dzien > 9:
                fse "Mamy jeszcze wolny wakat. Byłby pan zainteresowany pracą?"
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
                $ persistent.work += czas
                $ czas = 0
                "Przepracowałeś cały dzień"

            "Mam kwiateczki dla ładnej babeczki" if inventory.has_item(Kwiat) == True and frogrel < 6:
                achieve Gtm
                $ inventory.remove_item(Kwiat)
                fse ":fluszed"
                fse "To bardzo miłe z twojej strony, dziękuję"
                if stan["Kasia"] == 0 and frogrel == 5:
                    $ stan["Kasia"] = 1
                $ frogrel += 1

            "Potrzebuję leczenia" if stan["Kasia"] > 4 and HP < MaxHP and frogsy > 499:
                fse "Spoczko [old_pn], już podaję leki"
                $ HP = MaxHP
                $ frogsy -= 499
                $ persistent.frgout += 499
                
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
            $ Cap += 1
            $ edki -= (Cap) * 100
            achieve Mocz
            p "Zwiększaj"
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

        gk "To co masz ogarnąć to destrukcja Vist. Jakaś kurwa z Arasaki chce przejąć nad nimi kontrolę"
        p "Ależ to skurwysyn musi być"
        gk "To prawda, każdy pracownik korpo to skurwysyn ale ten skurwysyn, to taki super skurwysyn"
        gk "Będziesz musiał zebrać drużynę i razem wyruszycie pozbyć się kutasa"
        p "Ja pierdolę! Ty na prawdę wymagasz ode mnie, żebym się dogadał z tymi debilami"
        p "Przecież to jest kurwa niewykonalne"
        gk "Dlatego to zadanie będzie dla ciebie wyzwaniem. Jeśli je wykonasz, to dostaniesz potężną wypłatę"
        p "Już trzeci raz słyszę o ogromnej wypłacie! Opowiedz mi dokładnie, co JA KURWA DOSTANĘ"
        gk "Wypłatę"
        show cypher with moveinleft
        c "Hi Hi ha ha"
        hide cypher with moveoutright
        gk "O nie, ta kreatura się tu materializuje. Potem Ci wyjaśnię, teraz muszę się ukryć"
        gk "Pamiętaj, musisz się zaprzyjaźnić z CyberDzbanami"
        show cypher with moveinleft
        c "The Game ©"
        hide cypher with moveoutright
        gk "To jest coraz mocniejsze! Znikam"
        hide genken with dissolve
        p "No i zniknął, jak zwykle kurwa. I wyjdzie, że dostanę 7,50 edka"
        p "Nienawidzę NC, Nienawidzę NC"
        $ wojsko_stan = 1
        $ bigquest = 5
        p "No to wracam do bazy"
        jump rozstaje

    if Frakcja == 1 or Frakcja == 3 or Frakcja == 4:
        gk "Dobra robota szczylu."
        gk "Udało Ci się zdobyć przyjaźń z potężną frakcją"
        menu:
            gk "Jesteś gotowy na tajną misję?"
            "Kurwa no pewex":
                gk "Git"
            
            "Daj mi jeszcze trochę czasu":
                gk "Spoczko"
                jump rozstaje

        jump wojowezadanie

    elif wojsko_stan > 0:
        "Opowiedziałeś Kenowi o swoim progresie"
        if stan["Laskawca"] == 2:
            "Pochwaliłeś się przyjaźnią z Łaskawcą"
            gk "Czyli Łaskawca jest gotowy Ci pomóc? Healer zawsze się przyda"
            $ wojsko_stan += 1
            $ stan["Laskawca"] = 6

        if stan["Gun"] == 5:
            "Pochwaliłeś się przyjaźnią z Gunem"
            gk "Gun chce wykonać zadanie dla mnie? Nie wiem czy to dobry znak"
            gk "Kiedyś jak dostał zadanie, to do teraz go nie skończył"
            gk "Na szczęście kapitan Sójeczka był w okolicy. Tak im namieszał w papierach, że sami nam pojazd oddali"
            $ wojsko_stan += 1
            $ stan["Gun"] = 6

        if stan["Kalach"] == 5:
            "Pochwaliłeś się przyjaźnią z Kałachem"
            gk "Jeśli Kałach leci z tobą, musisz go pilnować. Jeśli znajdę jakiegokolwiek dildosa na terenie akcji"
            gk "To Ciebie złapią konsekwencje"
            $ wojsko_stan += 1
            $ stan["Kalach"] = 6

        if stan["Hartmann"] == 5:
            "Pochwalileś się przyjaźnią z Hatrmannem"
            gk "Twardy zawodnik dołączył do Ciebie? Tylko musisz uważać, jak Gun dostanie auto w ręce"
            gk "Mogą być straty w cywilach"
            $ wojsko_stan += 1
            $ stan["Hartmann"] = 6

        if stan["Jhin"] == 4:
            "Pochwalileś się przyjaźnią z Jhinem"
            gk "Ten Taki idzie z Tobą? Szalone jak sam skurwysyn ale to jego decyzja"
            $ wojsko_stan += 1
            $ stan["Jhin"] = 6

        if stan["Cypher"] == 5 or stan["Cypher"] == 6:
            "Dumnie ogłosiłeś dołączenie Cyphera"
            gk "Dlaczego?"
            $ wojsko_stan += 1
            $ stan["Cypher"] = 9

        if stan["Krateus"] == 5:
            "Pochwaliłeś się przyjaźnią z Krateusem"
            gk "Krateus też tam jest? Powinien wykonywać zadanie bojowe"
            gk "Oj, będę musiał z nim pogadać"
            $ wojsko_stan += 1
            $ stan["Krateus"] += 1


    if wojsko_stan > 4: 
        if wojsko_stan > 7:
            achieve Full
            mg "Gratulacje, zebrałeś całą drużynę! Wasze szanse na przetrwanie są zwiększone"

        gk "Dobra robota szczylu."
        gk "Udało Ci się zdobyć przyjaźń z innymi dzbanami"
        menu:
            gk "Jesteście gotowi na tajną misję?"
            "Kurwa no pewex":
                gk "Git"
            
            "Daj mi jeszcze trochę czasu":
                gk "Spoczko"
                jump rozstaje

        gk "Więc lecicie na super tajną misję. Siłą przyjaźni musicie wysadzić jedno z vniazd"
        gk "Prowadzą tam badania nad ściśle tajnym projektem Vezuwiusz. Niech bóg was przyjmie"
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
        $ oldFrakcja = 0
        scene vniazdo
        "Poprowadziłeś punków prosto w vniazdo"
        p "Panowie, Kennedy wybrał mnie jako szefa tej operacji, więc proszę słuchajcie się mnie"
        "O dziwo nikt nie miał z tym problemu"
        "Teraz jako szef, czeka Cię wyzwanie kierowania swoją ekipą. Wskaźnik zagrożenia jest na poziomie 100"
        "Jeśli spadnie do 0 to osiągniesz giga sukces. Nie spodziewaj się tego wyniku"
        "To jakie masz możliwości zależy od ludzi w ekipie i od tego jaki masz sprzęt"
        "Wracając do wyroku śmierci. Macie kilka opcji na wykonanie tej roboty"
        menu:
            "Po Cichu":
                "Brak w tobie cyberowego ducha walki"
                p "Panowie, robimy to tak Cicho jak się tylko da i to będzie bardzo trudne"
                p "Trzeba teraz dostać się do środka. Co my mamy do wyboru"
                menu:
                    "Jak wchodzisz?"
                    "Drzwi główne":
                        "Dostaliście się do środka głównymi drzwiami"
                        "Najgorsze możliwe wejście ale okazało się niestrzeżone"
                        $ helper -= 10

                    "Okno" if stan["Krateus"] > 5:
                        p "Krateus, wskakuj oknem i nam pomożesz"
                        kr "Tajest kierowniku! Chopaky, to jest schowek na miotły! Wskakujcie, macie tu linę"
                        $ helper -= 15
                        hide krateus
                        "A po nim wskoczyła cała reszta"

                    "Drzwi dla personelu" if inventory.has_item(Wytrych) == True:
                        p "Na szczęście mam wytrych przy sobie"
                        p "Fiku foku loku picku"
                        $ inventory.remove_item(Wytrych)
                        "Zręczne palce koniobijcy pomogły Ci otworzyć drzwi"
                        "Panowie, zapraszam"
                        $ helper -= 20

                    "Wentylacja" if stan["Gun"] > 5:
                        p "Gun, możesz wentować?"
                        show gun
                        g "Dlaczego ja?"
                        p "W kombosach do KTG jesteś w spiskowcach a to jednak jest trochę sus"
                        g "To ma sers"
                        $ helper -= 25
                        hide gun
                        scene agunus
                        g "Kurwa, ciemno tu! O! Jest chyba wyjście"
                        "Gun skończył wentować"
                        g "Przycisk z napisem tajne vejście a se kliknę"
                        "I dzięki temu, reszta drużyny dostała się do środka"

                scene vards
                "Jesteście przy drzwiach 2"
                "Zbliżając się, usłyszeliście vrażników"
                v "Vrombał bym coś"
                v "Vejm"
                v "Vo voviesz na vot-voga?"
                v "Vybornie"
                p "Trzeba się ich pozbyć. Tylko jak to zrobię?"
                menu:
                    "Atak frontalny":
                        p "Za hordę"
                        "AAAAAAAA"
                        call checkHP(10) from _call_checkHP_20
                        "Dzielnie szturmowaliście parę Vist"
                        "Niestety jeden z vist miał przy sobie terminal"
                        $ edki = 0
                        "I w taki sposób zabrał Ci wszystkie pieniądze"
                        $ helper -= 5
                        
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
                        v "Vo Volera! Darmowy granat"
                        v "Jest mój"
                        v "Nie jest mój"
                        "Dzika bijatyka się zaczęła i Visty wybiły się ze sceny"


                    "Kałach, dywersja" if stan["Kalach"] > 5:
                        show kalach
                        k "Hej seksiaki"
                        v "O, siemka Kałach, co tam"
                        k "A vista z hot-dogami przyjechał"
                        v "VO VOLERA! VUSZAMY VIELNIE"
                        "I dzielnie vybiegli"
                        $ helper -= 25
                        p "Dobra robota Kałach"
                        k "Wiem"
                        hide kalach

                scene vezuwiusz
                "Przeszliście przez straż. Idziecie dalej przez gniazdo i dzielnie dostrzegasz znak vaboratorium"
                p "Chopaky, jesteśmy na miejscu! Pora zrobić rozpierdol"
                menu:
                    "Jak spacyfikuję laba"
                    "Atak frontalny":
                        call checkHP(5) from _call_checkHP_19
                        "Wbiegliście do środka atakując każdego Vistę w okolicy"
                        $ helper -= 10

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
                        "I tak jak przewidywałeś, jebnął go prąd"
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
                        kr "Ni Chu Ja! Hadong! Boom szakalaka!"
                        kr "Walę Vistę prosto w ptaka"
                        play sound "hit1.ogg"
                        "Brazylijska sztuka walki rozgromiła Visty ale sam Krateus też trochę oberwał (głównie od siebie)"
                        p "Myślałeś może o poprawieniu celności?"
                        kr "Bracie, w Brazyli było gorzej"
                        hide krateus
                        $ helper -= 10

                    "Łaskawca, anestezja bojowa" if stan["Laskawca"] > 5:
                        show laskawca
                        pl "Się robi"
                        "Łaskawca podszedł pod szyb i dał trochę gazu"
                        v "Vopaki, vide vpać. Vamimir"
                        pl "Słodkich snów chuje"
                        p "Jeszcze cukrzycy dostaną"
                        pl "Jakieś minusy?"
                        p "Nie wiemy jaki wpływ ma nadmiar insuliny na środowisko Vista"
                        pl "To jest sprawa oczywista, będą grubi. Dzięki temu będą słabsi w unikaniu"
                        $ helper -= 25
                        hide laskawca

                "Laboratorium jest wasze. Badając dokumenty odkryłeś vistowy plan"
                p "Oni są tak głupi że ja pierdolę. Próbowali wrzucić Guna do wulkanu"
                p "I tak chcieli przywołać boga gniewu. No debile"
                "Po przeszukiwaniu postanowiliście wysadzić laba. Szybki trik i cały lab się wyjebie za pięć minut"
                p "Spierdalamy"
                "Zaczęliście biec do wyjścia ale na waszej drodze stanął VPrime"
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
                        "I w taki sposób wyszliście z vazy"
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
                        v "Co kurwa? Jak ty niby chcesz zrzucić bombę w budynku?"
                        v "Jakby, tu nie ma jak wlecieć a jak spadnie na dach to chuja mi zrobić"
                        v "Kurwa, przecież Cypher stoi obok. To nie ma prawa działać"
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
                        g "Kupiłem szczurom RC autko i Hartmann podczepił minę p.piech"
                        p "Sprytne"
                        stop music
                        play music "CMS.mp3" volume 0.2
                        $ helper -= 20
                        jump akt1pods

            "Na głośno":
                p "Kurwa chłopaki, nie pierdolimy się w tańcu! Zapierdalamy na nich"
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
                        $ helper -= 15

                    "Kałach bazooka" if stan["Kalach"] > 5:
                        show kalach at left
                        k "Boom, boom, boom, boom I'm going to Coom"
                        "I Kałach wystrzelił ale rakieta wybuchła fajerwerkami"
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
                        kr "Los españoles necesitan ayuda! Cavador, tienes que cavar"
                        kr "Artillero, nos están cubriendo i teraz atak ostateczny"
                        kr "Ekspansja domeny: KRATA DZIKA"
                        mg "Przyjmuję twoją ofertę"
                        kr "Otwarte"
                        "I drzwi się otworzyły"
                        p "Jak ty to zrobiłeś?"
                        kr "Battle pass słonko"
                        $ helper -= 25

                    "Gun, miej fun" if stan["Gun"] > 5:
                        show gun at left
                        g "Tajest ale zaskoczę was wszystkich, tym razem nie prowadzę"
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
                        g "O CHOLERA, ON ŻYJE! RATTER POTTER"
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
                        "Możesz dzielnie iść dalej ale nie możesz zapomnieć o lootowaniu"
                        $ edki += 150
                        "Trochę mamony się znalazło"
                        $ inventory.add_item(AR)
                        $ inventory.add_item(Vron)
                        $ vdolce += 3
                        "I trochę Vidolcy"
                        $ helper -= 20

                    "Pora Geentować" if stan["Laskawca"] > 5:
                        show laskawca at left
                        pl "Się robi"
                        "Łaskawca zaczął strzelać na oślep. Trafił wszystkie 11 strzałów"
                        "Spytasz się, jak 11 strzałów na 10 vist. Odpowiedź jest bardzo prosta"
                        "Jeśli kiedykolwiek będzie kombat w którym Gun nie dostanie rykoszetu"
                        "To się chyba posram."
                        g "Aua ):"
                        $ helper -= 15

                    "Hartmann! Spaw bojowy" if stan["Hartmann"] > 5:
                        show hartmann at left
                        h "No to spawamy! Ja nie wiem co to jest rzecz niemożliwa. Fach w ręku, tak bywa"
                        h "Czasem beton, cementem się spawa, Czasem, Visty się doprawia"
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
                                $ session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
                                $ persistent.czasGry += session_time
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
                                $ inventory.remove_item(NRG)
                                mg "Oj kolego, kupiłeś mnie tym jak paczkę żelków. Oto moje błogosławieństwo"
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
                                mg "Ambitnie. Przyjmuję tę ofertę"
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
                "Ich głównymi składnikami są ocet i soda kuchenna. Oznacza to zagrożenie poziomu Demon"
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
                        call cipflash from _call_cipflash_16
                        mg "Obrzydzasz mnie"
                        "Wypiłeś cały ocet jaki mieli"
                        "Dzięki twojej brawurze visty poniosły straty finansowe"
                        "Całe 4,50 w plecy"
                        play sound "BURP.mp3"
                        p "To chyba tyle. Misja wykonana. Możemy wychodzić"
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
                        p "No dobra, punkt dla Ciebie. To wychodzi na to, że żadnego zagrożenia nie ma"
                        p "Spermastycznie. Wychodzimy!"
                        "I spokojnym krokiem wyszliście z pomieszczenia"
                        $ helper -= 15

                    "Zrobię delikatny trolaż" if inventory.has_item(Kokos):
                        p "Mam taki śmieszny pomysł"
                        "Podszedłeś do stołu i zamieniłeś sodę na koks"
                        p "Co prawda wychodzę przez to na minus ale będzie śmiesznie jak im to nie zadziała"
                        "Po delikatnym sabotażu wyszliście z vazy"
                        $ helper -= 20

                p "Kurwa panowie, to było zajebiście łatwe"
                v "Vie Vwal vnia vrzed vachodem vłońca"
                p "Co kurwa"
                scene vinalvoss
                stop music
                play music "bossa.mp3"
                v "Vestem V-Max. Vopowa vakość V"
                p "Oj nie zesraj się"
                v "Va vóźno"
                "Widzisz jak V-Max się powiększa"
                p "No tak, chuj mi w dupę"
                v "Va Va Va! Vykuj vię va vmierć"
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
                        kr "Właśnie nie, oni celują w głowę ale tam jest ciężka amunicja"
                        p "Ale głupota"
                        kr "No. Dlatego ja polegam na pięściach"
                        v "Vo vo vo ven ved-valk?"
                        kr "Dla jajec"
                        v "V vensie"
                        "Przez całą pogadankę Kreteus zbliżał się do V-Maxa"
                        kr "Egg stiler"
                        v "Vvaaaaaaaaaa"
                        kr "Turbo kręcenie wora! I teraz finiszer, cios prosto w prostatę"
                        play sound "Bonk.mp3"
                        scene black
                        "Ze względu na brutalną naturę tej sceny zastąpiłem ją opisem jajec"
                        "Wielkie i czerwone jak pomidory"
                        "Dziękuję za uwagę"
                        show krateus
                        kr "Kurwa, chyba przesadziłem"
                        p "Chłopie, tortury Trewora były bardziej ludzkie"
                        kr "Serio?"
                        p "No, chodźmy stąd, muszę chyba iść na terapię"
                        kr "No sorson, ale jak to pisze jest miesiąc geja, przez to nie mam hamulców"
                        $ helper -= 10
                        jump akt1pods

                    "Volololo" if stan["Kalach"] > 5:
                        k "Niech będą pochwalone uda. I jak powiedział kiedyś prorok:"
                        k "„Błogosławione uda, które nie postępują w radzie bezbożnych, ani nie stoją na drodze bonera, ani nie siedzą na tronie simpów. Ale jego upodobanie jest w prawie THICC Ud!"
                        v "Vo vy vierdolisz?"
                        k "Twoją matkę"
                        v "Vooooo! Vylko vie voją vamusie! Varża"
                        k "Vistolo volololo"
                        v "Vo vaj vad"
                        "Takim dziwnym sposobem V-Max dołączył do drużyny"
                        v "Vitam vanowie. Vychodzimy?"
                        p "Wychodzimy"
                        "Wychodzicie z vazy"
                        v "Vo vo vak vikło?"
                        p "VMax nieee"
                        "I Vistę vysadziło"
                        "Vista opuszcza drużynę"
                        $ helper -= 15
                        jump akt1pods
                        

    elif Frakcja == 1:
        $ oldFrakcja = 1
        show cypher
        c "Hihi ha ha"
        c "Pozwól młody że ja zajmę się dowodzeniem"
        p "No spoko, szefie"
        c "Szybko się uczysz, będą z Ciebie psy. Diamentowe takie"
        scene cypherkopter
        play sound "heli.mp3"
        "Pyr pyr pyr"
        p "Gdzie my lecimy?"
        c "To jest ważna misja! Lecimy do żabki!"
        stop sound
        scene frogszop
        stop music
        play music "szop.mp3"
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
        fse "Są mochery płacące rachunki są żule i w ogóle"
        fse "Dramat wielki"
        p "Faktycznie brzmi strasznie"
        fse "No. Cieszę się że mam tu ochronę. Jest dzielny Kacperek, siedzi tam z tyłu"
        fse "Cały dzień obstawia mecze ale jak jest potrzeba to przychodzi"
        c "Szajse ale tu jest duży wybór! Ponętne towary, chciałbym nabyć je wszystkie" 
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
        fse "Macie kurcze szczęście, grubcio zaczął już wstawać"
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
        c "Proszę proszę, tożto laboratorium! Sprawdźmy to"
        p "Dobrze Cypher"
        c "Kurwa, oczekiwałem jakiegoś entuzjazmu! Dobra jebać. Dawaj do środka"
        "Weszliście do środka"
        c "CO TO KURWA JEST"
        p "W sensie?"
        c "CZY TY TEGO KURWA NIE WIDZISZ? TE SKURWYSYNY DOMALOWAŁY MI WĄSY"
        p "Zabawne"
        c "A CI PIERDOLNE! TO JEST ATAK NA MÓJ WIZERUNEK"
        c "PRZYSTOJNEGO PATRIOTY I WYCHODZI JAKIŚ CHUJ Z WĄSEM"
        c "ABSOLUTNIE NIEWYBACZALNE"
        p "Spokojnie"
        c "JAK JA MAM BYĆ KURWA SPOKOJNY?"
        p "O patrz"
        "Podszedłeś do plakatu i oderwałeś wąs"
        scene vezuwiusz
        show cypher
        c "No dobra, uspokoiłem się"
        p "Serio?"
        c "NIE KURWA. JEDYNYM WEZUWIUSZEM TU JESTEM JA! ROZPIERDOLĘ ICH"
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
            p "Ty kurwa, ja mam Vombe! Rozpierdolę ich ich własną bronią"
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
        v "Vozjebaliście vi vazę, vniszczyliście vasze vadania"
        v "Vrujnowaliście vój vom v vabiliście voich vrzyjaciół"
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
        c "Ale nie umarłeś i to się liczy"
        c "Zaczynam cię lubić [player_name]"
        hide hellciper
        show cypher
        $ postacie["Cypher"] += 3
        p "Wracajmy już do domu"
        call cipflash from _call_cipflash_17
        c "Tak wcześnie?"
        p "No zrobiliśmy to co mieliśmy"
        c "Nudziaż! Jednak mi się nie podobasz"
        c "Wracasz z buta ja lecę do żabki"
        c "Jak to mówimy w niemczech, Adios"
        "I Cypher odleciał"
        p "Adios jest po Hiszpańsku"
        jump akt1pods

    elif Frakcja == 3:
        $ oldFrakcja = 3
        p "Dobra kurwa, jestem Vista"
        p "Nie mogę pozwolić aby nasze tajne projekty zostały zniszczone ale z drugiej strony"
        p "Nikt mi za obronę nie płaci. Co powinienem zrobić?"
        menu:
            "Pozostań V":
                p "Dobra kurwa, co ja teraz zrobię. Zawsze jest opcja kulki w łep"
                p "Ale to zostawię sobię na potem"
                p "Wiem kurwa!"
                p "Zadzwonię do Vistów i powiem im żeby spierdalali. Następnie ściągniemy tam VMaxów"
                p "Jak oni tam wejdom to sie zesrają! Hihihaha"
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
                pl "Dobra spokojnie, wchodzimy. Ciekawe czemu [player_name] nie jest z nami"
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
                k "Koło chuja mi to lata! Wypierdalasz na tamagoczi"
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
        $ oldFrakcja = 4
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
        k "Ta, to tylko Visty, nie chce mi się marnować ammo plus, Vista jest śmieszny"
        p "Jakim cudem ty jesteś jeszcze głową tego kościoła?"
        k "Niebotyczna charyzma, inteligencja Ejnsztajna i wątroba z tytanu"
        p "Tylko tyle wystarczy?"
        k "Jakie kurwa tylko tyle? Chopie, to jest w chuj pracy. Raz na dwa dni muszę wrzucać zdjęcie na stronę"
        k "Skurwysyńsko męcząca praca"
        p "Się znalazł influenser po chuju"
        k "TO PATRZ I SIĘ KURWA UCZ"
        "Kałach sam poszedł prosto do gniazda"
        p "Popierdoliło go albo promile nie są już procentami"
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
        k "W imię ojca, i syna i uda wielkiego! Niech wpierdol dosięgnie jego"
        v "Vo Vhuj Vi vodzi?"
        k "Specjalny atak Alfonsowy! Pora na udowy atak krzyżowy"
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
                $ Frakcja = 0
                $ oldFrakcja = 6
                jump wojowezadanie

            "Może uciekniemy stąd razem?":
                fse "OMG Anon, myślałam o tym odkąd Cię zobaczyłam"
                p "No to klawo, spierdalajmy"
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
    p "Kurwa, chyba tu umrę. Powiedz mojej żonie, że jej nie mam"
    p "Karamba, całe życie przeleciało mi przed oczami. Chyba za dużo grałem na kompie"
    "Podszedł do Ciebie jakiś mężczyzna ubrany na czarno"
    sb "A kogo my tu mamy [player_name] jak na talerzu"
    sb "To nie jest pora jeszcze umierać mam co do Ciebie plany"
    achieve GG1
    jump a2intro

label amongthev:
    stop music fadeout 1.0
    scene black
    if Frakcja != 1:
        p "Wysłali mnie prosto do wypizdowa. Nie dali jakichkolwiek wytycznych"
        p "Wiem że mam wykraść coś z archiw. Przyjaciele po chuju ale chuj, podobno dostanę 2k edków"
    
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
    v "Vitam v vlubie! Vestem Viesiek vędę vwoim vrzewodnikiem"
    v "Vprowadzę Vię vo vokolicy"
    show vechnik
    v "Vutaj vamy vechnika vie vrzeszkadzaj vu vepiej. Vak vo vkurwisz, vo Vi veszcze Vpierdoli"
    hide vechnik
    v "Vobra, przejdź się po okolicy, poszukaj dla siebie roboty"
    v "Vajo"
    $ bigquest = 1
    hide vista
    jump vtimefri


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
        v "Nie no, yaycuję. W tym obozie nic nie ma za darmo ale możesz wykonać dla mnie bojowe zadanie"
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
                $ varchiwa_stage = 2
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
                    $ persistent.dywanomierz += 1
                    "Kliknąłeś już ten jebany dyvan [persistent.dywanomierz] razy"
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
        "Vygrałeś, reszta się Vystraszyła"
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
    v "Vózg v vłynie jest skuteczny, muszę vodziękować Vanowi. Vestem viekav, co jeszcze ugotuje"
    p "Kinda sus, ngl. Co oni tu jeszcze mają?"
    "Kolejny dokument"
    v "Vroń testowa jest strasznie vujowa. Vechnikowi powinienem urwać yaya i yondra!"
    v "Vstrzeliłem i nic się nie stało. Vkurwiam się, vopierdoli mnie"
    p "Lmao rip"
    p "O coś jeszcze ciekawego"
    v "Populacja V vnosi około 20 tysięcy. Mnożymy się jak świeże bułeczki"
    v "Jeszcze pół roku i Arasaka straci nad nami vładzę ale my musimy jeszcze czekać jak karaczany"
    v "Va szczęście dołączenie do naszej społeczności nie jest trudne. Vstarczy vpisać vardcorevorn.vom"
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
                    g "Na raty chrystusa, ty żyjesz! Znaczy ten, gRATulacje, udało Ci się"
                    g "Zobaczmy co tam przyniosłeś ciekawego"
                    "Oddałeś podrobione papiery"
                    g "Oj karamba, grube dowody. Prawie zapomłem, oto twoja nagroda"
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
        g "Na raty chrystusa, ty żyjesz! Znaczy ten, gRATulacje, udało Ci się"
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
        g "Dobra, nie pierdol. Od teraz jesteś prawdziwym bazownikiem"
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
        c "Pojebało Cię"
        hide cypher with dissolve
        jump kuchnia
