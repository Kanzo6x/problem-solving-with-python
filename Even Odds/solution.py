#https://codeforces.com/contest/318/problem/A
string = input()
range_of_numbers,the_index_number = int(string.split()[0]),int(string.split()[1])

if range_of_numbers % 2 == 1 :
    if the_index_number > (range_of_numbers //2 + 1):
        print((the_index_number - (range_of_numbers // 2 + 1)) * 2)
    else:
        print(the_index_number* 2 - 1)
else:
    if the_index_number > (range_of_numbers // 2):
        print((the_index_number - range_of_numbers // 2) * 2)
    else:
        print(the_index_number * 2 - 1)
