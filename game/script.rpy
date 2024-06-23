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
#Extra here im not sure if bill and kidnapper are the same or not
# K = kidnapper

label start:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    call SceneOne
    with fade
    return
