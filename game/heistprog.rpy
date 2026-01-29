
label heistprogsc:
    scene black
    mg "Takie delikatne info teraz dla Ciebie"
    mg "Teraz będziesz dawał polecenia swoim ziutkom"
    mg "W trakcie akcji, będzie się zwiększać ich poziom przypału"
    mg "Jak się nabije duży, to będą mięli problem"
    mg "Więc postaraj się dobrze decydować"
    scene spacer
    show jax at left
    show vio at right
    p "Dobra panowie, jedziemy z tym zadaniem"
    vi "Masz już jakiś plan przygotowany?"
    p "Na spokojnie, wszystko już sobie obmyślałem"
    vi "No niech będzie, wszyscy na łączach?"
    ja "Pewnie, że tak"
    p "Dobrze was słychać, możemy zaczynać powoli"
    p "Pamiętajcie, nie możemy panikować. Ben jest czujny jak pies podwójny"
    ja "I ma bardzo dobrych strażników przy sobie"
    vi "I ta jego lafirynda obserwuje zawsze co się dzieje"
    p "Będzie trzeba ich oślepić nim coś zrobimy"
    ja "Dobre podejście"
    scene kasyno
    p "Podejście pod miejście akcji"
    menu:
        p "Jak podchodzimy to tego zadania?"
        "Na przypale":
            p "Dobra panowie, plan jest prosty, wbijamy sobie głównym wejściem"
            vi "Oho, dobrze się zapowiada"
            p "Cicho, nie zapeszaj"
            p "Po wejściu, pogramy sobie trochę a później się rozdzielimy"
            p "Powoli będziemy progresować do pomieszczenia ze wszczepem"
            p "Tylko będzie trzeba się pozbyć tych jebanych kamer"
            menu:
                p "Kto wyłączy kamery?"
                "VIO":
                    p "Będziesz w stanie się ich pozbyć?"
                    vi "Jasna sprawa"
                    $ stan2["Vio"] = 1
                    $ stan2["Jax"] = 1

                "JAX":
                    p "Będziesz w stanie się ich pozbyć?"
                    vi "Jasna sprawa"
                    $ stan2["Jax"] = 2
                    $ stan2["Vio"] = 2

            p "Przed wyłączeniem, ten drugi zrobi zamieszanie"
            p "Jak będą ślepi, to zobaczymy co nas dalej czeka"
            p "Spotkamy się w środku i zobaczymy co nas czeka"
            p "Zrozumiały plan?"
            ja "Tajest"
            scene kasyno
            p "Panowie, rozproszyć się"
            "I tak, każdy z was poszedł do własnego stołu"
            menu:
                "Na jakie stawki chcesz grać?"
                "Wysokie" if edki > 4999:
                    $ zakład = 5000

                "Średnie" if edki > 2499:
                    $ zakład = 2500

                "Niskie" if edki > 999:
                    $ zakład = 1000

                "Minimalne":
                    $ zakład = 50

            $ edki -= zakład
            p "Dobra, let's go gambling"
            "Teraz zobaczmy jak Ci poszło"
            $ helper = renpy.random.randint(25, 100)
            if helper < fart:
                "Ciemna cipa, udało Ci się wygrać"
                $ edki += zakład * 2

            else:
                "Jasny chuj, nic nie siadło"

            p "Dobra, pora powolutku zmieniać miejsce"
            p "Mój wybraniec poszedł już wyłączyć kamery"
            sb "Ej patrz tam, ziomek robi salto jak wygrywa"
            p "Ten drugi zrobił delikatne zamieszanie"
            p "Mogę się powolutku udawać do strefy dla pracowników"
            $ heistprog["Main"] = 1
            scene korytarzCasino
            $ helper = 0
            while helper == 0:
                menu:
                    "Gdzie idę?"
                    "Pierwsze drzwi" if heistprog["D1"] == 0:
                        "Przechodzisz przez pierwsze drzwi"
                        "Trafiasz prosto do składzika na miotły"
                        "Nie ma tu zbytnio nic ciekawego"
                        $ heistprog["D1"] = 1

                    "Drugie drzwi" if heistprog["D2"] == 0:
                        "Sprawdzasz drugie drzwi, jest tu szyb wentylacyjny"
                        if inventory.has_item(Srubo) == True:
                            "Odkręcasz szyb i wskakujesz do środka"
                            "Trochę sobie tuptasz i wychodzisz w innym pomieszczeniu"
                            "W taki sposób otwierasz sobie koeljne drzwi"
                            $ heistprog["D4"] = 1
                        
                        "Bez śrubokrętu nic tu nie wskórasz"
                        $ heistprog["D2"] = 1

                    "Trzecie drzwi" if heistprog["D3"] == 0:
                        "Przechodzisz przez trzecie drzwi"
                        "W środku czekali na Ciebie twoi kompani"
                        show jax at left
                        show vio at right
                        ja "Siemaneczko"
                        p "Witam"
                        p "Dobrze nam poszło, szkoda, że się tutaj schowaliście, mógłbym was nie znaleźć"
                        vi "Vie vartw vię, va vglądam vorytarz vrzez vizjer"
                        p "No dobra, to było całkiem szczwane"
                        p "Dobra, wyskakujemy i sprawdzamy dalej"
                        $ heistprog["D3"] = 1
                    
                    "Czwarte drzwi" if heistprog["D4"] == 1:
                        "Sprawdzasz ostatnie drzwi, tutaj jest sejf naścienny"
                        if heistprog["D3"] == 1:
                            p "VIO, możesz otworzyć?"
                            vi "Jasna sprawa szefie"
                            "Raz dwa VIO zhackował zabezpieczenia"
                            

                        $ heistprog["D4"] = 2

                    "Wyjście":
                        $ helper = 1

        "Na skradaka":
            "Tit"