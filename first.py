# # a = "hello"
# # b = 'good'
# # #a==hello
# # print(a * 10)
# # print(a[1])
# # print("a의 slicing : ", a[1])
# # print(a[1:3])
# # print(a.replace("l","b"))
# # print(a)

# # mytext = int(input("여기에다 입력하세요 : "))
# # print(type(mytext))
# mylist = list()# 빈 리스트
# mylist2 =[]
# mylist3 = [1,2,3,4]
# mylist4 = ['글자',1,['숫자',5]]
# print(mylist4)
# print(mylist4[2][1])
# print(mylist4[1:])


# #메서드(편리한 기능)

# mylist.append("1")
# mylist.append("2")
# mylist.append("4")
# mylist.append("3")

# # print(mylist)
# # mylist.remove("2")
# # print(mylist)
# # mylist

# mylist.reverse()
# print("역순 :" ,mylist)
# mylist.sort()
# print("오름차순:", mylist)
# print(mylist.count("2"))


# tmp_str = ",".join(mylist)
# print(tmp_str)

# result_list = tmp_str.split(",")
# print(result_list)

# mytuple = ()
# mytuple2 = (1,)
# mytuple3 = (1,2)
# mytuple3 = (1,2,(1,2))
# mytuple4 = (1,2,4)
# mytuple5 = 1,2,5
# mytuple3[0] = 100
# print(mytuple3)

#Dictionary 자료형
mydict = {1: 'hello'}
mydict1 = dict()
mydict2 ={}
mydict3 = {"가":1,"나":"두번째","다":[1,2,3]}

mydict3["라"] = "비어 있으니까 넣자"

print(mydict3.keys())
print(mydict3.items())  #키 벨류를 보여준다.
print(mydict3.values())

print(mydict3["멋직"])