#소인수분해 프로그램만들기


n=int(input("구할 소인수 분해 값을 입력해라"))
d=2

while d<=n:
    if n % d == 0:
        print(d,"는 ",n,"의 소인수이다")
        n = n // d

    else:
        d = d + 1
