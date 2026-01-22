label side_intro:
    scene spacer
    mg "Witaj młodzieńcze, oto przed tobą nowy segment tej gry milenium"
    mg "Od tego momentu, możesz zbierać sobie fajki, by mieć możliwość odczuwania sidestory"
    mg "To, co Ci tutaj przedstawie, nie ma zbytnio dużego wpływu na grę, tylko będzie fóni"
    mg "Te magiczne szlugi gdzieś będziesz mógł znaleźć, albo chyba kupić"
    mg "Co Cię tu dalej znajdzie, zobaczymy"
    mg "Teraz możesz czmychać, ja będę wymyślał głupoty"

label side_Jax_1:
    achieve Faj
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
    p "No spoczko, ja tutaj poczekam"
    "Jax zszedł w podziemny tunel"
    menu:
        "Co terez robisz?"
        "A podsłucham, co tam porabia":
            "Skibidi"

        "Poszukam sobie jakiegoś zajęcia":
            "Skibi"

        "A odpocznę sobie":
            "Usiadłeś sobie na krześle i uciąłeś komara"
            $ HP += 5
            $ fart += 5
            "Jakoś Ci się lepiej na duszy aż zrobiło"

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
    return