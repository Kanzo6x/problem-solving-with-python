#https://codeforces.com/contest/160/problem/A
size =int(input())
array = list(map(int,input().split()))
array.sort()
target =sum(array) // 2
counter,counter2 = 0,0
for i in range(size-1,-1,-1):
    counter += array[i]
    if counter > target:
        counter2+=1
        break
    counter2+=1
print(counter2)

# time complexity is O(n log n)