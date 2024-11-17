#https://codeforces.com/contest/731/problem/A
string = input()
ptr,counter = 'a' ,0
for s in string:
    if abs(ord(s)-ord(ptr)) <= 13:
        counter += int(abs(ord(s)-ord(ptr)))
        ptr = s
    else:
        counter += 26 - abs(ord(s)-ord(ptr))
        ptr = s
print(counter)