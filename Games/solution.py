#https://codeforces.com/contest/268/problem/A
size = int(input())
home,away = [],[]
count = 0
for i in range(size):
    string = input()
    home.append(string.split()[0])
    away.append(string.split()[1])
for i in range(size):
    count += home.count(away[i])
print(count)
