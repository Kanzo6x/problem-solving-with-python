#https://codeforces.com/problemset/problem/71/A

def repeat():
    string = input()
    if(len(string)>10):
        print("{0}{1}{2}".format(string[0],len(string)-2,string[-1]))
    else:
        print(string)

n = int(input())
while not(n==0):
    repeat()
    n -= 1