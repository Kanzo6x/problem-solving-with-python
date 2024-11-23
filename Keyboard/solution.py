#https://codeforces.com/contest/474/problem/A
keywords = ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]
direction = input()
string = input()
result = []

for char in string:
    for row in keywords:
        if char in row:
            shift = -1 if direction == 'R' else 1
            new_index = row.index(char) + shift
            result.append(row[new_index])
            break

output = ''.join(result)
print(output)