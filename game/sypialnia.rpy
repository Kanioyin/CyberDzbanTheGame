label sypialnia:
    scene pokoj
    show screen hud
    call bigunl from _call_bigunl_1
    p "Pusto tu"
    menu:
        "Jesteś w swoim pokoju, co chcesz zrobić?"
        "Idę spać":
            call spanko from _call_spanko_1
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