image target:
    "hunt/target.png"
    zoom 0.5

transform moving_target:
    ypos 275
    linear 3.0 xpos 2000
    xpos -300
    repeat

# Edit By ShadowyJaw - Removed the unneeded label and added it to the main label.
# Without updating to the newest renpy version, there is not much we can really improve. 
    
label hunting:
    $ shots_fired = 0
    $ targets_hit = 0
    scene black
    show target at moving_target
    $ position = At(ImageReference("target"), moving_target)
    show expression position

    $ ui.imagebutton("hunt/crosshair.png", "hunt/crosshair_focused.png", clicked = ui.returns("fired"), xpos= 996, ypos = 163)
    $ fired_gun = ui.interact()
    
    show expression position
    if position.xpos > 950 and position.xpos < 1100:
        with vpunch
        "You Hit. "
        $ shots_fired = shots_fired + 1
        $ targets_hit = targets_hit + 1
        if shots_fired >= 3:
            return
        call hunting
    
    with vpunch
    "You Missed."
    $ shots_fired = shots_fired + 1
    if shots_fired == 3:
        return   
    return
