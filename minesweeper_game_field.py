from random import randint
# simulates Minesweeper game field of given size
# cells are set to be open so user can observe entire field


class Cell:

    def __init__(self, around_mines, mine, fl_open=True):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GameField:

    def __init__(self, sz, num_mines):
        self.sz = sz
        self.num_mines = num_mines
        self.initialize()

    def initialize(self):
        self.field = [[Cell(0, False) for _ in range(self.sz)] for _ in range(self.sz)]
        while self.num_mines_checker(self.field) < self.num_mines:
            x, y = randint(0, self.sz - 1), randint(0, self.sz - 1)
            if not self.field[x][y].mine:
                self.field[x][y].mine = True

        area = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.sz):
            for y in range(self.sz):
                if not self.field[x][y].mine:
                    m = sum((self.field[x + i][y + j].mine for i, j in area if
                             0 <= x + i < self.sz and 0 <= y + j < self.sz))
                    self.field[x][y].around_mines = m

    @staticmethod
    def num_mines_checker(f):
        return sum(map(sum, [[i.mine for i in line] for line in f]))

    def show(self):
        for sub in self.field:
            print(*map(lambda x: ("*" if x.mine else x.around_mines) if x.fl_open else "#", sub))


field_game = GameField(8, 10)
field_game.show()
