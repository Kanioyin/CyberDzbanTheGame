# BobCAchievements Code by Bob Conway 2023
# For use with the Ren'Py engine

# Available with a Creative Commons 0 (CC0) license
# Attribution appreciated; please link bobcgames.com

# Software is provided "as is" without warranty of any kind

############################################
#             USAGE DIRECTIONS             #
############################################

# This file is optional, but provides a way to display a list of gained
# achievements to the player.

# 1) This file requires 0bobcachievements.rpy to work. Please ensure
#    that you have added that file to your game/ directory and customized
#    it as desired before using sbobachievements.rpy.

# 2) Drop this file (sbobcachievements.rpy) into the game/ folder of your Ren'Py project.

# 3) Open screens.rpy in your Ren'Py project and search for "screen navigation():"
#    (without the quotes). Add the following line (without the leading #) below the
#    Preferences button on that screen:
#        textbutton _("Achievements") action ShowMenu("bobcachievements")

#    The code should now look something like this (without the leading #):
#        textbutton _("Preferences") action ShowMenu("preferences")
#        textbutton _("Achievements") action ShowMenu("bobcachievements")
#    (Ensure that the indentation of the new Achievements button matches.)

# That's all you need to do! 
# Now, once you obtain an achievement in your game, you can open the menu
# and click the new "Achievements" button to view your achievements!

# To customize the way the achievements screen looks, you can modify the below
# screen (but this is entirely optional).
# Customizing these variables will also let you change some aspects of the screen:

define BOBCACHIVEMENTS_SPACING = 20
define BOBCACHIVEMENTS_HIDDEN_ACHIEVEMENT_TEXT = _("???")
define BOBCACHIEVEMENTS_SPACING_CHAR = _("-")
define BOBCACHIEVEMENTS_GRANTED_COLOR = gui.text_color
define BOBCACHIEVEMENTS_UNGRANTED_COLOR = gui.insensitive_color

# Additional available achievement-related variables for screen customization:
# - BOBCACHIEVEMENTS_NUMACHIEVEMENTS : integer number of total achievements registered in the framework
# - BOBCACHIEVEMENTS_MAP : map of {reference_id:str : (title:str, description:str, is_hidden:boolean)}
screen bobcachievements():
    tag menu
    default numachievements = len(persistent._achievements)
    use game_menu(_("Wyczyny"), scroll="viewport"):
        style_prefix "about"
        vbox:
            text _("Odblokowałeś [numachievements] / [BOBCACHIEVEMENTS_NUMACHIEVEMENTS] osiągnięć!") size gui.label_text_size
            null height BOBCACHIVEMENTS_SPACING
            for achievement_id in BOBCACHIEVEMENTS_MAP:
                hbox:
                    spacing BOBCACHIVEMENTS_SPACING
                    if achievement.has(achievement_id):
                        # We have the achievement, so show its name and description
                        text BOBCACHIEVEMENTS_MAP[achievement_id][0] color BOBCACHIEVEMENTS_GRANTED_COLOR
                        text BOBCACHIEVEMENTS_SPACING_CHAR color BOBCACHIEVEMENTS_GRANTED_COLOR
                        text BOBCACHIEVEMENTS_MAP[achievement_id][1] color BOBCACHIEVEMENTS_GRANTED_COLOR
                    elif BOBCACHIEVEMENTS_MAP[achievement_id][2]:
                        # The achievement has not been achieved, and it is marked as
                        # hidden, so don't show a description
                        text BOBCACHIVEMENTS_HIDDEN_ACHIEVEMENT_TEXT color BOBCACHIEVEMENTS_UNGRANTED_COLOR
                    else:
                        # The achievement has not been achieved but it is not hidden
                        # so just show its name
                        text BOBCACHIEVEMENTS_MAP[achievement_id][0] color BOBCACHIEVEMENTS_UNGRANTED_COLOR
                        text BOBCACHIEVEMENTS_SPACING_CHAR color BOBCACHIEVEMENTS_UNGRANTED_COLOR
                        text BOBCACHIVEMENTS_HIDDEN_ACHIEVEMENT_TEXT color BOBCACHIEVEMENTS_UNGRANTED_COLOR