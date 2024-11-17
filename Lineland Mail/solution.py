#https://codeforces.com/contest/567/problem/A
size = int(input())
string = input()
arr = [int(x) for x in string.split()]
arr2 = []
for i in range(size): # O(n)
    if i == 0:
        arr2.append([abs(arr[0]-arr[1]),abs(arr[0]-arr[size-1])])
    elif i == size-1:
        arr2.append([abs(arr[size-1]-arr[size-2]),abs(arr[size-1]-arr[0])])
    else:
        arr2.append( [ min( abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1])),max( abs(arr[i]-arr[0]),abs(arr[i]-arr[size-1])) ] )
for i in range(size): # O(n)
    print('{0} {1}'.format(arr2[i][0],arr2[i][1]))