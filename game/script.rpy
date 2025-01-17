# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc= Character("MC")
image mc = Placeholder("boy")
define James = Character("James")
image James = Placeholder("boy")
define punch=False
# The game starts here.

label start:

    "Disclaimer: This story contains references to Homophobia, Depression, and Abuse"
    show disclaimer at truecenter with dissolve
    " "
    hide disclaimer with dissolve
    scene bg_outside_school

    show mc at left with moveinleft
    "It was a day like any other"
    "Go to school, go to class, and survive"
    mc "Ah finally."
    mc "School."
    mc "{i}I really dont like this school{/i}"
    mc"{i}especially with the blatent homophobia I experience daily{/i}"
    mc"{i}i hate that im forced to go here until another school accepts my application{/i}"
    hide mc

    scene bg_school_hallway
    show mc at left with moveinleft
    show James at right with moveinright
    James "Hello, mc"
    mc "Hello, James"
    mc "What do you want"
    James "well i wanted to ask if you have found a therapist yet"
    mc "For what?"
    James "for your homosexuality."
    mc ":("
    James "Isnt homosexuality a mental disorder?"
    mc "It hasnt been since 1973 though :("
    James "Well anyway"
    James "Fuck you, you boykisser"
    menu
        "punch him???"

        "Punch him":
            $ punch=True
            "you punch him in the face"
        
        "dont punch him":
            "you dont punch him"
    label after_menu:

        "ugh"
return