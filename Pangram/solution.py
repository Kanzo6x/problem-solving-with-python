#https://codeforces.com/contest/520/problem/A
size = int(input())
uniq_chars = {x.lower() for x in input()}
if len(uniq_chars) == 26:
    print("YES")
else:
    print("NO")
