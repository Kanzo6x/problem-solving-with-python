#https://codeforces.com/contest/228/problem/A
string = input()
set1= {int(x) for x in string.split()}
print(4 - len(set1))