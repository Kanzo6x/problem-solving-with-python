#https://codeforces.com/contest/431/problem/A
string1 = input()
strips = [int(x) for x in string1.split()]
string2 = input()
count = 0
for i in string2:
    count+=strips[int(i)-1]
print(count)