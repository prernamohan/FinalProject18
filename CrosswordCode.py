import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 800))


class Cell:
    def __init__(self, x, y, is_blank, value=" "):
        self.x = x
        self.y = y
        self.is_blank = is_blank
        if self.is_blank:
            self.value = "*"
        else:
            self.value = value
    def show_cell(self):
        print(self.value, end=" ")

class Grid:
    def __init__(self, rows, cols):
        self.grid = []
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(Cell(x, y, True))
            self.grid.append(row)

    def make_word(self, word, direction, x, y):
        for n in range(len(word)):
            if direction == 'horizontal':
                self.grid[y][x+n].value = word[n]
            elif direction == 'vertical':
                self.grid[y+n][x].value = word[n]

    def show_grid(self):
        for row in self.grid:
            for cell in row:
                cell.show_cell()
            print("")
        print("-"*30)

grid = Grid(3, 5)
grid.show_grid()
grid.make_word('cat', 'horizontal', 0, 0)
grid.make_word('cow', 'vertical', 0, 0)
grid.show_grid()

print("Welcome to the Magnet-Themed Crossword Game!")
#player_name = input("Enter player name:")

#class Crossword_position:
#"""Class describing position of letters"""
    #def __init__(self, coord, answer, guessed)
     #   self.coord = [(26,0), (30,0), (17,-1), (24,-1), (26, -1), (30, -1), (17, -2), (24, -2), (26, -2), (30, -2), (41, -2), (42, -2), (43, -2), (44, -2),(45, -2), (46, -2),
      #  self.answer =
       # self.guessed =

#class Crossword:
"""Class describing clues of crossword with list of words"""

 #   def __init__(self, word, clue):
  #      self.word = word
   #     self.clue = clue


'''
sanservino = Crossword("Sanservino", "the junior year teacher everyone hates")
gupta = Crossword("Dr.Gupta", "the freshmen year teacher who gave us the most work")
omay = ("Omay", "the IT help for our tech class")
great_gatsby = ("The Great Gatsby", "
python = ("Python", "the language we are learning")
jenn = ("Jenn", "
rfl = ("Relay for Life", "event in March")
magnet_madness = ("Magnet Madness", "a spirit event at the end of the year where the reward is popsicles")
speakeasy = ("Speakeasy", "
engineering = ("Engineering", "the reason why we are 'here' but no one wants to pursue the career")
arnold
ap = ("AP Exams", "hell week in May")
studentgov = ("Student Government",
timeline =
makerspace = ("Makerspace", "the one specialized room in Magnet that no other school has")
allison
nowakoski = ("Nowakoski", "the teacher who introduced derivational morphology")
autocad_certification = ("AutoCad Exam", "the exam we were all forced to take at the end of sophomore year and are required to pass for our vocation")
semi_formal = ("Semi-formal dance", "the dance no one shows up to")
slogan1 = ("For the Brand", "Rafalowski slogan that caused many the controversy")
slogan2 = ("Think Positive and Stay Attraactive", "the slogan that went on our sweatshirts")
gerstein = ("Gerstein", "our favorite junior year tech teacher")
'''
