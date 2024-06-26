screen hud():
    modal False

    imagebutton auto "bg_hud_inventory_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Inventory")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventory") , Hide("hud")

    imagebutton auto "phone_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "phone")
        unhovered SetVariable("screen_tooltip", "")
        action Show("phone"), Hide("hud")

screen inventory():
    add "bg_inventory_screen"
    modal True

    vbox:
        pos 0.1, 0.25
        for item in inventory.items:
            text "{size=30}[item.name] - [item.desc] \n{/size}"

    imagebutton auto "inventory_screen_return_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("inventory"), Show("hud")

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

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("phone"), Show("hud")

screen znaj():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.25
        text "{color=000}Cypher: [postacie['Cypher']] \n Kałach: [postacie['Kalach']] \n Gun: [postacie['Gun']] \n Hartmann: [postacie['Hartmann']] \n Łaskawca: [postacie['Laskawca']] \n Krateus: [postacie['Krateus']] \n Jhin: [postacie['Jhin']]"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("znaj"), Show("phone")

screen day():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.25
        text "{color=000} Dzień: [dzien] \n"
        if czas > 0:
            text "{color=000} Zostało mi jeszcze [czas] \n jednostek czasu"
        elif czas < 1:
            text "{color=000} Mama każe iść spać"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("day"), Show("phone")

screen bank():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.25
        text "{color=000} Masz na koncie [edki] edków"

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("bank"), Show("phone")

screen frak():
    modal True
    add "cyberfon_clear.png"
    vbox:
        pos 0.4, 0.25
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

    imagebutton auto "cyberfon_won_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("frak"), Show("phone")

