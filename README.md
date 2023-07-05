## Description
Implementation of the [Base 128 varint](https://protobuf.dev/programming-guides/encoding/#varints) encoding used in protocol buffers.

This is an exercise from the [CS Primer](https://csprimer.com/courses/) Computer System's course.

## Usage
```
$ python3 -m src.varintpy test/maxint.uint64
Stats(n=18446744073709551615, bytes_before=8, bytes_after=10)
OK
```