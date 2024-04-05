with open('3-misol.txt', 'w') as file:
    
    s = input("Input: ")
    file.write(s)
    
    file.close()
    
with open('3-misol.txt', 'r') as file:
    s = file.read()
    gap  = s.split()
    
    print(gap)
    lis = []
    for word in gap:
        count = 0 
        for i in range(len(word)):
            if word[i]  not in word[i+1:]:
                count += 1
        if count == len(word):
            lis.append(word)
            
    for i in range(len(lis)):
        n = len(lis[i]) // 2
        if len(lis[i]) % 2 == 0:
            lis[i] = lis[i][n:] + lis[i][:n]
        else:
            lis[i] = lis[i][(n)+1:] + lis[i][:(n)+1]
            
    print(lis)
        