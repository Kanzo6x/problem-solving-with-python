#https://codeforces.com/contest/766/problem/A
string1 = input()
string2 = input()

if string1 == string2:
    print(-1)
elif len(string1) > len(string2):
    print(len(string1))
else:
    print(len(string2))