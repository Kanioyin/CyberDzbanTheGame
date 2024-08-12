label a2intro:
    sb "Aj karamba, bolało"
    sb "Mam nadzeję, że jesteś cały"
    sb "Zobaczmy z czego jesteś zbudowany"
    menu:
        "Co jest moją mocną stroną?"
        "Siła":
            if helper == 0:
                $ cechy["BC"] = 6

            elif helper > 50:
                $ cechy["BC"] = 4

            elif helper > 0:
                $ cechy["BC"] = 5

        "Zwinność":
            if helper == 0:
                $ cechy["ZW"] = 6

            elif helper > 50:
                $ cechy["ZW"] = 4

            elif helper > 0:
                $ cechy["ZW"] = 5

        "Charyzma":
            if helper == 0:
                $ cechy["CHAR"] = 6

            elif helper > 50:
                $ cechy["CHAR"] = 4

            elif helper > 0:
                $ cechy["CHAR"] = 5

        "Mózg":
            $ cechy["Myslenie"] = 3
            if helper == 0:
                $ cechy["INT"] = 6

            elif helper > 50:
                $ cechy["INT"] = 4

            elif helper > 0:
                $ cechy["INT"] = 5

    menu:
        "Gdy trzeba walczyć, co robię?"
        "Strzelam":
            $ cechy["Bron"] = 4

        "Spierdalam":
            $ cechy["Atletyka"] = 4

        "Perswaduje":
            $ cechy["Gadanie"] = 4

    sb "No dobra, pora otworzyć oczy"
    scene opor
    show kris
    sb "Dzień dobry [player_name]"
    p "Kim ty kurwa jesteś?"
    sb "Faktycznie, wypada się przedstawić"
    sb "Krzysztof czerownopole"
    cr "Do usług"
    p "Dobra kurwa ale skąd ty wiesz jak ja się nazywam?"
    cr "Mam swoje źródła"
    show jax at left
    show vio at right
    cr "Oto przed tobą: Jax"
    ja "Witam"
    cr "I VIO"
    vi "Vitam"
    p "On nie jest kurwa Vistą?"
    vi "Jestem, takim udomowionym"
    p "Ok, zrozumiałe"