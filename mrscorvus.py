print("Mrs. Corvus - By Ian B.")
print()
player_name = input("Enter your name, traveler: ")
print()
print("You awaken abruptly in a cozy bedroom, disoriented and uncertain of your surroundings. The room is adorned with rustic charm, featuring wooden beams overhead and walls adorned with paintings of serene natural landscapes. Sunlight streams through lace curtains, casting a warm and inviting glow. You're nestled in a comfortable bed, the sheets soft and inviting, and the scent of fresh pine wafts through the air. As you sit up, the creaking of the wooden floor underfoot echoes through the room. Everything seems oddly familiar and yet utterly foreign. You can't recall how you came to be in this bedroom, but the mystery is undeniable. Your heart races, and a sense of curiosity mixed with trepidation fills your thoughts. However, something catches your eye, filling you with an inexplicable sense of unease. On the wooden door frame, your name, "+ player_name + ", is engraved. It's an eerie sight, leaving you with more questions than answers. You can't recall how you came to be in this bedroom, but the mystery is undeniable. Where exactly are you, and how did you end up in this quaint and enigmatic bedroom?")
print()
print("You decided to stay in the bedroom and investigate for clues. Carefully, you swing your legs over the side of the bed, your bare feet meeting the polished wooden floor. The room seems to hold secrets in its every nook and cranny. You begin by examining the antique dresser adorned with a collection of porcelain figurines, each one delicately crafted. The mirror on the dresser reflects your puzzled expression as you search for any signs of how you came to be here. Feeling a growing sense of curiosity, you know there's much more to uncover, and you contemplate your next move.")
print()
print("1. Search the drawers.")
print("2. Look under the bed.")
print("3. Investigate the open closet")
print()

choice7 = "1"
choice6 = choice7

