screen hud():
    modal False

    imagebutton auto "bg_hud_inventory_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Inventory")
        unhovered SetVariable("screen_tooltip", "")
        action Play("sound", "opi.wav"), Show("inventory") , Hide("hud")

    imagebutton auto "phone_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "phone")
        unhovered SetVariable("screen_tooltip", "")
        action Show("phone"), Hide("hud")

screen inventory():
    add "bg_inventory_screen"
    modal True

    vbox:
        pos 0.05, 0.1
        text "Pojemność [inventory.quantity]/[Cap]"

    vbox:
        pos 0.1, 0.25
        for item in inventory.items:
            text "{size=40}[item.name] - [item.desc] \n{/size}"

    imagebutton auto "inventory_yeet_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Call("yeet")

    imagebutton auto "inventory_screen_return_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("inventory"), Show("hud"), Play("sound", "opi.wav")


screen phone():
    add "cyberfon_clear.png"
    modal True
    
    imagebutton auto "cyberfon_znaj_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("znaj")
    
    imagebutton auto "cyberfon_frak_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("frak")

    imagebutton auto "cyberfon_hajs_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("bank")

    imagebutton auto "cyberfon_day_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("day")
    
    if akt > 1:
        imagebutton auto "cyberfon_cechy_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("phone"), Show("cechy")

        imagebutton auto "cyberfon_skil_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("phone"), Show("skile")
    if kody < 6:
        imagebutton auto "cyberfon_kody_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("phone"), Show("kody")

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("hud")

screen znaj():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        if akt == 1:
            text "{color=000}Cypher: [postacie['Cypher']] \n Kałach: [postacie['Kalach']] \n Gun: [postacie['Gun']] \n Hartmann: [postacie['Hartmann']] \n Łaskawca: [postacie['Laskawca']] \n Krateus: [postacie['Krateus']] \n Jhin: [postacie['Jhin']]"
        else:
            text "{color=000} Nie wiem czy muszę się \n z nimi zaprzyjaźniać"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("znaj"), Show("phone")

screen day():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Dzień: [dzien] \n"
        if dzien % 7 == 0:
            text "{color=000} Poniedziałek"
        elif dzien % 7 == 1:
            text "{color=000} Wtorek"
        elif dzien % 7 == 2:
            text "{color=000} Środa"
        elif dzien % 7 == 3:
            text "{color=000} Czwartek"
        elif dzien % 7 == 4:
            text "{color=000} Piątek"
        elif dzien % 7 == 5:
            text "{color=000} Sobota"
        elif dzien % 7 == 6:
            text "{color=000} Niedziela"
        if czas > 0:
            text "{color=000} Zostało mi jeszcze [czas] \n jednostek czasu"
        elif czas < 1:
            text "{color=000} Mama każe iść spać"

        text "{color=000}\n Aktualne zadanie:"
        if akt == 1:
            if bigquest == 0:
                if dzien == 3:
                    text "{color=000} Przyjdź do Guna jutro"

                elif dzien < 3:
                    text "{color=000} Przyjdź do Guna za [4-dzien] dni"        

                elif dzien > 3:
                    text "{color=000} Idź do Guna"

            elif bigquest == 1:
                text "{color=000}Ukradnij intel z archiv"

            elif bigquest == 2:
                text "{color=000}Uciekaj z tego \n pozbawionego boga miejsca"

            elif bigquest == 3:
                if dzien == 9:
                    text "{color=000}Wróć do Guna jutro"

                elif dzien < 10:
                    text "{color=000}Wróć do guna za [10-dzien] dni"

                elif dzien > 9:
                    text "{color=000} Idź do Guna"

            elif bigquest == 4:
                text "{color=000} Idź do wojska"

            elif bigquest == 5:
                text "{color=000} Zaprzyjażnij się z dzbanami, \n zostali Ci jeszcze:"
                if stan["Gun"] < 5:
                    text "{color=000} Gun"
                
                if stan["Kalach"] < 5:
                    text "{color=000} Kałach"

                if stan["Hartmann"] < 5:
                    text "{color=000} Hartmann"

                if stan["Jhin"] < 4:
                    text "{color=000} Jhin"

                if stan["Cypher"] < 5:
                    text "{color=000} Cypher"

                if stan["Krateus"] < 5:
                    text "{color=000} Krateus"

        elif akt == 2:
            if bigquest == 1:
                text "{color=000} Zdobądż [5-chipy] chipów"


    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("day"), Show("phone")

