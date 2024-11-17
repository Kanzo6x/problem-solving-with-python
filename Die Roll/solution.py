#https://codeforces.com/contest/9/problem/A
string = input()
x , y = int(string.split()[0]) ,int(string.split()[1])
if max(x,y)==1:
    print("1/1")
elif max(x,y)==2:
    print("5/6")
elif max(x,y)==3:
    print("2/3")
elif max(x,y)==4:
    print("1/2")
elif max(x,y)==5:
    print("1/3")
else:
    print("1/6")