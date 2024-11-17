#https://codeforces.com/contest/791/problem/A
string = input()
limik , bob = int(string.split()[0]),int(string.split()[1])
if limik == bob:
    print(1)
else:
    counter = 0
    while limik<=bob :
        limik *=3
        bob *=2
        counter +=1
    print(counter)
