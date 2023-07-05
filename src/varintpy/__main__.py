#!/usr/bin/env python3

import struct
import sys
from typing import List

from .varint import decode, encode


def main(args: List[str]):
    if len(args) < 2 or not args[1]:
        print("Please provide a file name")
        return 1

    file_name = args[1]

    with open(file_name, "rb") as f:
        # Read 8 bytes as big-endian unsigned long long
        n = struct.unpack(">Q", f.read(8))[0]
        encoded_value, stats = encode(n)
        assert decode(encoded_value) == n, f"Failed to encode {n}"
        print(stats)
        print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
