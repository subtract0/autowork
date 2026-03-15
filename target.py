from __future__ import annotations


def sort_numbers(values: list[int]) -> list[int]:
    """Naive starting point for algorithm optimization."""
    data = list(values)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
