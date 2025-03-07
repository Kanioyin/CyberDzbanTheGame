label frogsimp:
    $ czas -= 1
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
        "Film został oglądnięty"
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
        hide jax
        p "Standard o 19? Co to jest standard o 19?"
        fse "Nie interesuj się tak [old_pn]. A właśnie! Czemu Jax do ciebie mówił [player_name]?"
        p "Bo ja jestem teraz tajnym agentem, a to jest mój kryptonim"
        fse "Też mam do Ciebie mówić [player_name]?"
        p "Nah, ty jesteś przecież zwykłym cywilem, po kiego miałabyś trzymać się naszego kodenamu?"
        fse "Tja, jestem tylko zwykłym, niewinnym cywilem"
        p "Tak jak mówię. Dobra, pora kończyć te pogadanki, pora na zakupy"
        $ stan["Kasia"] = 7

    elif stan["Kasia"] == 7:
        fse "Yo"


    show screen map_screen
    window hide
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    pause 1
    jump frogszop