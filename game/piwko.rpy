label piwko:
    $ czas -= 5
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

        elif postacie2["Jax"] == 1 and bigquest > 1:
            p "Kurwa, jak mnie ta dziura wymęczyła"
            ja "Nie tylko Ciebie [old_pn], nim się pojawiłeś, to wielu ludzi przez nią straciliśmy"
            p "Jak to wyglądało wcześniej?"
            ja "Jak tylko pojawiał się jakiś świerzak, to tam leciał. Zbierał się cały pluton egzekucyjny i tam go wrzucaliśmy"
            ja "A w tle leciał motyw spadającego Kratosa. Kurwa, to były czasy"
            p "Tęsknisz za tym wszystkim?"
            ja "I tak i nie. Ta ekipa jest strasznie spokojna, a to bardzo ułatwia nie umieranie"
            ja "Tamci, byli dla mnie jak rodzina i to taka, która walczy dla Ciebie do samego końca"
            p "Ta, chyba tylko w twoim przypadku, mnie chuje zostawiły"
            ja "Może to był fragment ich planu? Wiesz, i tak szli do pierdla."
            p "Jestem na 16 procent pewny, że nie. Po prostu mili wyjebane"
            ja "Straszny z Ciebie doomer, uśmiechnij się czasami, to nie boli"
            p "Się znalazł kołcz kurwa, ja jestem MC w bezbekowej gierce. Nie mam niczego, z czego byłbym szczęśliwy"
            ja "Przesadzasz z tym piwem chyba"
            p "Nie kurwa, mówię serio serio powaga2"
            ja "Zdecydowanie za dużo wypiłeś"
            p "Obiecuję Ci Jax, jeśli będziesz żywy w ostatnim akcie, to uciekniesz ze mną"
            ja "Pewnie"
            "W schizowej atmoswerze, przepiliście browarki"
            $ postacie2["Jax"] = 2

        elif postacie2["Jax"] == 2 and stan["Kasia"] > 6:
            p "Dobra Jax, opowiadaj, co ty za interesy robisz z Kasią?"
            ja "Co ty się tak interesujesz [old_pn]?"
            p "Wiesz, ciekawi mnie to strasznie. Jak jest kilka NPC w jednym mieście i to w moim wątku frogowym"
            ja "Czy ty się zainteresowałeś Kasią?"
            p "Kurwa, to ja tu zadaję pytania ale nie jest to wykluczone"
            ja "Oj stary, ty nie wiesz na co się nawet piszesz"
            p "Jax, opowiadaj mi wszystkie informacje jakie o niej wiesz"
            ja "Nie mogę Ci tak dużo dać, powiem Ci tylko kilka drobnych informacji"
            p "Czemu ty tak ją chronisz? Jax, czy ty masz romans na boku?"
            ja "Na łep upadłeś, na mnie żonka z dzieckiem czeka. Nie chcę zdradzać info, bo pracujemy razem."
            p "Side biznes z Frogiem?"
            ja "Nah, nie interesuj się aż tak. Kasia ma dostęp do wielu ciekawych informacji"
            p "Nie mów mi, że ona jest jakimś turbo fixerem"
            ja "Nah, praca we frogu daje sporo informacji o ludziach. Jakby, wyobraź sobie, że nasz team idzie do froga"
            ja "Wystarczy siedem sekund i wszystkie informacje będą publiczne"
            p "Masz trochę racji Jax. I twierdzisz, że ona handluje takimi informacjami?"
            ja "I to nie tylko ze mną, wielu brokerów przychodzi do niej po info"
            p "Czyli wszystko co ja powiem, ona może sprzedać komuś innemu?"
            ja "Nom, jeśli nie lubi Cię zbyt bardzo, to info zostanie sprzedane"
            p "Czyli powinienem podbijać swoją relecję z Kasią, wtedy informacje będą bezpieczne"
            ja "Tak to działa. Dlatego, ja mam dobre stosunki z Kasią"
            p "Dobra, to mi wystarczy. Teraz ja mam jakiegoś haka na Kasię, mam nadzieję, że nigdy nie będę musiał go użyć ale chuj wie"
            ja "Święte słowa młody, święte słowa"
            $ postacie2["Jax"] = 3

        else:
            pass

    elif kompan == 1:
        if postacie2["VIO"] == 0:
            p "No to opowiadaj Vio, jak Ci życie mijo"
            vi "Va vobrze vobrze, vziękować"
            p "A jak tam żona? Zdrowa?"
            vi "Va vdrowa vdrowa, vziękować"
            p "A jak tam Visty? Zdrowe?"
            vi "Vo vo vest vurwa vroblem, veszcze vie"
            p "Jak Ci w ogóle idzie praca nad szczepionką?"
            vi "Vowoli, vbyt vovoli. Vowinienem vieć viększe vaboratorium, v vięcej vbiektów vestowych"
            p "Porwać Ci może jakiś? Sam wiesz, że Visty kręcą się po ulicy, jak muchy po gównie"
            vi "Vo vie vak vowinno vyglądać, va vusze vajpierw vieć vobrą versję, vopiero votem vogę vestować valej"
            p "No ma to trochę sensu, jak się Visty uodporną na szczepionkę, to będzie totalne gówno"
            vi "Vrawda, va veszcze vie viem vak vygląda vroces veczenia"
            p "Jak stworzysz tą ostateczną wersję, to planujesz zaaplikować ją sobie?"
            vi "Vo vie vest vakie vroste [old_pn], va vam vpecjalną versję vutacji"
            p "Rety naplety, myślisz, że to będzie się dało uleczyć?"
            vi "Vleczyć vo vątpię, vle voże vuda vi vię vo vłagodzić"
            p "I tak do końca życia będziesz gadał z v na początku słowa?"
            vi "Vam vadzieję ve vie"
            mg "Nie będzie tak gadał, pojabie mnie inaczej"
            p "No dobra, całkiem zrozumiałe, w ogóle, zauwazyłem, że nie ciągnie Cie już aż tak do mięsa"
            vi "Vo vrawda, vgólnie vgraniczam vrzemoc, viem ve vej vie vniknę vle varto vrubować"
            p "Fair point, będę Ci musiał dalej przynosić mięsko w zamian za leczenie?"
            vi "Vak, va vie vhce vię vić, vięc vy vusisz vi vrzynosić vięcej varcia"
            p "No ok"
            p "Dobra VIO, fajnie się pijo ale ja muszę już spadać, narka"
            vi "Vajo"
            achieve Bir
        
        elif postacie2["VIO"] == 1:
            vi "Zaczynamy"

        elif postacie2["VIO"] == 2:
            vi "Jestem z VIO"

    else:
        "Wyjebali Cię z baru"

    jump opor