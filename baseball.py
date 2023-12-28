p1,p2,p3 = map(int,input().split())
num = [p1,p2,p3]


while True:
    us_num1,us_num2,us_num3 = map(int,input().split())
    us_num = [us_num1,us_num2,us_num3]
    # if num[0] == us_num[0] and num[1] == us_num[1] and num[2] == us_num[2]:
    #     print("{}S".format())

    if num == us_num :
        print("3S")
        print("프로그램 종료")
        break
    elif num != us_num:
        print("아웃")
        pass
    elif num != us_num:
        print("ball")

