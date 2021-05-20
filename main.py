import sys
import time
import random
startgame = input("Would you like to see how fast you can type?  Y/N ")

words = ["The quick brown fox jumps over the lazy dog", "Be the change you wish to see in the world.","Try and fail, but never fail to try.",  ]

def typing_test(picker):
  
  if startgame == "N":
    print("Ok, have a great day! ")
    sys.exit()

  elif startgame == "Y":
    print("Okay, type out this prompt: ")
    print(picker)
    start = int(time.time())
    basetest = input("")

    while basetest != picker:
      print("Please try again")
      print(picker)
      basetest = input("")
   
    end = int(time.time())
    wpm = round(len(picker) / 5 / ((end - start) / 60 ))
    print(str(wpm) + " Words per Minute" )
    
  else:
    print("Error: Input not recognized")
    sys.exit()


typing_test(random.choice(words))