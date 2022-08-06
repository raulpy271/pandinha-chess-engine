
import sys
import re

from src.logger import logger, send_uci_msg

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

def start_uci_comunication():
    current_game = None
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
            elif line == 'quit\n':
                break
            else:
                raise Exception(f'Command not found: {line}')
        except Exception as e:
            logger.error(e)
