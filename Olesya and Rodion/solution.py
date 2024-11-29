#https://codeforces.com/contest/584/problem/A
s = input()
a , b =int(s.split()[0]), int(s.split()[1])
if b != 10:
    print(str(b)*a)
else:
    if a == 1:
        print(-1)
    else:
        print('1',end='')
        print('0'*(a-1))

#time complexity is O(1)