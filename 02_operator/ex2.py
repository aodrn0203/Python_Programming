# 비트 연산자
a = 5           # 0000 0101
b = 3           # 0000 0011
print(a & b)    # 0000 0001
print(a | b)    # 0000 0111
print(a ^ b)    # 0000 0110
print(a << b)
print(40 >> b)
print(~a)       # 1111 1010 -> 0000 0110

# 멤버쉽 연산자
print("a" in "apple")
print(3 in [1,2,3])

# 삼항 연산자
# int max = a > b ? a : b
a, b = 2, 3
max_num = a if a > b else b
print(max_num)
print("짝수" if a % 2 == 0 else "홀수")

score = 85

print("A" if score % 10 >= 9 else "B" if score % 10 >= 8 else "C" if score % 10 >= 7 else "D")