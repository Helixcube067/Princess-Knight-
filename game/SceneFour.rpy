label SceneFour:
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
    scene forest day with fade
    "The next day dawns bright and early. You all pack up with minimal complaints, though Harper exudes enough negative energy to make those around her cower away."
    "You're jittery with nervous energy, and would vibrate out of your own clothes if not for the steadying hand Harper keeps on your back."
    "Your group approaches the tower with a confidence that seems unshakable— right up until you see the dragon that's guarding the tower."
    "There's a series of groans. Dragons always end up difficult to deal with, even when you're the one they're working for."
    "The dragon opens one big yellow eye, before jolting up like it was shocked."
    Dragon "Oh, shit— {w=0.75}BEWARE, MORTALS. YOU SHALL NOT PASS UNLESS THE MASTER WISHES IT."
    "Harper cups her hands around her mouth and shouts at him." with sshake
    show harper side at right with dissolve
    Harper "Listen, whatever your name is—"
    Darrell "IT'S DARRELL." with sshake
    show harper frown at right
    "She snickers."
    show harper side at right
    Harper "Okay, Darrell, listen. Is this worth it?{w=0.75} Is this really, truly worth it?{w=0.75} What are you even getting paid?"
    Darrell "THREE SHEEP AND A PIG'S BLOOD."
    "Gasps ring out among the group. That's practically slave labor at this point. That's below minimum wage."
    show calliope mad at left with dissolve
    Cal "Darrell, c'mon! You can do so much better than this guy as an employer! That's not even a living wage. My kingdom pays at least ten cows per day spent curled around a tower!"
    Darrell "FOR REAL?"
    Cal "For real."
    Darrell "AW MAN, THIS WAS MY FIRST GIG. IT SUCKS THAT IT WAS BULLSHIT."
    Darrell "YOU ALL CAN JUST PASS. I KIND OF WANNA EAT THIS GUY NOW."
    "He uncurls from around the tower, stretching with a groan before beginning to stumble away from the building."
    "On his way out, you hand him a business card for your kingdom's dragon distribution business. You can never be too timid with networking, mother always says."
    "With the dragon out of the way, it's child's play to storm inside."
    scene tower with fade
    "The closer you get, the louder Muse's protests get, and the faster you run."
    "Eventually you all stumble across the right room. Muse is tied to a stupid looking steel post, a wedding dress shoved half on top of her."
    show muse neu at center with dissolve
    "It looks like they couldn't manage to make her wear it. You're very proud of the hell she probably raised."
    "She looks up at your entrance, relief and confusion warring in her eyes."
    Muse "Calliope?! What on earth are you doing here?"
    show calliope determined at left with dissolve
    Cal "Saving you, dummy!"
    Kidnapper "Ah, dammit! Your stupid knight got here!"
    show kidnapper frown at right with dissolve
    Muse "I'm the knight, dumbass! That's the princess! I kept telling you that you got this all wrong, but you weren't listening."
    show calliope neu at left
    "The kidnapper begins sputtering and coughing, attempting to deny."
    Kidnapper "No, no! I can't have possibly mixed it up!"
    Muse "Then explain why I was standing alone outside of a meeting room while the Princess was inside. Go on. Explain why I was in a guards position."
    "Muse is talking to him like you would talk to a small child, only with a lot more exasperation and a lot less fondness."
    "She seems to be three seconds away from breaking her ropes with her bare hands and smacking the man."
    "The kidnapper stands there gobsmacked."
    Kidnapper "I… {w=0.75}hadn't thought of that."
    "Muse raises one incredibly judgemental brow."
    Muse "Trust me, I can tell."
    "He draws himself up to his full height, and forges on."
    show kidnapper happy at right
    Kidnapper "Nevertheless, plans can be adjusted!"
    show calliope mad at left
    "He lunges for you. You dodge backwards."
    "Suddenly he's hit with a blast of magic so strong it causes the hair's of your neck to raise."
    hide kidnapper
    "You turn to stare at the culprit— {w=0.75}Harper, who looks at all of you staring with an embarrassed look on her face."
    show harper side at right with dissolve
    Harper "Listen, I know this was going to be a cool fight, but then he lunged at you and I panicked!"
    "You laugh, and Muse joins in after a few seconds."
    menu:
        "With him out of the way, you smile at the both of them." if musePoints <= 0 and harperPoints <= 0:
            show calliope neu at left
            Cal "I can't believe it was that easy."
            "You and Harper hurry over to Muse and begin to untie her. She slumps out of the bindings with a sigh of relief."
            show calliope happy at left
            show muse happy at center
            Muse "Thank you."
            Muse "What were you thinking, though? You could've been hurt! I've been training you, yes, but not full knight's training!"
            Cal "You were taken because of me, of course I had to get you back!"
            Cal "Besides, you save me all the time. I wanted to help you out for once."
            "Muse sighs a fond sigh."
            Muse "You don't have to protect me, it's my job to protect you. I don't mind doing my job, nor do I mind protecting my friend."
            "She looks over at the people gathered behind you, chattering among themselves, and at Harper who's twirling her knife."
            Muse "You did good, though. Maybe we'll make this a thing we do. Me as the decoy and you as the knight."
            show calliope vhappy at left
            "You beam. That sounds wonderful."
        "With him out of the way, you run over to Muse." if musePoints >= 1 and harperPoints <= 0:
            hide harper with dissolve
            Cal "Muse, you're okay!"
            show calliope happy at left
            Muse "Of course I am. He was creepy but mostly harmless. He was very poetic about my hair, though. That was kind of weird."
            show muse determined at center
            "You both shudder."
            Cal "I wish you could've seen my cool fighting moves though. I was kind of hoping I could've shown you when the big rescue happened. I've been practicing with the other knights to surprise you."
            "Muse looks at you in surprise before it melts into a fond smile, and then she kisses your cheek."
            show muse vhappy at center
            "Your brain stops working for a little."
            "Once it reboots, all you can register is that her lips are soft, and you could feel her smile pressed into your cheek."
            Muse "You'll just have to show me later then, huh?"
            Cal "Guess I will."
            show calliope vhappy at left
            "You like the sound of that."
        "You hug Harper in thanks." if harperPoints >= 1 and musePoints <= 0:
            hide muse
            show calliope happy at left
            Cal "Thanks for having my back!"
            "You kiss her cheek. You do this a lot— it's an excuse to be close to her, and you're a very affectionate person anyway."
            show harper blush at right
            "Her cheek goes hot under your touch, and when you go to pull away she screws closed her eyes and pulls you in for a proper kiss"
            "Your eyes widen even as she pulls away and shuts her eyes."
            Harper "Sorry, sorry! Not the time, I know! I'm just riding the adrenaline high."
            "Your lips begin to pull up in a grin."
            show calliope vhappy at left
            Cal "Now's not the time, but later we'll talk, okay?"
            "She nods mutely."
            "You run off to untie Muse with a grin still on your face."
    stop music fadeout 3.0