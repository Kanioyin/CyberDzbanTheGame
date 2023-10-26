screen hud():
    modal False

    imagebutton auto "bg_hud_inventory_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Inventory")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventory") , Hide("hud")

screen inventory():
    add "bg_inventory_screen"
    modal True

    vbox:
        pos 0.1, 0.25
        for item in inventory.items:
            text "[item.name] - [item.desc] \n"

    imagebutton auto "inventory_screen_return_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip","")
        action Hide("inventory"), Show("hud")
