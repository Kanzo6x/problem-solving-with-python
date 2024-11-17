#https://codeforces.com/problemset/problem/4/A

def main():
    a = int(input())
    if a % 2 == 0 and not(a==2):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()