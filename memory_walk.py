# This is the Mind Palace, memory walk, or method of Loci
class MemoryPalace:
   def __init__(self):
      self.location = []
      self.name = "Name"

   def populate(self, i, iterator):
      self.location.append(Location())
      self.location[i].newLocation(iterator)

   def displayLocations(self, index):
      print()
      print(self.name)
      iterator = 1
      for i in range(0, index + 1):
         self.location[i].displayLocation(iterator)
         iterator += 1

   def createPalace(self):
      print("What is the name of this mind palace?")
      self.name = input()

# This records all the individual locations
class Location:
   def __init__(self):
      self.locationName = "Location name"
      self.description = "Description"
      self.focus = "focus"

   def setLocation(self, iterator):
      print("What is location {}?".format(iterator))
      self.locationName = input()

   def setFocus(self):
      print("What is the focus of this area?")
      self.focus = input()

   def setDescription(self):
      print("Briefly describe the area, include your focus:")
      self.description = input()

   def newLocation(self, iterator):
      self.setLocation(iterator)
      self.setFocus()
      self.setDescription()

   def displayLocation(self, iterator):
      print()
      print("Location {}: {}".format(iterator, self.locationName))
      print("Focus: {}".format(self.focus))
      print("Description--")
      print("{}".format(self.description))

#This is to help with user error
def errorChecking(answer):
   answer = answer.lower()
   while (answer != 'y' and answer != 'n'):
      print("Please enter y (yes) or n (no):")
      answer = input()
      answer = answer.lower()

   return answer

#This is for a new location in the Mind Palace
def newPalaceLocation():
   print()
   print("Would you like to add another location to your palace? (y/n)")
   newLocation = input()
   return errorChecking(newLocation)

def main():
   #Not the most effecient, but it would allow for searching at a later implementation
   locationIndex = 0 
   iterator = 1
   mindPalace = MemoryPalace()
   mindPalace.createPalace()
   mindPalace.populate(locationIndex, iterator)
   response = newPalaceLocation()
   
   while (response == 'y'):
      locationIndex += 1
      iterator += 1
      mindPalace.populate(locationIndex, iterator)
      response = newPalaceLocation()
   
   mindPalace.displayLocations(locationIndex)
   return 0

main()
