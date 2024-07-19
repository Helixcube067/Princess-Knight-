#Variables
define harperPoints = 0
define musePoints = 0

#region Characters
define Cal = Character("Calliope", color = "#F00771")
define Muse = Character("Muse", color = "#5865D6")
define Harper = Character("Harper", color = "#D6044D")
define Witch = Character("Witch", color = "#6F00B8")
define Darrell = Character("Darrell", color = "#D40000")
define Dragon = Character("Dragon", color = "#D40000")
define Advisor = Character("Advisor", color = "#029020")
define Mystery = Character("Mysterious Man", color = "#010054")
define Bill = Character("Bill", color = "#FF1F00") 
define Kidnapper = Character("Kidnapper", color = "72000E")
#endregion

label start:
    call SceneOne from _call_SceneOne
    label specialThanks:
        scene black
        with fade
        "And thanks all! Thanks for reading everybody!"
        "Here's a link to our lovely artist: {a=https://dorianmack.carrd.co/}Dorian's portfolio{/a}. Please check them out!"
        "Our lovely musician is Luke \“lessashamed\” Williams"
        "And I'm helix I'm the programmer! You can check me out {a=https://helixcube.itch.io}here{/a} "
    return
