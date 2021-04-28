from PIL import Image 

beingwatched = False
peoplecontrolled = 1370
autodestruction = False

def takemindcontrol():
  hypnotic = Image.open(r"hypnotic.png") 
  hypnotic.show()

if beingwatched:
  takemindcontrol()
  peoplecontrolled+=peoplecontrolled
