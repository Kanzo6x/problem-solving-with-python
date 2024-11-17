#https://codeforces.com/contest/2030/problem/A
def solve():
    n = int(input())
    string = input()
    if n == 1:
        return 0
    array = [int(x) for x in string.split()]
    solution = max(array) - min(array) 
    return solution*(n-1)
    

test =int(input())
while test!=0:
    print(solve())
    test-=1