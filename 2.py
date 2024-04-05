

s = input("Input: ")
n = len(s)//2

while len(s) % 2 != 0:
    s = s[(n)+1:] + s[:(n)+1]
    break
while n % 2 != 0:
    s = s[n:] + s[:n]
    break
print(s)