# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 5:
        break
else:
    print("End")

nums = [1, 3, 5, 7 , 9]
target = 2

for i in nums:
    if i == target:
        print("찾았다")
        break
else:
    print("못 찾았다")

nums = [1, 3, 5, 7 , 9]
target = 2
i = 0
# found = False

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found.")
        # found = True
        break
    i += 1
else:
    print(f"{target} not found.")

# if not found:
#     print(f"{target} not found.")

# 1 ~ 10까지의 합
i = 1
tot = 0

while i <=10:
    if i % 2 == 1:
        continue
    tot += i
    i += 1
else:
    print(tot)

