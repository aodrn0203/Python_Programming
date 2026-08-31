#변수
a = 2
b = 3
print(a,b)

# a = 2, b = 3
# a = (2, b) = 3

a, b = 2, 3
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

x = y = z = 0

# 변수명 규칙 (C와 동일)
# 숫자로 시작 불가
# 예약어 사용 금지
# 알파벳, 숫자, 특문 _ 만 가능
# 대소문자 구분

# 2name = "뽀로로"
# !name = "크롱"
# class = "루피"

이름 = "에디"
print(이름) # 비권장

student_name = "루피"   # snake_case
sutdentName = "포비"    # camelCase

MAX_SCORE = 100 # 상수는 대문자로

