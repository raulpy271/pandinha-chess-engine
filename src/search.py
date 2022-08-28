
from math import inf
from random import choice
from multiprocessing.pool import Pool
from itertools import starmap
from typing import Optional

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

def search_and_get_move(game, move):
    alpha = -inf
    beta = inf
    valuation = search_value(game.execute_move(move), settings.DEPTH - 1, alpha, beta)
    logger.info(f'Valuation of the move {game.construct_move_str(move)}: {valuation}')
    return valuation, move

def search(game: Game, worker_pool: Optional[Pool] = None) -> Move:
    best_moves: list[Move] = []
    best_valuation: float = 0
    pair_game_moves: map[tuple[Game, Move]] = map(
        lambda move: (game, move),
        game.get_possible_moves()
    )
    if worker_pool:
            valuation_and_moves = worker_pool.starmap(search_and_get_move, pair_game_moves)
    else:
        valuation_and_moves = list(starmap(search_and_get_move, pair_game_moves))
    if game.current_player == 'White':
        best_valuation = - inf
        for value, move in valuation_and_moves:
            if value > best_valuation:
                best_valuation = value
                best_moves = [move]
            elif value == best_valuation:
                best_moves.append(move)
    else:
        best_valuation = inf
        for value, move in valuation_and_moves:
            if value < best_valuation:
                best_valuation = value
                best_moves = [move]
            elif value == best_valuation:
                best_moves.append(move)
    send_uci_msg(f'info depth {settings.DEPTH} score cp {best_valuation}')
    return choice(best_moves)
