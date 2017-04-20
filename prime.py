def primes(number):
    if not isinstance(number, int):
        raise ValueError("Only integers expected as arguments")
    if number == 2:
        return [2]
    elif number < 2:
        return []
    numbers = [x for x in range(3, number + 1, 2)]
    square_root_number = number ** 0.5
    mid = (number + 1) / 2 - 1
    x = 0
    y = 3
    while y <= square_root_number:
        if numbers[x]:
            z = (y * y - 3) // 2
            numbers[z] = 0
            while z < mid:
                numbers[z] = 0
                z += y
        x += 1
        y = 2 * x + 3
    return [2] + [a for a in numbers if a]

