label frogsimp:
    $ czas -= 1
    $ baba_name = "Kasia"
    if kompan > 0:
        $ renpy.notify("Kompan Cię opuszcza")
        $ kompan = 0

    if stan["Kasia"] == 1:
        scene frogsimp
        show kasia_dym at right
        if Frakcja == 6:
            p "O cześć Kasia, przerwa?"
            fse "Tak, szef wpadł na nowy pomysł i sie szykuję na jajca"
            p "Co mu znowu do łba wpadło?"
            fse "W zdrapkach mają być jakieś specjalne nagrody"
            p "O kurwica"
            fse "Robert taki. Ale muszę się zgodzić, to będzie jeszcze więcej roboty."
            p "Wiadomo jakie to mają być nagrody?"
            fse "Coś gadał o mieczach, tarczach i kuponach na zakupy"
            p "Ej kurwa! To brzmi worth. Chyba zaczne kupować więcej zdrapek"
            fse ":czacha"
            p "A! Fakt. To będzie jeszcze więcej roboty."
            fse "No, najgorzej będzie z wydawaniem tych wielkich itemów, wyobraź sobie mnie podnoszącą miecz"
            p "Oj tam, dasz radę. Opcjonalnie szybki przeszczep i będzie ez"
            fse "Jakbym miała pieniądze na przeszczep, to bym nie pracowała we frogu"
            p "Fair point."
            fse "Dobra, pora kończyć tę przerwę. Trzymaj się [old_pn]"
            p "Baj baj"
            $ stan["Kasia"] = 2

        else:
            p "Dzień dobry, masz może szlugiem poratować?"
            fse "Dzień dobry, proszę, jeszcze mi zostało kilka"
            p "Dziękuje, ciężki dzień? Pierwszy raz Cie widzę przed sklepem"
            fse "Trochę luzu jest teraz ale za jakiś czas wchodzą ulepszenia do zdrapek"
            p "Jakie ulepszenia?"
            fse "Będą do wygrania jakieś fizyczne nagrody"
            p "Jakie?"
            fse "Miecz, tarcza, kupon na zakupy i jakieś jeszcze inne itemki"
            p "Brzmi jak więcej robory"
            fse "Dokładnie tym to jest"
            p "Kurde balans, współczuje ale dobra, pora kończyć. Btw [old_pn] jestem."
            fse "Kasia"
            $ baba_name = "Kasia"
            $ stan["Kasia"] = 2

    elif stan["Kasia"] == 2:
        scene frogszop
        p "Cześć Kasia, pytanko mam"
        fse "Co tam [old_pn]?"
        p "Masz jakieś plany po robocie?"
        fse "Niestety, sama praca tutaj mi nie pozwala na opłacanie wszystkiego i robię jeszcze dorywczo"
        p "Kurwa, na śmierć się tak zarobisz"
        fse "To nie jest nic ciężkiego, zajmuję się dziećmi korposów. Ci zawsze w pracy, nie oszczędzają na opiekunkach"
        p "Masz aż tak dobrą renomę, że tyle Ci płacą?"
        fse "Czasmi trafi się klient, co płaci mi więcej niż dniówka tutaj"
        if Frakcja == 6:
            p "No nam płaci gówno"
        
        else:
            p "Aż tak słabo płaci wielki Frog"
        
        fse "Może jakby dał jakąś podwyżkę to byłoby lepiej ale nie ma na co liczyć"
        p "OOF. Hebrajski szef, podobno w bazie mioch znajomych był taki kiedyś"
        fse "Gdzie pracują Ci twoi znajomi?"
        p "Krawędziują"
        fse "Zadajesz się z bardzo niebezpiecznym towarzystwem, pracujesz z nimi?"
        if akt == 1:
            p "Tak"

        else:
            p "Wcześniej z nimi pracowałem"

        fse "Nie wyglądasz na takiego typowego krawędziowca"
        p "Jestem zbudowany inaczej"
        fse "Widać"
        p "Co?"
        fse "Klient przyszedł, muszę spadać"
        p "Papatki"
        $ stan["Kasia"] = 3

    elif stan["Kasia"] == 3:
        "Wędrując sobie po mieście, udało Ci się znaleźć Kasię, stojącą w kolejce pod kinem"
        scene kino
        p "OMG, to Kasia, >_< chyba podejdę ją napastować poza miejscem pracy"
        p "Pierwszy raz ją widzę gdziekolwiek poza Frogiem, chyba ma wolne"
        p "Pora podejść i zagadać"
        p "Hai Hai!"
        show kasia_basic at right with moveinright
        fse "O! Cześć [old_pn]! Do kina przyszedłeś?"
        p "Raz na ruski rok trzeba zaznać trochę cooltury"
        fse "A na co idziesz?"
        p "Dobre pytanie"
        call cipflash from _call_cipflash_15
        fse "To może ta nowa komedyjka fantasy?"
        p "Jak to się nazywa?"
        fse "Łan men, Łan czar. Film o czarodzieju co zna tylko gobelin blast"
        p "Brzmi tak głupio, że aż pójdę."
        "Poszliście do kasy i kupiliście bilety"
        $ edki -= 15
        scene absolutnekino
        p "Pusto tu dość"
        fse "Nic dziwnego, mało ludzi teraz chodzi do kina. Lepszą rozrywkę zwykle mają na ulicy"
        p "Popierdoleńcy, tylko latać z gnatem i strzelać do każdego. Chyba tylko Łaskawca czerpie z tego fun"
        fse "Nie znam gościa, ktoś z twoich znajomych?"
        menu:
            "Opowiadać o dzbanach?"
            "Wysprzęgl się":
                $ kasiaknow += 1
                p "Nom, Łaskawca jest medykiem, trochę pierdolnientym ale dobrym"
                p "I przy okazji jeszcze nam towar produkuje"
                p "I to jest chyba jeden z normalniejszych w naszym składzie"

            "Jebać 60":
                p "Nom, taki kumpel z roboty"
                p "Dużoby gadać"

        fse "Cii, film się zaczyna"
        "Średnio co pięć minut leciała reklama"
        p "Pojebie mnie z tymi reklamami, po chuj to dają tak często?"
        fse "No wiesz, trzeba zarabiać na każdym miejscu"
        p "Ciekawe co jeszcze wpadnie im do głowy, reklamy na cyberoczach?"
        fse "Może lepiej przestań krakać"
        "Oglądaliście dalej i film został oglądnięty"
        $ czas -= 2
        scene kino
        show kasia_basic at right
        p "Kurwa ale to było głupie"
        achieve Abs
        fse "Ale fajne efekty zrobili, postarali się tym razem"
        p "Bywało gorzej?"
        fse "Nah, czasami chodzę na te bolywoodzkie filmidła, straszna głupota ale mnie bawi"
        p "Ok, nie dopytuje. Muszę się już zbierać. Siemaneczko Kasia, do następnego"
        mg "(updata)"
        fse "Papatki [old_pn]"
        $ frogrel += 1
        $ stan["Kasia"] = 4

    elif stan["Kasia"] == 4:
        scene frogszop
        p "Hejo Kasia, jak tam dzionek mija?"
        fse "Hejo [old_pn]! A bardzo spokojnie wszystko się dziś zaczęło."
        mg ":trollface"
        p "A mogę mieć do Ciebie takie dość personalne pytanie?"
        fse "Pytaj śmiało, jak będzie zbyt osobiste, to po prostu nie odpowiem"
        p "No i g. Więc, jak to się stało, że jesteś kotem? Biorzeźbiarstwo czy ksenogenetyka?"
        fse "Pomidor"
        p "Cholipka, to może powiesz mi, czemu kolor twoich uszu i ogona się zmienia?"
        fse "Mój sprzęg neuralny jest za to odpowiedzialny. Zwykle dopasowywuje się do nastroju"
        p "O! Ciekawe, nie wiedziałem, że to ma takie możliwości"
        fse "No widzisz, człowiek uczy się całe życie"
        p "A jak to zmienia z nastrojem tylko czasmi, to co się dzieje w reszcie przypadków?"
        fse "Nie wiem w sumie, ten mój sprzęg jest uszkodzony i portafi szwankować"
        p "Chcesz może kontakt do doktorka? Jak z nim pogadam, to może zrobi Ci go po kosztach"
        fse "Dzięki za propozycje ale na ten moment nie mogę sobie pozwolić na większe wydatki"
        fse "Ani w sumie na jakieś dni wolne, strasznie krucho z edkami"
        p "Karamba, strasznie chujowa sytuacja"
        "I w momencie jak to powiedziałeś, gówno uderzyło w wiatrak. Do sklepu wbił rozsierdzony gangus"
        gg "Ręce do kurwa góry, to jest pierdolony napad."
        "Widzisz, jak Kasia patrzy na Ciebie przerażona"
        p "Kolego, tak się nie zachowuje w sklepie"
        gg "I co mi niby zrobisz kasztanie"
        p "A mam pod ręką tajemniczy mysi sprzęt "
        play sound "pif.wav"
        "Nim zdążyłeś wyjąć broń, napastnik strzelił do Ciebie"
        call checkHP(19) from _call_checkHP_36
        gg "Trzebabyło dawać więcej refleksu kurewko"
        p "Dzięki bogu dałem sporo w wytrzymałość"
        play sound "pif.wav"
        "Trafiłeś gangusa prosto w cymbał"
        p "Celność też nie jest najgorsza"
        "Niestety rana jaką otrzymałeś jest dość poważna, przez co padasz na podłogę"
        scene frogmercy
        fse "Trzymaj się [old_pn], zaraz Ci pomogę"
        "Kasia ostrożnie ustabilizowała twoje rany"
        fse "Postaraj się nie ruszać teraz, wstrzyknę Ci nasz turbouzdrawiacz"
        $ Hp = MaxHP
        "Ten medykament niesamowicie Cie sieknął, pierwszy raz tak dziwnie się poczułeś"
        scene frogszop
        fse "Lepiej?"
        p "Chyba nigdy w życiu nie czułem się lepiej, co to było?"
        fse "Nasz nowy program usługowy, froghealing, specjalna możliwość dla posiadaczy frogsów"
        p "Czemu mi tego wcześniej nie powiedziałaś? To jest lepsze od parów"
        fse "Dopiero teraz to wprowadziliśmy, teoretycznie za kilka dni miało oficjalnie wchodzić"
        p "To będę chyba częściej z tej możliwości korzystał"
        fse "Dzięki za ochronę btw. Kacperek pewnie dopiero wstaje z krzesła"
        p "Luzik, dla mnie takie strzelaniny to codzienność"
        $ frogrel += 1
        $ czas -= 7
        p "Muszę już spadać, mam trochę roboty jeszcze"
        fse "Spoczko, uważaj na siebie [old_pn]"
        $ stan["Kasia"] = 5

    elif stan["Kasia"] == 5:
        "Jak sobie spacerowałeś, zobaczyłeś Kasię w kawiarni"
        "Jako totalny creep, postanowiłeś iść zakłócać jej spokój"
        scene cafe
        p "Hajo Kasia"
        show kasia_kofi at right
        fse "O [old_pn], na kawę przyszedłeś?"
        p "Nom, trochę mi się przepiły te całe potworki"
        fse "To co teraz popijasz?"
        p "Ta kawka bez wody, africano chyba to się nazywa"
        fse "Przerażasz mnie czasami"
        p "Nie raz już mówiłem, ja jestem zbudowany inaczej"
        $ edki -= 25
        "Zapłaciłeś za kawę i przysiadłeś się do Kasi"
        p "Jak tam Ci dzionek mija?"
        fse "A powoli dość, spokojny weekend się trafił"
        p "Trochę sus, amogus. Cały weekend masz wolny?"
        fse "Nom, jeszcze nikt nie napisał, że potrzebuje opiekunki"
        p "A masz jakieś plany?"
        fse "No wiesz, typowe takie babskie zajęcia. Cybflix, starsaks i lumpexy"
        p "Jasny Gun, to brzmi jak cały dzień roboty"
        fse "Bo to jest cały dzień roboty. Przynajmniej jest jakkolwiek zająć głowę"
        p "Ja jak nie mam co robić, to strzelam se w łe.."
        fse "._."
        p "Sorka, mówiłem, jestem zbudowany ina"
        fse "Trzeci raz mi to mówisz"
        p "A ty chyba wiesz nawet dlaczego"
        fse "To jest jakiś twój catchfrase?"
        p "Nie, jestem jasnowidzem i widzę kraweńdziobiegaczy. Tam to jest główne lore"
        fse "Nie pytam i nie chcę odpowiedzi"
        p "Szybko się uczysz"
        fse "Tego wymaga ode mnie aktualny rynek pracy"
        p "Dlatego, ja się cieszę, że moja praca nie wymaga specjalnych skili"
        menu:
            fse "To co ty takiego robisz na utrzymanie?"

            "Jestem kraweńdziażem":
                "Opowiedziałeś trochę Kasi o swojej pracy"
                $ kasiaknow += 1
                fse "Jak wy robicie takie nie do końca legalne sprawki"
                fse "To nie powinienieś tego trzymać jako sekret?"
                p "Oni opowiadali o największej swojej broni, swoim największym przeciwnikom"
                p "My nie mamy sekretów, tylko ciekawostki do opowiadania"

            "Pomidor":
                p "Pomidor"
                fse "Pomidor"

        $ czas -= 10
        fse "Robi się już późno, pora się zbierać"
        p "Trzymaj się Kasia"
        hide kasia_kofi
        p "Kolejny raz przeszkadzałem jej w aktywnościach. Jestem sigma, patryk batman"
        $ stan["Kasia"] = 6

    elif stan["Kasia"] == 6:
        scene frogszop
        p "To pora na kolejne udane zakupy"
        p "Zostanę posiadaczem wielu frogowych itemków"
        show jax at left
        p "O rety naplety, co ty tu robisz JAX?"
        ja "Na zakupy przyszedłem, co się tak pytasz?"
        p "No wiesz, pierwszy raz widzę jakiegoś NPC-a we frogu"
        ja "Co ty pierdolisz [player_name]?"
        p "Jestem główną postacią w tej gierce, ja mam swoją gwarę"
        ja "Nie mam pojęcia co to jest, masz może jakieś punkty w gwarze ulicy?"
        fse "Przyzwyczaisz się, on tak zawsze gada."
        p "Ej no, nie mam aż tak wielkiego mózgozgnicia"
        ja "Masz"
        fse "Masz"
        p "Takie same, to po 5"
        fse "Właśnie o tym mówię"
        ja "Dobra, ja będę spadał, mam jeszcze obowiązki, standard o 19?"
        fse "Spoczko"
        hide jax with moveoutleft
        p "Standard o 19? Co to jest standard o 19?"
        fse "Nie interesuj się tak [old_pn]. A właśnie! Czemu Jax do ciebie mówił [player_name]?"
        p "Bo ja jestem teraz tajnym agentem, a to jest mój kryptonim"
        fse "Też mam do Ciebie mówić [player_name]?"
        p "Nah, ty jesteś przecież zwykłym cywilem, po kiego miałabyś trzymać się naszego kodenamu?"
        fse "Tja, jestem tylko zwykłym, niewinnym cywilem"
        p "To dobrze, jakbyś była na przykład tajnym agentem, to byłoby nieciekawie"
        fse "Gdzie, ja? Tajną agentką? [old_pn] nie przesadzaj"
        p "I dzięki bogu."
        fse "Nom, siedzę tutaj, dorabiam gdzie indziej i jakoś żyje się dalej"
        p "Dobra, pora kończyć te pogadanki, pora na zakupy"
        $ stan["Kasia"] = 7

    elif stan["Kasia"] == 7:
        scene spacer
        "Wędrując sobie po mieście, znowu znalazłeś Kasię. Tym razem szła ona z jakimś dzieckiem"
        p "Jasna dupa, to jest Kasia w swojej kolejnej pracy, powinienem ją śledzić"
        "Niestety, nie jesteś dobrym skradaczem"
        scene kasia_con_chico
        fse "[old_pn]! Co ty robisz?"
        p "Pomidor"
        fse "O nie nie nie, tak łatwo nie uciekniesz od tej odpowiedzi. Co ty tu robisz?"
        p "Ja tu tylko spaceruję, nie robię żadnych cienistych sprawek, frfr"
        fse "I ja mam Ci w to uwierzyć?"
        p "Tak. Mówię absolutnie szczerze"
        fse "Masz szczęście, że jestem w pracy teraz, inaczej byśmy poważniej porozmawiali"
        p "Dobra, dobra, sorki"
        "I kasia poszła sobie dalej"
        scene spacer
        p "Kurde balans, nie spodziewałem się, że tak ostro zareaguje"
        "Więc chodzisz sobie dalej po mieście w spokoju"
        $ czas -= 4
        "NAGLE, słyszysz strzały. W sensie, że wiesz, takie nietypowe. Chyba powinieneś to sprawdzić"
        p "Rety kotlety, bardzo bizzarne, ruszę to sprawdzić"
        "I jak sprawdziłeś, to się przerazileś, Kasia dostała"
        p "O JA PIERDOLE"
        "Podbiegłeś żeby sprawdzić co się stało"
        scene kasia_pif_pafed
        p "Kasia! Kasia! Jesteś cała!?"
        fse "Mogło być gorzej, rana nie wygląda jakoś poważnie"
        p "Obstawiam, że nie masz wykupionej Traumy?"
        fse "Za pracę we Frogu nie stać mnie na takie luksusy. Powiedz mi lepiej gdzie jest mały"
        "Rozglądasz się po okolicy i widzisz szczyla za doniczką"
        p "Stosuje wietnamskie taktyki kamuflażu"
        fse "Dobrze, jakby coś mu się stało, to mogłabym już się żegnać ze światem"
        p "Tak się przywiązałaś do tego malucha?"
        fse "Nie pozbierałabym się finansowo z pozwu od jego rodziców"
        p "Faktycznie, korpogówniaki muszą być hardcorowo obsadzeni prawnikami"
        "Widzisz, że Kasia zaczyna powoli wstawać"
        p "Nie rozpędzaj się może aż tak, jesteś dość poważnie ranna"
        fse "Weź agenta i zadzwoń po taksówkę, muszę odesłać młodego do domu"
        p "A może zajmiesz się wpierw sobą?"
        fse "Nie stać mnie na to"
        "Wezwałeś taksówę i czekasz z Kasią aż przyjedzie"
        fse "Obstawiam, że nie masz zielonego pojęcia o pierwszej pomocy"
        p "Nom, zawsze chodziłem do doktorków po leczenie"
        fse "Tak się spodziewałam"
        "Taksówka przyjechała, Kasia podała gdzie ma zawieźć młodego"
        p "Co teraz zrobimy?"
        fse "Muszę się dostać do swojego domu, jakkolwiek się ustabilizować i wytłumaczyć co się stało"
        p "Potrzebujesz może jakieś pomocy?"
        fse "Obawiam się, że nie dam sobie rady sama, mogą tam na mnie czekać"
        p "Kto?"
        fse "..."
        p "Dobra chuj, dawaj idzeimy"
        "Wziąłeś Kasię pod ramię i pomogłeś jej wrócić do domu"
        $ czas -= 6
        scene kasiadom
        p "Holipka, ładne masz mieszkanko"
        fse "A dziękuję, staram się je utrzymać w porządku. Idź do łazienki i weź zestaw do pierwszej pomocy"
        p "Się robi"
        "Do łazienki skoczyłeś i z apteczką wróciłeś"
        fse "Dobra, teraz muszę sie skupić i przypomnieć sobie jak to się wszystko robi"
        "Widzisz jak kasia zaczyna zdejmować garnitur"
        p "Ehm, ja pójdę i poczekam przed drzwiami, może jakieś gangusy będą coś chciały"
        fse "Dobry pomysł"
        "Wychodzisz czatować przed drzwiami i dajesz w taki sposób Kasi trochę prywatności"
        scene klatka
        p "Kurde balans, w co się ona wpakowała, to nie wygląda na przypadkowy strzał"
        "Poczekałeś sobie chwilę i zobaczyłeś sus duet wchodzący po schodach"
        gg "Kolego"
        gg "Masz może petem poratować?"
        p "Pewnie, łap"
        "Dałeś gangusowi jednego ze znaleźnych szlugów"
        gg "Dzięki. Widziałeś tu może taką babeczkę z różowymi włosami i kocimi uszkami?"
        p "Z tego co mi się wydaje, to wchodziła tam do bloku obok"
        gg "Kurwa wiedziałem, dzięki za info stary"
        "I gangusy sobie poszły, poczekałeś chwilę i dałeś Kasi znak"
        fse "Na pewno już sobie poszli?"
        p "Tak, co jak co ale wyglądali niebezpiecznie"
        fse "Wskakuj tutaj"
        scene kasiadom
        p "Dobra, to już nie jest śmieszne. Powiedz mi w końcu co się dzieje"
        fse "Nie dam rady [old_pn]. Jest za wcześnie na to, jestem Ci wdzięczna za pomoc ale nie mogę Ci jeszcze o wszystkim powiedzieć"
        p "No dobra, niech będzie. Ja się będę musiał w sumie zbierać. Poradzisz sobie dalej sama?"
        fse "Tak mi się wydaje, dzięki, jeszcze raz"
        p "Nie ma za co"
        $ stan["Kasia"] = 8

    elif stan["Kasia"] == 8:
        scene spacer
        show kasiacall
        fse "Hej [old_pn], masz może chwilkę?"
        p "Pewnie, trzeba coś pomóc?"
        fse "Nom, zamówiłam sobie zakupy ale kuriera ktoś napadł, przyniósłbyś mi je?"
        p "Żaden problem, podaj mi tylko lokację"
        fse "Musisz jechać w okolicę takiego baru, Srebrny Smok się nazywa"
        p "A to chyba nawet wiem gdzie, kurier z jakiej firmy był?"
        fse "Outpost, ci od tych śmiesznych automatów toaletowych"
        p "Więcej informacji nie potrzebuję, ruszam na poszukiwania"
        fse "Dziękuję"
        scene miasto
        p "Tup tup tup, zaraz skopię kilka dup"
        "Wesoło sobie wędrujesz po mieście i znalazłeś płonący pojazd"
        p "Jasna dupa, dobrze, że te płomienie są tylko w mojej głowie, inaczej byłby problem"
        call testSkili("Atletyka", "ZW", 9)
        if wynik == 1:
            "Szczęśliwie, płomienie faktycznie były fantomowe"

        else:
            p "AŁA KURWA, TO PIECZE"
            mg "Piekło tak!"
            $ HP -= 15

        "Wyciągnąłeś reklamówkę z zakupami"
        p "Dobra, teraz mogę ruszać do Kasi"
        gg "Nie tak szybko kolego"
        "Odwracasz się i widzisz jakiegoś kasztana z Tiger Claws"
        p "Czego chcesz? Zajęty jestem"
        gg "Widzisz chyba jak skończył twój poprzednik, odstaw to lepiej i spieralaj"
        p "Jaki kurwa poprzednik? Ja tu swoje przyszedłem odebrać"
        gg "Aha, to przepraszam za najście, miłego dnia"
        p "Bywaj"
        "I żółtek sobie podzedł"
        p "Delikatnie obsrałem zbroję"
        "Umyłeś ją i poszedłeś do Kasi"
        scene kasiadom
        show kasia_basic
        fse "Hai Hai!"
        p "Hai Hai! Mam zakupki"
        fse "Dzięki wielkie [old_pn]"
        "Pomogłeś jeszcze Kasi rozpakować zakupy. Widzisz, że między basic jedzeniem, jest pistolet i paczka amunicji p.panc"
        p "Powiedz mi Kasiu, jesteś tu zagrożona?"
        fse "Delikatnie, głównie Ci łowcy głów mogą mi zniszczyć dzień"
        p "W skali od rambar do dżambar, jak duże masz kłopoty?"
        fse "Obawiam się, że to może być poziom dżambar. Strasznie się sprawy pokićkały"
        p "I tym pistoletem chcesz się obronic?"
        fse "Nie tylko, mam jeszcze kilka zapasowych źródeł ochrony i umiem całkiem dobrze unikać"
        p "A co jeśli zaatakują z zaskoczenia? Jak sobie wtedy dasz radę?"
        fse "Będę improwizować"
        p "Kasiu, obawiam się że"
        fse "[old_pn]. Nie wiesz do czego jestem zdolna. Nie wiesz ile syfu się za mną ciągnie. Nie wiesz ile ważą moje grzechy"
        p "No nie wiem. Ja chciałbym tylko pomóc"
        fse "Masz jakis syndrom głównego bohatera że tak wszystkim pomagasz?"
        p "Kasieńko, ja jestem głównym bohaterem"
        mg "Niestety"
        fse "Nie mam już siły na dziś, chyba muszę się przespać"
        p "Dobrze, to ja zmykam, papatki"
        "I zostawiłeś Kasię samą z jej myślami"
        $ stan2["Kasia"] = 9

    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    jump frogszop