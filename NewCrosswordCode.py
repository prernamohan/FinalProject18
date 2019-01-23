import random

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



grid = Grid(20, 46)
grid.show_grid()


word = ["ARNOLD", "SEMIFORMAL", "NOWAKOSKI", "THINKPOSITIVEANDSTAYATTRACTIVE", "GERSTEIN", "FORTHEBRAND", "OMAY", "THEGREATGATSBY", "MAGNETMADNESS", "MAKERSPACE", "AUTOCADCERTIFICATION", "SPEAKEASY", "RELAYFORLIFE", "ALLISON", "STUDENTGOVERNMENT", "ENGINEERING", "TIMELINE", "SANSERVINO", "APEXAMS", "GUPTA", "JENN", "PYTHON"]
position = ["H5", "H6", "H7", "H11", "H13", "H15", "H16", "H19", "H20", "V1", "V2", "V3", "V4", "V5", "V6", "V8", "V9", "V10", "V12", "V14", "V17", "V18"] 
correct_guesses = []

def display_clue(self):
    print(f"H1:  ")

def display_word(self):
    if correct_guesses == word:
        print("Congratulations! You finished!")
    elif guess == "ARNOLD": 
        grid.make_word("ARNOLD", "horizontal", 40, 2)
        grid.show_grid()
    elif guess == "SEMIFORMAL":
        grid.make_word("SEMIFORMAL", "horizontal", 3, 3)
        grid.show_grid()
    elif guess == "NOWAKOSKI":
          grid.make_word("NOWAKOSKI", "horizontal", 13, 4)
          grid.show_grid()
    elif guess == "THINKPOSITIVEANDSTAYATTRACTIVE":
        grid.make_word("THINKPOSITIVEANDSTAYATTRACTIVE", "horizontal", 0, 8)
        grid.show_grid()
    elif guess == "GERSTEIN":
        grid.make_word("GERSTEIN", "horizontal", 33, 8)
        grid.show_grid()
    elif guess == "FORTHEBRAND":
        grid.make_word("FORTHEBRAND", "horizontal", 29, 12)
        grid.show_grid()
    elif guess == "OMAY":
        grid.make_word("OMAY", "horizontal", 12, 13)
        grid.show_grid()
    elif guess == "THEGREATGATSBY":
        grid.make_word("THEGREATGATSBY", "horizontal", 23, 15)
        grid.show_grid()
    elif guess == "MAGNETMADNESS":
        grid.make_word("MAGNETMADNESS", "horizontal", 3, 16)
        grid.show_grid()
    elif guess == "MAKERSPACE":
        grid.make_word("MAKERSPACE", "vertical", 25, 0)
        grid.show_grid()
    elif guess == "AUTOCADCERTIFICATION":
        grid.make_word("AUTOCADCERTIFICATION", "vertical", 29, 0 )
        grid.show_grid()
    elif guess == "SPEAKEASY":
        grid.make_word("SPEAKEASY", "vertical", 16, 1)
        grid.show_grid()
    elif guess == "RELAYFORLIFE":
        grid.make_word("RELAYFORLIFE", "vertical", 23, 1)
        grid.show_grid()
    elif guess == "ALLISON":
        grid.make_word("ALLISON", "vertical", 40, 2)
        grid.show_grid()
    elif guess == "STUDENTGOVERNMENT":
        grid.make_word("STUDENTGOVERNMENT", "vertical", 3, 3)
        grid.show_grid()
    elif guess == "ENGINEERING":
        grid.make_word("ENGINEERING", "vertical", 31, 5)
        grid.show_grid()
    elif guess == "TIMELINE":
        grid.make_word("TIMELINE", "vertical", 34, 5)
        grid.show_grid()
    elif guess == "SANSERVINO":
        grid.make_word("SANSERVINO", "vertical", 18, 7)
        grid.show_grid()
    elif guess == "APEXAMS":
        grid.make_word("APEXAMS", "vertical", 13, 8)
        grid.show_grid()
    elif guess == "GUPTA":
        grid.make_word("GUPTA", "vertical", 10, 12)
        grid.show_grid()
    elif guess == "JENN":
        grid.make_word("JENN", "vertical", 25, 14)
        grid.show_grid()
    elif guess == "PYTHON":
        grid.make_word("PYTHON", "vertical", 36, 14)
        grid.show_grid()


guess_right = 0
while guess_right == 0:
  guess_position = input("Enter position: ").upper()
  guess = input("Enter a guess(no spaces): ").upper()
  if guess in word:
    guess_index = word.index(guess)
    check_position = position[guess_index]
    if check_position == guess_position:
      print("you are correct")
      correct_guesses[guess_index:guess_index] = [guess]
      display_word(guess)
  else:
    print("you were wrong")
    guess_right = 0


