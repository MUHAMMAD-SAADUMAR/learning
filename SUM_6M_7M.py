"""Harmonic sum over a range of integers.

Computes  1/start + 1/(start+1) + ... + 1/end   (both ends included).
Default range: 6,000,000 to 7,000,000.
"""
import math
import sys
import time

START = 6_000_000
END = 7_000_000


def harmonic_sum(start, end):
    """Return the sum of 1/n for n = start .. end (inclusive)."""
    return math.fsum(1.0 / n for n in range(start, end + 1))


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else START
    end = int(sys.argv[2]) if len(sys.argv) > 2 else END

    t0 = time.perf_counter()
    result = harmonic_sum(start, end)
    elapsed = time.perf_counter() - t0

    print(f"Range        : {start:,} to {end:,} (inclusive)")
    print(f"Terms        : {end - start + 1:,}")
    print(f"Harmonic sum : {result:.15f}")
    print(f"Time taken   : {elapsed:.3f} s")
