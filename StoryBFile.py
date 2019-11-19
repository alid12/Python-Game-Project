def storyB():
  print("This is story B...")
    # Contine adventure Here
  print("a) You try to look around the room for clues")
  print("b) You run to the door")
  x = input("Enter a or b: ")
  if x=="a": 
    print("You notice things are flying around in the room. You look out of the window and see something that looks like planets, stars and rocks.......You are in a space shuttle DAMN.")
    print("a) You start opening all the closed boxes.")
    print("b) You pinch yourself to make sure you are awake.")
    x=input ("Enter a or b")
    if x=="a": 
      print("a) You find a key in one of the boxes.")
      print("b) You find a paper written on it YOU WERE PRANKED.")
      x=input ("Enter a or b")
      if x=="a": 
        print("a) The key opens the door and you get shot once outside.")
        print("b) You open the door as a timed bomb goes off and the shuttle explodes.")
      if x=="b": 
        print("a) You open the door and your friends are laughing outside. it was only a simulator.")
        print("b) You faint from the shock.")
      else:
        print("That was not an option.  Game Over")
    if x=="b": 
      print("a) You wake up sweating and realise it was a dream.")
      print("b) As always luck isn't on your side and you are not sleeping.")
      if x=="b": 
        print("a) You scream and the door opens and Aliens come in and knock you out.")
        print("b) You find a button and press it . You hear an recorded voice saying you were chosen.")
    else:
        print("That was not an option.  Game Over")
    
  elif x == "b":
    print("a) You find the door opened. ")
    print("b) You find the door locked.")
    x=input ("Enter a or b")
    if x=="a": 
      print("a) You look around and realise you are alone in a villa.")
      print("b) You find someone infront of you that knocks you out.")
      x=input ("Enter a or b")
      if x=="a": 
        print("a) You start pounding on the door.")
        print("b) You try breaking the glass.")
      else:
        print("That was not an option.  Game Over")
    if x=="b": 
      print("a) You break the window and climb down.")
      print("b) You pick the door lock.")    
      x=input ("Enter a or b")
      if x=="a": 
        print("a) You loose balance and fall to the ground and loose consiousness.")
        print("b) You land safely and start running.")
      if x=="b": 
        print("a) You break a vase, expose yourself and immeadiately get shot.")
        print("b) You run out of the building and descover you are stuck in an island.")
      else:
        print("That was not an option.  Game Over")