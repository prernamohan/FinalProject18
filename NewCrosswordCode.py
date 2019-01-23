
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

def display_clue():
    print(f"""            H5: The teacher who went to Harvard Law
            H6: The main dance at UCVTS hosted by Student Government
            H7: Literature teacher who told us bizzare stories about his life
            H11: The slogan on our Magnet sweatshirts
            H13: The teacher who participates in PowerWheels competition
            H15: Rafalowski slogan that caused many a controversy 
            H16: The IT help for our class who deserves a round of applause for the help he gave
            H19: Our literature midterm essay will be on this book
            H20: Spirit event at the end of the year where the reward is popsicles
            _________________________________________________________________________
            V1: The one room in Magnet that exists nowhere else on campus
            V2: At the end of sophomore year we are forced to take the _______ exam
            V3: Our major junior year project before winter break 
            V4: The event where we spend the night at school 
            V5: Her last name is alphabetically between Festa and Fleishman
            V6: Organization that runs school events
            V8: The reason why we are 'here' but many people do not actually want to pursue this career
            V9: Sanservino's dreaded ________ project
            V10: The class that many Magnet juniors fear
            V12: A week in May that if you don't take certain classes you won't have to experience
            V14: We did a Strawberry DNA lab in this class
            V17: My bitter best friend
            V18: Could be a snake or a language""")
    

def display_word(self):
    if correct_guesses == word:
        print("Congratulations! You finished!")
    elif guess == "ARNOLD": 
        grid.make_word("ARNOLD", "horizontal", 40, 2)
        grid.show_grid()
        display_clue()
    elif guess == "SEMIFORMAL":
        grid.make_word("SEMIFORMAL", "horizontal", 3, 3)
        grid.show_grid()
        display_clue()
    elif guess == "NOWAKOSKI":
          grid.make_word("NOWAKOSKI", "horizontal", 13, 4)
          grid.show_grid()
          display_clue()
    elif guess == "THINKPOSITIVEANDSTAYATTRACTIVE":
        grid.make_word("THINKPOSITIVEANDSTAYATTRACTIVE", "horizontal", 0, 8)
        grid.show_grid()
        display_clue()
    elif guess == "GERSTEIN":
        grid.make_word("GERSTEIN", "horizontal", 33, 8)
        grid.show_grid()
        display_clue()
    elif guess == "FORTHEBRAND":
        grid.make_word("FORTHEBRAND", "horizontal", 29, 12)
        grid.show_grid()
        display_clue()
    elif guess == "OMAY":
        grid.make_word("OMAY", "horizontal", 12, 13)
        grid.show_grid()
        display_clue()
    elif guess == "THEGREATGATSBY":
        grid.make_word("THEGREATGATSBY", "horizontal", 23, 15)
        grid.show_grid()
        display_clue()
    elif guess == "MAGNETMADNESS":
        grid.make_word("MAGNETMADNESS", "horizontal", 3, 16)
        grid.show_grid()
        display_clue()
    elif guess == "MAKERSPACE":
        grid.make_word("MAKERSPACE", "vertical", 25, 0)
        grid.show_grid()
        display_clue()
    elif guess == "AUTOCADCERTIFICATION":
        grid.make_word("AUTOCADCERTIFICATION", "vertical", 29, 0 )
        grid.show_grid()
        display_clue()
    elif guess == "SPEAKEASY":
        grid.make_word("SPEAKEASY", "vertical", 16, 1)
        grid.show_grid()
        display_clue()
    elif guess == "RELAYFORLIFE":
        grid.make_word("RELAYFORLIFE", "vertical", 23, 1)
        grid.show_grid()
        display_clue()
    elif guess == "ALLISON":
        grid.make_word("ALLISON", "vertical", 40, 2)
        grid.show_grid()
        display_clue()
    elif guess == "STUDENTGOVERNMENT":
        grid.make_word("STUDENTGOVERNMENT", "vertical", 3, 3)
        grid.show_grid()
        display_clue()
    elif guess == "ENGINEERING":
        grid.make_word("ENGINEERING", "vertical", 31, 5)
        grid.show_grid()
        display_clue()
    elif guess == "TIMELINE":
        grid.make_word("TIMELINE", "vertical", 34, 5)
        grid.show_grid()
        display_clue()
    elif guess == "SANSERVINO":
        grid.make_word("SANSERVINO", "vertical", 18, 7)
        grid.show_grid()
        display_clue()
    elif guess == "APEXAMS":
        grid.make_word("APEXAMS", "vertical", 13, 8)
        grid.show_grid()
        display_clue()
    elif guess == "GUPTA":
        grid.make_word("GUPTA", "vertical", 10, 12)
        grid.show_grid()
        display_clue()
    elif guess == "JENN":
        grid.make_word("JENN", "vertical", 25, 14)
        grid.show_grid()
        display_clue()
    elif guess == "PYTHON":
        grid.make_word("PYTHON", "vertical", 36, 14)
        grid.show_grid()
        display_clue()


guess_right = 0
display_clue()
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


