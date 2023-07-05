import ctypes
import struct
from collections import namedtuple

Stats = namedtuple("Stats", ["n", "bytes_before", "bytes_after"])


def encode(n: int) -> tuple[bytearray, Stats]:
    """
    Return a bytearray object of integer *n* encoded as a base 128 variable-
    width integer.

    Based on Google's Protocol Buffer varint encoding.
    """
    if ctypes.c_uint64(n).value != n:
        raise ValueError(f"Expected unsigned long long, instead got {n}")

    src = n

    byte_seq = bytearray()
    while True:
        byte = n & 0x7F

        n >>= 7

        if n > 0:
            byte |= 0x80  # set msb to 1 (continuation bit)
            byte_seq.append(byte)
        else:
            byte_seq.append(byte)
            break
    assert len(byte_seq) <= 10, "Exceeded 10 bytes"

    return byte_seq, Stats(src, len(struct.pack('@Q', src)), len(byte_seq))


def decode(varint: bytearray) -> int:
    """
    Return an integer representation of the bytearray *varint*.

    Based on Google's Protocol Buffer varint encoding.
    """
    n, byte_index = 0, 0
    for byte in varint:
        n += (byte & 0x7F) << (byte_index * 7)
        byte_index += 1

    assert len(struct.pack("@Q", n)) == 8, "Expected 8 bytes"
    return n
