import pygame
import time

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
done = True

class Crossword():
    def __init__(self, word, direction, x, y):
        self.word = word
        self.direction = direction
        self.x = x
        self.y = y

word = ["omay", "juan"]
position = ["H1", "V1"] 
correct_guesses = []
omay = Crossword("omay", "horizontal", 50, 150)
juan = Crossword("juan", "vertical", 130, 70)

class Display:

    def __init__(self, word, x, y):
        self.word = word
        self.x = x
        self.y = y

    def display_text(self):
        text1 = font.render(self.word, True, red)
        gameDisplay.blit(text1, (self.x, self.y))
        pygame.display.update()

omay1display = Display("o", omay.x, omay.y)
omay2display = Display("m", omay.x + 40, omay.y)
omay3display = Display("a", omay.x + 80, omay.y)
omay4display = Display("y", omay.x + 120, omay.y)

juan1display = Display("j", juan.x, juan.y)
juan2display = Display("u", juan.x, juan.y + 40)
juan3display = Display("a", juan.x, juan.y + 80)
juan4display = Display("n", juan.x, juan.y + 120)

class ShowWord:

    def display_omay(self):
        omay1display.display_text()
        omay2display.display_text()
        omay3display.display_text()
        omay4display.display_text()

    def display_juan(self):
        juan1display.display_text()
        juan2display.display_text()
        juan3display.display_text()
        juan4display.display_text()

font = pygame.font.SysFont("monospace", 22)
show_word = ShowWord()

def main_code():
    guess_right = 0
    while guess_right == 0:
        pygame.display.update()
        gameDisplay.fill(white)  
        b1 = pygame.image.load("crossword4.jpg") 
        gameDisplay.blit(b1, (0,0))
        pygame.display.update()
        guess_position = input("Enter position: ")
        guess = input("Enter a guess: ")
        if guess in word:
            guess_index = word.index(guess)
            check_position = position[guess_index]
            if check_position == guess_position:
                print("you are correct")
                correct_guesses[guess_index:guess_index] = [guess]
                if guess == "omay":
                    show_word.display_omay()
                elif guess == "juan":
                    show_word.display_juan()

            if correct_guesses == word:
                guess_right = 1
        else:
            print("you were wrong")
            guess_right = 0

 

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.display.update()
    gameDisplay.fill(white)  
    b1 = pygame.image.load("crossword4.jpg") 
    gameDisplay.blit(b1, (0,0))
    pygame.display.update() 
    main_code()

    pygame.display.flip()









# def display_text(text, x, y):
#     text1 = font.render(text, True, red)
#     gameDisplay.blit(text1, (x, y))
#     pygame.display.update()
# def display_omay():
#     display_text("o", omay.x, omay.y)
#     display_text("m", omay.x + 40, omay.y)
#     display_text("a", omay.x + 80, omay.y)
#     display_text("y", omay.x + 120, omay.y)

# def make_word(self, word, direction, x, y):
#         for n in range(len(word)):
#             if direction == 'horizontal':
#                 self.grid[y][x+n].value = word[n]
#             elif direction == 'vertical':
#                 self.grid[y+n][x].value = word[n]
# class Crossword():
#     def __init__(self, word, direction, x, y)
#         self.word = word
#         self.direction = direction
#         self.x = x
#         self.y = y

# word = ["omay", "himanee"]
# position = ["H1", "V1"] 
# correct_guesses = []
# H1 = Crossword("omay", "horizontal", 40, 140)
# V1 = Crossword("himanee", "vertical", 40, 160)

# guess_right = 0
# while guess_right == 0:
#   guess_position = input("Enter position: ")
#   guess = input("Enter a guess: ")
#   if guess in word:
#     guess_index = word.index(guess)
#     check_position = position[guess_index]
#     if check_position == guess_position:
#       print("you are correct")
#       correct_guesses[guess_index:guess_index] = [guess]
#       if correct_guesses == word:
#           guess_right = 1
#   else:
#     print("you were wrong")
#     guess_right = 0


# omay = Crossword("omay", "horizontal", 40, 140)
# class Crossword():
#     def __init__(self, word, )
# def display_text(text):
#     text1 = font.render(text, True, red)
#     gameDisplay.blit(text1, (300,300))
#     pygame.display.update()

# positions = pygame.Surface._pixels_address 
# print({positions})   
# x = 300
# y = 300
# keyPressed = pygame.key.get_pressed()
# if keyPressed(pygame.K_DOWN):
#     if keyPressed(pygame.K_a):
#         display_text("a")
# if keyPressed(pygame.K_UP):
#     y -= 20
# if keyPressed(pygame.K_DOWN):
#     y += 20
# if keyPressed(pygame.K_RIGHT):
#     x += 20
# if keyPressed(pygame.K_LEFT):
#     x -= 20
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

