#https://codeforces.com/contest/43/problem/A
n = int(input())
dix = {}
for i in range(n):
    s = input()
    if s in dix:
        dix[s] += 1
    else:
        dix[s] = 1

print(dix.get(max(dix)))