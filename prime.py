def primes(n):
    if not isinstance(n, int):
        raise ValueError("Only integers expected")
    if n == 2:
        return [2]
    elif n < 2:
        return []
    numbers = range(3, n + 1, 2)
    root_n = n ** 0.5
    mid = (n + 1) / 2 - 1
    x = 0
    y = 3
    while y <= root_n:
        if numbers[x]:
            z = (y * y - 3) / 2
            numbers[z] = 0
            while z < mid:
                numbers[z] = 0
                z += y
        x += 1
        y = 2 * x + 3
    return [2] + [a for a in numbers if a]

