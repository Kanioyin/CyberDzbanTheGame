# BobCGallery Code by Bob Conway 2023
# Version 1.1 - October 30, 2023 - Updated thumbnail fade to matrixcolor
# Version 1.0 - June 15, 2023 - Initial Release
# For use with the Ren'Py engine

# Available under a Creative Commons 0 (CC0) license
# Attribution appreciated; please link bobcgames.com

# Software is provided "as is" without warranty of any kind

############################################
#             USAGE DIRECTIONS             #
############################################

# 1) Drop this file (0bobcgallery.rpy) into the game/ folder of your Ren'Py project.

# 2) This framework is capable of automatically picking up all image files
#    (jpg, png, webp) under the images/bobcgallery directory. If you do not
#    wish to use this functionality, change this value from True to False.
#    To use this functionality, create a directory named "bobcgallery" under
#    the game/images folder and add images there. For example:
#    game/images/bobcgallery/cg0.png
#    game/images/bobcgallery/cgs/cg1.png
#    Images added in such a manner will have "names" of the filename without
#    the extension. For example cg0.png will be named cg0.
define BOBCGALLERY_AUTOIMPORT = True

# 3) To add additional images to the gallery, you can define them below as
#    tuples of (name, image), and this works with all displayables including
#    layeredimage and manually defined image values. For example, to add
#    the layeredimage "eileencg happy" with the name "eileencg", add a row:
#    ("eileencg", "eileencg happy"),
#    If all CGs are autoimported as above, you do not need to modify this list.
#    Images do NOT have to be the size of the screen (ex: 1920x1080).
define BOBCGALLERY_MANUAL_CGS = (
    (None, None),
    # example single image:
    #("eileen asleep", "images/cg/eileen_asleep.png"),
    # example image defined as "image eileen beach = Composite((1920, 1080), (0,0), "eileen beach body", (0,0), "beach background")"
    #("eileen beach", "eileen beach"),
    # example image defined as "layeredimage eileen coffeetime"
    #("eileen coffee", "eileen coffeetime"),
    )
    
# 4) By default, the framework validates images that are added to the above
#    list of gallery images. The validation *should* be fairly comprehensive,
#    but if it's causing you too much trouble, you can disable it here.
define BOBCGALLERY_VALIDATE_MANUAL_CGS = True

# 5) This gallery supports images that are NOT the size of the screen
#    (ex: 1920x1080), but if they all are, set this to False to improve performance.
define BOBCGALLERY_USE_NON_SCREEN_IMGS = True
    
# 6) By default, any auto-imported CGs will be included after the manually-
#    defined ones in the gallery view. To change this behavior and include
#    them first, change this value from True to False.
define BOBCGALLERY_MANUALFIRST = True

# 7) This screen is the basic gallery view screen. You may customize it as
#    desired, including changing the constants determining how many CGs to
#    show per page or the size of the thumbnails.
define BOBCGALLERY_PER_PAGE = 9
define BOBCGALLERY_THUMB_XMAXIMUM = 384
define BOBCGALLERY_THUMB_YMAXIMUM = 216
define BOBCGALLERY_THUMB_SPACING = 20
define BOBCGALLERY_TRANSITION = Dissolve(0.5)

image bobcgallery_locked_cg = Transform("#aaa", xysize=(BOBCGALLERY_THUMB_XMAXIMUM, BOBCGALLERY_THUMB_YMAXIMUM))

transform bobcgallery_thumb:
    matrixcolor TintMatrix("#666666")
    on hover:
        linear 0.5 matrixcolor TintMatrix("#ffffff")
    on idle:
        linear 0.5 matrixcolor TintMatrix("#666666")

screen bobcgallery():
    tag menu
    default pagenum = 0
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"
        hbox:
            box_wrap True spacing BOBCGALLERY_THUMB_SPACING box_wrap_spacing BOBCGALLERY_THUMB_SPACING
            for name, thm, img in BOBCGALLERY_IMAGE_SETS[pagenum]:
                if name in persistent.bobcgallery_unlocked:
                    imagebutton idle thm at bobcgallery_thumb action Show("bobcgallery_showcg", img=img, transition=BOBCGALLERY_TRANSITION)
                else:
                    add "bobcgallery_locked_cg"
    if BOBCGALLERY_NUM_SETS > 1:
        hbox:
            xcenter 0.5 yalign 1.0 spacing 20
            textbutton _("<") action SetScreenVariable("pagenum", pagenum-1) sensitive pagenum > 0
            for i in range(BOBCGALLERY_NUM_SETS):
                textbutton str(i + 1) action SetScreenVariable("pagenum", i) selected pagenum == i
            textbutton _(">") action SetScreenVariable("pagenum", pagenum+1) sensitive pagenum < (BOBCGALLERY_NUM_SETS-1)
            

