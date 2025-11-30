import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:         
        break

    divisors = []    
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    s = sum(divisors)

    if s == n:  
        expression = " + ".join(map(str, divisors))
        print(f"{n} = {expression}")
    else:
        print(f"{n} is NOT perfect.")