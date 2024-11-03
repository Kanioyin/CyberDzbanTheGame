# BobCAchievements Code by Bob Conway 2023
# Version 1.0 - June 6, 2023
# For use with the Ren'Py engine

# Available with a Creative Commons 0 (CC0) license
# Attribution appreciated; please link bobcgames.com

# Software is provided "as is" without warranty of any kind

############################################
#             USAGE DIRECTIONS             #
############################################

# 1) Drop this file (0bobcachievements.rpy) into the game/ folder of your Ren'Py project.

# 2) Add your achievements to the below code as tuples of (reference_id, user title, user description)
#    or (reference_id, user title, user description, True) if you want your achievement name to be hidden
#    when using sbobcachievements.rpy.
#   (You can also replace or remove the two sample achievements.)
#   (If you're using Steam, the reference_ids should be the API name of the achievements.)
#   (This does not currently support progress stats.)
define BOBCACHIEVEMENT_LIST = (
    ("Poczatek", _("Weź w to zagraj"), _("Tylko 3 procent cyberdzbanów to ma!")),
    ("GitGud",_("Umarłeś"), _("Dwukropek czacha.")),
    ("Iabk", _("Wróciłem!"), _("Niespodzianka skurwysyny!")),
    ("Aboes", _("A bajt of 45?"), _("Fryderyk zasmakował twojej krwi.")),
    ("Gunpp", _("Gun++"), _("Gun dołączył do ataku.")),
    ("Kalpp", _("Kałach++"), _("Kałach dołączył do ataku.")),
    ("Cippp", _("Cypher++"), _("Cypher dołączył do ataku.")),
    ("Harpp", _("Hartmann++"), _("Hartmann dołączył do ataku.")),
    ("Laspp", _("Łaskawca++"), _("Łaskawca dołączył do ataku.")),
    ("Jhipp", _("Jhin++"), _("Jhin dołączył do ataku.")),
    ("Krapp", _("Krateus++"), _("Krateus dołączył do ataku.")),
    ("Musk", _("Giga Musk"), _("Bardzo się starałeś...")),
    ("GG1", _("Fin"), _("...ale chuja dostałeś,")),
    ("Ttsd", _("TO TAK SIĘ DA?"), _("Umarłeś przy tworzeniu postaci.")),
    ("Msnc", _("Mi się nie chce"), _("Uciekłeś przed przygodą")),
    ("Holy", _("Krzyżowiec"), _("Dołączyłeś do kościoła Kałacha.")),
    ("Damm", _("Pies"), _("Zostałeś psem, takim z diamentów.")),
    ("Smrut", _("Ale to śmierdzi"), _("Dałeś Gunowi ser.")),
    ("Fedex", _("Kurier"), _("Po co mu to przyniosłeś?")),
    ("Shizo", _("Schizo"), _("Gadasz ze szczurem!")),
    ("Mill", _("Ogar na wolności"), _("Młynarczyk jest jednak niebezpieczny.")),
    ("Pyro", _("Roasted"), _("Nadpaliłeś sojuszników. Gratulacje, czy coś.")),
    ("Foch", _("Chyba ma okres"), _("Cypher się na ciebie obraził.")),
    ("Impostor", _("CZTERY!"), _("Ten Taki gryzie piach.")),
    ("Alesex", _("Podrywacz"), _("Żadna kobitka nie uciekła!")),
    ("Futa", _("Giga siur"), _("Halinka swoje w łóżku potrafi")),
    ("Bomb", _("Vgień Vistobójczy"), _("Wysadziłeś ich, ich własną bombą.")),
    ("Bogol", _("Bogol"), _("Jak Cię było na to stać?")),
    ("Ocult", _("Okultysta"), _("Dlaczego akurat Kałach?")),
    ("Dis", _("Brak gustu"), _("Na prawdę Ci to smakowało???")),
    ("Hero", _("Łaskawca 2"), _("Nie możesz teraz zginąć, to nie kanoniczne")),
    ("Curs", _("Przeklęty"), _("Dopadła Cię klątwa.")),
    ("Frik", _("Pierwsza działka"), _("Ten koks to faktycznie fajna sprawa.")),
    ("Tam", _("Jeść, pić, spać"), _("Srać mi też się chce.")),
    ("Full", _("Drużyna pierdzenia"), _("Jak ty chyba masz max charyzmy.")),
    ("Clos", _("Było blisko"), _("Faktycznie warto było go mieć.")),
    ("Mocz", _("Super pęcherz"), _("Teraz mój wór jest większy!")),
    ("Fri", _("Piątkowa noc"), _("Takiej imperzy się nie spodziewałem.")),
    ("Bug", _("ON ISTNIEJE"), _("Porozmawiałeś z głosem w głowie.")),
    ("Cip", _("Wcipiam się"), _("Pierwszy cip zdobyty.")),
    ("Red", _("Czytelnik"), _("A se poczytam.")),
    ("Zns", _("Zło nie śpi"), _("A nawet czasami leczy.")),
    ("Zjw", _("Pomekon"), _("Znalazłeś je wszystkie?.")),
    ("Psy", _("Cipnik"), _("Ty weź może strzelaj a nie edki wydajesz")),
    ("Eko", _("Ekolog"), _("Po chuj ty to wyjebałeś")),
    ("Crg", _("Cringe"), _("Po co Ci ta baba?")),
    ("Frg", _("Żabiarz"), _("Pierwsze frogi w nogi")),
    ("Egg", _("Ale jaja"), _("Znalazłeś przeklęte jajca")),
    ("Bir", _("Dobre piwko"), _("Dobry browarek nie jest zły"),)
    ("Wow" _("Poszukiwacz"), _("Szukałeś złota, znalazłeś futro"))
    )
    