choice1 = input("> ")
if choice1 == "1":
    print("You decide to search the drawers. With cautious curiosity, you approach the antique dresser adorned with porcelain figurines. Carefully, you begin to open each drawer one by one, hoping to find some clues about your current situation. The soft creaking of the aged wood accompanies your search, and you discover a collection of items, each holding its own small mystery. As you delve into the second drawer, your fingers brush against something cold and metallic. To your surprise, you find an old, ornate key nestled among the jewelry. It's an intriguing discovery that could unlock more secrets, but at the same time, you hear faint footsteps approaching from outside the room, growing louder with each passing second.")
    print()
    print("1. Stop searching and hide the key, hoping to avoid any suspicion.")
    print("2. Keep searching as you desperately seek more information.")
    print()
    choice2 = input( "> ")
    if choice2 == "1":
        print("You choose to stop searching, realizing that the footsteps are drawing nearer, and it's best to avoid any suspicion. You quietly close the drawer and stand by the dresser just as Mrs. Corvus walks into the room, her ebony feathers rustling with a curious demeanor. She notices you are awake and standing by her dresser, and a hint of suspicion flickers in her piercing eyes. With a measured tone, Mrs. Corvus inquires, 'Have you been digging through my things?' The air grows tense as she watches you closely, suspicion etched on her face. You're caught in a moment of uncertainty, unsure whether to tell the truth or craft a lie. The weight of your decision hangs heavily in the room as Mrs. Corvus awaits your response.")
        print()
        print("1. Tell a lie.")
        print("2. Tell the truth.")
        print()
        choice3 = input( "> ")
        if choice3 == "1":
            print("You choose to craft a lie, but as you weave your deception, it becomes painfully clear that Mrs. Corvus can see through your dishonesty. Her eyes fill with disappointment, and without a word, she reaches out, her sharp claws gripping your tongue, causing excruciating pain and a gushing of blood. Your life fades away due to blood loss, a tragic consequence of your failed attempt to deceive the enigmatic Mrs. Corvus.")
            print("Ending #5 - The Deceptive Tongue")
        elif choice3 == "2":
            print("You choose to tell the truth, deciding that honesty is the best course of action. As you explain your actions to Mrs. Corvus, she listens attentively, her piercing eyes fixed on you. After your confession, she shows appreciation for your honesty, though it's tempered with a hint of sternness. 'I value your truthfulness,' she says, 'but remember that certain actions come with consequences.' Following this conversation, Mrs. Corvus informs you that, due to your recent behavior, you are undeserving of breakfast. With a solemn nod, she leaves the room, finding yourself alone in the room, contemplating your next move and what lies ahead in this enigmatic cabin.")
            print()
            print("1. Explore the house.")
            print("2. Plan to murder Mrs. Corvus.")
            print("3. Go back to bed and sleep.")
            print()
            choice4 = input("> ")
            if choice4 == "1":
                print("You decide to explore the house by sneaking downstairs, taking care not to alert Mrs. Corvus while she's busy making breakfast. As you venture further, you stumble upon a locked door. To your surprise, the key you hold fits the keyhole perfectly, and you can unlock it. You're uncertain whether to open the door and investigate what's inside or retreat back upstairs to your room.")
                print()
                print("1. Return to your room.")
                print("2. Investigate further.")
                print()
                choice5 = input("> ")
                if choice5 == "2":
                    print("You open the door to the basement as quietly as possible, not wanting to alert Mrs. Corvus to your exploration. The basement reveals itself as a dim, dusty space filled with old boxes and shelves. It appears to be a place long forgotten and untouched by the passage of time. As you survey the basement, you can't shake the feeling that there may not be much to find in this forgotten storage area.")
                    print()
                    print("1. Return to your room.")
                    print("2. Continue your search in the basement.")
                    print()
                    choice6 = input("> ")
                if choice5 == "1" or choice6 == choice7:
                    print("You decide to return to your room, concluding that there's likely nothing of interest in the basement. As you quietly retreat from the basement, your footsteps carry you back up the stairs. However, when you emerge from the basement, you suddenly find Mrs. Corvus standing there, seemingly appearing out of nowhere. She gazes at you with an inquisitive look and asks why you're out of your room. The unexpected encounter with Mrs. Corvus leaves you feeling vulnerable and uncertain about how to explain your presence outside of your room.")
                    print()
                    print("1. Fabricate a lie.")
                    print("2. Don't say anything.")
                    print()
                    choice8 = input("> ")
                    if choice8 == "1":
                        print("You opt to fabricate a lie, quickly explaining to Mrs. Corvus that you were just looking for the bathroom. However, despite your efforts to deceive her, Mrs. Corvus senses the dishonesty in your words. Her anger flares, and she swiftly takes action. With a calculated and sinister intent, Mrs. Corvus ends your life, her motive veering toward preparing you as her next meal. Your failed attempt at deception leads to a grim and unsettling ending within the enigmatic cabin.")
                        print("Ending #13 - On the Menu")
                    elif choice8 == "2":
                        print("You choose to remain silent, and Mrs. Corvus, upon noticing your silence, assumes that you might be shy or hesitant. She sighs, seemingly understanding your disposition, and then guides you back to your room. In a gentle tone, she advises you to stay in your room for the time being so as not to disrupt her activities. With her instructions, you find yourself back in your room, contemplating the mysterious Mrs. Corvus and her peculiar ways. In the quiet of the room, you hear a soft rustling and see movement in the corner. To your surprise, a humanoid figure emerges from the shadows. It's a humanoid frog, and they introduce themselves as Anura. They explain that they've been held captive and are desperately trying to find a way to escape, revealing that they were the shadowy figure hiding in the closet. After the surprising encounter with Anura, who expresses a strong desire to escape, you find yourself at a crossroads. Anura's plea for help seems genuine, but you must decide whether or not to trust this enigmatic character, who now stands before you.")
                        print()
                        print("1. Trust Anura.")
                        print("2. Don't trust Anura.")
                        print()
                        choice9 = input ("> ")
                        if choice9 == "1":
                            print("You decide to trust Anura, introducing yourself as " + player_name + " feeling that their plea for help is sincere. Anura, stands before you, relieved by your decision to extend your trust. They explain that they've been held captive within Mrs. Corvus's mysterious cabin and have been searching for a way to escape. Anura shares a crucial detail of the escape plan: you can only leave at midnight when Mrs. Corvus is sound asleep. Anura explains that this is the safest time to slip away without arousing her suspicion. As you both prepare for the escape, the weight of the situation hangs heavy in the room. Anura is resolute in their determination to find freedom in the woods, and you can't help but feel a mix of hope and trepidation about the journey that awaits you both. The midnight hour approaches, and you stand on the precipice of a daring escape from the enigmatic cabin.")
                            print()
                            print("1. Leave the cabin and escape to the forest with Anura.")
                            print("2. Stay at Mrs. Corvus's cabin.")
                            print()
                            choice14 = input ("> ")
                            if choice14 == "1":
                                print("You decide to leave the cabin and escape to the forest with Anura, your hearts filled with a mix of hope and trepidation. As you venture deeper into the woods, the darkness obscures your path, and you both quickly become disoriented. Panic sets in as you realize you're hopelessly lost. In the ominous silence of the forest, a shadowy figure emerges. It's a man, wielding an ax. He descends upon you and Anura, with cruel intentions. The axe falls, and Anura is struck down with brutal force, their life abruptly extinguished. You're left paralyzed with fear and grief, unable to comprehend the identity of this shadowy assailant. The man now turns his attention to you, and as terror courses through your veins, you're poised on the brink of the same dark fate, haunted by the enigma of this mysterious woodsman.")
                                print("Ending #10 - The Failed Escape")
                            elif choice14 == "2":
                                print("You choose to stay at Mrs. Corvus' cabin, explaining to Anura that you're concerned about the safety of the woods. Anura, understanding your worries, nods and decides to brave the forest alone. Hours pass, and as the midnight hour approaches, Anura returns, running back to the cabin, screaming and crying for help. She describes being chased by a menacing hawk. The commotion alarms Mrs. Corvus, who rushes downstairs with a shotgun in hand. As the intruder breaks down the front door, Mrs. Corvus takes aim and fires, hitting him and ending the threat. Mrs. Corvus sighs in relief and is genuinely happy to see that you and Anura are both safe. This unexpected turn of events reveals a different side of Mrs. Corvus, showing that she might not be as malevolent as initially thought. In the midst of this tense encounter, you come to realize that staying with Mrs. Corvus might be the best choice for your safety and well-being. The mysteries of the cabin and its occupants still shroud much in uncertainty, but for now, you find some semblance of comfort in the presence of your enigmatic host.")
                                print("Ending #11 - Forever in Mrs. Corvus's Care")
                        elif choice9 == "2":
                            print("You decide not to trust Anura, maintaining caution and skepticism about their true intentions. Anura, understanding your hesitation, attempts to gain your trust by grabbing hold of your arm. In a shocking turn of events, it becomes evident that Anura's touch is poisonous. The venom courses through your veins swiftly, and you pass out from the excruciating pain. Anura, in shock and fear of what they've unintentionally done, cries out in despair as you succumb to the deadly effects of the poison.")
                            print("Ending #9 - Accidental Venom")
                elif choice6 == "2":
                    print("You opt to continue your search in the basement, driven by the desire to uncover any hidden secrets that may be concealed within the dusty confines. As you begin to sift through the old boxes, one in particular piques your curiosity. However, as you attempt to lift it, you realize it's much heavier than expected. In a tragic turn of events, your attempt to handle the heavy box inadvertently causes the shelves of boxes to topple over. The weight of the falling boxes crushes you, and you meet an untimely demise beneath the weight of the hidden mysteries of the basement.")
                    print("Ending #12 - Crushed by Curiosity")
            elif choice4 == "2":
                print("You decide to make a plan, driven by a deep sense of fear and uncertainty about what Mrs. Corvus might do next. In this disturbing moment, you begin to devise a sinister scheme within the confines of the room, your thoughts consumed by the idea of harming Mrs. Corvus. Your emotions are a turbulent mix of anger and fear, but you know that you must carefully craft a plan if you're to carry it out successfully.")
                print()
                print("1. Attempt to poison Mrs. Corvus during a meal.")
                print("2. Seek out a weapon within the cabin.")
                print()
                choice10 = input("> ")
                if choice10 == "1":
                    print("You decide to attempt to poison Mrs. Corvus during a meal, but as you search the room you're in, you can't find any suitable substances for your sinister plan. Frustration and desperation mount and you ultimately abandon the poisoning idea. Instead, you opt to seek out a weapon to address your fear and uncertainty in a different way.")
                    print()
                if choice10 == "2" or choice10 == "1":
                    print("You ultimately decide to seek out a weapon, your fear of Mrs. Corvus propelling you into action. With cautious steps, you sneak out of your room and find yourself in the upstairs hallway. The dim light casts eerie shadows on the walls, and you must make a quick decision about where to go next. To your left, you notice a room shrouded in darkness. To your right, another door beckons, offering a mysterious path. With your heart pounding, you are unsure which room could contain a weapon.")
                    print()
                    print("1. Investigate the room to your left.")
                    print("2. Investigate the room to your right.")
                    print()
                    choice11 = input("> ")
                    if choice11 == "1":
                        print("You decide to investigate the room to your left, curiosity and fear driving you forward. As you slowly open the door and step inside, you find yourself in what appears to be another bedroom, most likely a guest room. The room is dimly lit, with heavy curtains drawn, and the air feels stagnant. In this guest bedroom, your eyes fall upon a small nightstand, and on it, you discover a weapon—an old, ornate dagger. It's a chilling find, and the weight of your earlier plan bears down on you. With the weapon now in your possession, you are hesitant of whether or not you should continue with your plan.")
                        print()
                        print("1. Run back to your room.")
                        print("2. Execute your sinister plan.")
                        print()
                        choice12 = input("> ")
                        if choice12 == "1":
                            print("You choose to have a change of heart and run back to your room, abandoning your dark intentions. As you rush back up the stairs, a sense of remorse gnaws at you. You close the door to your room, wrestling with the consequences of your sinister plan. In the quiet of the room, you hear a soft rustling and see movement in the corner. To your surprise, a humanoid figure emerges from the shadows. It's a humanoid frog, and they introduce themselves as Anura. They explain that they've been held captive and are desperately trying to find a way to escape, revealing that they were the shadowy figure hiding in the closet. After the surprising encounter with Anura, who expresses a strong desire to escape, you find yourself at a crossroads. Anura's plea for help seems genuine, but you must decide whether or not to trust this enigmatic character.")
                            print()
                            print("1. Trust Anura.")
                            print("2. Don't trust Anura.")
                            print()
                            choice13 = input ("> ")
                            if choice13 == "1":
                                print("You decide to trust Anura, introducing yourself as " + player_name + " feeling that their plea for help is sincere. Anura, stands before you, relieved by your decision to extend your trust. They explain that they've been held captive within Mrs. Corvus's mysterious cabin and have been searching for a way to escape. Anura shares a crucial detail of the escape plan: you can only leave at midnight when Mrs. Corvus is sound asleep. Anura explains that this is the safest time to slip away without arousing her suspicion. As you both prepare for the escape, the weight of the situation hangs heavy in the room. Anura is resolute in their determination to find freedom in the woods, and you can't help but feel a mix of hope and trepidation about the journey that awaits you both. The midnight hour approaches, and you stand on the precipice of a daring escape from the enigmatic cabin.")
                                print()
                                print("1. Leave the cabin and escape to the forest with Anura.")
                                print("2. Stay at Mrs. Corvus's cabin.")
                                print()
                                choice14 = input ("> ")
                                if choice14 == "1":
                                    print("You decide to leave the cabin and escape to the forest with Anura, your hearts filled with a mix of hope and trepidation. As you venture deeper into the woods, the darkness obscures your path, and you both quickly become disoriented. Panic sets in as you realize you're hopelessly lost. In the ominous silence of the forest, a shadowy figure emerges. It's a man, wielding an ax. He descends upon you and Anura, with cruel intentions. The axe falls, and Anura is struck down with brutal force, their life abruptly extinguished. You're left paralyzed with fear and grief, unable to comprehend the identity of this shadowy assailant. The man now turns his attention to you, and as terror courses through your veins, you're poised on the brink of the same dark fate, haunted by the enigma of this mysterious woodsman.")
                                    print("Ending #10 - The Failed Escape")
                                elif choice14 == "2":
                                    print("You choose to stay at Mrs. Corvus' cabin, explaining to Anura that you're concerned about the safety of the woods. Anura, understanding your worries, nods and decides to brave the forest alone. Hours pass, and as the midnight hour approaches, Anura returns, running back to the cabin, screaming and crying for help. She describes being chased by a menacing hawk. The commotion alarms Mrs. Corvus, who rushes downstairs with a shotgun in hand. As the intruder breaks down the front door, Mrs. Corvus takes aim and fires, hitting him and ending the threat. Mrs. Corvus sighs in relief and is genuinely happy to see that you and Anura are both safe. This unexpected turn of events reveals a different side of Mrs. Corvus, showing that she might not be as malevolent as initially thought. In the midst of this tense encounter, you come to realize that staying with Mrs. Corvus might be the best choice for your safety and well-being. The mysteries of the cabin and its occupants still shroud much in uncertainty, but for now, you find some semblance of comfort in the presence of your enigmatic host.")
                                    print("Ending #11 - Forever in Mrs. Corvus's Care")
                            elif choice13 == "2":
                                print("You decide not to trust Anura, maintaining caution and skepticism about their true intentions. Anura, understanding your hesitation, attempts to gain your trust by grabbing hold of your arm. In a shocking turn of events, it becomes evident that Anura's touch is poisonous. The venom courses through your veins swiftly, and you pass out from the excruciating pain. Anura, in shock and fear of what they've unintentionally done, cries out in despair as you succumb to the deadly effects of the poison.")
                                print("Ending #9 - Accidental Venom")
                        elif choice12 == "2":
                            print("You choose the dark path of executing your sinister plan. With the dagger you found in hand, you make your way downstairs, the weight of your actions heavy on your conscience. As you reach the lower level of the cabin, you find Mrs. Corvus in the kitchen, her back turned as she tends to her cooking. Seizing the opportunity, you stealthily approach, your heart pounding with a mix of fear and determination. With a swift, calculated strike, you use the weapon to take Mrs. Corvus by surprise. Her life quickly slips away, her body crumpling to the floor. Your actions have led to a shocking and irreversible outcome, forever altering the course of your journey within the enigmatic cabin. Filled with a mix of fear and desperation, you make a hasty retreat from the cabin and into the surrounding woods, hoping to find freedom and evade any consequences that may be lurking in the shadows.")
                            print("Ending #8 - The Murderous Escape")
                    elif choice11 == "2":
                        print("You decide to explore the room to your right, a glimmer of hope for a potential weapon. However, as you attempt to open the door, you discover it's locked, resisting your efforts to force it open. Frustration mounts as you struggle with the stubborn door, the sound of your attempts echoing through the upstairs hallway. Mrs. Corvus, alerted by the commotion, suddenly appears, her anger evident in her eyes. In a fit of fury at your attempt to open a door without her permission, she swiftly picks you up and hurls you down the stairs. Helpless, you tumble down, the fall causing your untimely demise. Your ill-fated decision to trespass within her cabin has led to a tragic end.")
                        print("Ending #7 - The Uninvited Consequence")
            elif choice4 == "3":
                print("You decide to go back to bed and sleep, hoping to clear your mind and make sense of the bewildering situation. The moment your head hits the pillow, you fall into a deep slumber, oblivious to the passing time. When you awaken, it's no longer the soft morning light that greets you. Instead, it's evening, and the room is cast in shadows. The ticking of a nearby clock adds to the eerie atmosphere. Your heart quickens as you hear the sound of a window breaking, and a shadowy figure enters your room. You're unable to make out their identity, but their intent becomes horrifyingly clear as they raise an ax above your head, poised to strike.")
                print("Ending #6 - The Silent Strike")
    if choice2 == "2":
        print("You choose to keep searching, despite the growing sound of footsteps approaching. As you continue to sift through the drawer, your heart races with a mixture of anxiety and curiosity. However, your quest for answers is abruptly interrupted when the bedroom door swings open, and Mrs. Corvus strides in, her feathers rustling with an unmistakable anger. With a furious screech, Mrs. Corvus confronts you, her patience worn thin as she accuses you of invading her privacy and rifling through her personal belongings. In a fit of rage, she grabs you and forcefully bashes your head into the dresser, causing the room to spin and your vision to fade into darkness. Your recklessness has led to a painful and abrupt end to your quest for answers in Mrs. Corvus's cabin.")
        print("Ending #4 - Unwanted Intrusion")
