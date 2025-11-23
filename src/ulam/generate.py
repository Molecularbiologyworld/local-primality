# ============================================
# Ulam Spiral & Primality Utilities
# ============================================

import numpy as np
from math import sqrt


def is_prime(n: int) -> bool:
    """
    Check if an integer is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_ulam_spiral(size: int) -> np.ndarray:
    """
    Generate an Ulam spiral of odd dimension (size x size)
    with numbers arranged starting from the center.
    """
    if size % 2 == 0:
        raise ValueError("Size must be an odd number")

    spiral = np.zeros((size, size), dtype=int)

    x = y = size // 2
    dx, dy = 0, -1
    num = 1

    for _ in range(size * size):
        if (-size // 2 < x <= size // 2) and (-size // 2 < y <= size // 2):
            spiral[y + size // 2, x + size // 2] = num
            num += 1

        # Change direction
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx

        x += dx
        y += dy

    return spiral


def generate_prime_mask(spiral: np.ndarray) -> np.ndarray:
    """
    Returns a binary mask where primes are 1 and others are 0.
    """
    prime_vectorized = np.vectorize(is_prime)
    return prime_vectorized(spiral).astype(int)


if __name__ == "__main__":
    # Quick sanity check
    s = generate_ulam_spiral(7)
    p = generate_prime_mask(s)

    print("ULAM SPIRAL:\n", s)
    print("\nPRIME MASK:\n", p)
