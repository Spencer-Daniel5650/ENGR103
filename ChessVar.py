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

        moving_piece = self.__board[row_from][col_from]
        if (moving_piece.isupper() and self.__turn != 'white') or (moving_piece.islower() and self.__turn != 'black'):
            return False

        if not self.__is_valid_move(col_from, row_from, col_to, row_to):
            return False

        self.__handle_capture(col_to, row_to, moving_piece)
        self.__board[row_to][col_to] = moving_piece
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
        dir_col = col_to - col_from
        dir_row = row_to - row_from
        dist = max(abs(dir_col), abs(dir_row))

        if moving_piece == 'p':
            return self.__is_valid_pawn_move(col_from, row_from, col_to, row_to, dir_col, dir_row, dist)
        elif moving_piece in 'rnkbq':
            return self.__is_valid_piece_move(moving_piece, col_from, row_from, col_to, row_to, dir_col, dir_row, dist)
        elif moving_piece in 'fh':
            return self.__is_valid_fairy_piece_move(moving_piece, col_from, row_from, col_to, row_to, dir_col, dir_row)
        else:
            return False

    def __is_valid_pawn_move(self, col_from, row_from, col_to, row_to, dir_col, dir_row, dist):
        initial_row = 6 if self.__turn == 'white' else 1
        move_direction = 1 if self.__turn == 'white' else -1
        if col_from == col_to and self.__board[row_to][col_to] == '.':
            if (dist == 1 and dir_row == move_direction) or (
                    dist == 2 and row_from == initial_row and self.__board[row_from + move_direction][col_to] == '.'):
                return True
        elif abs(dir_col) == 1 and dir_row == move_direction and dist == 1:
            if self.__board[row_to][col_to] != '.' and self.__board[row_to][col_to].isupper() != (
                    self.__turn == 'white'):
                return True
        return False

    def __is_valid_piece_move(self, piece, col_from, row_from, col_to, row_to, dir_col, dir_row, dist):
        if piece == 'r' and (dir_col == 0 or dir_row == 0):  # Rook
            return self.__is_path_clear(col_from, row_from, col_to, row_to)
        elif piece == 'b' and abs(dir_col) == abs(dir_row):  # Bishop
            return self.__is_path_clear(col_from, row_from, col_to, row_to)
        elif piece == 'n' and (
                (abs(dir_col) == 2 and abs(dir_row) == 1) or (abs(dir_col) == 1 and abs(dir_row) == 2)):  # Knight
            return True
        elif piece == 'q' and (dir_col == 0 or dir_row == 0 or abs(dir_col) == abs(dir_row)):  # Queen
            return self.__is_path_clear(col_from, row_from, col_to, row_to)
        elif piece == 'k' and max(abs(dir_col), abs(dir_row)) == 1:  # King
            return True
        return False

    def __is_valid_fairy_piece_move(self, piece, col_from, row_from, col_to, row_to, dir_col, dir_row):
        forward_move = dir_row > 0 if self.__turn == 'white' else dir_row < 0
        if piece.lower() == 'f':  # Falcon
            if forward_move and abs(dir_col) == abs(dir_row):  # Moves like a bishop
                return True
            elif not forward_move and (dir_col == 0 or dir_row == 0):  # Moves like a rook
                return True
        elif piece.lower() == 'h':  # Hunter
            if forward_move and (dir_col == 0 or dir_row == 0):  # Moves like a rook
                return True
            elif not forward_move and abs(dir_col) == abs(dir_row):  # Moves like a bishop
                return True
        return False

    def __is_path_clear(self, col_from, row_from, col_to, row_to):
        dir_col = (col_to - col_from) // max(abs(col_to - col_from), 1)
        dir_row = (row_to - row_from) // max(abs(row_to - row_from), 1)

        cur_col, cur_row = col_from + dir_col, row_from + dir_row
        while cur_col != col_to or cur_row != row_to:
            if self.__board[cur_row][cur_col] != '.':
                return False
            cur_col += dir_col
            cur_row += dir_row
        return True

    def __handle_capture(self, col, row, moving_piece):
        captured_piece = self.__board[row][col]
        if captured_piece != '.':
            player = 'white' if captured_piece.islower() else 'black'
            self.__lost_pieces[player].append(captured_piece)
            # This is a placeholder. Implement any specific logic for fairy piece eligibility here.

    def __update_game_state(self):
        white_king_present = black_king_present = False
        for row in self.__board:
            if 'K' in row:
                white_king_present = True
            if 'k' in row:
                black_king_present = True

        if not white_king_present:
            self.__game_state = 'BLACK_WON'
        elif not black_king_present:
            self.__game_state = 'WHITE_WON'
        else:
            self.__game_state = 'UNFINISHED'

    def __toggle_turn(self):
        self.__turn = 'black' if self.__turn == 'white' else 'white'
