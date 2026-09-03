# 조건문 : if문, match문

age = 17

if age >= 18:
    print("성년")
else:
    print("미성년")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# match문
grade = "A"

match grade:
    case "A":
        print("우수")
    case "B":
        print("양호")
    case "C" | "D":
        print("보통")
    case _ :               #default
        print("알수없음")