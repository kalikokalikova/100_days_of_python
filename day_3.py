def love_check(name1, name2):
  true = ['t','r','u','e']
  love = ['l','o','v','e']

  names = (name1 + name2).lower()
  true_count = 0
  love_count = 0

  for char in true:
    true_count += names.count(char)
  
  for char in love:
    love_count += names.count(char)

  score = love_count + (true_count * 10)

  if 90 > score < 10:
    statement = "Coke and mentos"
  elif 50 > score < 40:
    statement = "Alright"
  else:
    statement = "???"
  
  print("You are " + str(score) + "% compatible")
  print(statement)

love_check("Arianna Rebolini", "Channing Tatum")



def treasure_hunt():
  treasure_img = r"""
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
  """
  print(treasure_img)
  print("Welcome to Treasure Island. You mission is to find the treasure.")

  left_or_right = input("left or right? ").lower()
  if left_or_right == "left":
    swim_or_wait = input("swim or wait? ").lower()
    if swim_or_wait == "wait":
      door = input("Choose a door: blue, red, or yellow? ").lower()
      if door == "red":
        print("Burned by fire. Game over.")
      elif door == "yellow":
        print("YOU FOUND THE TREASURE!!! HOORAY!!")
      elif door == "blue":
        print("Eaten by beasts. Game over.")
      else:
        print("You typed nonsense. Game over.")
    else:
      print("Attacked by trout. Game over.")
  else:
    print("Fall into a hole. Game over.")

treasure_hunt()


