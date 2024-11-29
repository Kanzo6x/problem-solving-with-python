#https://codeforces.com/contest/1/problem/A
import math 
s = list(map(int,input().split()))
print(math.ceil(s[0]/s[2])*math.ceil(s[1]/s[2])) 