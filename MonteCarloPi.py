import random


def estimate_pi(max_points):
    points = 0
    count = 0

    while points < max_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if (x**2) + (y**2) <= 1:
            count += 1

        points += 1

    result = (4.0 * count) / max_points
    return result


print(estimate_pi(100))
