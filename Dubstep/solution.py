#https://codeforces.com/contest/208/problem/A
s = input()
text = s.replace('WUB', ' ')  
cleaned_text = " ".join(text.split())   
print(cleaned_text)