# 3) In your game script, when you want to grant an achievement, type "achieve <reference_id>" without the
#    quotes or <> (and without a leading $). For example, to grant the sample "Started The Game" achievement:
#
#    label my_test_label:
#        "This is some sample script."
#        achieve started
#        "Now you've granted the "Started The Game" achievement!"
#
#    If you need to grant an achievement via python code, use bobcachievement_grant(reference_id)
    
# 4) By default, achievement grants will be displayed using renpy.notify with this prefix text. If you
#    want to display them using a custom screen instead, override the screen variable with a string of
#    the name of the screen you want to use. Or just change the prefix text to whatever you desire.
define BOBCACHIEVEMENT_SCREEN_NAME = None
define BOBCACHIEVEMENT_NOTIFY_PREFIX = _("Osiągnąłeś:")
define BOBCACHIEVEMENT_SCREEN_TRANSITION = Dissolve(0.5)

# 5) If you use a screen instead, it must take two string params of achievement title and description.
#    This is an example screen that you can use by setting above:
#    define BOBCACHIEVEMENT_SCREEN_NAME = "bobcachievement_samplescreen" 
screen bobcachievement_samplescreen(achievement_title, achievement_description):
    timer 5.0 action Hide("bobcachievement_samplescreen", transition=BOBCACHIEVEMENT_SCREEN_TRANSITION)
    vbox:
        xanchor 1.0 xpos 0.95 yanchor 0.0 ypos 0.05
        style_prefix "bobcachievement"
        text BOBCACHIEVEMENT_NOTIFY_PREFIX text_align 1.0 xalign 1.0
        text achievement_title text_align 1.0 xalign 1.0

style bobcachievement_text:
    color "#000"
    outlines [(5, "#fff", 0, 0)]
    
# 6) That's it! To display achievements to the user, please see directions in sbobcachievements.rpy

#############################################
# YOU SHOULD NOT MODIFY ANYTHING BELOW HERE #
#############################################
python early:
    def parse_bobcachievement(lexer):
        return lexer.rest()
    def bobcachievement_grant(achiname):
        if achiname not in BOBCACHIEVEMENTS_MAP:
            renpy.error("Achievement '" + achiname + "' was not registered. Please modify BOBCACHIEVEMENT_LIST in 0bobcachievements.rpy to add it.")
            return
        if not achievement.has(achiname):
            if BOBCACHIEVEMENT_SCREEN_NAME is not None:
                if BOBCACHIEVEMENT_SCREEN_TRANSITION is not None:
                    renpy.transition(BOBCACHIEVEMENT_SCREEN_TRANSITION)
                renpy.show_screen(BOBCACHIEVEMENT_SCREEN_NAME, BOBCACHIEVEMENTS_MAP[achiname][0], BOBCACHIEVEMENTS_MAP[achiname][1])
            else:
                renpy.notify(__(BOBCACHIEVEMENT_NOTIFY_PREFIX) + " " + __(BOBCACHIEVEMENTS_MAP[achiname][0]))
            achievement.grant(achiname)
            achievement.sync()
    def lint_bobcachievement(achiname):
        if achiname not in BOBCACHIEVEMENTS_MAP:
            renpy.error("Achievement '" + achiname + "' was not registered. Please modify BOBCACHIEVEMENT_LIST in 0bobcachievements.rpy to add it.")
    renpy.register_statement("achieve", parse=parse_bobcachievement, execute=bobcachievement_grant, lint=lint_bobcachievement)
            
init python:
    # Validate that the achievement list is well-formed and form it into a map for ease of access
    # Map is {reference_id:str : (title:str, description:str, is_hidden:boolean)}
    BOBCACHIEVEMENTS_MAP = {}
    if not isinstance(BOBCACHIEVEMENT_LIST, tuple):
        renpy.error("The BOBCACHIEVEMENT_LIST is not a tuple.")
    else:
        for v in BOBCACHIEVEMENT_LIST:
            if not isinstance(v, tuple):
                renpy.error("Found a malformed achievement in BOBCACHIEVEMENT_LIST: " + str(v))
                continue
            if len(v) != 3 and len(v) != 4:
                renpy.error("Achievement " + str(v[0]) + " did not have three or four portions. Each achievement must have a reference_id, title, and description, and an optional hidden status: " + str(v))
                continue
            if not isinstance(v[0], str):
                renpy.error("Achievement " + str(v[0]) + " reference_id was not a string")
                continue
            if not isinstance(v[1], str):
                renpy.error("Achievement " + str(v[0]) + " title was not a string: " + str(v[1]))
                continue
            if not isinstance(v[2], str):
                renpy.error("Achievement " + str(v[0]) + " description was not a string: " + str(v[2]))
                continue
            ishidden = False
            if len(v) == 4:
                if not isinstance(v[3], bool):
                    renpy.error("Achievement " + str(v[0]) + " hidden flag was not True or False: " + str(v[3]))
                    continue
                ishidden = v[3]
            if v[0] in BOBCACHIEVEMENTS_MAP:
                renpy.error("Achievement " + str(v[0]) + " is defined twice in BOBCACHIEVEMENT_LIST. Each achievement must have a unique reference_id.")
                continue
            BOBCACHIEVEMENTS_MAP[v[0]] = (v[1], v[2], ishidden)
            achievement.register(v[0])
    # Store the total number of achievements, for display
    BOBCACHIEVEMENTS_NUMACHIEVEMENTS = len(BOBCACHIEVEMENTS_MAP)
    del BOBCACHIEVEMENT_LIST
