label wojowezadanie:
    stop music
    play music "CMS.mp3"
    $ helper == 100
    $ config.rollback_enabled = False
    if Frakcja == 0:
        $ oldFrakcja = 0
        scene vniazdo
        "Poprowadziłeś punków prosto w vniazdo"
        p "Panowie, Kennedy wybrał mnie jako szefa tej operacji, więc proszę słuchajcie się mnie"
        "O dziwo nikt nie miał z tym problemu"
        "Teraz jako szef, czeka Cię wyzwanie kierowania swoją ekipą. Wskaźnik zagrożenia jest na poziomie 100"
        "Jeśli spadnie do 0 to osiągniesz giga sukces. Nie spodziewaj się tego wyniku"
        "To jakie masz możliwości zależy od ludzi w ekipie i od tego jaki masz sprzęt"
        "Wracając do wyroku śmierci. Macie kilka opcji na wykonanie tej roboty"
        menu:
            "Po Cichu":
                "Brak w tobie cyberowego ducha walki"
                p "Panowie, robimy to tak Cicho jak się tylko da i to będzie bardzo trudne"
                p "Trzeba teraz dostać się do środka. Co my mamy do wyboru"
                menu:
                    "Jak wchodzisz?"
                    "Drzwi główne":
                        "Dostaliście się do środka głównymi drzwiami"
                        "Najgorsze możliwe wejście ale okazało się niestrzeżone"
                        $ helper -= 10

                    "Okno" if stan["Krateus"] > 5:
                        p "Krateus, wskakuj oknem i nam pomożesz"
                        kr "Tajest kierowniku! Chopaky, to jest schowek na miotły! Wskakujcie, macie tu linę"
                        $ helper -= 15
                        hide krateus
                        "A po nim wskoczyła cała reszta"

                    "Drzwi dla personelu" if inventory.has_item(Wytrych) == True:
                        p "Na szczęście mam wytrych przy sobie"
                        p "Fiku foku loku picku"
                        $ inventory.remove_item(Wytrych)
                        "Zręczne palce koniobijcy pomogły Ci otworzyć drzwi"
                        "Panowie, zapraszam"
                        $ helper -= 20

                    "Wentylacja" if stan["Gun"] > 5:
                        p "Gun, możesz wentować?"
                        show gun
                        g "Dlaczego ja?"
                        p "W kombosach do KTG jesteś w spiskowcach a to jednak jest trochę sus"
                        g "To ma sers"
                        $ helper -= 25
                        hide gun
                        scene agunus
                        g "Kurwa, ciemno tu! O! Jest chyba wyjście"
                        "Gun skończył wentować"
                        g "Przycisk z napisem tajne vejście a se kliknę"
                        "I dzięki temu, reszta drużyny dostała się do środka"

                scene vards
                "Jesteście przy drzwiach 2"
                "Zbliżając się, usłyszeliście vrażników"
                v "Vrombał bym coś"
                v "Vejm"
                v "Vo voviesz na vot-voga?"
                v "Vybornie"
                p "Trzeba się ich pozbyć. Tylko jak to zrobię?"
                menu:
                    "Atak frontalny":
                        p "Za hordę"
                        "AAAAAAAA"
                        call checkHP(10) from _call_checkHP_20
                        "Dzielnie szturmowaliście parę Vist"
                        "Niestety jeden z vist miał przy sobie terminal"
                        $ edki = 0
                        "I w taki sposób zabrał Ci wszystkie pieniądze"
                        $ helper -= 5
                        
                    "Chessy akcja" if inventory.has_item(Ser) == True:
                        p "Żryjcie to kutafony"
                        "Rzuciłeś serem w Visty"
                        $ inventory.remove_item(Ser)
                        v "Ty viekki, akurat byłem głodny"
                        p "Luzik arbuzik, smacznego"
                        v "Dawaj Varek, idziemy na obiad"
                        play sound "EAT OR MUNCH.mp3"
                        $ helper -= 10

                    "Granat" if inventory.has_item(Granat) == True:
                        $ inventory.remove_item(Granat)
                        $ helper -= 15
                        "Poturlałeś granat w kierunku Vist"
                        v "Vo Volera! Darmowy granat"
                        v "Jest mój"
                        v "Nie jest mój"
                        "Dzika bijatyka się zaczęła i Visty wybiły się ze sceny"


                    "Kałach, dywersja" if stan["Kalach"] > 5:
                        show kalach
                        k "Hej seksiaki"
                        v "O, siemka Kałach, co tam"
                        k "A vista z hot-dogami przyjechał"
                        v "VO VOLERA! VUSZAMY VIELNIE"
                        "I dzielnie vybiegli"
                        $ helper -= 25
                        p "Dobra robota Kałach"
                        k "Wiem"
                        hide kalach

                scene vezuwiusz
                "Przeszliście przez straż. Idziecie dalej przez gniazdo i dzielnie dostrzegasz znak vaboratorium"
                p "Chopaky, jesteśmy na miejscu! Pora zrobić rozpierdol"
                menu:
                    "Jak spacyfikuję laba"
                    "Atak frontalny":
                        call checkHP(5) from _call_checkHP_19
                        "Wbiegliście do środka atakując każdego Vistę w okolicy"
                        $ helper -= 10

                    "Pora na blackout" if stan["Jhin"] > 5:
                        p "Ten taki, odetnij im kable"
                        show jhin
                        j "Spoczko foczko"
                        "Widzisz że Jhin wyjmuję katane"
                        p "Nie tak deklu, prąd cię jebnie"
                        j "Fakt"
                        "Schował kanatę i wyjął broń z ręki"
                        p "NIEEEEEE"
                        "Jhin przeciął kable ostrzem z dłoni"
                        "I tak jak przewidywałeś, jebnął go prąd"
                        j "Oj karamba"
                        p "Jhin, jesteś cały?"
                        j "Powiedz mojej żonie, że jej nie mam"
                        if inventory.has_item(THeal) == True:
                            p "Spokojnie kentaki"
                            "Dałeś Jhinowi Turbo uzdrawiacz"
                            $ inventory.remove_item(THeal)
                            $ postacie["Jhin"] += 3
                            achieve Hero
                            j "Dzięki stary"

                        "Reszta dostała się do środka i po ciemku i cichu wybiła resztę"
                        hide jhin
                        $ helper -= 15

                    "Brazylijska sztuka walki" if stan["Krateus"] > 5:
                        show krateus
                        kr "Ni Chu Ja! Hadong! Boom szakalaka!"
                        kr "Walę Vistę prosto w ptaka"
                        play sound "hit1.ogg"
                        "Brazylijska sztuka walki rozgromiła Visty ale sam Krateus też trochę oberwał (głównie od siebie)"
                        p "Myślałeś może o poprawieniu celności?"
                        kr "Bracie, w Brazyli było gorzej"
                        hide krateus
                        $ helper -= 10

                    "Łaskawca, anestezja bojowa" if stan["Laskawca"] > 5:
                        show laskawca
                        pl "Się robi"
                        "Łaskawca podszedł pod szyb i dał trochę gazu"
                        v "Vopaki, vide vpać. Vamimir"
                        pl "Słodkich snów chuje"
                        p "Jeszcze cukrzycy dostaną"
                        pl "Jakieś minusy?"
                        p "Nie wiemy jaki wpływ ma nadmiar insuliny na środowisko Vista"
                        pl "To jest sprawa oczywista, będą grubi. Dzięki temu będą słabsi w unikaniu"
                        $ helper -= 25
                        hide laskawca

                "Laboratorium jest wasze. Badając dokumenty odkryłeś vistowy plan"
                p "Oni są tak głupi że ja pierdolę. Próbowali wrzucić Guna do wulkanu"
                p "I tak chcieli przywołać boga gniewu. No debile"
                "Po przeszukiwaniu postanowiliście wysadzić laba. Szybki trik i cały lab się wyjebie za pięć minut"
                p "Spierdalamy"
                "Zaczęliście biec do wyjścia ale na waszej drodze stanął VPrime"
                scene vinalvoss
                stop music
                play music "bossa.mp3"
                v "Vavava"
                p "Spierdalaj"
                v "NIE"
                p "A powiesz o chuj wam chodzi z tymi klaunami?"
                v "Taki vress vode"
                p "Mogłem się domyślić"
                menu:
                    "Ostatni przeciwnik"
                    "Let mi solo him":
                        v "Oh? You're approaching me? Instead of running away, you're coming right to me?"
                        p "I can't beat the shit out of you without getting closer."
                        v "Oh ho! Then come as close as you like."
                        p "Ora"
                        v "Too slow, too slow! The Vorld is the ultimate Stand."
                        "ora ora ora ora vs vuda vuda vuda vuda"
                        p "It's over VMax. I have a high ground"
                        v "Vurwa"
                        p "GIŃ"
                        play sound "hit.mp3"
                        "Dostałeś srogi wpierdol ale pokonałeś wroga"
                        call checkHP(20) from _call_checkHP_15
                        v "To jeszcze nie jest koniec"
                        p "Panowie wychodzimy"
                        "I w taki sposób wyszliście z vazy"
                        $ helper -= 10
                        jump akt1pods
                    
                    "Pora na spawanie" if stan["Hartmann"] > 5:
                        p "Hartmann, bier migomat"
                        show hartmann
                        h "PORA NA SPAWANIE WORA"
                        v "Nieeeeeeeee"
                        "Szybkim ruchem Hartmann zespawał Vprima"
                        v "Moje kochones"
                        p ":czacha"
                        h ":czacha"
                        p "Panowie wychodzimy"
                        " I w taki sposób wyszliście z vazy"
                        $ helper -= 15
                        hide hartmann
                        jump akt1pods

                    "Góra, prawo, dół dół dół" if stan["Cypher"] > 5:
                        show hellciper
                        p "Cypher, pora na nalot"
                        c "Cypher łan w drodze"
                        v "Co kurwa? Jak ty niby chcesz zrzucić bombę w budynku?"
                        v "Jakby, tu nie ma jak wlecieć a jak spadnie na dach to chuja mi zrobić"
                        v "Kurwa, przecież Cypher stoi obok. To nie ma prawa działać"
                        c "To pa ten trick"
                        "Cypher wziął potężnego bucha i nad v prime pojawiła się chmura"
                        v "I to wszystko?"
                        c "Hi Hi Ha Ha"
                        "Z chmury wypadła mała bomba"
                        v "Co do kurwy"
                        "I ta bomba wybombowała vprima"
                        p "Nie wierzę że to mówię ale dobra robota Cypher"
                        c "DH poleca się"
                        p "Panowie wychodzimy"
                        " I w taki sposób wyszliście z vazy"
                        $ helper -= 25
                        hide hellciper
                        jump akt1pods

                    "Zielone światło" if stan["Gun"] > 5:
                        scene idrive
                        play music "idrive.mp3" volume 0.2
                        g "Ja jadę"
                        v "Ale jak, ty nawet nie masz auta"
                        g "Brum Brum"
                        play sound "BOOM.mp3"
                        "No i Vista zrobił boom"
                        p "Jak ty to zrobiłeś? "
                        g "Kupiłem szczurom RC autko i Hartmann podczepił minę p.piech"
                        p "Sprytne"
                        stop music
                        play music "CMS.mp3" volume 0.2
                        $ helper -= 20
                        jump akt1pods

            "Na głośno":
                p "Kurwa chłopaki, nie pierdolimy się w tańcu! Zapierdalamy na nich"
                "Dzielenie ruszacie szturmować vazę"
                menu:
                    "Jak się teraz dostaniecie do środka?"
                    "Zapukam":
                        p "Puk Puk"
                        v "Vto vam?"
                        p "Dzień dobry. Nazywam się [player_name]. Jestem nowym V"
                        v "O! Klawo! Zapraszamy."
                        "Vista otworzył drzwi"
                        v "Zaraz, zaraz, ja was chyba znam"
                        p "To prawda"
                        "I zastrzeliłeś Vistę"
                        p "Hasta la vista, vista"
                        "Dostaliście się do środka"
                        $ helper -= 15

                    "Kałach bazooka" if stan["Kalach"] > 5:
                        show kalach at left
                        k "Boom, boom, boom, boom I'm going to Coom"
                        "I Kałach wystrzelił ale rakieta wybuchła fajerwerkami"
                        k "Co jest kurwa"
                        show cypher
                        c "Hi Hi Ha Ha"
                        hide cypher with dissolve
                        p "To co teraz?"
                        k "Chuj"
                        "Kałach podszedł bliżej i kopnął drzwi"
                        k "Tada!"
                        "Możecie teraz wejść"
                        $ helper -= 10

                    "Krateus, Los pollos hermanos" if stan["Krateus"] > 5:
                        show krateus at left
                        kr "Los españoles necesitan ayuda! Cavador, tienes que cavar"
                        kr "Artillero, nos están cubriendo i teraz atak ostateczny"
                        kr "Ekspansja domeny: KRATA DZIKA"
                        mg "Przyjmuję twoją ofertę"
                        kr "Otwarte"
                        "I drzwi się otworzyły"
                        p "Jak ty to zrobiłeś?"
                        kr "Battle pass słonko"
                        $ helper -= 25

                    "Gun, miej fun" if stan["Gun"] > 5:
                        show gun at left
                        g "Tajest ale zaskoczę was wszystkich, tym razem nie prowadzę"
                        p "Faktycznie plottwist"
                        g "Spokojnie [player_name], Mączysław prowadzi"
                        p "Co kurwa?"
                        r "Skłik Skłik"
                        "Widzisz jak rozpędzony tir jedzie prosto w drzwi"
                        g "Pamiętaj o hamulcach"
                        r "Skłik?"
                        g "NIEEEEE MĄCZYSŁAW!!!"
                        "Tir jebnął"
                        g "MÓJ AGENT"
                        p "Nie martw się Gun, pewnie trafił do ratowego nieba"
                        g "Gówno, on był diabłem wcielonym"
                        r "Skłik Skłik!"
                        g "O CHOLERA, ON ŻYJE! RATTER POTTER"
                        "Ominąłeś chwilę czułości i poszedłeś dalej"
                        $ helper -= 20 

                "Jesteście w środku"
                scene vrogi
                "Biegnie na was z dziesięć rozsierdzonych vist"
                menu:
                    "Co teraz?"
                    "Pif Paf słoneczko":
                        "Rozpocząłęś strzelanie, a drużyna strzelała wraz z tobą."
                        call checkHP(15) from _call_checkHP_22
                        "Troszeczkę oberwałeś ale udało Ci się zostać bogiem gniewu i wojny"
                        "Możesz dzielnie iść dalej ale nie możesz zapomnieć o lootowaniu"
                        $ edki += 150
                        "Trochę mamony się znalazło"
                        $ inventory.add_item(AR)
                        $ inventory.add_item(Vron)
                        $ vdolce += 3
                        "I trochę Vidolcy"
                        $ helper -= 20

                    "Pora Geentować" if stan["Laskawca"] > 5:
                        show laskawca at left
                        pl "Się robi"
                        "Łaskawca zaczął strzelać na oślep. Trafił wszystkie 11 strzałów"
                        "Spytasz się, jak 11 strzałów na 10 vist. Odpowiedź jest bardzo prosta"
                        "Jeśli kiedykolwiek będzie kombat w którym Gun nie dostanie rykoszetu"
                        "To się chyba posram."
                        g "Aua ):"
                        $ helper -= 15

                    "Hartmann! Spaw bojowy" if stan["Hartmann"] > 5:
                        show hartmann at left
                        h "No to spawamy! Ja nie wiem co to jest rzecz niemożliwa. Fach w ręku, tak bywa"
                        h "Czasem beton, cementem się spawa, Czasem, Visty się doprawia"
                        "Vięso Vist topiło się pod wpływem spawarki do ludzi"
                        "Czujesz się strasznie,jesteś niczym więcej niżeli potworem"
                        "Kreatura twojego rodzaju nie powinna mieć kontaktu z ludźmi"
                        "Szczęśliwie to jest tylko gra i nie będziesz chciał powtarzać tego irl?"
                        "Prawda"
                        menu:
                            "Prawda?"
                            "Prawda":
                                "To dobrze"
                                "Wiedźmin 3: kamień z serca"
                                $ helper -= 10
                            
                            "Fałsz":
                                "Ty chory pojebie"
                                $ session_time = int((renpy.get_game_runtime() - persistent.session_start_time) / 60)
                                $ persistent.czasGry += session_time
                                $ renpy.quit()

                    "Czy moc pay to play też na mnie działa?" if edki > 199:
                        achieve Bug
                        mg "TAK"
                        p "O jasna dupa, to Wielki Dzik"
                        mg "To prawda, jestem więc myślę"
                        p "Czy możesz mi pomóc w walce z Vistami?"
                        mg "Mogę zrobić wszystko ale ile jesteś gotowy za to zapłacić?"
                        menu:
                            "Ilę chcę dać?"
                            "Może dziczeg?" if inventory.has_item(NRG) == True:
                                $ inventory.remove_item(NRG)
                                mg "Oj kolego, kupiłeś mnie tym jak paczkę żelków. Oto moje błogosławieństwo"
                                p "Dziękuję wielki dziku"
                                $ helper -= 25

                            "Masz tu 200 edków i spierdalaj":
                                mg "Przyjmuję tę ofertę"
                                p "Fr fr?"
                                mg "Tak"
                                mg "Vistus znikus"
                                "I tyle było z Vist"
                                p "Dziękuję wielki dziku"
                                "Ale dzika już tu nie było"
                                $ helper -= 25

                            "Dusza Kałacha":
                                mg "Ambitnie. Przyjmuję tę ofertę"
                                show kalach at right
                                k "Co kurwa?"
                                mg "bywaj Kałachu"
                                k "KURWAAAAAAAAAAAAAAAAAAAAAAAA"
                                hide kalach with dissolve
                                $ stan["Kalach"] = -1
                                $ postacie["Kalach"] = -9999
                                mg "Paskudny w smaku"
                                "Wielki dzik potężnym beknięciem wystrzelił Visty poza czwartą ścianę"
                                p "Dziękuję wielki dziku"
                                "Ale dzika już tu nie było"
                                achieve Ocult
                                $ helper -= 15
                            
                            "Jednak nie, spierdalaj":
                                mg "Teraz mnie wkurwiłeś"
                                p "O nie, tylko nie to, JESTEŚ TYLKO WYTWOREM MOJEJ WYOBRAŹNI"
                                mg "Kłamstwo"
                                scene vibechec
                                play sound "skokostrach.mp3"
                                $ MainMenu(confirm=False)()

                "Idąc dalej widzisz laboratorium"
                scene vab
                "Visty planują zbudować wielki wulkan"
                "Masz rację, pojebało ich"
                "Ich głównymi składnikami są ocet i soda kuchenna. Oznacza to zagrożenie poziomu Demon"
                "Całe NC może zostać zalane wulkanową wydzieliną"
                p "Pora ich powstrzymać"
                p "Hujsaria"
                menu:
                    "Wybierz styl dewastacji"
                    "Bombka" if inventory.has_item(Granat):
                        p "Przeciwpiechotny granat sromotny!"
                        p "A teraz. SPIERDALAMY!"
                        play sound "BOOM.mp3"
                        "Granat wybuchając wymieszał składniki granatu"
                        "Ta bojowa mieszanka zaczęła reagować"
                        "Nie minęła chwila jak to gówno zaczęło wypełniać vazę"
                        p "Szybciej panowie, szybciej!"
                        "Resztkami sił udało wam się wybiec z placówki"
                        $ helper -= 25
                    
                    "Ocet jest smaczny, wypiję":
                        call cipflash from _call_cipflash_16
                        mg "Obrzydzasz mnie"
                        "Wypiłeś cały ocet jaki mieli"
                        "Dzięki twojej brawurze visty poniosły straty finansowe"
                        "Całe 4,50 w plecy"
                        play sound "BURP.mp3"
                        p "To chyba tyle. Misja wykonana. Możemy wychodzić"
                        "I spokojnym krokiem wyszliście z pomieszczenia"
                        achieve Dis
                        $ helper -= 10

                    "Łaskawca, obczaj ten proszek" if stan["Laskawca"] > 5:
                        show laskawca at left
                        pl "Wydaje mi się że to jest kreda"
                        p "Jak kurwa kreda?"
                        pl "No normalnie"
                        p "A wulkan nie powinien działać z sodą?"
                        pl "Powinien ale to jest Vista dynamicks"
                        p "No dobra, punkt dla Ciebie. To wychodzi na to, że żadnego zagrożenia nie ma"
                        p "Spermastycznie. Wychodzimy!"
                        "I spokojnym krokiem wyszliście z pomieszczenia"
                        $ helper -= 15

                    "Zrobię delikatny trolaż" if inventory.has_item(Kokos):
                        p "Mam taki śmieszny pomysł"
                        "Podszedłeś do stołu i zamieniłeś sodę na koks"
                        p "Co prawda wychodzę przez to na minus ale będzie śmiesznie jak im to nie zadziała"
                        "Po delikatnym sabotażu wyszliście z vazy"
                        $ helper -= 20

                p "Kurwa panowie, to było zajebiście łatwe"
                v "Vie Vwal vnia vrzed vachodem vłońca"
                p "Co kurwa"
                scene vinalvoss
                stop music
                play music "bossa.mp3"
                v "Vestem V-Max. Vopowa vakość V"
                p "Oj nie zesraj się"
                v "Va vóźno"
                "Widzisz jak V-Max się powiększa"
                p "No tak, chuj mi w dupę"
                v "Va Va Va! Vykuj vię va vmierć"
                p "No to pvp"
                menu:
                    "No to jak cię zabiję?"
                    "Stary dobry pistolet" if inventory.has_item(Pistolecik):
                        p "Giń Visto"
                        "Wystrzeliłeś z pistoletu ale vista podszedł do Ciebie bliżej"
                        v "V vasz"
                        call checkHP(19) from _call_checkHP_16
                        p "Kurwa bolało"
                        v "V veraz vrugi vtak"
                        p "Ej kurwa, to jest nie fair"
                        p "Musisz poczekać na swoją turę"
                        v "V viździe vo vam"
                        call checkHP(2) from _call_checkHP_17
                        "Potężny atak Visty tylko cię drasnął"
                        p "Ja też"
                        play sound "Paf.mp3"
                        v "Vkurwysyn"
                        p "Spoczywaj w koszu v"
                        p "Misja ukończona"
                        $ helper -= 25
                        jump akt1pods
                        
                    "Pora na kręcienie wora" if stan["Krateus"] > 5:
                        show krateus
                        kr "Chodź tu kurewko"
                        v "Vde"
                        kr "Zostaniesz świadkiem brazylijskich eggzekucji"
                        p "W sensie?"
                        v "Vlus veden"
                        kr "No bo chodzi o to, że w brazyli jest dużo eunuchów"
                        kr "Bo tam terroryści strzelali w jaja"
                        p "To dobrego cela mają"
                        kr "Właśnie nie, oni celują w głowę ale tam jest ciężka amunicja"
                        p "Ale głupota"
                        kr "No. Dlatego ja polegam na pięściach"
                        v "Vo vo vo ven ved-valk?"
                        kr "Dla jajec"
                        v "V vensie"
                        "Przez całą pogadankę Kreteus zbliżał się do V-Maxa"
                        kr "Egg stiler"
                        v "Vvaaaaaaaaaa"
                        kr "Turbo kręcenie wora! I teraz finiszer, cios prosto w prostatę"
                        play sound "Bonk.mp3"
                        scene black
                        "Ze względu na brutalną naturę tej sceny zastąpiłem ją opisem jajec"
                        "Wielkie i czerwone jak pomidory"
                        "Dziękuję za uwagę"
                        show krateus
                        kr "Kurwa, chyba przesadziłem"
                        p "Chłopie, tortury Trewora były bardziej ludzkie"
                        kr "Serio?"
                        p "No, chodźmy stąd, muszę chyba iść na terapię"
                        kr "No sorson, ale jak to pisze jest miesiąc geja, przez to nie mam hamulców"
                        $ helper -= 10
                        jump akt1pods

                    "Volololo" if stan["Kalach"] > 5:
                        k "Niech będą pochwalone uda. I jak powiedział kiedyś prorok:"
                        k "„Błogosławione uda, które nie postępują w radzie bezbożnych, ani nie stoją na drodze bonera, ani nie siedzą na tronie simpów. Ale jego upodobanie jest w prawie THICC Ud!"
                        v "Vo vy vierdolisz?"
                        k "Twoją matkę"
                        v "Vooooo! Vylko vie voją vamusie! Varża"
                        k "Vistolo volololo"
                        v "Vo vaj vad"
                        "Takim dziwnym sposobem V-Max dołączył do drużyny"
                        v "Vitam vanowie. Vychodzimy?"
                        p "Wychodzimy"
                        "Wychodzicie z vazy"
                        v "Vo vo vak vikło?"
                        p "VMax nieee"
                        "I Vistę vysadziło"
                        "Vista opuszcza drużynę"
                        $ helper -= 15
                        jump akt1pods
                        

    elif Frakcja == 1:
        $ oldFrakcja = 1
        show cypher
        c "Hihi ha ha"
        c "Pozwól młody że ja zajmę się dowodzeniem"
        p "No spoko, szefie"
        c "Szybko się uczysz, będą z Ciebie psy. Diamentowe takie"
        scene cypherkopter
        play sound "heli.mp3"
        "Pyr pyr pyr"
        p "Gdzie my lecimy?"
        c "To jest ważna misja! Lecimy do żabki!"
        stop sound
        scene frogszop
        stop music
        play music "szop.mp3"
        show cypher at right
        c "Dzień dobry szanowny pracowniku tego sklepi"
        fse "Dzień dobry? Pomóc w czymś?"
        c "Tak młody, potrzebuję knura, najlepiej z dwa"
        fse "W sensie, że dzika, tego energetyka?"
        c "Czytasz mi w myślach brachu"
        fse "To są one w lodówce, tam"
        c "Wielkie dzięki szanowny kawalerze"
        hide cypher
        p "Przepraszam za niego, Szef nie wierzy w kobiety"
        fse "To i tak nie jest najdziwniejszy klient"
        p "Bywali gorsi?"
        fse "Bywali tacy co chcieli hot-doga dwie minuty przed zamknięciem"
        fse "Są mochery płacące rachunki są żule i w ogóle"
        fse "Dramat wielki"
        p "Faktycznie brzmi strasznie"
        fse "No. Cieszę się że mam tu ochronę. Jest dzielny Kacperek, siedzi tam z tyłu"
        fse "Cały dzień obstawia mecze ale jak jest potrzeba to przychodzi"
        c "Szajse ale tu jest duży wybór! Ponętne towary, chciałbym nabyć je wszystkie" 
        fse "Tylko proszę tam nic nie rozwalić!"
        c "Spokojnie młody, jestem ostrożny"
        p "Nie, on nie jest ostrożny"
        fse "Właśnie widzę"
        show cypher at right
        c "Dobra, mam wszystko"
        fse "No dobrze, to będzie razem 40 edków"
        c "Karamba drogo"
        "Cypher wyjął cygaro i je zapalił"
        fse "Proszę pana, tu nie wolno palić"
        c "To pa ten trick"
        "Cypher wziął giga bucha i zadymił cały sklep"
        hide cypher with dissolve
        fse "OCHRONA"
        p "Nie będzie potrzebna, ja zapłacę"
        $ edki -= 40
        fse "Macie kurcze szczęście, grubcio zaczął już wstawać"
        p "Przepraszam za kłopot"
        "Wróciłeś do DH koptera"
        stop music
        scene cypherkopter
        play sound "heli.mp3"
        p "Co to kurwa miało być"
        c "Portfela zapomniałem ):"
        p "Nie mogłeś powiedzieć?"
        c "Honor mi zabrania"
        p "Powiedz mi że masz to co chciałeś"
        c "Nie"
        p "TO CO TY KURWA KUPIŁEŚ?"
        c "Panini"
        play sound "EAT OR MUNCH.mp3"
        c "Całkiem smaczne"
        p "Popierdoli mnie"
        c "Cichaj tam, najedzony punk to gotowy punk"
        p "To mogłeś coś mi kupić"
        c "Kupiłem ale zjadłem"
        p "Niby kiedy?"
        c "Jak rozmawiałeś z typem"
        p "Szef roku kurwa jego mać"
        c "A dziękuję"
        "Resztę drogi lecieliście w ciszy"
        c "To to jest ta cała vaza?"
        p "Nie wiem, ty nastawiłeś nawigację"
        c "No to mamy czeski remis"
        c "Chuj, Młynarczyk! Pora na bombę!"
        p "Na randomowy budynek chcesz zrzucić bombę?"
        c "Jeszcze jak"
        "Bomba spadła, niestety nie trafiła"
        c "To mi się podoba, kolejny sukces"
        p "Ale ty nie trafiłeś"
        c "To był zrzut ostrzegawczy"
        p "Masz więcej bomb?"
        c "Nie"
        p "To co teraz robimy?"
        c "Wchodzimy"
        play music "CMS.mp3"
        p "W sensie?"
        "Ciper kopter zaczął lecieć prosto w budynek"
        stop sound
        play sound "BOOM.mp3"
        scene black
        c "Kolejne udane lądowanie (2 martwych, 14 rannych)"
        scene wonsuwiusz
        show cypher
        c "Proszę proszę, tożto laboratorium! Sprawdźmy to"
        p "Dobrze Cypher"
        c "Kurwa, oczekiwałem jakiegoś entuzjazmu! Dobra jebać. Dawaj do środka"
        "Weszliście do środka"
        c "CO TO KURWA JEST"
        p "W sensie?"
        c "CZY TY TEGO KURWA NIE WIDZISZ? TE SKURWYSYNY DOMALOWAŁY MI WĄSY"
        p "Zabawne"
        c "A CI PIERDOLNE! TO JEST ATAK NA MÓJ WIZERUNEK"
        c "PRZYSTOJNEGO PATRIOTY I WYCHODZI JAKIŚ CHUJ Z WĄSEM"
        c "ABSOLUTNIE NIEWYBACZALNE"
        p "Spokojnie"
        c "JAK JA MAM BYĆ KURWA SPOKOJNY?"
        p "O patrz"
        "Podszedłeś do plakatu i oderwałeś wąs"
        scene vezuwiusz
        show cypher
        c "No dobra, uspokoiłem się"
        p "Serio?"
        c "NIE KURWA. JEDYNYM WEZUWIUSZEM TU JESTEM JA! ROZPIERDOLĘ ICH"
        hide cypher
        "Rozsierdzony wyszedł z labu"
        "I po chwili zawył alarm"
        play sound "alarm.ogg"
        p "Pojebie mnie"
        p "Ale dobra, jestem tu sam, muszę skończyć misję"
        if inventory.has_item(Granat):
            p "Siepię granatem"
            "Granat poleciał"
            p "A ja spierdalam"

        elif inventory.has_item(Vomba):
            p "Ty kurwa, ja mam Vombe! Rozpierdolę ich ich własną bronią"
            "Bomb has been planted"
            p "Pora wiać"

        else:
            p "Jasny chuj, nic nie mam"
            p "Proces autodestrukcji, Visty muszą to mieć"
            p "A ten wielki przycisk nie klikać chyba będzie od tego"
            p "I tak nie mam innego wyjścia"
            "Nacisnąłeś przycisk i zacząłeś uciekać"
            "Niestety Visty zaczęły strzelać"
            call checkHP(15) from _call_checkHP_18

        p "Jasna dupa, zaraz tu umrę"
        "Vistowa grupa bojowa jest tuż za tobą"
        p "KURWA CYPHER"
        show cypher at bounce
        c "Jestem"
        p "Co!"
        c "Pa na to"
        "Cypher zaczął strzelać w kierunku Vist"
        "Cały magazynek wystrzelił"
        "Niestety miał tylko 4 pociski"
        p "Serio kurwa?"
        c "Sorka, kontrola rodzicielska od Ocelota"
        c "Ale mam jeszcze granatnik"
        "Z ręki Cyphera wysuwa się granatnik"
        c "Ciekawe czy działa"
        "Po strzale, z granatnika leci strumień ognia"
        c "Ło kurwa"
        p "Niezły ten granatnik"
        c "Customowy"
        "Okazało się, że Visty są słabe na ogień"
        c "Przed Cypherem udeż czołem, Cypher górą, chociaż dołem"
        p "A to co kurwa jest"
        c "A se wymyśliłem, śmiesznie brzmi"
        p "Cypher, jesteśmy we wrogiej bazie"
        c "No i?"
        p "Możemy zaraz umrzeć"
        c "Ja nie. Ja mam plot armor"
        p "Aha 66"
        c "Koniec smęcenia, wychodzimy"
        p "I teraz nagle chcesz wychodzić?"
        c "Nom, nowy helikopter jest"
        p "Jak to? Przecież zawsze miałeś tylko jeden"
        c "Magia dzika młody"
        p "Nic już nie rozumiem"
        c "Same"
        "Skończyliście rozmawiać i wyszliście z laba"
        "Ale na waszej drodze stanął V-Max"
        scene vinalvoss
        stop music
        play music "bossa.mp3"
        v "Vrrr"
        c "Spierdalaj ziomo, śpieszy nam się"
        v "Vozjebaliście vi vazę, vniszczyliście vasze vadania"
        v "Vrujnowaliście vój vom v vabiliście voich vrzyjaciół"
        v "Vlaczego viałbym Vię vie vabić v vej vwili?"
        c "Bo ja będę pierwszy"
        hide cypher
        show hellciper
        c "Góra, prawo, dół, dół, dół"
        v "Vo?"
        c "Półtonowa bomba Młynarczykowa"
        "Precyzyjnie udeżyła w Vistę"
        p "Kurwa Cypher, od kiedy masz takie skile?"
        c "Od zawsze w sumie"
        p "To czemu tego wcześniej nie wezwałeś?"
        c "Nie byłoby takich emocji"
        c "Mogliśmy sobie jak rodzinka postrzelać"
        p "Ja prawie umarłem"
        c "Ale nie umarłeś i to się liczy"
        c "Zaczynam cię lubić [player_name]"
        hide hellciper
        show cypher
        $ postacie["Cypher"] += 3
        p "Wracajmy już do domu"
        call cipflash from _call_cipflash_17
        c "Tak wcześnie?"
        p "No zrobiliśmy to co mieliśmy"
        c "Nudziaż! Jednak mi się nie podobasz"
        c "Wracasz z buta ja lecę do żabki"
        c "Jak to mówimy w niemczech, Adios"
        "I Cypher odleciał"
        p "Adios jest po Hiszpańsku"
        jump akt1pods

    elif Frakcja == 3:
        $ oldFrakcja = 3
        p "Dobra kurwa, jestem Vista"
        p "Nie mogę pozwolić aby nasze tajne projekty zostały zniszczone ale z drugiej strony"
        p "Nikt mi za obronę nie płaci. Co powinienem zrobić?"
        menu:
            "Pozostań V":
                p "Dobra kurwa, co ja teraz zrobię. Zawsze jest opcja kulki w łep"
                p "Ale to zostawię sobię na potem"
                p "Wiem kurwa!"
                p "Zadzwonię do Vistów i powiem im żeby spierdalali. Następnie ściągniemy tam VMaxów"
                p "Jak oni tam wejdom to sie zesrają! Hihihaha"
                "Dzwonisz do Vist"
                v "Halo"
                p "Za halo w morde walo"
                v "Vrzepraszam"
                p "Vo v vit"
                "Opowiedziałeś V swój plan"
                v "Vurwa vądry vesteś"
                p "Viem"
                v "Vykonajmy vo"
                "I zaczęliście wykonywać swój genitalny plan"
                scene vniazdo
                show kalach at right
                k "Kurwa, pusto tu"
                show laskawca at left
                pl "Kurde blaszka masz rację"
                k "Ja zawsze mam rację"
                pl "Dobra spokojnie, wchodzimy. Ciekawe czemu [player_name] nie jest z nami"
                p "Oj zaraz się dowiesz"
                scene vaxy
                v "Viespovianka"
                "Słyszałeś bardzo brutalne dźwięki walki"
                p "Słodkich snów chuje"
                scene black
                "Chillowałeś sobie w spokoju, do pewnego momentu"
                show kalach at right
                show laskawca at left
                pl "Pobudka słoneczko"
                p "Vo vest vurwa"
                k "Sprzedałeś nas kurwisynu"
                p "Vo? Va vigdy!"
                pl "Słyszymy jak mówisz, sorki stary"
                p "Vie, vanowie, va vie vhciałem"
                k "Koło chuja mi to lata! Wypierdalasz na tamagoczi"
                "Dostałeś taktycznym paralizatorem"
                k "Idziemy do bazy, czeka Ciebie przesłuchanie"
                scene bev
                achieve Tam
                "GG byczku"
                $ MainMenu(confirm=False)()


            "Wróć do normalności":
                p "Koniec z Vistami"
                p "SV-vists: off"
                $ Frakcja = 0
                jump wojowezadanie


    elif Frakcja == 4:
        $ oldFrakcja = 4
        scene vniazdo
        show kalach
        k "Dobra, ja szefuje"
        p "Dobrze Kałach"
        k "Plan jest prostrzy niż budowa uda"
        k "Robimy krucjatę"
        p "Nic mi to nie mówi"
        k "Bo w dupie byłeś i gówno widziałeś"
        k "Krok 1: piszę posta o wojnie"
        k "Krok 2: wyznawcy się pojawiają"
        k "Krok 3: ???"
        k "Krok 4: Profit"
        p "Czemu nie znasz kroku trzeciego?"
        k "Ja wtedy chleję"
        p "I to jest cały twój plan, wezwać ludzi niech to zrobią za Ciebie?"
        k "Ta, to tylko Visty, nie chce mi się marnować ammo plus, Vista jest śmieszny"
        p "Jakim cudem ty jesteś jeszcze głową tego kościoła?"
        k "Niebotyczna charyzma, inteligencja Ejnsztajna i wątroba z tytanu"
        p "Tylko tyle wystarczy?"
        k "Jakie kurwa tylko tyle? Chopie, to jest w chuj pracy. Raz na dwa dni muszę wrzucać zdjęcie na stronę"
        k "Skurwysyńsko męcząca praca"
        p "Się znalazł influenser po chuju"
        k "TO PATRZ I SIĘ KURWA UCZ"
        "Kałach sam poszedł prosto do gniazda"
        p "Popierdoliło go albo promile nie są już procentami"
        "Słyszysz tonę strzałów z vniazda"
        p "Zobaczę jak mu idzie, jeśli zdechł to free itemy"
        scene vniazdo
        p "Jasna dupa, jaka rzeź"
        "A Kałach cały czas strzela"
        p "Co on, w boga wojny się zmienił?"
        k "A żebyś kurwa wiedział"
        show kalach
        k "Jak jestem wkurwiony"
        k "To nie troluje i napierdalam"
        p "No to dobrze Ci idzie"
        k "Spokojnie, ja dopiero się rozkręcam"
        scene vinalvoss
        stop music
        play music "bossa.mp3"
        show kalach at left
        k "Ło kurwa, VMax się pojawił"
        v "Vrrrr"
        k "[player_name] zajmiesz się nim?"
        p "Popierdoliło Cię, jak ja mam chujowe staty"
        k "No to patrz na to"
        scene stand
        k "W imię ojca, i syna i uda wielkiego! Niech wpierdol dosięgnie jego"
        v "Vo Vhuj Vi vodzi?"
        k "Specjalny atak Alfonsowy! Pora na udowy atak krzyżowy"
        v "Vo vie"
        "I VMax dostał wpierdol"
        p "Cholipka Kałach"
        k "Widzisz? Tak się kończy jak mnie wkurwisz"
        p "No dobra, przepraszam"
        k "A spierdalaj"
        p "Aha 66"
        "I Kałach poszedł sobie w pizdu"
        jump akt1pods

    elif Frakcja == 6:
        scene frogszop
        fse "Siema [player_name], mam wiadomość od szefa"
        p "O kierwa, co on takiego chce?"
        fse "Powiedział, że jak pójdziesz na tą robotę od wojska to Cie wyjebie z roboty"
        p "Pojebało go"
        fse "Dokładnie to samo mu powiedziałam"
        fse "I co masz teraz w planach"
        menu:
            "Co ja teraz zrobię?"
            "Żegnaj żabko":
                p "Odchodzę, to jednak nie dla mnie"
                fse "Tylko nie daj się zabić"
                p "Pa teraz"
                $ Frakcja = 0
                jump wojowezadanie

            "Zapłacę mu za czas mojej nieobacności" if edki > 1999:
                fse "Bardzo to ambitne z twojej strony, raczej to mu się spodoba"
                $ edki -= 2000
                p "Oto moje pieniądze, bywaj natenczas"
                fse "Żegnaj, adios"
                $ Frakcja = 0
                $ oldFrakcja = 6
                jump wojowezadanie

            "Może uciekniemy stąd razem?":
                fse "OMG Anon, myślałam o tym odkąd Cię zobaczyłam"
                p "No to klawo, spierdalajmy"
                scene bew
                achieve Crg
                "CRINGE DETEKTED"
                $ MainMenu(confirm=False)()

    return