label side_intro:
    scene spacer
    mg "Witaj młodzieńcze, oto przed tobą nowy segment tej gry milenium"
    mg "Od tego momentu, możesz zbierać sobie fajki, by mieć możliwość odczuwania sidestory"
    mg "To, co Ci tutaj przedstawie, nie ma zbytnio dużego wpływu na grę, tylko będzie fóni"
    mg "Te magiczne szlugi gdzieś będziesz mógł znaleźć, albo chyba kupić"
    mg "Co Cię tu dalej znajdzie, zobaczymy"
    mg "Teraz możesz czmychać, ja będę wymyślał głupoty"
    return

label side_Jax_1:
    achieve Faj
    $ sideseen.append("side_Jax_1")
    scene japiwko
    ja "Siemandero [old_pn], dzięki za tego Malboraska"
    p "Spoczko Jax, żaden problem. Nawet nie wiem co one robią"
    ja "No ogólnie to możesz je palić ale tutaj, dostaniesz ode mnie historię"
    p "No dobra, to opowiadaj"
    ja "A więc, w bazie zacząłem pracę jako basicowy gangus"
    ja "To były jeszcze gówniane czasy, gdy Bezi był naszym fixerem"
    ja "Gangusy były ogólnie takim tanim mięsem armatnim a jak umierali to dzwonił do szefa po nowych"
    ja "W naszej bazie latało sporo popierdoleńców podobnie jak teraz w sumie"
    ja "Ale był taki jeden kasztan, co wyjątkowo mnie wkurwiał"
    ja "Taki ziomek Aki, fan innego martwego już zjeba Kody"
    ja "Próbował ze mną stanąć w szranki ale dostał koncertowy wpierdol"
    ja "Niestety niczego go to nie nauczyło"
    ja "Po pewnej akcji, Aki zaatakował innego bazownika CJ-a"
    ja "Wtedy do walki wkroczyłem ja"
    ja "Dostał takiego potężnego Luja, że go ze schodów zjebało"
    ja "Niestety to uruchomiło nowe, niespodziewane wydarzenia"
    ja "I w taki magiczny i zaczarowany sposób, powstała legenda 60 procent"
    p "Warto znać takie legendy, dzięki za info"
    ja "Żaden problem, ale pora się już zbierać, muszę jeszcze gdzieś skoczyć"
    p "Nie potrzebujesz towarzystwa?"
    ja "A w sumie, czemi nie, wstawaj idziemy"
    scene spacer
    show jax at left
    p "To dokąd ruszamy?"
    ja "Do mojego znajomego szmuglera, Rubin się nazywa"
    p "A co takiego chcesz przeszmuglować?"
    ja "Muszę wysłać pieniądze do rodziny"
    p "Nie wiedziałem, że masz rodzinę"
    ja "Mam żonę i małego synka, dostał nawet kiedyś pistolet od ekipy"
    ja "Miał wygrawerowane na sobie mały popierdoleniec"
    ja "Ahh, brakuje mi trochę tych starych, szalonych czasów"
    ja "Ale to już przeszłość, teraz trzeba być odpowiedzialnym ojcem"
    ja "Dobra, widzisz tamto wejście do metra?"
    p "No widzę, a co?"
    ja "Schodzimy tam, na trzecim peronie jest ukryte przejście, tam zejdę do Rubina"
    p "A ja nie mogę zejść?"
    ja "Nie da rady, on przyjmuje tylko sprawdzonych przez siebie klientów"
    "Zeszliście z Jaxem do metra"
    scene metro
    ja "Oj, kolejne wspomnienia się odblokowują"
    p "A jakie tym razem?"
    ja "Pewnego strasznego dnia, jak w bazie pojaiwł się Cypher"
    ja "Musięli dostać się do pomieszczenia technicznego na środku trasy"
    ja "Jak się możesz domyślać, ochrona nie chciała ich przepuścić"
    ja "To te kretyny odpaliły granat dymny i tam nasrały"
    ja "Absolutnie kretyński pomysł"
    call cipflash from _call_cipflash_20
    ja "Skończyło się na tym, że Kałach załatwił im przejście"
    p "No dobra, to serio była kretyńska akcja"
    ja "Dlatego mi się teraz głupio do metra wchodzi"
    p "W pełni zrozumiały krindż, dzięki bogu mnie jeszcze nie połączyli z resztą"
    ja "Jeszcze, to jest słowo klucz"
    ja "Ale dobra, to tutaj będę schodził, zostań tutaj"
    p "No spoczko, ja tutaj poczekam"
    "Jax zszedł w podziemny tunel"
    menu:
        "Co terez robisz?"
        "A podsłucham, co tam porabia":
            ja "Siema Rubin, ja po to co zwykle"
            sus "Cześć Jax, może być mały problem"
            ja "Co się dzieje?"
            sus "Na Jokohamie zaczęła się mała wojenka gangów, ich najwięksi bosowie Jakuz gdzieś zniknęli"
            sus "I teraz cały narybek walczy o władzę"
            ja "I pewnie napadają na wszystko, co związane z pieniędzmi"
            sus "Dokładnie, więc mogę przyjąć hajs ale go nie wyślę aktualnie"
            ja "Wiesz kiedy mniej więcej może to się skończyć?"
            sus "Nie mam pojęcia, musimy czekać na pojawienie się jakieś większej ryby"
            ja "Kurwa mać, są jakieś straty w cywilach?"
            sus "Nie, walczą między sobą, ludności nie tykają"
            sus "Mówimy o japońcach a nie o izraelitach"
            ja "Dobra, przesyłam Ci edki i się zawijam"
            sus "Dziękim dam Ci znać jak przelew dotrze do twoich, bywaj"

        "Poszukam sobie jakiegoś zajęcia":
            "Radośnie tuptasz sobie po stacji i znajdujesz smutnego biznesmena"
            p "Panie, coś pan taki smutny?"
            "Ziomek opowiedział Ci jak stracił swoje pieniądze na giełdzie"
            "Zaoferował Ci przyjęcię od niego jego akcji a ty, przyjąłeś je bez zastanowienia"
            $ iloscAkcjiSp1 += 1
            "A następnie wskoczył pod nadjeżdżający pociąg metra"
            "Przykra sprawa troszeczkę"
            p "Jest jak jest mordziaty"

        "A odpocznę sobie":
            "Usiadłeś sobie na krześle i uciąłeś komara"
            $ HP += 5
            $ fart += 5
            "Jakoś Ci się lepiej na duszy aż zrobiło"

    "Jax wychodzi z przejścia"
    ja "No siema, jestem już z powrotem"
    p "I jak poszło?"
    ja "Całkiem nieźle, powoli zmniejsza prowizję od wysyłki i coraz lepiej na tym wychodzimy"
    p "A czemu w ogóle robisz to tak na około? Nie byłoby lepiej wysłać normalnego bliczka?"
    ja "Blika niestety nie ma w Night City"
    p "Wiem, jaja se robie"
    ja "Moja rodzina jest tam, gdzie nasze banki nie dadzą rady wysłać mamony"
    p "Czyli gdziekolwieko poza NC?"
    ja "W sumie ta, ogólnie przewalotowanie edków to jakiś dramat jest"
    p "No ta"
    ja "Pora kończyć już te pogadanki, pora wracać do domu"
    p "Dobrze powiedziane panie Jaxie"
    ja "No to wracamy"
    $ postacie2["Jax"] += 1
    return

