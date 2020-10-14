import random


pks = [77,67,95,50,-100,5,78,90]

print("영어",pks[0])
print("국어",pks[1])
print("수학",pks[2])
print("과학",pks[3])
print("체육",pks[4])
print("미술",pks[5])
print("음악",pks[6])
print("실과",pks[7])

r = 0

for x in range(8):
    r = r + pks[x]


print("박기서님의 수능 총점수는 ",r,"점입니다")
print("박기서님의 수능 평균점수는 ",r/8,"점입니다")

if r/8 < 80:
    print("바보 인가요?")
else : 
    print("잘하시네요")





print(random.choice(pks))