# 8) Open screens.rpy in your Ren'Py project and search for "screen navigation():"
#    (without the quotes). Add the following line (without the leading #) below the
#    Preferences button on that screen:
#        textbutton _("Gallery") action ShowMenu("bobcgallery")

#    The code should now look something like this (without the leading #):
#        textbutton _("Preferences") action ShowMenu("preferences")
#        textbutton _("Gallery") action ShowMenu("bobcgallery")
#    (Ensure that the indentation of the new Gallery button matches.)

# 9) If you wish to customize the way that CGs are shown to the user, you
#    can customize this screen, but it is not necessary.
define BOBCGALLERY_CGBG = "#000a"
screen bobcgallery_showcg(img):
    modal True
    zorder 99
    add BOBCGALLERY_CGBG
    add img fit "scale-down" xcenter 0.5 ycenter 0.5
    imagebutton idle "#fff0" action Hide("bobcgallery_showcg", transition=BOBCGALLERY_TRANSITION)
    
# 10) To unlock an image in the gallery without displaying the image, type
#    "galleryunlock <image name>" in your script.
#    For example, to unlock the sample CG eileen asleep, type
#    galleryunlock eileen asleep
#    To unlock an image *and* display it to the user, use "gallery" instead.
#    gallery eileenasleep

#    For example, to unlock eileen asleep and show (and unlock) eileen beach:
#    label my_test_label:
#        "Eileen was asleep, but you woke her up."
#        galleryunlock eileen asleep
#        "Now you go to the beach together!"
#        gallery eileen beach
#        "Now the player has clicked to hide the CG, and the game continues."
    
#############################################
# YOU SHOULD NOT MODIFY ANYTHING BELOW HERE #
#############################################
default persistent.bobcgallery_unlocked = Set()

python early:
    def parse_bobcgallery(lexer):
        return lexer.rest()
    def bobcgallery_unlockonly(imgname):
        if imgname not in BOBCGALLERY_VALID_IMAGES:
            return
        persistent.bobcgallery_unlocked.add(imgname)
    def bobcgallery_unlockshow(imgname):
        if imgname not in BOBCGALLERY_VALID_IMAGES:
            return
        persistent.bobcgallery_unlocked.add(imgname)
        renpy.transition(BOBCGALLERY_TRANSITION)
        renpy.show_screen("bobcgallery_showcg", img=BOBCGALLERY_VALID_IMAGES[imgname])
    def lint_bobcgallery(imgname):
        if imgname not in BOBCGALLERY_VALID_IMAGES:
            renpy.error("Gallery image '" + imgname + "' was not recognized. Please ensure an image with that name was imported or manually added.")
    renpy.register_statement("galleryunlock", parse=parse_bobcgallery, execute=bobcgallery_unlockonly, lint=lint_bobcgallery)
    renpy.register_statement("gallery", parse=parse_bobcgallery, execute=bobcgallery_unlockshow, lint=lint_bobcgallery)

