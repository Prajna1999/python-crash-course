#!/usr/bin/env python3
"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""                                                  

storyFormat = """                                       
In the heart of a forgotten jungle, where vines whispered secrets to the trees,
lived a curious {animal}. This {animal} had a peculiar love for {food},
though the jungle offered only a meager taste of it.

One humid afternoon, an explorer stumbled upon the {animal},
and was astonished to learn of its fondness for {food}.
Wanting to help, the explorer gently coaxed the {animal}
into an adventure far from home.

They traveled to the bustling city of {city}, where {food}
was abundant and the {animal} feasted joyfully for days.

But as the city lights twinkled each night, the {animal}
longed for the rustling leaves and the chorus of frogs.
Homesick and weary, it yearned for the wild it once knew.

Touched by its sorrow, the explorer returned the {animal}
to its jungle home—this time, with a grand stash of {food}
and a promise to visit again.

And so, the {animal} lived happily, savoring each bite beneath the stars.

The End.
"""
                                         

def tellStory():
    while True:
                                             
        userPicks = dict() 
        for cue in ['animal', 'food', 'city']:
            addPick(cue, userPicks)                                       
        story = storyFormat.format(**userPicks)
        print("\n" + "-"*50 + "\n")
        print(story)
        print("-"*50 + "\n")
        
        again=input("Want to create a new story?(yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            break
        print("Goodbye! Thanks for playing")
        
        
                                                    
def addPick(cue, dictionary):
    '''Prompt for a user response using the cue string,
    and place the cue-response pair in the dictionary.
    '''
    prompt = 'Enter an example for ' + cue + ': '
    response = input(prompt).strip() 
    dictionary[cue] = response                                                             

tellStory()                                               
