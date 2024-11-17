#https://codeforces.com/contest/709/problem/A
string = input()
n,b,d = int(string.split()[0]),int(string.split()[1]),int(string.split()[2])
string = input()
oranges =  [int(x) for x in string.split()]
total = 0
counter = 0
for i in oranges:
    if i <= b:
        total += i
    if total > d:
        counter+=1
        total = 0
print(counter)
