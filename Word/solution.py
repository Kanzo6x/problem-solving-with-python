#https://codeforces.com/contest/59/problem/A
string = input()
counter1,counter2 = 0,0
for i in string:
    if(i.isupper()):
        counter1 += 1
    else:
        counter2 += 1
if(counter1 > counter2):
    print(string.upper())
else:
    print(string.lower())
