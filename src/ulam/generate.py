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
    spiral[y, x] = 1

    num = 2
    step = 1

    while num <= size * size:
        # Move right
        for _ in range(step):
            x += 1
            if 0 <= x < size and 0 <= y < size:
                spiral[y, x] = num
                num += 1

        # Move down
        for _ in range(step):
            y += 1
            if 0 <= x < size and 0 <= y < size:
                spiral[y, x] = num
                num += 1

        step += 1

        # Move left
        for _ in range(step):
            x -= 1
            if 0 <= x < size and 0 <= y < size:
                spiral[y, x] = num
                num += 1

        # Move up
        for _ in range(step):
            y -= 1
            if 0 <= x < size and 0 <= y < size:
                spiral[y, x] = num
                num += 1

        step += 1

    return spiral


def generate_prime_mask(spiral: np.ndarray) -> np.ndarray:
    """
    Returns a binary mask where primes are 1 and others are 0.
    """
    prime_vectorized = np.vectorize(is_prime)
    return prime_vectorized(spiral).astype(int)


if __name__ == "__main__":
    s = generate_ulam_spiral(7)
    p = generate_prime_mask(s)

    print("ULAM SPIRAL:\n", s)
    print("\nPRIME MASK:\n", p)
