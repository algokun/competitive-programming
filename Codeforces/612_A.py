# https://codeforces.com/contest/1286/problem/A
# Author : Mohan 

def findComplexity(numbers: list) -> int:
    complexity = 0
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        if(numbers[i] != numbers[i+1]):
            complexity += 1
    return complexity


def main():
    # geting no. of test cases
    N = int(input())

    # getting n spaced integers and storing them in array
    numbers = [int(n) for n in input().split()]

    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = -1
        else:
            numbers[i] = numbers[i] % 2

    for i in range(len(numbers)):
        if(numbers[i] == -1):
            if i == 0:
                if numbers[i+1] == -1:
                    numbers[i] = 0
                else:
                    numbers[i] = numbers[i+1]

            if numbers[i-1] > numbers[i]:
                numbers[i] = numbers[i-1]

    print(findComplexity(numbers))

if __name__ == "__main__":
    main()
