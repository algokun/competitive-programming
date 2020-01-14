def main():
    # getting n spaced integers and storing them in array
    numbers = [int(n) for n in input().split()]

    complexity = 0

    for i in range(len(numbers)):
        if numbers[i] == 1:
            if i == len(numbers) - 1:
                break

            numbers[i] = 0
            numbers[i+1] = 1
            complexity += 1

    print(complexity + 1, numbers)


if __name__ == "__main__":
    main()
