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
                k "Jak tam poszło? Postrzelałeś? Poruchałeś? Może coś popiłeś?"
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
                k "Niech mnie uda i zimna wóda! Wróciłeś żywy z siedliska Vist"
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
                    k "To zostaniesz zgilotynowany i granie Briar też się liczy."
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

            k "No witam witam. Przyszedłeś po przebaczenie grzechów?"
            p "Nie Kałachu, muszę zostać twoim przyjacielem"
            k "Co kurwa?"
            p "Kennedy szuka ludzi na misję a ja muszę się z wami zakumplować"
            if [player_name] == "Hubert":
                k "Kurwa Hubert, spierdalaj"
                $ stan["Kalach"] = 9
                jump rozstaje

            k "Łe dobra, nie strasz mnie kurwa. Już myślałem że Hubert gra"
            k "A wiesz, on jest fanem Yaoj a to nie jest dating sim tylko CPTG"
            k "Ale no dobra, nie chce mi się z tobą gadać"
            k "Powiedzmy, że jak będziemy musieli się napierdalać to masz mój karabin"
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
            k "Czego ty kurwa chcesz? Nie mam teraz czasu na gadanie"
            k "Spierdalaj"
            jump rozstaje

    jump rozstaje