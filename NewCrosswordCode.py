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



grid = Grid(6, 6)
grid.show_grid()

class Crossword():
  def __init__(self, word, direction, x, y):
    self.word = word
    self.direction = direction
    self.x = x
    self.y = y


word = ["omay", "juan"]
position = ["H1", "V1"] 
correct_guesses = []
omay = Crossword("omay", "horizontal", 40, 140)
juan = Crossword("juan", "vertical", 40, 160)

  
guess_right = 0
while guess_right == 0:
  guess_position = input("Enter position: ")
  guess = input("Enter a guess: ")
  if guess in word:
    guess_index = word.index(guess)
    check_position = position[guess_index]
    if check_position == guess_position:
      print("you are correct")
      correct_guesses[guess_index:guess_index] = [guess]
      if guess == "omay": 
        grid.make_word("omay", "horizontal", 1, 3)
        grid.show_grid()
      if guess == "juan":
        grid.make_word("juan", "vertical", 3, 1)
        grid.show_grid()
      if correct_guesses == word:
          guess_right = 1
  else:
    print("you were wrong")
    guess_right = 0


