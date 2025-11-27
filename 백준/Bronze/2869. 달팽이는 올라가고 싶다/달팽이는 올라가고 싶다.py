import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

up_per_day = A - B

need_before_last = V - A

days_before_last = math.ceil(need_before_last / up_per_day)

answer = days_before_last + 1

print(answer)