class Cell:
    """Creates a class named Cell to create a cell where a potential letter could be in the crossword"""
    def __init__(self, x, y, is_blank, value=" "):
#Defines all the arguments
        self.x = x
        self.y = y
        self.is_blank = is_blank
#The if statement determines that if the cell is blank then the value of that cell is an asterik.
#  This will be useful later when we print the value of the cell. 
        if self.is_blank:
            self.value = "*"
#If the cell is not blank then the value of the cell is just the value 
        else:
            self.value = value

    def show_cell(self):
        print(self.value, end=" ")

class Grid:
    """This creates a class called Grid to display a grid that will be the base of the crossword"""
    def __init__(self, rows, cols):
    #This defines the dimensions of the grid in terms of rows and columns

        self.grid = []
        for y in range(rows):
            row = []
#This for loop will add cells to the rows and columns to create a grid 
            for x in range(cols):
                row.append(Cell(x, y, True))
            self.grid.append(row)

    def make_word(self, word, direction, x, y):
        """This function will take a given word and depending on the direction increase the position of each letter by one in the x direction or by one in the y direction."""

        for n in range(len(word)):
#If the direction is horizontal then it will increase x by each n value and then display the value so it shows the word in crossword
            if direction == 'horizontal':
                self.grid[y][x+n].value = word[n]
#If the direction is vertical then it will increase y by each n value and then display the value so the word shows vertical in the crossword
            elif direction == 'vertical':
                self.grid[y+n][x].value = word[n]


    def show_grid(self):
        """This function will show the value of the cells in a grid and then print a space and a dotted line to separate the grid from the space where the user enters their guess"""
        for row in self.grid:
            for cell in row:
                cell.show_cell()
            print("")
        print("-"*30)


#This defines the dimension of the crossword which is 20 rows and 46 columns; It then displays the grid
grid = Grid(20, 46)
grid.show_grid()


#The list word lists the different terms used in the crossword which corresponds to the position listed in list position 
#This will let the program to check the index of both lists and if they match then the guess is right at that position
#The list correct_guesses will be list that correct guesses are added to for a final comparison to determine whether the crossword has been solved
word = ["ARNOLD", "SEMIFORMAL", "NOWAKOSKI", "THINKPOSITIVEANDSTAYATTRACTIVE", "GERSTEIN", "FORTHEBRAND", "OMAY", "THEGREATGATSBY", "MAGNETMADNESS", "MAKERSPACE", "AUTOCADCERTIFICATION", "SPEAKEASY", "RELAYFORLIFE", "ALLISON", "STUDENTGOVERNMENT", "ENGINEERING", "TIMELINE", "SANSERVINO", "APEXAMS", "GUPTA", "JENN", "PYTHON"]
position = ["H5", "H6", "H7", "H11", "H13", "H15", "H16", "H19", "H20", "V1", "V2", "V3", "V4", "V5", "V6", "V8", "V9", "V10", "V12", "V14", "V17", "V18"] 
correct_guesses = []

def display_clue():
    """This function displays the clues with the position in front and then clue following. The letter/number combination 
    in the beginning will be the position they enter when they guess"""
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
    """This function checks first to see whether the crossword has been completed. If not then it will 
    check to see what word matches the correct guess of the user and whatever word it matches, it will display
    that word at the correct location."""
    if correct_guesses == word:
        print("Congratulations! You finished!")
    elif guess == "ARNOLD":
#The grid.make_word is from a perviously defined function with the arguments given.  
        grid.make_word("ARNOLD", "horizontal", 40, 2)
#This will display the grid after the word has been added to it. 
        grid.show_grid()
#This will display the clues once more so the user can continue guessing. This is the same format to check the word for all terms. 
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

#This is the main code to take user input and determine if it is a correct guess
#Setting guess_right = 0 helps set up a while loop to let the program run until the crossword is solved
guess_right = 0
#This will display the clues so the user can guess
display_clue()
while guess_right == 0:
#Guess_position defines the position they enter and guess defines the user guess
  guess_position = input("Enter position: ").upper()
  guess = input("Enter a guess(no spaces): ").upper()
#This if statement check to see if the user guess is contained in the list above. If not is prints you're wrong. 
  if guess in word:
#If the guess is in the list then it assigns guess_index the index number associated with the term the user guessed. 
    guess_index = word.index(guess)
#This assigns check_position the position at the same, corresponding index number that was returned previously. 
    check_position = position[guess_index]
#The if statement checks to see if the correct position value at the user guess is the same as the position the user entered to check if the user got the right answer at the right position. 
    if check_position == guess_position:
#If the if statement is true, it means the user is right and prints you are correct. It then appends the correct guess to the correct_guesses list.
      print("you are correct")
      correct_guesses[guess_index:guess_index] = [guess]
#This runs the function to check which word the user guessed and whatever word it was, it will display that word in the right place. 
      display_word(guess)
#This is the else statement from the previous if statement that determined whether the guess was in the word. 
  else:
    print("you were wrong")
    guess_right = 0


