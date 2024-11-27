#https://codeforces.com/contest/469/problem/A
number_of_levels = int(input())
string1 = input().split()
string2 = input().split()
set_of_levels ={int(string1[i]) for i in range(1,len(string1))}
for i in range(1,len(string2)):
    set_of_levels.add(int(string2[i]))
print("I become the guy.") if len(set_of_levels) == number_of_levels else print("Oh, my keyboard!")