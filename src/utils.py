
def decode_ascii_char(value_integer: int) -> str:
    return str(bytes([value_integer]), 'ascii')
