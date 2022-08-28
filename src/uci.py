
import sys
import re
from multiprocessing.pool import Pool
from random import choice
from typing import Optional

from src import settings
from src.logger import logger, send_uci_msg
from src.game import Game
from src.search import search


Position = str
MovesInStr = list[str]


def remove_line_break(moves):
    new_moves = moves.copy()
    new_moves[-1] = moves[-1][:-1]
    return new_moves

def parse_position_command(string) -> tuple[Position, MovesInStr]:
    if re.match('^position startpos\n', string):
        return ('startpos', [])
    elif re.match('^position startpos moves( \w\d\w\d)+\n', string):
        moves = string.split(' ')[3:]
        moves = remove_line_break(moves)
        return ('startpos', moves)
    elif re.match('^position fen', string):
        tokens = string.split(' ')
        if len(tokens) == 8:
            fen_parts = tokens[2:]
            fen_parts = remove_line_break(fen_parts)
            fen_string = ' '.join(fen_parts)
            return (fen_string, [])
        else:
            raise Exception('Can\'t parse "position" command')
    else:
        raise Exception('Can\'t parse "position" command')

def uci_command_handler():
    send_uci_msg('id name pandinhaEngine')
    send_uci_msg('id author raulpy271')
    send_uci_msg('uciok')

def start_uci_comunication(worker_pool: Optional[Pool] = None):
    current_game: Optional[Game] = None
    for line in sys.stdin:
        try:
            logger.info(f'received command: {line}')
            if line == 'uci\n':
                uci_command_handler()
            elif line == 'isready\n':
                send_uci_msg('readyok')
            elif 'position' in line:
                position, moves = parse_position_command(line)
                logger.info(f'position: "{position}"')
                logger.info(f'moves: "{moves}"')
                if position == 'startpos':
                    raise Exception(f'Command not found: {line}')
                else:
                    current_game = Game.construct_board_from_fen_string(position)
            elif 'go' in line:
                if current_game:
                    move = search(current_game, worker_pool)
                    move_str = current_game.construct_move_str(move)
                    send_uci_msg(f'bestmove {move_str}')
                else:
                    raise Exception('Before send "go" command, set the game using "position" command')
            elif line == 'quit\n':
                break
            else:
                raise Exception(f'Command not found: {line}')
        except Exception as e:
            logger.error(e)

def start_uci_comunication_with_pool_of_process():
    if settings.SEARCH_PARALLEL:
        logger.info('Running in MULTI PROCESS mode')
        with Pool(settings.PROCESSES_NUMBER) as pool:
            start_uci_comunication(pool)
    else:
        logger.info('Running in SINGLE PROCESS mode')
        start_uci_comunication()
