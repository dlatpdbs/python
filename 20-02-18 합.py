
def sum_n(a):
    s =0
    for i in range(1,a+1):
        s = s + i
    return s

def sum_q(a):
    return a*(a+1)//2


print(sum_n(10))
print(sum_n(100))

print(sum_q(99))
print(sum_q(100))
