#############  구구단 출력 ##############
# for a in range(2,10):
#     print("구구단",a,"단")
#     for b in range(1,10):
#         print(a," x ",b, "=",a*b)

        ######### 한번만 답할수 있는 구구단 게임#########
        
# import random

# a = random.randrange(2,10)
# b = random.randrange(1,10)
# answer = a*b

# print("구구단을 외자 구구단을외자",a, "x",b, "?" )
# c = int(input("입력하세요 : "))

# if (c == answer):
#     print("정답입니다.")
    
# else:
#     print("틀렸습니다.")


        ######### 반복 가능한 구구단 게임#########

import random

def gugudan():
    a = random.randrange(2,10)
    b = random.randrange(1,10)
    answer = a*b
    print("구구단을 외자 구구단을외자",a, "x",b, "?" )
    input_value = int(input("입력하세요 : "))

    if (input_value == answer):
        print("정답입니다.")
        return True
    
    else:
        print("틀렸습니다.")
        return False
        
while True:
    gogo = gugudan()
    
    if (gogo== False):
        break
    