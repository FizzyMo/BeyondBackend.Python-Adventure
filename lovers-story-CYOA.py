import sys
import time
import os
# Colored text in the terminal
TITLE_COLOR = '\033[1;36m'  # Cyan, bold
TEXT_COLOR = '\033[0m'      # Default
CHOICE_COLOR = '\033[1;33m' # Yellow, bold
RESET = '\033[0m'           

def clear_screen():
    # Clear the terminal screen based on OS.
    os.system('cls' if os.name == 'nt' else 'clear')

def print_story(text):
    
    print(f"{TEXT_COLOR}{text}{RESET}")
    time.sleep(1)

def print_title(text):
    
    print(f"{TITLE_COLOR}{text}{RESET}")
    time.sleep(0.5)

def print_choices(choices):
    
    print(f"\n{CHOICE_COLOR}What will you do?{RESET}")
    for i, choice in enumerate(choices, 1):
        print(f"{CHOICE_COLOR}{i}. {choice}{RESET}")
    print()

def get_choice(valid_choices):
    # Gets player's name with validation
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and int(choice) in valid_choices:
            return int(choice)
        print(f"Please enter a valid choice ({', '.join(map(str, valid_choices))})")

def introduction():
    # Introduces background of the story
    clear_screen()
    print_title("\n=== LEAGUE OF LEGENDS: A TALE OF FEATHERS ===\n")
    
    print_story("Cast your mind back to the year 2009, when League of Legends was forged into existence.")
    print_story("Feel the weight of years, as the game grew, evolved, and etched its mark in the annals of gaming history.")
    print_story("Riot Games, the architects of this digital battleground, stand as pioneers in the vast world of multiplayer online battle arenas.")
    
    while True:
        name = input("\nEnter your name: ")
        if name.isalpha():
            print_story(f"And you, {name}, have ventured into a League of Legends story.")
            break
        else:
            print("Invalid input! Please enter a name without numbers or punctuation.")
    
    time.sleep(2)
    clear_screen()
    print_title("\n=== THE JOURNEY BEGINS ===\n")
    # Adventure's premise
    print_story("Yet, today is not about summoner spells or pixelated battles; it's about an adventure untold.")
    print_story("A choose-your-own odyssey where the destiny of two enchanting soulmates, Xayah and Rakan, lies in your hands.")
    print_story("Are you prepared to embark on this journey, shaping fate with every decision?")
    print_story("The stage is set. The tale awaits.")
    print_story("Let the adventure commence!\n")
    
    input("Press Enter to continue...")
    clear_screen()

def scene_prison_break():
    # First scene: Prison Break planning.
    print_title("\n=== THE PRISON BREAK ===\n")
    
    print_story("There are moments in life where you need to decide where your passion is.")
    print_story("Xayah sighs, exasperated with her partner. \"This is a prison break. Rakan is the worst! I swear he is focusing on his perfect golden feathers. Let's hope he doesn't mess up the plan.\"")
    print_story("Rakan looks up, confusion on his face. \"Huh? What??\"")
    print_story("Xayah gestures impatiently. \"The guards. You'll distract the guards away from the western gate. Once that happens I'll throw a feather into the sky.\"")
    print_story("Rakan nods, confidence returning. \"You got it babe.\"")
    
    print_choices(["Rakan messes up the plan and gets caught", "Rakan distracts the guards and meets up with Xayah"])
    choice = get_choice([1, 2])
    
    if choice == 1:
        return scene_rakan_caught()
    else:
        return scene_successful_distraction()

def scene_rakan_caught():
    # Scene where Rakan gets caught by the guards.
    print_title("\n=== CAPTURED ===\n")
    
    print_story("Xayah watches Rakan from a distance. \"Alright things are going smooth. Time to move.\"")
    print_story("Suddenly, the guards surround Rakan. Xayah's heart sinks.")
    print_story("\"NO NO! PLEASE! RAKAN!\" she screams, her voice echoing across the prison grounds.")
    
    return scene_lay_on_ground()