init 999 python:
    def bobcgallery_get_thumb(img):
        if BOBCGALLERY_USE_NON_SCREEN_IMGS:
            timg = Composite((config.screen_width, config.screen_height),(0,0), BOBCGALLERY_CGBG, (0,0), Fixed(Transform(img, fit="scale-down", xcenter=0.5, ycenter=0.5), xysize=(config.screen_width, config.screen_height)))
        else:
            timg = img
        return Transform(timg, xsize=BOBCGALLERY_THUMB_XMAXIMUM, ysize=BOBCGALLERY_THUMB_YMAXIMUM)
    def bobcgallery_append_manuals(allimgs):
        if len(BOBCGALLERY_MANUAL_CGS) <= 0:
            return
        validimages = renpy.list_images()
        for itm in BOBCGALLERY_MANUAL_CGS:
            if not isinstance(itm, tuple):
                renpy.error("BOBCGALLERY_MANUAL_CGS list had a badly-formatted item: " + str(itm))
                return
            if len(itm) != 2:
                renpy.error("BOBCGALLERY_MANUAL_CGS list had an item that was not name and image: " + str(itm))
            if itm == (None, None):
                continue
            if not isinstance(itm[0], str):
                renpy.error("BOBCGALLERY_MANUAL_CGS image name " + str(itm[0]) + " must be a string")
            if not isinstance(itm[1], str):
                renpy.error("BOBCGALLERY_MANUAL_CGS image " + str(itm[1]) + " must be a string")
            if BOBCGALLERY_VALIDATE_MANUAL_CGS:
                if itm[1] not in validimages:
                    if " " in itm[1]:
                        itmsplit = itm[1].split(" ")
                        itmfirst = itmsplit[0]
                        attrs = itmsplit[1:]
                        if itmfirst in validimages:
                            validattrs = renpy.get_ordered_image_attributes(itmfirst)
                            if validattrs is None or len(validattrs) == 0:
                                renpy.error("BOBCGALLERY_MANUAL_CGS image " + itm[1] + " has invalid attributes")
                            else:
                                for a in attrs:
                                    if a not in validattrs:
                                        renpy.error("BOBCGALLERY_MANUAL_CGS image " + itm[1] + " has invalid attribute " + str(a))
                    else:
                        renpy.error("BOBCGALLERY_MANUAL_CGS image " + itm[1] + " was not a valid image")
            allimgs.append((itm[0], bobcgallery_get_thumb(itm[1]), itm[1]))
    def bobcgallery_handle_autoimport(allimgs):
        for path in renpy.list_files():
            if path.startswith("images/bobcgallery/"):
                pathlist = path.split("/")
                imgname = pathlist[-1]
                ridx = imgname.rindex(".")
                if ridx < 0:
                    renpy.error("Gallery image " + path + " did not have a file extension and will be skipped from auto-import")
                    continue
                namepart = imgname[0:ridx]
                suffixpart = imgname[ridx+1:]
                if suffixpart.lower() in ("jpg", "png", "webp"):
                    allimgs.append((namepart, bobcgallery_get_thumb(path), path))
                else:
                    BOBCGALLERY_LINT_ERRORS.add("Gallery image " + path + " was not a recognized extension (jpg, png, webp) and will be skipped from auto-import")
                    continue
    def bobcgallery_lint_badimages():
        if len(BOBCGALLERY_LINT_ERRORS) > 0:
            for err in BOBCGALLERY_LINT_ERRORS:
                print("\n" + err)
    config.lint_hooks.append(bobcgallery_lint_badimages)
    BOBCGALLERY_VALID_IMAGES = {}
    BOBCGALLERY_IMAGE_SETS = []
    BOBCGALLERY_LINT_ERRORS = Set()
    bobcgallery_all_images = []
    if BOBCGALLERY_MANUALFIRST:
        bobcgallery_append_manuals(bobcgallery_all_images)
    if BOBCGALLERY_AUTOIMPORT:
        bobcgallery_handle_autoimport(bobcgallery_all_images)
    if not BOBCGALLERY_MANUALFIRST:
        bobcgallery_append_manuals(bobcgallery_all_images)
    if len(bobcgallery_all_images) <= 0:
        renpy.error("You don't have any gallery images defined. Please add at least one image, via auto-import or in the manual list.")
    for nm, thmb, img in bobcgallery_all_images:
        BOBCGALLERY_VALID_IMAGES[nm] = img
    while len(bobcgallery_all_images) > BOBCGALLERY_PER_PAGE:
        BOBCGALLERY_IMAGE_SETS.append(tuple(bobcgallery_all_images[0:BOBCGALLERY_PER_PAGE]))
        bobcgallery_all_images = bobcgallery_all_images[BOBCGALLERY_PER_PAGE:]
    BOBCGALLERY_IMAGE_SETS.append(tuple(bobcgallery_all_images))
    del bobcgallery_all_images
    del BOBCGALLERY_MANUAL_CGS
    BOBCGALLERY_NUM_SETS = len(BOBCGALLERY_IMAGE_SETS)
