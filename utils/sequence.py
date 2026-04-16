def generate_sequence(n: int):
    result = []
    num = 1

    while len(result) < n:
        result.extend([num] * num)
        num += 1

    return result[:n]


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(generate_sequence(n))