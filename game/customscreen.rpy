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
        pos (0.05, 0.1)
        text "Pojemność [inventory.quantity]/[Cap]"

    grid 20 5: 
        pos (0.1, 0.25)
        spacing 20
        for item in inventory.items:
            frame:
                padding (10, 10)
                vbox:
                    spacing 5
                    xalign 0.5
                    imagebutton:
                        idle item.image
                        hover item.image
                        action Show("item_details", item=item)

    
    imagebutton auto "inventory_screen_return_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("inventory"), Show("hud"), Play("sound", "opi.wav")

screen item_details(item):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        vbox:
            spacing 10
            xalign 0.5
            image item.image
            text "[item.name]" size 40
            text "[item.desc]" size 30
            textbutton "Wyrzuć" action Hide("item_details"), Function(drop_item, item)
            textbutton _("Zamknij") action Hide("item_details")


screen phone():
    add "tapety/bg1.png"
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
    
    imagebutton auto "cyberfon_postac_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("postac")

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("hud")

screen znaj():
    modal True
    add "tapety/bg1.png"
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        if akt == 1:
            text "{color=000}Cypher: [postacie['Cypher']] \n Kałach: [postacie['Kalach']] \n Gun: [postacie['Gun']] \n Hartmann: [postacie['Hartmann']] \n Łaskawca: [postacie['Laskawca']] \n Krateus: [postacie['Krateus']] \n Jhin: [postacie['Jhin']]"
        else:
            text "{color=000} Nie wiem czy muszę się \n z nimi zaprzyjaźniać"
        if znajOkol > 1:
            text "{color=000} Żabiara: [frogrel] \n"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("znaj"), Show("phone")

screen day():
    modal True
    add "tapety/bg1.png"
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
            if bigquest == 0:
                text "{color=000} Zdobądź [5-chipy] chipów"

            elif bigquest == 1:
                text "{color=000} Odzyskaj dane z bazy"
                if stan2["Bo"] == 1 or stan2["Bo"] == 3 or (stan2["Bo"] == 4 and stan2["Kris"] == 5) or stan2["Bo"] == 5:
                    text "{color=000} Idź do bazy"

                if stan2["Bo"] == 2:
                    text "{color=000} Czekaj na SMS"

            elif bigquest == 2:
                if stan2["BB"] == 0 or stan2["BB"] == 1 or stan2["BB"] == 2:
                    text "{color=000} Pracuj dla Pierdexu"

                if stan2["BB"] < 4:
                    text "{color=000} Przywieź Cypherowi ser"

                if stan2["BB"] < 5:
                    text "{color=000} Daj Cypherowi 500 edków"

                if stan2["BB"] < 6:
                    text "{color=000} Weź Itemki od Cyphera"
                
                if stan2["BB"] < 7:
                    text "{color=000} Dostarcz paczkę do Jax-a"

                if stan2["BB"] < 8:
                    text "{color=000} Wracaj do Cyphera"

                if stan2["BB"] < 9:
                    text "{color=000} Pogadaj z szefem"


    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("day"), Show("phone")

screen bank():
    modal True
    add "tapety/bg1.png"
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.1
        text "{color=000} Masz na koncie [edki] edków"
        text "{color=000} Masz na koncie [vdolce] Vdolców"
        text "{color=000} Masz na koncie [frogsy] frogsów"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("bank"), Show("phone")

screen frak():
    modal True
    add "tapety/bg1.png"
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

screen postac():
    modal True
    add "tapety/bg1.png"
    add "cyberfon_clear"
    vbox:
        pos 0.4, 0.10
        text "{color=000}HP: [HP]/[MaxHP]"
    if akt > 1:
        vbox:
            pos 0.4, 0.13
            text "{color=000} Twoje cechy"
            text "{color=000} Budowa ciała: [cechy['BC']]"
            text "{color=000} Zwinność: [cechy['ZW']]"
            text "{color=000} Charakter [cechy['CHAR']]"
            text "{color=000} Umysł [cechy['INT']]"

        vbox:
            pos 0.4, 0.32
            text "{color=000} Twoje umiejętności"
            text "{color=000} Strzelanie: [skile['Bron']]"
            text "{color=000} Gadanie: [skile['Gadanie']]"
            text "{color=000} Spierdalanie: [skile['Atletyka']]"
            text "{color=000} Myślenie: [skile['Myslenie']]"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("postac"), Show("phone")

screen map_screen():
    add "mapa.png"
    modal True

    if akt == 1:
        imagebutton auto "city_dom_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("rozstaje")
    if czas > 4:
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

    if jajca == 1:
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

    if akt == 2 and bigquest == 2: 
        imagebutton auto "city_pierd_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("pierdex")

    if chipy < chiplok:
        imagebutton auto "city_chip_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("chipnik")

    if akt == 2 and bigquest > 0:
        imagebutton auto "city_dom_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip", "Return")
            unhovered SetVariable("screen_tooltip","")
            action Hide("map_screen"), Jump("anomalia")

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
