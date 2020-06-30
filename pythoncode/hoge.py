
def add(a,b):#a+b
    return a+b
def double(n):#n*2
    return n*2
def is_even(n):#偶数
    return n % 2 == 0
def max2(a,b):#abの大きいほう
    if a>b:
        return a
    else:
        return b
def max3(a,b,c):
    if a >= b:
        if c >= a:
            return c
        else:
            return a
    elif b > c:
        return b
    else:
        return c
def max_1(a,b,c):#abcの一番大きい
    return max2(max2(a,b),c)
def gpa(score):#scoreに応じてDCBAS判定
    if score <= 59:
        return "D"
    else:
        if score < 70:
            return "C"
        elif score < 80:
            return "B"
        elif score < 90:
            return "A"
        elif score < 100:
            return "S"
def kuku():#九九表示
    for i in range(9):
        for n in range(9):
            print(((i+1)*(n+1)),end=" ")
        print()
def create_row(row):#指定した段の九九
    for col in range(9):
        print(row*(col+1),end = " ")

#print(is_even(3))
#print(max3(12,5,8))
#print(max2(22,8))
#print(gpa(72))
#print(max_1(15,5,8))
#print (list(map(double,[2,3,4])))
#print(kuku())
#print(create_row(12))
#a,b = map(str,input().split())