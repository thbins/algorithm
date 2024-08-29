word = input()
check = []

l = len(word)

for n in range(l // 2): 
    if word[n] == word[l - n - 1]: 
        check.append('1')
    else:
        check.append('0')

if '0' not in check:
    print('1') 
else:
    print('0') 