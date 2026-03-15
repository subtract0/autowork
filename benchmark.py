from __future__ import annotations

import random
import time

import target


def main() -> None:
    rng = random.Random(42)

    # correctness
    assert target.sort_numbers([3, 1, 2]) == [1, 2, 3]
    assert target.sort_numbers([]) == []
    assert target.sort_numbers([9]) == [9]
    assert target.sort_numbers([4, 4, 1]) == [1, 4, 4]

    # score
    batch = []
    for _ in range(20):
        values = [rng.randint(-10_000, 10_000) for _ in range(5_000)]
        batch.append(values)

    t0 = time.perf_counter()
    for values in batch:
        out = target.sort_numbers(values)
        assert out == sorted(values)
    t1 = time.perf_counter()

    elapsed = t1 - t0
    score = 1.0 / max(elapsed, 1e-9)  # higher is better
    print(f'AI_OPTIMIZER_RESULT={{"passed": true, "score": {score}, "details": "higher is better"}}')


if __name__ == "__main__":
    main()
