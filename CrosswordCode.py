import pygame
import time

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
crossword = pygame.image.load("crossword.png") 


done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    gameDisplay.blit(crossword, (400,400))
    

#print("Welcome to the Magnet-Themed Crossword Game!")

#def guess_word():
 #   guess_position = input("Enter the box number:")
  #  guess_word = input("Enter your guess:")
#player_name = input("Enter player name:")

#class Crossword_position:
#"""Class describing position of letters"""
    #def __init__(self, coord, answer, guessed)
     #   self.coord = [(26,0), (30,0), (17,-1), (24,-1), (26, -1), (30, -1), (17, -2), (24, -2), (26, -2), (30, -2), (41, -2), (42, -2), (43, -2), (44, -2),(45, -2), (46, -2),
      #  self.answer =
       # self.guessed =

#class Crossword():
 #   def __init__(word, clue, direction, x, y):
  #      Crossword.word = word
   #     Crossword.clue = clue
    #    Crossword.direction = direction
        # Crossword.x = x
        # Crossword.y = y
    



# sanservino = Crossword("sanservino", "the junior year teacher everyone hates", "vertical", 19, 8)

# gupta = Crossword("Dr.Gupta", "the freshmen year teacher who gave us the most work")
# omay = ("Omay", "the IT help for our tech class")
# great_gatsby = ("The Great Gatsby", "
# python = ("Python", "the language we are learning")
# jenn = ("Jenn", "
# rfl = ("Relay for Life", "event in March")
# magnet_madness = ("Magnet Madness", "a spirit event at the end of the year where the reward is popsicles")
# speakeasy = ("Speakeasy", "
# engineering = ("Engineering", "the reason why we are 'here' but no one wants to pursue the career")
# arnold
# ap = ("AP Exams", "hell week in May")
# studentgov = ("Student Government",
# timeline =
# makerspace = ("Makerspace", "the one specialized room in Magnet that no other school has")
# allison
# nowakoski = ("Nowakoski", "the teacher who introduced derivational morphology")
# autocad_certification = ("AutoCad Exam", "the exam we were all forced to take at the end of sophomore year and are required to pass for our vocation")
# semi_formal = ("Semi-formal dance", "the dance no one shows up to")
# slogan1 = ("For the Brand", "Rafalowski slogan that caused many the controversy")
# slogan2 = ("Think Positive and Stay Attraactive", "the slogan that went on our sweatshirts")
# gerstein = ("Gerstein", "our favorite junior year tech teacher")


#Syntax for printing clues
#def print_clues():
#Horizontal:

#print(f"1:{sanservino.clue}")"""

