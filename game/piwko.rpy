label piwko:
    if kompan == 2:
        scene japiwko
        if postacie2["Jax"] == 0:
            ja "Kurwa, przyjemnie tak sobie skoczyć na browca"
            p "Ciężko się z tobą nie zgodzić"
            ja "To opowiadaj [old_pn], co tam u Ciebie"
            p "Pamiętasz moje imię nawet, jestem pełen podziwu"
            ja "No słuchaj, to jest tylko zmienna"
            mg "(Jeśli się nie wyjebało)"
            p "Tak czy siak, podziwko."
            ja "Wracajmy do tematu, jak tam Ci życie mija?"
            p "No powoli to jakoś leci, wiesz, questy się robi, edki zarabia"
            ja "Czyli po staremu"
            p "Gadaj lepiej jak u Ciebie"
            ja "No co, czekam aż koledzy wyjdą z pierdla i staram nie dać się zabić"
            p "To jest już klasyk"
            ja "Nom, jak już wrócą to czeka nas bojowe zadanie"
            p "O kurwens, brzmi poważnie. Co to za robota"
            ja "Ty jeszcze szczylem jesteś w mieście, nie mieszaj się w to"
            p "Kurwa, teraz to mnie zainteresowałeś, opowiadaj"
            ja "VIO znalazł jednego z ziomków którzy mnie porwali. Musimy go teraz dopaść"
            p "Jak VIO dał radę coś takiego w ogóle znaleźć?"
            ja "On ma swoje sposoby, tak Ci powiem w tajemnicy, on nie jest tak głupi na jakiego się wydaje"
            p "Ciekawe, cały czas siedzi pod taką przykrywką?"
            ja "To jest bardziej jak Doktor Jekyll i pan Hyde"
            p "Takie pojebane rozdwojenie jaźni, ciekawe. Tak miał od startu czy od niedawna"
            ja "Jak drużyna trafiła do więzienia zaczął przesiadywać w labie Łaskawcy"
            ja "Prawdopodobnie udało mu się zrobić szczepionke na Visty"
            p "Pierdolisz"
            ja "Serio, poszedł testować to na dzikich Vistach i się sam przeraził, to zadziałało ale odkrył coś jeszcze gorszego"
            p "Visty zaczęły szczekać?"
            ja "Powstała nowa generacja Vist. V5 zaczyna wchodzić do obiegu. Mają zwiększone limity inta"
            p "Do jakiego stopnia?"
            ja "Teraz mogą mieć max 4"
            p "To serio jest niebezpieczne i tam się dowiedział o agentach?"
            ja "Coś w tym rodzaju. Jakiś korpos był na miejscu, potem wpadł w ręce VIO"
            p "Jak bardzo groźnie tam może być?"
            ja "Sami agenci nie są niebezpieczni, jest ich chyba trzech, z czego jeden robił to tylko dla awansu"
            p "Jebane korposzczury"
            ja "Złapiemy jakiegoś z nich i znajdziemy szefa. Potem będę mógł się zemścić i spierdalać z tego miasta"
            p "Znudziło Ci się bycie gangusem?"
            ja "Żonka z dzieckiem na mnie czekają"
            p "Kurwa Jax, czy ty chcesz zrobić sobie dobre zakończenie?"
            ja "Przelałem już wystarczająco dużo krwi"
            p "Kurwa.... głębokie"
            "I tak spędziłeś wieczorek na piwerku z Jaxem"
            achieve Bir
            $ postacie2["Jax"] = 1

        elif postacie2["Jax"] == 1:
            "Na ten moment Jax nie chce więcej gadać"

    elif kompan == 1:
        vi "Pije solo"

    else:
        "Wyjebali Cię z baru"

    jump opor