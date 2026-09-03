# for문
# for (int i = 0; i <= 10; i++)
# for i in iterable 객체


# 0 ~ 4
for i in range(5):
    print(i, end=" ")
    

a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1,6):
    print(i, end=" ")
print()

# 0 ~ 10까지 숫자 중 짝수
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 5 4 3 2 1 거꾸로 출력
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(tot)
    
print(sum(range(1,11)))

s = "hi12!@한글❤️"
for c in s:
    print(c, end=" ")

print(len(s))

#구구단 출력

# 2 * 1 = 2   2 * 2 = 4   ..  2 * 9 = 18
# ..
# 9 * 1 = 9   9 * 2 = 18   ..  9 * 9 = 81

for i in range(2,10):
    for j in range(2, 10):
        print(f"{i} * {j} = {i * j:<5d}", end="")
    print()
else:
    print("End")
