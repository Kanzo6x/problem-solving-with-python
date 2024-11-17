#https://codeforces.com/contest/265/problem/A
mona = input()
instructions = input()
ptr1,ptr2 = 0,0
while ptr1!=len(instructions) and ptr2!=len(mona)-1:
    if instructions[ptr1] == mona[ptr2]:
        ptr2+=1
    ptr1+=1
print(ptr2+1)