def scene_lay_on_ground():
    # Scene where Xayah is heartbroken after Rakan's capture.
    print_title("\n=== HEARTBREAK ===\n")
    
    print_story("Xayah passes out from the trauma of seeing her love being taken away by HUMANS!")
    print_story("She slowly starts to wake up, laying on the cold ground with a broken heart.")
    
    print_choices(["Continue..."])
    get_choice([1])
    
    print_story("As Xayah continues to lay there, all she can feel is heartbreak. Heartbreak from seeing humans even think of touching him.")
    print_story("\"We are partners!\" she whispers.")
    print_story("\"No... we are not just partners.\"")
    print_story("\"Rakan is my soul mate, my lover, my best friend.\"")
    print_story("Her mind begins to race with rage!")
    
    return scene_face_humans_or_rakan()

def scene_successful_distraction():
    # Scene where Rakan successfully distracts the guards.
    print_title("\n=== THE DISTRACTION ===\n")
    
    print_story("Rakan leaps back and forth between the walls, leading the guards away with graceful movements.")
    print_story("Xayah watches with pride. \"I knew you could do it.\"")
    print_story("Rakan smirks. \"I know.\"")
    print_story("\"My god,\" Xayah thinks to herself. \"I don't know if I want to slap him, kiss him, or both.\"")
    print_story("She shakes her head as Rakan walks over to her.")
    print_story("\"Your soul belongs to me,\" he whispers.")
    print_story("Xayah touches Rakan's face. \"Let's go.\"")
    
    return scene_together_rakan()

def scene_together_rakan():
    # Scene where Xayah and Rakan are reunited.
    print_title("\n=== REUNITED ===\n")
    
    print_story("The wind starts to pick up, and Xayah takes advantage of the opportunity to climb higher.")
    print_story("Not knowing how long this favorable breeze will persist, she laughs aloud, her laughter resonating across the atmosphere as she expands her wings.")
    print_story("She's lifted above the jail premises by the currents, giving her a higher view of the landscape.")
    print_story("Her gaze focuses on Rakan as she soars; he is quick and nimble, leading the guards on a risky chase between the walls.")
    print_story("She feels a mixture of pride and frustration as she watches his acrobatics below.")
    print_story("She descends softly and lands close to Rakan as he gathers his breath.")
    
    return scene_go_choice()

def scene_face_humans_or_rakan():
    # Scene where Xayah must choose between evasion or confrontation.
    print_title("\n=== THE CHOICE ===\n")
    
    print_story("Xayah moves in the direction of the gate. She takes a moment to step back, preparing to wreak havoc on those who have imprisoned her and taken Rakan.")
    print_story("She laughs out loud as she is carried effortlessly by the wind across the jail grounds, enjoying the freedom of flight and the vast space.")
    print_story("Gazing downward from this perspective, she witnesses Rakan deftly dodging the approaching guards.")
    print_story("Suddenly, there's danger as she floats through the air. Crossbow-wielding enforcers arrive on magical gliders.")
    print_story("Xayah is in their sights.")
    
    print_choices([
        "Evade: Make evasive maneuvers to dodge the incoming arrows",
        "Confront: Face the enforcers directly to protect Rakan"
    ])
    choice = get_choice([1, 2])
    
    if choice == 1:
        return scene_evade_arrows()
    else:
        return scene_confront_enforcers()

def scene_evade_arrows():
    # Scene where Xayah evades the arrows.
    print_title("\n=== EVASION ===\n")
    
    print_story("In a fit of rage, Xayah unleashes a storm of deadly feathers, swiftly eliminating every enforcer in sight.")
    print_story("The air is thick with tension as the last echoes of battle fade away. She stands alone, surrounded by the fallen.")
    print_story("As the reality of the aftermath settles, she finds herself consumed by a haunting emptiness.")
    print_story("The victory is hollow without Rakan by her side. She collapses to the ground, overwhelmed by the weight of loss.")
    print_story("As she wakes up from the horror that her own mind has been reminding her, a new day burns her eyes from the tears shed during her restless sleep.")
    print_story("Though only moments may have passed, Rakan's absence feels like a lifetime.")
    
    return scene_rev_plan()

