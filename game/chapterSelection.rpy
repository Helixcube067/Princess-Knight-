label chapterSelection:
    play music "audio/music/Princess Knight Main Theme.mp3" fadein 3.0 if_changed
    image chSelect =  "gui/game_menu.png"
    scene chSelect
    menu:
        "Chapter 1":
            jump SceneOne
            with fade
        "Chapter 2":
            jump SceneTwo
            with fade
        "Chapter 3":
            jump SceneThree
            with fade
        "Chapter 4":
            jump SceneFour
            with fade