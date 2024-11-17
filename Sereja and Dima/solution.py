#https://codeforces.com/contest/381/problem/A
useless = input()
string = input()
numbers = [int(x) for x in string.split()]
dima,serja =0,0
while not(len(numbers)==0):
    dima += max(numbers[0],numbers[-1])
    numbers.remove(max(numbers[0],numbers[-1]))
    if  len(numbers)==0:
        break
    serja += max(numbers[0],numbers[-1])
    numbers.remove(max(numbers[0],numbers[-1]))
print(dima,serja)