def scene_confront_enforcers():
    # Scene where Xayah confronts the enforcers.
    print_title("\n=== CONFRONTATION ===\n")
    
    print_story("Xayah dreams of Rakan. She remembers how he tells her to be careful.")
    print_story("That was the last time she saw him before they parted ways. Her heart continues to sink.")
    print_story("Fueled by rage and an unyielding desire to protect Rakan, she abandons evasion and dives straight towards the enforcers on their magical gliders.")
    print_story("Her feathers surround her like a tempest as she descends, a force of nature ready to confront those who dare threaten her love.")
    print_story("The enforcers, taken aback by her sudden offensive, try to adjust their aim, but the chaotic dance of her feathers makes it difficult for them to lock on.")
    print_story("In a burst of fury, she unleashes a barrage of razor-sharp feathers towards the approaching threat.")
    print_story("The clash between magic and feathers unfolds in the night sky. The air echoes with the sounds of battle as Xayah fights to keep the enforcers at bay.")
    print_story("Rakan, watching from below, is awestruck by the display of power.")
    print_story("\"That's my girl!\" he shouts proudly.")
    
    return scene_face_humans_or_rakan_end()

def scene_rev_plan():
    # Scene where Xayah must decide on revenge or sticking to the plan.
    print_title("\n=== CROSSROADS ===\n")
    
    print_story("\"Where do I go from here?\" Xayah wonders, facing a critical decision.")
    
    print_choices([
        "Seek revenge against those responsible",
        "Stick to the original plan and escape"
    ])
    choice = get_choice([1, 2])
    
    if choice == 1:
        return scene_seek_revenge()
    else:
        return scene_stick_to_plan()

def scene_seek_revenge():
    # Scene where Xayah seeks revenge.
    print_title("\n=== VENGEANCE ===\n")
    
    print_story("Xayah takes a moment to slow down her mind, to remember every detail of the humans who took Rakan.")
    print_story("\"What did they look like?\"")
    print_story("\"Where did they take Rakan?\"")
    print_story("\"How will I get him back?\"")
    print_story("\"What do I need to pull it off?\"")
    print_story("\"Am I strong enough?\"")
    
    return scene_go_choice()

def scene_stick_to_plan():
    # Scene where Xayah sticks to the original plan.
    print_title("\n=== THE ESCAPE ===\n")
    
    print_story("\"Time to fight,\" Xayah whispers.")
    print_story("Suppressing the burning desire for revenge, she focuses on the original plan: escape and find Rakan.")
    print_story("The winds of determination propel her forward as she navigates through the prison grounds, avoiding any potential threats.")
    print_story("As she moves stealthily, weaving through shadows and ducking behind structures, the distant sounds of alarms and shouts echo through the air.")
    print_story("The chaos caused earlier has drawn the attention of more guards, but their numbers are no match for her agility and lethal precision.")
    print_story("The prison layout becomes familiar as she approaches the designated escape route. It's a labyrinth of corridors and hidden passages, known only to those who have spent years studying the intricacies of the prison's design.")
    print_story("Suddenly, a group of guards blocks her path. There's no avoiding them, and confrontation seems inevitable. With a deep breath, she summons her feathers, ready to face the onslaught.")
    print_story("The guards, however, are hesitant. The tales of her earlier rampage have spread, and fear is evident in their eyes. Without a word, they part, allowing her a clear path forward.")
    print_story("As she reaches the exit, the night air greets her, and the open sky beckons. Freedom is within reach.")
    print_story("The moonlight illuminates her golden feathers, a stark contrast to the darkness that surrounds her.")
    print_story("\"Rakan, wherever you are, I'm coming.\"")
    
    return scene_rev_plan_end()