if choice1 == "2":
    print("You decide to look under the bed, and as you search, you notice a small slip of paper tucked away in the dusty shadows. Upon retrieving it, you discover the number '2098' scrawled on the paper. Its significance remains a mystery, leaving you to ponder its meaning as you continue your exploration of the room.")
    print()
if choice1 == "3" or choice1 == "2":
    print("You decide to investigate the open closet. However, before you can take another step closer, your gaze is drawn to a pair of gleaming eyes and a shadowy figure within the closet. Panic surges through you as you lock eyes with this enigmatic presence, its intent unclear, and your mind racing with questions. Just as you're about to take a closer look, the closet door suddenly closes with an eerie creak. Your heart races, and you're left in the dimly lit room, bathed in an unsettling silence. Moments later, the bedroom door swings open, and Mrs. Corvus enters, her ebony feathers rustling with an air of calm authority. She greets you warmly, her eyes filled with a mixture of curiosity and wisdom, and says, 'Ah, you've finally woken up " + player_name + "! Welcome to my humble abode!' You're scared and unsure of what to do or say, your thoughts a chaotic whirlwind of fear and curiosity.")
    print()
    print("1. Respond rudely & insult her.")
    print("2. Express gratitude for her hospitality.")
    print("3. Attempt to escape by leaping out of the window.")
    print()
    choice15 = input ("> ")
    if choice15 == "1":
        print("You choose to respond rudely and insult Mrs. Corvus. Your disrespectful words cut through the warm atmosphere like a chilling wind, and you can see the hurt in her eyes quickly turning to anger. With an agitated screech, she extends her ebony wings and unsheathes her razor-sharp claws. In a swift and deadly motion, Mrs. Corvus slashes at your neck, her claws leaving a gruesome trail of blood. Your vision blurs, and the room spins as you collapse to the floor. Gasping for breath, you realize your grave mistake, but it's too late. Mrs. Corvus's lethal strike has sealed your fate, and darkness swiftly claims you.")
        print("Ending #1 - The Fatal Insult")
    elif choice15 == "2":
        print("You decide to express gratitude for her hospitality. While you're still uneasy and confused about your surroundings, you realize that being polite might be your best course of action. You thank Mrs. Corvus for her warm welcome, your words carrying a sincere tone. Mrs. Corvus smiles, her eyes softening as she acknowledges your gratitude. 'You're most welcome,' she says with a touch of kindness. 'I sensed you needed shelter, and my home is always open to those in need. You're safe here.' As she says this, she adds, 'Would you like to join me for breakfast?'")
        print()
        print("1. Politely refuse her offer to have breakfast.")
        print("2. Eat breakfast with Mrs. Corvus.")
        print()
        choice16 = input ("> ")
        if choice16 == "1":
            print("Mrs. Corvus smiles warmly and understandingly, realizing that you're not hungry at the moment. She leaves the room and gently closes the door behind her, leaving you in solitude.")
            print()
            print("You decide to go back to bed and sleep, hoping to clear your mind and make sense of the bewildering situation. The moment your head hits the pillow, you fall into a deep slumber, oblivious to the passing time. When you awaken, it's no longer the soft morning light that greets you. Instead, it's evening, and the room is cast in shadows. The ticking of a nearby clock adds to the eerie atmosphere. Your heart quickens as you hear the sound of a window breaking, and a shadowy figure enters your room. You're unable to make out their identity, but their intent becomes horrifyingly clear as they raise an ax above your head, poised to strike.")
            print("Ending #6 - The Silent Strike")
        elif choice16 == "2":
            print("As you sit down to eat breakfast with Mrs. Corvus, she serves a steaming bowl of worm and snail soup. The pungent aroma wafts from the bowl, and the sight and smell of the dish make your stomach churn. It's clear that this is a rather unconventional breakfast choice, and you find it challenging to muster the courage to consume it. Despite the unappetizing appearance and odor, you realize that it would be disrespectful to refuse the meal.")
            print()
            print("1. Throw the soup at her.")
            print("2. Politely decline the meal.")
            print("3. Force yourself to eat it.")
            print()
            choice17 = input ("> ")
            if choice17 == "1":
                print("You choose to throw the soup at Mrs. Corvus, an act of blatant disrespect. Her reaction is swift and furious, and in her anger, she grabs a nearby pot and bashes your head in, leading to a gruesome and untimely end.")
                print("Ending #14 - A Disastrous Display of Disrespect")
            elif choice17 == "2":
                print("You choose to politely decline the meal, expressing your aversion to the unappetizing worm and snail soup. Mrs. Corvus, seemingly understanding your reluctance, nods and proceeds to help herself to the remaining food you haven't touched. After breakfast, Mrs. Corvus extends an invitation to watch TV with her to pass the time. ")
                print()
                print("1. Go back to bed and sleep.")
                print("2. Join Mrs. Corvus to watch TV.")
                print()
                choice18 = input("> ")
                if choice18 == "1":
                    print("You decide to go back to bed and sleep, hoping to clear your mind and make sense of the bewildering situation. The moment your head hits the pillow, you fall into a deep slumber, oblivious to the passing time. When you awaken, it's no longer the soft morning light that greets you. Instead, it's evening, and the room is cast in shadows. The ticking of a nearby clock adds to the eerie atmosphere. Your heart quickens as you hear the sound of a window breaking, and a shadowy figure enters your room. You're unable to make out their identity, but their intent becomes horrifyingly clear as they raise an ax above your head, poised to strike.")
                    print("Ending #6 - The Silent Strike")
                elif choice18 == "2":
                    print("You decide to join Mrs. Corvus in the living room. The cozy living space is adorned with rustic wooden furniture, and you settle onto a plush, burgundy couch. The room has a homey feel, with a warm fireplace crackling in one corner and a few antique decorations adorning the walls. Mrs. Corvus hands you the remote control and kindly asks you to choose a channel. She mentions that there are 30 channels available for you to select from, leaving you with the decision to pick a channel of your choice.")
                    print()
                    choice19 = int(input("> "))
                    if choice19 > 30:
                        print("This T.V Channel does not exist.")
                        print("Invalid input. Your journey ends.")
                    if choice19 < 0:
                        print("This T.V Channel does not exist.")
                        print("Invalid input. Your journey ends.")
                    elif choice19 >= 20 and choice19 <= 30:
                        print("You decide to pick the channel " + str(choice19) + " and a sad drama show begins to play, depicting the heart-wrenching story of a husband and wife. Mrs. Corvus, watching the show, breaks down into tears, clearly moved by the emotional scenes.")
                        print()
                        print("1. Comfort Mrs. Corvus.")
                        print("2. Ignore her.")
                        print()
                        choice22 = input("> ")
                        if choice22 == "1":
                            print("You choose to comfort Mrs. Corvus, but your attempt to console her only worsens her state of mind. She becomes increasingly upset and agitated, expressing a strong desire to be left alone in her moment of grief. In a fit of sadness and anger, Mrs. Corvus takes a shocking and violent action, clawing your eyes out, leading to your gruesome and untimely demise.")
                            print("Ending #19 - A Tragic Misunderstanding")
                        elif choice22 == "2":
                            print("You choose to ignore her, allowing Mrs. Corvus some space to regain her composure. Over time, she manages to calm herself down and appreciates your consideration in giving her that time. Once she's in a more composed state, Mrs. Corvus begins to open up to you. She shares how the show reminded her of her late husband, Mr. Corvus, and reveals that he met a tragic end at the hands of a man named Mr. Bueto. She expresses her fear that Mr. Bueto may return to bring harm once more.")
                            print()
                            print("1. Promise to protect Mrs. Corvus.")
                            print("2. Stay silent and withhold any commitment.")
                            print()
                            choice23 = input("> ")
                            if choice23 == "1":
                                print("You decide to promise to protect Mrs. Corvus, and she's deeply grateful for your willingness to safeguard her. In an act of trust and bonding, she takes you to her room and shows you the shotgun she possesses, explaining how to use it. With the growing trust between you two, she feels secure with you by her side. As night falls and the two of you retire to your rooms, a sudden intrusion shatters the silence. An unidentifiable man breaks in, and your recognition of him as Mr. Bueto, based on Mrs. Corvus's previous description, sends a shiver down your spine. Quickly, you take action, grabbing the shotgun from beside your bed and swiftly eliminating the threat. Mrs. Corvus, alarmed by the disturbance, rushes into your room, finding Mr. Bueto's lifeless body. She embraces you in gratitude and relief, thanking you for keeping your promise to protect her. You offer reassurance that she can now feel safe and secure in the enigmatic cabin, free from further harm.")
                                print("Ending #20 - A Promise Fulfilled")
                            elif choice23 == "2":
                                print("You choose to stay silent, and Mrs. Corvus appreciates your presence and your willingness to lend an empathetic ear. After a long and somber day, she takes you to her room, where she requests your company for the night to help alleviate her loneliness. In the dead of night, a loud crash and shattering glass pierce the quiet. You and Mrs. Corvus are jolted awake, and you act swiftly, turning on the lights. The sight that greets you is a broken-down door, and your recognition of the intruder as Mr. Bueto, based on Mrs. Corvus's earlier description, sends a shiver down your spine. In her moment of panic, Mrs. Corvus reaches for the shotgun beside her bedside and takes action, firing upon Mr. Bueto. He falls lifeless, and Mrs. Corvus releases a sigh of relief, embracing you tightly. She expresses her happiness and gratitude for your safety, assuring you that there are no more threats looming over your home. With resolve, she pledges to protect both you and the enigmatic cabin, no matter what challenges may come your way.")
                                print("Ending #21 - A Guardian's Promise")
                    elif choice19 >= 10 and choice19 <= 20:
                        print("You decide to pick the channel " + str(choice19) + ", it turns out to be a delightful comedy. As you and Mrs. Corvus enjoy the humorous scenes on the screen, time flies by unnoticed. Laughter and shared enjoyment fill the room, and you realize that it's already dinner time. Mrs. Corvus, displaying a friendly and inviting demeanor, informs you that the fridge is empty, and she needs to venture into the woods to gather some food for the evening meal. She then turns to you with a warm smile and asks if you'd like to accompany her on this foraging adventure. The hours spent watching TV have brought a sense of camaraderie, and you find that you've genuinely enjoyed spending time with Mrs. Corvus.")
                        print()
                        print("1. Go back to bed and sleep.")
                        print("2. Go foraging with Mrs. Corvus.")
                        print()
                        choice20 = input("> ")
                        if choice20 == "1":
                            print("You choose to stay home, and Mrs. Corvus ventures out on her own to forage for food. Left to your own devices, you return to your room, and in the quiet of this space, you hear a soft rustling and see movement in the corner. To your astonishment, a humanoid figure emerges from the shadows. It's a humanoid frog, and they introduce themselves as Anura. Anura explains their captive status and their fervent quest for escape, confirming that they were indeed the enigmatic shadowy figure lurking in the closet. After this unexpected encounter, you stand at a crossroads, faced with a decision to place your trust in this enigmatic character or to remain cautious of their motives.")
                            print("Ending #6 - The Silent Strike")
                        elif choice20 == "2":
                            print("You decide to go foraging with Mrs. Corvus, but unfortunately, your efforts prove to be unsuccessful in finding any food. As the daylight begins to wane, Mrs. Corvus suggests heading back home as it's getting dark, expressing concern about the increasing difficulty of foraging in the fading light.")
                            print()
                            print("1. Suggest searching a bit longer.")
                            print("2. Agree to go home with Mrs. Corvus.")
                            print()
                            choice21 = input("> ")
                            if choice21 == "1":
                                print("You choose to suggest searching a bit longer, and together with Mrs. Corvus, you delve deeper into the woods in the hopes of finding dinner. Unfortunately, as time passes, you realize that you've become disoriented, and it's getting darker. The woods seem to close in around you, and exhaustion sets in. With a growing sense of unease, you and Mrs. Corvus continue to navigate the dense forest. However, the passage of time remains uncertain, and you are unable to find your way back home. Suddenly, a shadowy figure emerges from behind, wielding an ax. In a shocking and terrifying turn of events, the figure kills Mrs. Corvus and then turns its attention to you, leading to a gruesome and untimely end within the depths of the dark woods.")
                                print("Ending #17 - Lost in the Unforgiving Woods")
                            elif choice21 == "2":
                                print("You choose to agree to go home with Mrs. Corvus, and due to the lack of dinner, she suggests that you both head to bed. She kindly tucks you in for the night, ensuring you're comfortable and ready for rest. However, in the middle of the night, your slumber is abruptly shattered by the sound of shattering glass. An unidentifiable figure has broken into your room through the window, and before you can react, the intruder raises an ax and ruthlessly brings it down on you, leading to an untimely and tragic demise.")
                                print("Ending #18 - A Nightmarish Intrusion")
                        choice20 = input("> ")
                    elif choice19 >= 0 and choice19 <= 10:
                        print("You decide to pick the channel " + str(choice19) + ". In a stroke of ill-fated luck, the channel you select displays a horror movie, filled with unsettling scenes and eerie suspense. However, rather than enjoying the movie, Mrs. Corvus is horrified and deeply offended by your choice. In her anger and fear, she reacts swiftly and ruthlessly, snapping your neck on the spot.")
                        print("Ending #16 - Frightful Channel Choice")
            elif choice17 == "3":
                print("You decide to force yourself to eat the unappetizing worm and snail soup. However, as you endure each bite, the taste and texture become unbearable. The situation takes a grim turn when your body rejects the unusual meal, causing you to throw up uncontrollably. The intensity of your retching causes you to pass out, and you collapse, your neck striking the table as you fall.")
                print("Ending #15 - A Vomitous Misstep")
    elif choice15 == "3":
        print("You decide to attempt an escape by leaping out of the open window, driven by a deep-seated worry that Mrs. Corvus might do something unexpected. Without a moment's hesitation, you take the daring plunge. As you plummet towards the ground, your heart pounds in your chest. Miraculously, you land in a well-placed bush that breaks your fall, though you're left with some scratches and bruises. As you regain your footing, you survey your options. The open woods beckon with the promise of freedom, a chance to put distance between yourself and the enigmatic Mrs. Corvus. On the other hand, you notice that her backyard fence stands invitingly open, offering a hiding place that might help you evade her notice while remaining close to the cabin.")
        print()
        print("1. Run into the woods")
        print("2. Hide in the backyard")
        print()
        choice24 = input("> ")
        if choice24 == "1":
            print("You choose to run into the woods, hoping to put some distance between yourself and the enigmatic Mrs. Corvus. As you venture deeper into the dense forest, the trees close in around you, and you quickly become disoriented. The sun dips below the horizon, plunging the woods into darkness, and you find yourself hopelessly lost. In the black of night, you hear the rustling of leaves and the snapping of twigs, your heart pounding with each mysterious sound. Suddenly, a dark figure emerges from the shadows, wielding a gleaming, menacing object. Before you can make out any details, a chilling realization washes over you. You don't see the figure's face or hear its voice, but the fear that overtakes you in that instant is all-encompassing. Your final moments are shrouded in terror and confusion as the ax falls, ending your journey in the heart of the ominous woods.")
            print("Ending #2 - Silenced in the Woods")
        elif choice24 == "2":
            print("You choose to hide in the backyard, and as you discreetly approach the shed in the corner of Mrs. Corvus's property, you notice an unusual keypad lock on the shed's door. It leaves you wondering about the mysterious code needed to unlock it. ")
            print()
            choice25 = int(input("ENTER CODE: "))
            if choice25 == 2098:
                print("You type in the code " + str(choice25) + " and the shed door swings open! You hastily slip inside, closing the door behind you to conceal your presence. Your hearts race as you hear Mrs. Corvus exit the cabin. Fear grips you as you imagine the potential consequences of your actions. After what feels like an eternity, you hear her reenter the cabin, and you seize the moment to make your escape. With a sense of urgency, you quietly exit the shed and disappear into the surrounding woods, hopeful to find your way back home, leaving behind the enigmatic cabin and its mysteries.")
                print("Ending #22 - Code Escape")
            else:
                print("You type in the code " + str(choice25) + " however, your heart sinks when you hear an ominous beep, signaling that it's the incorrect code. Panic sets in as you fumble with the keypad, attempting a few more combinations to no avail. Frustration mounts, but your hope is short-lived as Mrs. Corvus emerges from the cabin, bewildered by your actions. Before you can explain, her demeanor shifts, her once-kind eyes turning cold and unrelenting. Without warning, she seizes a nearby garden hose, her fingers coiling around it with unnatural strength. In a horrifying turn of events, she lunges at you, and the hose tightens around your throat. Darkness quickly claims you, your vision fading as your life slips away in the grip of the enigmatic humanoid crow.")
                print("Ending #3 - The Stranglehold of Deceit")