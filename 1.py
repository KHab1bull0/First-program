

# s = input("Input: ")
s = 'sallom'
ans = ''
ls = []

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        print(i)
        for j in range(i+1, len(s)-1):      
            if s[j] != s[j+1]:
                ans += s[j]
                if j+1 == len(s)-1:
                    ans += s[j+1]
            else:
                ans += s[j+1]
                break
        ls.append(ans)
        ans = ''
        
print(ls)   
print(max(ls, key=len))