label side_Gun_1:
    scene kuchnia
    show gun at left
    $ sideseen.append("side_Gun_1")
    g "Siema [old_player_name], robota jest"
    p "Oho, co takiego tu się szykuje?"
    g "Musimy skoczyć na zakupy, szybka robota, minimum strat"
    p "A jakie straty przewidujesz?"
    g "Stratę czasu przeszukując alejki za przedmiotami"
    p "No dobra, powiedzmy, że Ci wierzę, gdzie jedziemy?"
    g "Jest tylko jeden sklep bliski memu sercu (i miejscu zamieszkania)"
    g "Dokładnie ptysiu, jedziemy do froga"
    scene idrive
    play music "idrive.mp3" volume 0.2
    p "W sumie, czemu nie mogę siedzieć normalnie?"
    g "Co to za pytaine"
    p "No wiesz, takie z ciekawości, nie pojawiam się tu na spritach bo siedzę schowany"
    g "To wszystko dla twojego bezpieczeństwa [player_name]"
    p "Co by się niby stało jakbym się wychylił?"
    g "Od razu zajebali by Cię, tutejsi snajperzy są bardzo dobrzy"
    p "Sranie w banie, po prostu nie chcecie ustalić wyglądu mojego"
    $ renpy.notify("Twórca potwierdza")
    p "No widzisz, mówiłem"
    g "Dobra tam, tłumaczenie ze snajperami jest bardziej normalne"
    p "Co jest w tym niby bardziej normalnego? Czemu w takim wypadku ty się tu pojaiwasz?"
    g "Bo ja mam plot armor, precyzując, nikt nie może mnie zabić poza Łaskawcą"
    p "Co kurwa?"
    g "No ta, mamy taką delikatną umowę, tylko jego koło fortuny może mnie zajebać"
    g "Tak jak w sumie praktycznie każdy z poprzednich punków"
    g "Nawet nie wiesz, ilu zostało zabitych przez Łaskawce"
    p "No, nie wiem, ilu?"
    g "A nie liczę tego, Eryka się pytaj, on ma jakiś fetysz liczenia tego"
    p "No spoko, kiedyś się go zapytam"
    g "To się pytaj, kończymy już ten dialog, dojechaliśmy"label frogszop:
    stop music
    play music "szop.mp3" volume 0.2
    scene frogszop
    $ baba_name = "Kasia"
    fse "Dzień dobry"
    g "Siemandero, dobra [player_name], weź mi poszukaj paczkę naczosów śmietanowych"
    g "Do tego jeszcze keczup ostry, żelki i srajta"
    p "Co ty za jakąś mieszankę wybuchową robisz?"
    g "A potrzebuję trochę smaczków przed zadaniem"
    p "Ja pierdolę, będziesz miał przynajmniej czym zapłacić?"
    g "Spokojna twoja rozczochrana, mam w skarpecie trochę mamony"
    p "Oszczędzasz na łakocie?"
    g "Nie, mam mały budżet smaczkowy"
    p "No dobra, to ja idę szukać tych itemków"
    "I dwadzieścia minut szukałeś słodyczy"
    g "Masz już wszystko?"
    p "Jakoś się udało, ale nieźle to było zakopane"
    "Przekazałeś Gunowi smaczki"
    $ postacie["Gun"] += 1
    g "Dzięki"
    fse "To za wszystko będzie 45 edków"
    p "Gun, mazs czym zapłacić prawda? Prawda?"
    g "No ta, czemu niby niemiałbym mieć? Przecież jechałem na zakupy, to oczywiste że mam jak zapłacić"
    call cipflash
    p "Oj, zaufaj mi, są postacie które idą na zakupy bez finansów"
    p "Ale dobra, jak zrobiliśmy zakupy, to możemy już wracać?"
    g "No pojebało Cię chyba, teraz możemy jechać dalej dopiero"
    p "No co ty pierdolisz, gdzie chcesz teraz jechać?"
    g "Oj kolego, teraz to się zacznie prawdziwe zadanie"
    p "Boże kurwa, jak teraz chcesz mi zabrać czas?"
    g "Jedziemy na wiec wyborczy Donuta Trundla"
    p "I co ma być niby w tym zadaniu?"
    g "Chcę posłuchać co takiego chce zrobić jak zostanie wybrany"
    p "W jakich wyborach on startuje?"
    g "Wyborach na szefa departamentu do spraw jedzenia"
    p "No dobra, no to jedziemy"
    scene idrive
    play music "idrive.mp3" volume 0.2
    p "Ty, czemu w ogóle są robione takie wiece na jakiś mniejszych wyborach?"
    g "Bo ten Trundel się pojawił, bez niego to byłyby zwykłe wybory"
    p "A co niby zmienia jeden ziutek?"
    g "To jest strasznie atencyjny skurwiel, przyciągnął sporo mediów dla fejmu"
    g "I podobno jeszcze ma jakieś układy z sovoilem"
    g "A do tego nie cierpi egipcjan i ich kultu anubisa"
    g "Opowiada, że przez to wartość Edka leci na łep na szyję"
    p "Kurwa, jaki lore. A kto jest jego przeciwnikiem w wyborach?"
    g "Taki inny dziwny typ, Joe Gajden"
