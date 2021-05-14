li=[3,1,'배가',4,'고파요',5,1]
li2=[3, 1, 4, 5, 2]

#1
print(li[2])
#2
print(li[0:2])
#3
print(len(li))
#4
li2.sort()
print(li2)
#5
# sort()로 내림차순 하는 법을 구글링해서 알아보도록 하자! (보너스 과제)
# 여기에 코드를 적어주세요(print문 사용)
li2.sort(reverse=True)
print(li2)
#6
print(li.index("배가"))
#7
print(li.count(1))

