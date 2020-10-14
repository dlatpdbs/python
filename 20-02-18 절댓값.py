import math
def abc_sigh(a) :
    if a >=0 :
        return a

    else:
        return a * (-1)



def  abs_s(b) :
    c = b * b
    return math.sqrt(c)


print(abc_sigh(-3))
print(abc_sigh(10))
print(abc_sigh(-17))

print(abs_s(-5))
print(abs_s(81))
print(math.sqrt(10))


