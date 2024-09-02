word = input().upper()

frequency = {}

for l in word:
    if l in frequency:
        frequency[l] += 1
    else:
        frequency[l] = 1

max_freq = max(frequency.values())

# most_frequent_letters = [k for k, v in frequency.items() if v == max_freq]
most_frequencies = []

for k, v in frequency.items():
    if v == max_freq:
        most_frequencies.append(k)

# 가장 많이 등장한 알파벳이 여러 개라면 '?'를 출력
if len(most_frequencies) > 1:
    print('?')
else:
    print(most_frequencies[0])