def scene_go_choice():
    # Scene where Xayah must choose between getting shot or reaching Rakan.
    print_title("\n=== AERIAL DANGER ===\n")
    
    print_story("The wind is starting to pick up.")
    print_story("Xayah uses this moment to get higher ground. Who knows how long the wind will continue.")
    print_story("She laughs high into the air, spreading her wings, allowing the air to carry her high above the prison grounds.")
    print_story("She sees Rakan in the distance.")
    
    print_choices([
        "Xayah gets shot down",
        "Xayah reaches Rakan"
    ])
    choice = get_choice([1, 2])
    
    if choice == 1:
        return scene_shot_down()
    else:
        return scene_reach_rakan()

def scene_shot_down():
    # Scene where Xayah gets shot down.
    print_title("\n=== FALLEN ===\n")
    
    print_story("An arrow pierces through Xayah's wing.")
    print_story("She spirals downward, unable to maintain flight.")
    print_story("The world around her blurs as she plummets towards the ground.")
    print_story("Her last thoughts are of Rakan as darkness engulfs her.")
    
    return scene_game_over()

def scene_reach_rakan():
    # Scene where Xayah reaches Rakan.
    print_title("\n=== REUNITED ===\n")
    
    print_story("\"There you are,\" Xayah says with relief as she spots Rakan.")
    
    return scene_plan_rak()

def scene_plan_rak():
    # Scene where Xayah must decide on a rescue approach.
    print_title("\n=== THE RESCUE ===\n")
    
    print_story("Taking a deep breath, Xayah assesses the situation. The wind still beneath her wings, she gathers her resolve.")
    print_story("\"Alright. There were four humans. Two in front of Rakan and two behind him. They took him to the North entrance. How can I get there from here?\"")
    
    print_choices([
        "Risk it all and go straight to the gate",
        "Make a careful plan for the rescue"
    ])
    choice = get_choice([1, 2])
    
    if choice == 1:
        return scene_direct_approach()
    else:
        return scene_careful_plan()

def scene_direct_approach():
    # Scene where Xayah takes a direct approach to rescue Rakan.
    print_title("\n=== DIRECT APPROACH ===\n")
    
    print_story("Knowing nothing matters but Rakan, Xayah takes a deep breath.")
    print_story("She shakes off any dark thoughts and starts running directly to the North gate. Maybe she's not that far behind and can still save him.")
    print_story("\"Hold on, my love! I'm coming!\"")
    print_story("As her feathers fall into all directions with a mind of their own, she gets closer to the North gate.")
    print_story("Traces of Rakan's golden feathers on the ground give her hope. He is close.")
    
    return scene_last_scene()

def scene_careful_plan():
    # Scene where Xayah makes a careful plan to rescue Rakan.
    print_title("\n=== THE PLAN ===\n")
    
    print_story("\"Take out two of the guards while Rakan deals with the other two guards. Good enough for me. Let's save him.\"")
    print_story("In the shadows, they silently approach the prison's entrance. Rakan, ever the charming distraction, engages the attention of the guards while Xayah prepares her feathers for a swift and precise strike.")
    print_story("As Rakan engages in playful banter, distracting the guards, she releases her deadly feathers with unparalleled precision.")
    print_story("Two guards fall without a sound, their eyes widening in surprise before they crumple to the ground.")
    print_story("\"Smooth, love,\" Rakan says with a smirk.")
    print_story("\"Save the compliments for later. We're not out of this yet,\" Xayah responds.")
    print_story("With half the guards dealt with, they move swiftly towards the remaining two. Rakan's charm is a weapon in itself, disorienting the guards just enough for Xayah to strike. The night air echoes with the clash of metal and the thud of incapacitated foes.")
    print_story("They reach the North entrance, victorious in their stealthy approach. The gate looms ahead, and Rakan gives her a sly grin.")
    print_story("\"Shall we?\" he asks.")
    print_story("\"Let's get out of here,\" Xayah responds.")
    print_story("Hand in hand, they slip through the gate, leaving the prison behind. The moonlight bathes them as they disappear into the night, ready for the adventures that await.")
    
    return scene_happy_ending()

