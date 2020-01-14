def findMin(numbers):
    min = 9999
    minIndex = 0

    for i in range(len(numbers)):
        if(numbers[i] == min):
            break

        if(numbers[i] < min):
            min = numbers[i]
            minIndex = i

    return minIndex


def findMax(numbers) -> int:
    max = 0
    maxIndex = 0
    for i in range(len(numbers)):
        if(numbers[i] > max):
            max = numbers[i]
            maxIndex = i
    return maxIndex


def main():
    r, c = input().split()
    r, c = int(r), int(c)

    matrix = []
    flag = 0

    for i in range(r):
        matrix.append([int(n) for n in input().split()])

    for i in range(r):
        minIndex = findMin(matrix[i])
        minElement = matrix[i][minIndex]
        maxElement = 0

        for j in range(r):
            if(matrix[j][minIndex] > maxElement):
                maxElement = matrix[j][minIndex]

        if(minElement == maxElement):
            flag = 1
            print(minElement)
            break

    if flag == 0:
        print("GUESS")


if __name__ == "__main__":
    main()
