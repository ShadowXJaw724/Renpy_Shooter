define e = Character('Eileen', color="#c8ffc8")
define y = Character('You', color="#c8c8ff")
define image bg beached = "images/beached.jpg"
define image Eileen:
    "images/eileen.png"
    zoom 1.3

label start:
    scene bg beached
    show Eileen
    "Micro Scenario for the shooter:"
    e "Hey, can you go try and shoot some people for me?"
    menu:
        "Sure! I will be right back.":
            e "Yay! I'm counting on you."
            call begin_hunt
            call ending_handler
        "No!":
            e "You're so mean. I could never love you."
            "Bad End - No Eileen"
            return

label ending_handler:
    scene bg beached
    show Eileen
    if targets_hit == 0:
        e "You didn't hit anyone, I am going to find someone else who can satisfy me."
        scene black with dissolve
        "And so Eileen left, leaving you to die alone with no one to ever love him."
        "Bad End - Lost Eileen"
    if targets_hit > 0:
        e "[targets_hit] of your shots ended up killing someone! Let's get married! UwU"
        scene black with dissolve
        "And so Eileen and you got married and had a nice family. You died with a fillia to keep you company in your last moments."
        "Good End - Married Eileen"

    return
