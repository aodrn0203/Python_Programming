# 사용자 정의 모듈
print("start2:",__name__)
PI = 3.141592

def add(a,b):
    return a+b

# 직접 모듈을 실행한 경우에만 출력
if __name__ == "__main__":
    print(PI)
    print(add(10,20))