
from src.board import BlackBishop, BlackKing, BlackKnight, BlackQueen, BlackRook, Board, Piece, Player, WhiteBishop, WhiteKnight, WhitePieces, BlackPieces, Move, EmptySquare, BlackPawn, WhitePawn, WhiteQueen, WhiteRook
from src.movements.rook import get_all_rook_moves
from src.movements.pawn import get_all_pawn_moves
from src.movements.bishop import get_all_bishop_moves
from src.movements.queen import get_all_queen_moves
from src.movements.knight import get_all_knight_moves


class Game(Board):
    def __init__(self, player: Player = 'White'):
        super().__init__(player)

    def _get_pieces_of_the_current_player(self) -> list[int]:
        pieces = []
        if self.current_player == 'White':
            is_current_player_piece = lambda piece: piece in WhitePieces
        else:
            is_current_player_piece = lambda piece: piece in BlackPieces
        for i, piece in enumerate(self.squares):
            if is_current_player_piece(piece):
                pieces.append(i)
        return pieces

    def get_possible_moves_of_this_piece(self, pieces_type: list[Piece], all_pieces: list[int], function_that_create_movements_of_single_piece) -> list[Move]:
        moves = []
        pieces_index = filter(
            lambda piece_index: self.squares[piece_index] in pieces_type, 
            all_pieces
        )
        for piece_index in pieces_index:
            moves.extend(function_that_create_movements_of_single_piece(self.squares, piece_index, self.current_player))
        return moves

    def get_possible_moves(self) -> list[Move]:
        movements = []
        pieces_to_move = self._get_pieces_of_the_current_player()
        movements.extend(
            self.get_possible_moves_of_this_piece([BlackPawn, WhitePawn], pieces_to_move, get_all_pawn_moves)
        )
        movements.extend(
            self.get_possible_moves_of_this_piece([BlackRook, WhiteRook], pieces_to_move, get_all_rook_moves)
        )
        movements.extend(
            self.get_possible_moves_of_this_piece([BlackBishop, WhiteBishop], pieces_to_move, get_all_bishop_moves)
        )
        movements.extend(
            self.get_possible_moves_of_this_piece([BlackQueen, WhiteQueen], pieces_to_move, get_all_queen_moves)
        )
        movements.extend(
            self.get_possible_moves_of_this_piece([BlackKnight, WhiteKnight], pieces_to_move, get_all_knight_moves)
        )
        return movements
