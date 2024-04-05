import sys
sys.set_int_max_str_digits(maxdigits=10000)

def rever(son):
    l = 0
    if len(str(son)) > 640:
        r = len(str(son))-1
        pass
    else:
        r = len(str(son))-1
        son = str(son)
        son = [i for i in son]
        while l <= r:
            son[l], son[r] = son[r], son[l]
            l += 1
            r -= 1
        return int(''.join(son))

s = int(input("Input: "))
count = 0

while 1:
    rev = rever(s)
    if s == rev:
        s = s
        break
    
    count += 1
    s = s + rev

print('count => ', count , '\nson->' , s)