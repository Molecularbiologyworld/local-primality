import numpy as np


def extract_windows(mask: np.ndarray, window_size: int = 7):
    """
    Extract sliding windows from a 2D mask.

    Returns:
        X : (n_samples, window_size, window_size)
        y : (n_samples,)  -> center cell label
    """
    if window_size % 2 == 0:
        raise ValueError("Window size must be odd")

    w = window_size // 2
    X = []
    y = []

    for i in range(w, mask.shape[0] - w):
        for j in range(w, mask.shape[1] - w):
            window = mask[i-w:i+w+1, j-w:j+w+1]
            label = mask[i, j]

            X.append(window)
            y.append(label)

    return np.array(X), np.array(y)
