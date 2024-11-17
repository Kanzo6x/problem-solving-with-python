#https://codeforces.com/contest/344/problem/A
size = int(input())
prev_magnet = input()
if size == 1:
    print(1)
else:
    counter = 0
    for i in range(size-1):
        curr_magnet = input()
        if prev_magnet != curr_magnet:
            counter+=1
        prev_magnet = curr_magnet
    print(counter+1)

