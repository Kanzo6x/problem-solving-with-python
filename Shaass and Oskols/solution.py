#https://codeforces.com/contest/294/problem/A
number_of_wires = int(input())
string = input()
birds = [int(x) for x in string.split()]
number_of_shots = int(input())
while number_of_shots != 0:
    string2 = input()
    x,y = int(string2.split()[0])-1,int(string2.split()[1])
    if x-1 >= 0:
        birds[x-1] += y-1
    if x+1 < number_of_wires:
        birds[x+1] += birds[x]-y
    birds[x]=0 
    number_of_shots -= 1
for i in birds:
    print(i)
