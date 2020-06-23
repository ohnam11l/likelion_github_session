## 사용자로 부터 인풋이 들오옴

word1 = input("끝말잇기를 시작합시다 : ") #인풋의 기본값은 str
preword=word1

if (len(word1) == 3):
   
   
    while True:

        word2 = input()
    
        if (len(word2) == 3) and (word2[0] == preword[-1]):
            print("정답입니다.")
            preword=word2
        else:
            print("오답입니다.")
            break
 
    
else:
    print("오답입니다.")


#그 인풋을 받아서 끝자리 음절과
#다음 인풋의 첫 음절이 같아야 통과다


