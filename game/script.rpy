#Variables
define harperPoints = 0
define musePoints = 0

#Characters
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

label start:
    default menuset = set()
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    call SceneOne from _call_SceneOne
    with fade
    call SceneTwo from _call_SceneTwo
    with fade
    call SceneThree
    with fade
    call SceneFour
    with fade
    return
