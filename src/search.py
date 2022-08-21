
from math import inf
from random import choice

from src import settings
from src.logger import logger, send_uci_msg
from src.board import Move
from src.game import Game
from src.evaluation import eval

def search_value(game: Game, depth: int, alpha: float, beta: float) -> float:
    if depth == 0:
        return eval(game)
    legal_moves = game.get_possible_moves()
    best_valuation: float = 0
    if game.current_player == 'White':
        best_valuation = - inf
        for move in legal_moves:
            best_valuation = max(
                best_valuation,
                search_value(game.execute_move(move), depth - 1, alpha, beta)
            )
            alpha = max(alpha, best_valuation)
            if best_valuation >= beta:
                break
    else:
        best_valuation = inf
        for move in legal_moves:
            best_valuation = min(
                best_valuation,
                search_value(game.execute_move(move), depth - 1, alpha, beta)
            )
            beta = min(beta, best_valuation)
            if best_valuation <= alpha:
                break
    return best_valuation

def search(game: Game) -> Move:
    alpha = -inf
    beta = inf
    best_valuation: float = - inf
    best_moves: list[Move] = []
    for legal_move in game.get_possible_moves():
        current_valuation = search_value(game.execute_move(legal_move), settings.DEPTH - 1, alpha, beta)
        logger.info(f'Valuation of the move {game.construct_move_str(legal_move)}: {current_valuation}')
        if current_valuation > best_valuation:
            best_valuation = current_valuation
            best_moves = [legal_move]
        elif current_valuation == best_valuation:
            best_moves.append(legal_move)
    send_uci_msg(f'info depth {settings.DEPTH} score cp {best_valuation}')
    return choice(best_moves)
