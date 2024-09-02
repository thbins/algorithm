word = input()
count = 0
i = 0
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

while i < len(word):
    if word[i:i+2] in croatian:  # 2글자 패턴 탐색
        count += 1
        i += 2
    elif word[i:i+3] == "dz=":   # 3글자 패턴 탐색 (dz=)
        count += 1
        i += 3
    else:  # 패턴이 아닌 경우
        count += 1
        i += 1

print(count)