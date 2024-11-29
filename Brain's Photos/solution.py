#https://codeforces.com/contest/707/problem/A
s = input()
string =''
for i in range(int(s.split()[0])):
    a = input()
    string+=a
if 'C' in string or 'M' in string or 'Y' in string:
    print('#Color')
else:
    print('#Black&White')