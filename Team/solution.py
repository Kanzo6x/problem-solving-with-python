#https://codeforces.com/problemset/problem/231/A
counter = 0
def repeat():
    s = input()
    array = [int(x) for x in s.split()]
    if array.count(1) > 1:
        return True
    else:
        return False

n = int(input())
while not(n==0):
    if repeat():
        counter+=1
    n-=1
print(counter)