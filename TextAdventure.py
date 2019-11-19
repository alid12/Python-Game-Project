from StoryAFile import storyA
from StoryBFile import storyB

print("----------4000CEM Week 4 Lab 2 Task----------")
print("----------------<InsertTitleHere>---------------")
print("---------------<InsertAuthorsHere>--------------")
print("\n")

print("You awake in a dark room.  Do you:")
print("a) Scream for help.")
print("b) Press the light switch")
x = input("Enter a or b: ")
if x == "a":
    print("Someone hears your screams...")
    storyA()
elif x == "b":
    print("The light comes on.")
    print("You do not recognise the room but you have a really bad feeling...")
    storyB()
else:
    print("That was not an option.  Game Over")
