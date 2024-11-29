#https://codeforces.com/contest/742/problem/A
n = int(input())
if n == 0:
    print(1)  
else:
    cycle = [6, 8, 4, 2]  
    print(cycle[n % 4])
