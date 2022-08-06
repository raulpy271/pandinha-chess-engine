
LIST_OF_POSSIBLE_PIECES_CHAR = ('p', 'b', 'n', 'r', 'q', 'k', 'P', 'B', 'N', 'R', 'Q', 'K')


def parse_line_piece_placement(line) -> list[int]:
    pieces = []
    for char in line:
        if char.isdigit() and char != '0':
            empty_squares = int(char)
            pieces.extend([0] * empty_squares)
        elif char in LIST_OF_POSSIBLE_PIECES_CHAR:
            pieces.append(ord(char))
        else:
            raise Exception(f'String not in FEN format: {line}')
    return pieces

def parse_piece_placement(pieces_str) -> list[int]:
    lines = pieces_str.split('/')
    pieces = []
    if len(lines) == 8:
        for line in reversed(lines):
            pieces.extend(
                parse_line_piece_placement(line)
            )
        return pieces
    else:
        raise Exception(f'String not in FEN format: {pieces_str}')
