from flask_socketio import SocketIO, emit, join_room

class HumanSocket:
    def __init__(self, socket):
        self.socket = socket
        self.game = None
        self.last_board = None

        @socket.on('move_made')
        def move_made(data):
            try:
                move = int(data.get('move'))
                self.game.make_move(move)
                print(f'Socket made move at: {move}')
            except Exception as e:
                print(f'Socket move failed with exception: {e}')
                self.request_move(self.last_board, self.game)

    def request_move(self, b, game):
        print('Requesting move...')
        self.game = game
        self.last_board = b
        self.socket.emit('request_move', {
            'p1': bin(b.b1)[2:][::-1],
            'p2': bin(b.b2)[2:][::-1],
            'turns': b.turns,
        })
