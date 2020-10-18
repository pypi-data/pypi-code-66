class Human:
    def request_move(self, b, game):
        move = self.make_move(b)
        game.make_move(move)

    def make_move(self, b):
        while 1:
            try:
                x = int(input('Type in row: '))
                y = int(input('Type in column: '))
            except Exception as e:
                print(e)
                x = -1
                y = -1

            if b.is_valid_move(x, y):
                return (x, y)
            print('Invalid move. Try again.')
