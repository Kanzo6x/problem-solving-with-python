#https://codeforces.com/contest/732/problem/A
string = input()
a,b = int(string.split()[0]),int(string.split()[1])
n = 1
while True:
    if (a*n)%10==b or (a*n)%10==0:
        break
    n += 1
print(n)