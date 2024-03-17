class ChessVar:
    def __init__(self):
        self.__board = self.__setup_board()
        self.__turn = 'white'
        self.__game_state = 'UNFINISHED'
        self.__fairy_pieces = {'white': ['F', 'H'], 'black': ['f', 'h']}
        self.__lost_pieces = {'white': [], 'black': []}
        self.__eligible_fairy_pieces = {'white': [], 'black': []}

    def __setup_board(self):
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def get_game_state(self):
        return self.__game_state

    def make_move(self, move_from, move_to):
        if self.__game_state != 'UNFINISHED':
            return False

        col_from, row_from = ord(move_from[0]) - ord('a'), 8 - int(move_from[1])
        col_to, row_to = ord(move_to[0]) - ord('a'), 8 - int(move_to[1])

        if not self.__is_valid_move(col_from, row_from, col_to, row_to):
            return False

        self.__handle_capture(col_to, row_to, self.__board[row_from][col_from])
        self.__board[row_to][col_to] = self.__board[row_from][col_from]
        self.__board[row_from][col_from] = '.'

        self.__update_game_state()
        self.__toggle_turn()
        return True

    def enter_fairy_piece(self, piece_type, position):
        if self.__game_state != 'UNFINISHED' or piece_type not in self.__fairy_pieces[self.__turn]:
            return False

        col, row = ord(position[0]) - ord('a'), 8 - int(position[1])
        if self.__board[row][col] != '.':
            return False

        if piece_type not in self.__eligible_fairy_pieces[self.__turn]:
            return False

        self.__board[row][col] = piece_type
        self.__fairy_pieces[self.__turn].remove(piece_type)
        self.__eligible_fairy_pieces[self.__turn].remove(piece_type)
        self.__toggle_turn()
        return True

    def __is_valid_move(self, col_from, row_from, col_to, row_to):
        moving_piece = self.__board[row_from][col_from].lower()
        if moving_piece == '.' or (self.__board[row_from][col_from].isupper() != (self.__turn == 'white')):
            return False

        dir_col = col_to - col_from
        dir_row = row_to - row_from
        dist = max(abs(dir_col), abs(dir_row))

        if moving_piece == 'p':
            return self.__is_valid_pawn_move(col_from, row_from, col_to, row_to, dir_col, dir_row, dist)
        elif moving_piece in 'rnkbq':
            if self.__is_valid_piece_move(moving_piece, col_from, row_from, col_to, row_to, dir_col, dir_row, dist):
                return self.__is_path_clear(col_from, row_from, col_to, row_to, moving_piece)
            return False
        elif moving_piece in 'fh':
            return self.__is_valid_fairy_piece_move(moving_piece, col_from, row_from, col_to, row_to, dir_col, dir_row)
        else:
            return False

    # Implement __is_valid_pawn_move, __is_valid_piece_move, __is_valid_fairy_piece_move as previously described

    def __is_path_clear(self, col_from, row_from, col_to, row_to, piece):
        if piece in ['n', 'p']:  # Knights and pawns don't need path clearance
            return True
        dir_col = (col_to - col_from) // max(abs(col_to - col_from), 1)
        dir_row = (row_to - row_from) // max(abs(row_to - row_from), 1)

        cur_col, cur_row = col_from + dir_col, row_from + dir_row
        while cur_col != col_to or cur_row != row_to:
            if self.__board[cur_row][cur_col] != '.':
                return False
            cur_col += dir_col
            cur_row += dir_row
        return True

    def __toggle_turn(self):
        self.__turn = 'black' if self.__turn == 'white' else 'white'

    # Placeholder for the other methods (__is_valid_pawn_move, __is_valid_piece_move, __is_valid_fairy_piece_move)
    # as described previously. Add those method implementations here to complete the class.
