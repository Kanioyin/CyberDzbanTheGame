# postacie
define c = Character(_("Cypher"), color="#00FFF7")
define g = Character(_("Gun"), color = "#3f4140")
define h = Character(_("Hartmann"), color = "#1945FF")
define pl = Character(_("Łaskawca"), color = "#696969")
define k = Character(_("Kałach"),color="#FF00FF")
define p = Character(_("[player_name]"))
define r = Character(_("Szczur"),color="#123456")
define j = Character(_("Jhin"),color = "#444444")
define v = Character(_("Vista"), color = "#213769")
define t = Character(_("Toro"), color = "#6969EE")
define gk = Character(_("Gen. Kennedy"), color = "#098703")
define kr = Character(_("Krateus"), color = "#023a10")
define mg = Character(_("Wielki Dzik"), color = "#482809")
define fse = Character(_("[baba_name]"), color = "#006600")
define sb = Character(_("Ktoś"), color = "#77036d")
define gr = Character(_("Grupa"), color = "#324511")
define cr = Character(_("Kris"), color = "#EE0000")
define ja = Character(_("Jax"), color = "#e4adf1")
define vi = Character(_("VIO"), color = "#ffbcbc")
define ec = Character(_("Evil Cypher"), color = "#FF0009")
define gkp = Character(_("Gatekeeper"), color = "#213213")
define be = Character(_("Szybki Ben"), color = "#ed4040")
define au = Character(_("Automatoniks"), color = "#383303")
define bo = Character(_("Borubabor"), color = "#abba69")
define ha = Character(_("Halina"), color = "#423123")
define bb = Character(_("Blink Blink"), color = "#3ef374")
define wr = Character(_("Wróżbitka"), color = "#f04eda")

# słowniki
default postacie = {"Kalach":0, "Gun":0, "Cypher":0, "Laskawca":0, "Hartmann":0, "Jhin":0, "Visty":0, "Kennedy":0, "Krateus":0}
default cechy = {"INT":2, "ZW":2, "CHAR":2,"BC":2}
default skile = {"Atletyka": 2, "Bron": 2, "Gadanie": 2, "Myslenie": 2}
default stan = {"Kalach":0, "Gun":0, "Cypher":0, "Laskawca":0, "Hartmann":0, "Jhin":0, "Visty":0, "Kennedy":0, "Krateus":0, "Kasia":0}

# inventory
default inventory = Inventory([],0)

# przedmioty
default AR = InventoryItem("AR", "Fajny karabin", "itemy/AR.png")
default Rat = InventoryItem("Szczur", "Grube bydle", "itemy/Rat.png")
default Flaszka = InventoryItem("Flacha", "Najlepszy przyjaciel Kałacha", "itemy/Flacha.png")
default Kokos = InventoryItem("Kokos","Tak na prawdę to kokaina","itemy/Koks.png")
default Pistolecik = InventoryItem("Pistolet","Prosta tania broń","itemy/Pistol.png")
default Granat = InventoryItem("Granat","Mały gadżet, robiący bum","itemy/Gran.png")
default Klapek = InventoryItem("Klapek","Klapek z twarzą Cyphera. Nie dotykałbym tego", "itemy/Klap.png")
default MalyArmor = InventoryItem("Pancerz","Standardowy cyberowy armor","itemy/Armor.png")
default Vron = InventoryItem("Vroń","Współczuję zakupu","itemy/Vron.png")
default Wytrych = InventoryItem("Wytrych","Cudowny sprzęt do otwierania drzwi i nie tylko","itemy/Lockp.png")
default Vomba = InventoryItem("Bomba","Bomba, tylko produkcji Vist","itemy/Vomb.png")
default Vranat = InventoryItem("Vranat","Wabajack tego uniwersum","itemy/Vran.png")
default Ser = InventoryItem("Ser","Strasznie cheesy, Gun musi go lubić", "itemy/Ser.png")
default THeal = InventoryItem("Turbouzdrawiacz","Turbo uzdrawia","itemy/THeal.png")
default NRG = InventoryItem("Energol","Waluta permium","itemy/Dzik.png")
default HuMeat = InventoryItem("Ludzkie mięso","VIO chętnie to schrupie","itemy/HMeat.png")
default Smoke = InventoryItem("Bomba dymna", "Taki szlug, tylko nie psuje płuc","itemy/Smoke.png")
default RadArm = InventoryItem("Hazmat", "Pancerz przeciw radjacji","Itemy/Hazmat.png")
default Kwiat = InventoryItem("Kwiatki", "Działają na kobiety jak dzik na MG","itemy/Kwiat.png")

#Stany postaci
default kibel_stan = 0
default wojsko_stan = 0
default persistent.dywanomierz = 0

#deklaracja reszty
default persistent.czasGry = 0
default persistent.session_start_time = 0
default persistent.monsters = 0
default persistent.skracz = 0
default persistent.work = 0
default edki = 0
default vdolce = 0
default frogsy = 0
default MaxHP = 20
default Fragi = 0
default akt = 0
default HP = 0
default Frakcja = 0
default oldFrakcja = 0
default tapeta = 0
# 0 = Niezrzeszony
# 1 = DH
# 2 = DN
# 3 = Visty
# 4 = Uda
# 5 = Wojsko
# 6 = Żabka
default Cap = 4
default dzien = 1
default armor = 0
default ammo = 0
default umieram = 0
default maxarmor = 0
default czas = 20
default veq = 0
default znajOkol = 0
# 1 = sklep
# 2 = żabka
# 3 = worek
# 4 = jaja
default lilquest = 0
default vrrr = 0
default bigquest = 0
default vron = 0
default helper = 1
default helper2 = 0
default part = 0
default testPass = 0
default kody = 0
default kompan = 0
# 0 = Nikt
# 1 = VIO
# 2 = JAX
# 3 = Borabor
default zawal = 0
default talkloop = 0
default chipy = 0
default chiplok = 0
default exp = 0
default wynik = 0
default odp = " "
default anom = 0
default frogrel = 0
default jajca = 0
default buul = ["bul1.mp3", "demon.mp3"]

# deklaracje co do V
default vechnik_stage = 0
default voktor_stage = 0
default varchiva_stage = 0
default valki = 5

# akt 2
default stan2 = {"Vio":0, "Jax":0, "Kris":0, "Bo":0, "Halina":0, "BB":0}
default postacie2 = {"Jax":0}
default atrefakty = {"Jaja":"szukane", "Kajdanki":"szukane"}