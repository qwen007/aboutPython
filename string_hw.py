#문자열 실습
#내장함수: 파이썬 안에 자체적으로 내장되어있는 함수

string1="멋쟁이 사자처럼 "
string2="은 좋은 동아리 입니다."
string3="멋쟁이 사자처럼은 사랑스러워"
string4 = "사과,바나나,포도"

#1
print(string1+string2)
#2
print(string1*3)
#3
print(string1[0])
#4
print(string1[3])
#5
print(string1[4:5])
#6
print(len(string1))
#7
print(string3.count('사'))
#8
print(string4.split(','))
#9
print(string4.split(' '))
#10
print("find: ",string3.find('사'))
print("index: ",string3.index('사'))
#11
print("find: ",string3.find('무'))
print("index: ",string3.index('무'))