def scene_last_scene():
    # Final scene of the direct approach path.
    print_title("\n=== THE FINAL CONFRONTATION ===\n")
    
    print_story("\"He better be okay or ELSE!\" Xayah threatens as she approaches.")
    print_story("She stops right in front of two guards. One guard is directly in front of her, and another holds Rakan by the wrists. She smirks.")
    print_story("\"Honey, you okay?\" she asks Rakan.")
    print_story("\"Oh, this is nothing. Me and the guys were just going for a walk,\" Rakan replies with his usual charm.")
    print_story("Xayah rolls her eyes. Even in danger, he still has something smart to say. She snaps her fingers, and her quills tear through both guards, leaving their corpses on the ground. She takes Rakan into her arms.")
    print_story("As they sprint towards the North entrance, adrenaline pumping through their veins, they encounter more resistance.")
    print_story("Guards pour in from all sides, alerted by the commotion. But together, with their combined skills, they cut through them like a whirlwind.")
    print_story("Finally, they reach the North gate. Rakan, though battered, wears a grin.")
    print_story("\"You took your sweet time, love,\" he teases.")
    print_story("\"Oh, shut up. Let's get out of here,\" Xayah responds.")
    print_story("They burst through the gate, leaving the prison behind. The wind carries them away as they soar into the night sky, free from the clutches of captivity.")
    
    return scene_love()

def scene_face_humans_or_rakan_end():
    # Ending scene for the confrontation path.
    print_title("\n=== VICTORY ===\n")
    
    print_story("As Xayah lands beside Rakan, her injured wing a testament to the intensity of the battle, they exchange a glance filled with both relief and concern.")
    print_story("\"You're incredible, love. But we need to go before more reinforcements arrive,\" Rakan says, his voice gentle yet urgent.")
    print_story("Together, hand in hand, they vanish into the night, leaving the scene of their triumph behind.")
    
    return scene_happy_ending()

def scene_rev_plan_end():
    # Ending scene for the stick to plan path.
    print_title("\n=== THE JOURNEY CONTINUES ===\n")
    
    print_story("Xayah's determination to stick to the original plan allows her to navigate the prison's challenges and escape.")
    print_story("The journey to find Rakan continues in the vast expanse beyond the prison walls.")
    print_story("If you'd like to embark on another adventure or have a new story idea, feel free to create it!")
    
    return scene_game_over()

def scene_game_over():
    # Game over scene.
    print_title("\n=== GAME OVER ===\n")
    
    print_story("Thank you for playing!")
    print_story("Copyright: Carisa Saenz-Videtto")
    
    return None

def scene_happy_ending():
    # Happy ending scene.
    print_title("\n=== HAPPY ENDING ===\n")
    
    print_story("Together, Xayah and Rakan have overcome the challenges that stood in their way.")
    print_story("Their bond, stronger than ever, will guide them through whatever adventures lie ahead.")
    print_story("Thank you for playing!")
    print_story("Copyright: Carisa Saenz-Videtto")
    
    return None

def scene_love():
    # Love ending scene.
    print_title("\n=== LOVE CONQUERS ALL ===\n")
    
    print_story("Xayah and Rakan's love triumphs over adversity as they escape the prison together.")
    print_story("Their journey continues in the vast expanse of Eldoria, where new adventures await.")
    print_story("Thank you for guiding Xayah through her tale. If you'd like to embark on another adventure, feel free to create a new story!")
    print_story("Hoped you enjoyed the story")
    print_story("Copyright: Carisa Saenz-Videtto")
    
    return None

def main():
    # Main game loop.
    introduction()
    
    current_scene = scene_prison_break
    while current_scene:
        current_scene = current_scene()
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()