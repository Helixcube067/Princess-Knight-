label SceneThree:
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
    "Day one of traveling does nothing except make the both of you tired and achey, and day two is looking to be the same."
    "You're bolstered, though, by the thought of finally getting to see Muse again. You're used to her being by your side constantly. The absence of her has begun to grate on you."
    "Sometimes you'll turn around to tell a joke, only to double take when it's Harper behind you instead of her."
    "Not that you don't appreciate Harper as a friend!{w=0.75} You do.{w=0.75}  You love her enough to fuel a universe. But Muse is part of your life now, and you miss her."
    "Harper groans again as you both get up from your self imposed five minute break."
    show harper frown at right with dissolve
    Harper "Must we go right away? He's obviously not going to kill her."
    show calliope mad at left with dissolve
    Cal "We absolutely must! I got shivers just from watching that creep for five seconds. Imagine how gross Muse feels right now being stuck with him for days on end?"
    "She thinks for a second, then shudders."
    show harper side at right with dissolve
    Harper "Fair point."
    "Suddenly, before either of you can blink, you're surrounded on all sides by men in theater masks. They point swords at you."
    stop music fadeout 3.0
    Mystery "Halt! You're being robbed! Please comply or you'll get hurt!" with sshake
    "All you can think is that maybe you really should've brought along someone with actual fighting prowess."
    "You know how to fight, but that's mostly just what Muse taught you. You're not an expert by any means."
    show calliope neu at left
    show harper frown at right
    Cal "Aw nuts."
    Mystery "Drop all of your belongings, then step away carefully—{w=0.75} Princess Calliope?"
    "A murmur spreads through the crowd of bandits, before the leader rips off his theater mask, exposing—"
    Cal "Bill!"
    play music "audio/music/Princess Knight Main Theme.mp3" fadein 3.0 if_changed
    show bill at center with dissolve
    show calliope happy at bounce, left
    "You're delighted by this turn of events. Bill is one of your many Designated Kidnappers, a role created by necessity during your mother's reign as queen."
    "A Designated Kidnapper is assigned to a princess, who will then kidnap her and make the appropriate threats in appropriate disguises."
    "He is then beat up tastefully to show the strength of the kingdom."
    "It's basically an open secret in the upper class of any kingdom, but nobody normal knows about it."
    "It's all the benefits of an actual kidnapping with none of the drawbacks."
    "Bill is your own Designated Kidnapper, and has been since you were a kid. He's practically your uncle."
    Cal "Bill, what are you doing out here?"
    Bill "What are you doing out here, Calliope? It's dangerous out here, you could get mugged!"
    "Harper snorts."
    Cal "Muse got kidnapped because the kidnapper thought she was me! I'm out here to save her."
    "Bill's eyes go wide and concerned. Everybody has a soft spot for Muse, even the people she performatively beats up to save you from."
    Bill "Oh no, do you know where you need to go?"
    "You point in the general direction you're supposed to be aiming for. Bill hums, thinking."
    Bill "And how far do you need to go?"
    Cal "One more day's travel on foot. We're almost to her!"
    "Bill seems to have come to a decision. He gestures sharply to his band of men, and they disperse in a line down the road."
    Bill "We'll help you. We can't spare much time, but one day is nothing to help you out."
    "You spin him into a hug, before darting off in the direction his men were directed to go."
    stop music fadeout 3.0
    play music "audio/music/Fireside Heart to Heart.mp3" fadein 3.0
    scene forest night with fade
    "Camp that night is much more lively than the last two nights. Instead of being just you and Harper, it's like a big get together with all of your extended family."
    "You see faces you haven't seen in years, and give out more hugs than you have in months."
    "Eventually Bill sits on a log next to you."
    show bill at right with dissolve
    Bill "How you holdin' up, Princess?"
    show calliope happy at left with dissolve
    Cal "As well as you can expect. I'm not really built for travel. I like it, though!"
    Bill "Yeah, I bet you never usually get to wander around like this. Your parents are a teeny bit overbearing. But nature's beautiful, ain't it?"
    "A squirrel falls out of a tree and onto one of the thieves' heads."
    Cal "...{w=0.75}Sure. Yeah. Beautiful."
    Bill "Hey, listen. We'll get her back, y'hear me? And then you'll get to impress her with how quick you were able to find her."
    "He wiggles his eyebrows, a smirk on his face."
    menu:
        "It's not like that!" if musePoints != 1:
            "Yeah, you love Muse, but purely in a friendly way. And you can't just let go of employees as good as her. Bill would know, running a gang of thieves."
            "Bill looks surprised, though he raises his hands in surrender."
            Bill "Well, either way, you're definitely gonna knock her socks off with this rescue. Make sure to do a few little extra flourishes to really impress her."
            "Bill gets up and does a few silly looking moves with a twig he picked up off the ground. You laugh at him, and he bows."
            pass
        "Hopefully…":
            show calliope vhappy at left with dissolve
            "You really do want to impress her. She does so much for you all the time, is so poised and proper, and you honestly just want to sweep her off her feet."
            "Bill pats your shoulder."
            Bill "I figured it was that. Make sure to really show your stuff, Princess. You'll be sure to knock her off her feet and straight into your arms!"
            pass
    "Bill leaves to go to his own sleeping roll."
    hide bill with dissolve
    "Before you can go to sleep, Harper walks up to you and sits down."
    show harper happy at right with dissolve
    "She knocks her shoulder into yours."
    Harper "You holding up?"
    "You don't have to put up a brave face around Harper the way you have to around Bill, so you answer honestly."
    show calliope neu at left
    Cal "Not really. I've been keeping up with acting like everything's fine, but I'm worried for her. She may be a seasoned knight, but she's not the one who's used to being kidnapped."
    Cal "I just want her to be okay."
    Harper "She'll be okay. She's the strongest person in both of our lives, honestly."
    Harper "That guy trying to marry her is going to be in for the shock of his life if he succeeds though."
    "You know exactly what she's talking about. Muse hides behind a perfectly poised guise, but she's able to raise more hell than you do. She just never wants to."
    Cal "Heh. Yeah."
    "Harper sends you a worried glance."
    Harper "You're not gonna stop worrying until she's back with us, are you."
    "It's not phrased as a question. You sigh."
    Cal "Yeah."
    menu:
        "You shake your head.":
            Cal "Muse wouldn't worry like this. She would just get stuff done."
            Harper "Muse is an inhuman automaton who probably can't even feel mortal feelings like pain and stress. Don't try to compare yourself to her."
            "You stare at Harper."
            Cal "That's kind of mean. Inhuman automatons have plenty of feelings."
            Harper "Have you spoken to any?"
            "You go silent. Harper nods, her point seemingly made."
            Cal "Wh— {w=0.75}okay, that's not even relevant, since Muse isn't even an automaton. She's just That Cool."
            Harper "If you say so, but I'm onto her."
            "Harper squints her eyes and makes a quick 'I'm watching you' gesture in the direction you're traveling."
            "Then she sobers, punching your shoulder."
            Harper "But she'll be fine. Try to get some sleep, okay Calliope? You need to be properly rented to be any good tomorrow."
            pass
        "You grab her hand." if musePoints <= 0:
            Cal "You're good to me, Harper."
            show harper blush at right with dissolve
            "She goes red, though you don't know why."
            Harper "I'm just being a good friend. That's all."
            "She averts her eyes."
            "You smile at her. Sometimes she gets a little shy like this, despite your years of friendship. You don't mind." 
            "It's honestly kind of cute, though you'd never admit it upon pain of death."
            "It's not cool or hip to think your best friend from the wet nurse is pretty when she blushes. You're too cool to have repressed feelings."
            "You cheerfully ignore how hard you're repressing your feelings."
            Harper "Anyway, try to get some sleep. You'll be no use tomorrow if you aren't rested."
            "She gets up and leaves."
            hide harper with dissolve
            $ harperPoints += 1
            pass
    jump SceneFour
    stop music fadeout 3.0
    with fade
