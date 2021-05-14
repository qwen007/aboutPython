#1) 85점 이상이면 pass, 85점 이하이면 fail 출력해보자!
score = int(input("점수를 입력하세요: "))
if(score>=85):
     print("pass")
else:
     print("fail")

#2) 친구한테 멋사자인지 물어보고, 멋사자이면 기쁨의 반응을 아니면 시무룩한반응
activity = input("너 동아리 멋쟁이 사자처럼이야?")
if(activity=="응"):
    print("어! 나도 멋사자야!")
else:
    print("아..그래...")

#3)
money = int(input("너 돈 얼마있어? "))
if(money>=50000):
    print("아웃백을 가자!")
elif(money>=10000):
    print("학식 먹으러 가자!")
elif(money>=5000):
    print("컵밥 먹으러 가자!")
elif(money>=1000):
    print("컵라면 먹으러 가자!")
else:
    print("집이나 가자")
