label SceneTwo:
    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    play music "audio/music/Princess Knight Main Theme.mp3" fadein 3.0 if_changed
    scene forest day with dissolve
    Cal "We need to find a witch first, obviously."
    show harper side at right with dissolve
    Harper "Why?"
    show calliope determined at left with dissolve
    Cal "To guide our way! Muse told me that she always went to a witch to find where I was being held. It expedites the process a lot. There's a lot of caves princesses can be held in around these parts."
    Harper "I'm so glad I'm not you."
    Cal "It's not all bad! My family and the kidnappers have an arrangement."
    Harper "...An arrangement?"
    show calliope happy at left
    Cal "An arrangement!"
    "You pause before getting back on track."
    Cal "Anyway! A witch. I actually know where one is, though mom says I'm only supposed to visit her in emergency situations. This definitely counts though!"
    Harper "Sure."
    "You cheerfully ignore Harper's doubt."
    "Traveling towards where The Witch was said to be by Muse ends up not taking that long, surprisingly."
    "The Witch lives reasonably close to the castle, presumably since that's where most magical requests come from. You end up stumbling across her cabin more or less by accident."
    "It's a very enchanting cabin. Something about it draws you in, makes you want to stay there forever. You shake your head. You need to rescue your knight! There's no time to get distracted."
    "With resolute steps and Harper timidly hiding behind you, you knock on the door."
    "It opens to a cranky looking woman. She looks surprisingly... normal? You're almost disappointed. You expected a witch to look really cool, though you suppose they're just normal people who know magic."
    "If you were a witch, you'd do something more cool with your appearance. Like turning your hair into snakes that you can feed people to."
    "Her grumpy expression fades when she sees you, getting slightly more friendly."
    show witch neu at center with dissolve
    Witch "Princess Calliope? Lady Harper? Is that you?"
    "You blink."
    show calliope neu at left with dissolve
    Cal "I'm sorry? I don't think I recognize you. Have we met?"
    Witch "No, we haven't. But your knight and I have gotten very acquainted throughout her tenure as your knight. You get kidnapped a surprising amount, young lady."
    Cal "She talks about me?"
    Witch "Complains, more like it."
    "The Witch huffs, though she's smiling."
    Witch "I know more about your antics than I know about that girl, though she's always laughing when she talks about you. I suppose that makes you more likable than most of my customers."
    Witch "Anyway, come in, come in. What do you need?"
    Cal "Muse has been kidnapped!"
    "The Witch's eyes widen. She giggles a bit before you glare at her."
    show calliope mad at left
    Witch "I'm sorry, I didn't mean to laugh, It's just that this is quite the role-swap! You going after her for once instead of her going after you. It's a bit funny."
    "It is a bit funny, but you were waiting to laugh about it until after you had Muse back from Creepy McCreepface. All knowing witch or not, if she didn't take this seriously you were going to leave."
    Cal "Will you help us find her? She got kidnapped because she got mistaken for me! It's practically my duty to get her back."
    Witch "To be fair, I would've thought she was the princess out of the two of you too."
    "You glare at her again."
    Witch "Okay, okay! I'll help you find her. I like her well enough anyway. She always brings offerings of snacks."
    "You hesitate for a moment."
    show calliope neu at left
    Cal "Did we need to bring snacks? I can give you an apple I brought. I don't really know witch etiquette."
    "The Witch gives you a deadpan stare. You don't say anything more."
    Witch "Now watch carefully, since I only feel like doing this once."
    "She sits you all down around a crystal ball, and begins dragging her hands across it in whimsical patterns. After a few minutes of tense silence, the crystal ball's image clears into an image of Muse."
    "She's tied up, though she looks mostly unharmed. She mostly just looks extremely tired of life."
    Muse "I'm not even the princess, sir. You've got the wrong girl."
    Kidnapper "Nonsense! I will not fall for your tricks!"
    Witch "And zooming out a little..."
    "The crystal ball image zooms out until it's a picture of a tower. Very cliche, but so is this kidnapper."
    Witch "There's your location. South of here, around two days of a journey on foot. Just outside of a little farming town. You got that?"
    "You nod, resolute. She waves away the image on the ball."
    Witch "Good. Now scram before my good will starts to tire."
    "You scram."
    jump SceneThree
    with fade