#https://codeforces.com/contest/236/problem/A
string = input()
set1 = {x for x in string}
if len(set1) %2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")