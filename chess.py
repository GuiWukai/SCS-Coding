class Chess:

    def __init__(self):
        self.board = [
            [-4,-2,-3,-5,-6,-3,-2,-4],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [4,2,3,5,6,3,2,4]
        ]

    def print_board(self):
        for i in range (0, 8):
            for j in range (0,8):
                if self.board[i][j] >= 0:
                    print(' ',end='')
                    print(self.board[i][j],end=' ')
                else:
                    print(self.board[i][j], end=' ')
            print()

    def remove_piece(self, x, y):
        self.board[y][x] = 0
        
    def add_piece(self, piece_value, x , y):
        self.board[y][x] = piece_value

    def move_piece(self, x1, y1, x2, y2):
        temp_piece_value = self.board[y1][x1]
        self.remove_piece(x1,y1)
        self.add_piece(temp_piece_value, x2, y2)

x = Chess()
x.move_piece(0,6,0,5)
x.print_board()