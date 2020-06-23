# a = int(input("숫자를 입력해주세요! : "))

# if (a>10):
#     print("a가 10 보다 큽니다.")
    
# elif(a==5):
#     print("a는 5입니다.")
# else:
#     print("a는 10이거나 작군요")


# if (a>5):
#     print("a는 5보다 큽니다.")

# if (a>0):
#     print("a는 자연수 입니다.")

# if (a>0):
#     print("a는 양수입니다.")
#     if(a%2==0):
#         print("짝수입니다.")
        
#     else:
#         print("홀수입니다.")
# else:
#     print("a는 음수입니다.")

###### 반복문 ###############

# i = 1

# while i < 1000:
#     print(i)
#     i = i+1
    
    
# for i in range(1000):
#     print("출력값 : ", i)


# tmp_Str = "오늘은날씨가좋은토요일오후입니다."
# for i in range(len(tmp_Str) ):
#     print(tmp_Str[i], "의 인덱스는 : ",i)


# for i in range(1000):
#     print(i)
    

# def forfunction(a):
#     for i in range(a):
#         print(i)
        
# forfunction(5)
# print("*"*100)
# forfunction(10)

# def hellofunction(a):
#     for i in range(a):
#         print("hello")
        
# hellofunction(3)

# def mysum(a,b):
#     c = a+b
#     return c # 함수는 return을 만나는 순간 반화하고 종료된다.
  
    
# print(mysum(5,10))

# for i in [1,2,3,4]:
#     if i==2:
#         continue
#     print(i)



class NS5: # 클래스가 공통으로 가지는 변수
    body="강화합금"
    
    def run(self):
        print("나는 달립니다.")
        
NS5_1 = NS5()
NS5_2 = NS5()


print(NS5_1.body)
        

