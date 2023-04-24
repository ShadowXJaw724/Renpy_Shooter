define e = Character('Eileen', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
image bg beached = "images/beached.jpg"
image Eileen:
    "images/eileen.png"
    zoom 1.3

label start:
    
    scene bg beached
    show Eileen 
    # Expanded Interaction from ShadowyJaw

    e "Hey, [m], can you try and shoot some people for me please?"
    menu:
        "No":
            e "Then I guess I'll do it myself"
            call End

        "Sure!":
            e "Great! Here is the gun!"
            call hunting 

    if targets_hit <= 0:
        call MissedAllShots
    elif shots_fired <= 0:
        call DidNotFire:
    elif targets_hit == 1:
        call ShotOneHuman:
    elif targets_hit == 2:
        call ShotTwoHuman:
    elif targets_hit == 3:
        call MassMurder
    else:
        call NeutralEnd
    
    if targets_hit == 0:
        e "You didn't hit anyone, I am going to find someone else."
        scene black with dissolve
        "and the hero died alone with no-one to love him."
    if targets_hit > 0:
        e "[targets_hit] of your shots ended up killing someone.  Lets get married"
        scene black with dissolve
        "and they lived happily ever after"
    

    "game over"

    return

label MissedAllShots:
    scene bg beached
    show Eileen 
    e "You are such a horrible shot! I hate you!"
    scene black 
    "You miss all your shots but still get arrested for illegal gun usage."
    return

label DidNotFire:
    "You didn't fire any bullets..."
    return

label ShotOneHuman:
    scene bg beached
    show Eileen 
    e "Not bad, but you didn't really shoot anyone. One person doesn't count honestly."
    scene black
    "You get arrested for first degree murder."

label ShotTwoHuman:
    scene bg beached
    show Eileen 
    e "Nice, you shot some people! Let's go and date."
    scene black
    "You get arrested for two first degree murder."

label MassMurder:
    scene bg beached
    show Eileen 
    e "I love you! Let's get married and have a family!"
    scene black 
    "You in fact did not get to go and marry."
    "You were sentenced for 20 years and the prisoners threw you over the cliff."
    "You died but not before you spent 2 weeks in the hospital fighting for your life."
    "The families of the man you murdered spit on you both in the hospital and on your grave."
    "Also [e] killer herself. boo hoo."
    "The End."    

label NeutralEnd:
    scene black with dissolve_scene_full
    "I dunno, you just don't get this at all."

label End:
    scene black with dissolve_scene_full
    "You did not shoot any people."
    "[e] got charged with mass murder though."
    "Congratulations for not murdering anyone."