screen bank():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Masz na koncie [edki] edków"
        text "{color=000} Masz na koncie [vdolce] Vdolców"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("bank"), Show("phone")

screen frak():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Należysz do:"
        if Frakcja == 0:
            text "{color=000} Nikogo"
        elif Frakcja == 1:
            text "{color=000} DiamandHunde"
        elif Frakcja == 2:
            text "{color=000} Draco Nero"
        elif Frakcja == 3:
            text "{color=000} Vist"
        elif Frakcja == 4:
            text "{color=000} Kościołu Ud"
        elif Frakcja == 6:
            text "{color=000} Żabki"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("frak"), Show("phone")

screen cechy():
    modal True
    add "cyberfon_clear"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Twoje cechy"
        text "{color=000} Budowa ciała: [cechy['BC']]"
        text "{color=000} Zwinność: [cechy['ZW']]"
        text "{color=000} Charakter [cechy['CHAR']]"
        text "{color=000} Umysł [cechy['INT']]"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("cechy"), Show("phone")

screen skile():
    modal True
    add "cyberfon_clear"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Twoje umiejętności"
        text "{color=000} Strzelanie: [skile['Bron']]"
        text "{color=000} Gadanie: [skile['Gadanie']]"
        text "{color=000} Spierdalanie: [skile['Atletyka']]"
        text "{color=000} Myślenie: [skile['Myslenie']]"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("skile"), Show("phone")


screen kody():
    modal True
    add "cyberfon_clear.png"

    if kody < 5:
        if nua > 4:
            imagebutton auto "cyberfon_kody_hajs_%s":
                focus_mask True
                hovered SetVariable("screen_tooltip", "Return")
                unhovered SetVariable("screen_tooltip","")
                action IncrementVariable("edki",500), IncrementVariable("kody",1)

        if nua > 9:
            imagebutton auto "cyberfon_kody_spac_%s":
                focus_mask True
                hovered SetVariable("screen_tooltip", "Return")
                unhovered SetVariable("screen_tooltip","")
                action IncrementVariable("cap",1), IncrementVariable("kody",1)

        if nua > 19 and akt > 1:
            imagebutton auto "cyberfon_kody_exp_%s":
                focus_mask True
                hovered SetVariable("screen_tooltip", "Return")
                unhovered SetVariable("screen_tooltip","")
                action IncrementVariable("exp",10), IncrementVariable("kody",1)

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("kody"), Show("phone")

screen map_screen():
    add "mapa.png"
    modal True

    if akt == 1:
        imagebutton auto "city_dom_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("rozstaje")

    imagebutton auto "city_tup_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("map_screen"), Call("spacerek")

    if znajOkol > 0:
        imagebutton auto "city_sklep_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Call("trader")

    if znajOkol > 1:
        imagebutton auto "city_zab_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Call("frogszop")

    if znajOkol > 2:
        imagebutton auto "city_wor_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Call("workowiec")

    if znajOkol > 3:
        imagebutton auto "city_jajo_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Call("jajquest")

    if Frakcja == 3:
        imagebutton auto "city_vlok_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Call("vradeZewn")

    if bigquest > 3 and akt == 1:
        imagebutton auto "city_army_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("wojsko")

    if akt == 2:
        imagebutton auto "city_hid_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("opor")

    if chipy == 0 and chiplok == 1 or chipy == 1 and chiplok == 2 or chipy == 2 and chiplok == 3 or chipy == 3 and chiplok == 4 or chipy == 4 and chiplok == 5:
        imagebutton auto "city_chip_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("chipnik")

screen oportalk():
    add "opor"
    modal True

    imagebutton auto "opor_kris_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("oportalk"), Call("krzis")

    imagebutton auto "opor_jax_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("oportalk"), Call("jaxowo")

    imagebutton auto "opor_vio_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("oportalk"), Call("viocha")

    imagebutton auto "opor_wlas_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("oportalk"), Show("map_screen")

    imagebutton auto "opor_slep_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("oportalk"), Call("oporslep")