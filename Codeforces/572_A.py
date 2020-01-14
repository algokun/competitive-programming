# https://codeforces.com/problemset/problem/1189/A

def isGood(string) -> bool :
    ones = 0
    zeroes = 0
    for i in string:
        if i == '0':
            zeroes += 1
        else:
            ones += 1
    return not ones == zeroes

string = "000111"

print(isGood(string))