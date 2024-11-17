#https://codeforces.com/contest/443/problem/A
string = input()
set1 = {x for x in string}
set2 = {"{","}"," ",","}
print(len(set1.difference(set2)))
