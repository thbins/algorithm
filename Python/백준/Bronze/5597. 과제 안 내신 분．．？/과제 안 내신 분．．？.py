# 학생이 30명, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 
# 그 중에서 제출 안 한 학생 2명의 출석번호를 구해야 한다.

all_students = []
good_students = []
bed_students = []

for _ in range(28):
    good_students.append(int(input()))

for i in range(30):
    all_students.append(i+1)

    
all_students.sort()
good_students.sort()

for j in all_students:
    if j not in good_students:
        bed_students.append(j)

bed_students.sort()
print(bed_students[0])
print(bed_students[1])