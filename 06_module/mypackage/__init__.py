# __init__.py (패키지 초기회 피일)
# 패키지가 로드될 때 실행되는 초기화 파일

# 1. 패키지를 import 할 때 실행되어야하는 초기화 로드 (환경 확인, 설정값 로드)
print("__init__")

# 2. 패키지 메타데이터 버전 설정 (버전, 작성자)
VERSION = "1.0.0"

# 3. 패키지 re-export
# from mypackage.mymath import add        # 절대 import
from .mymath import add                   # 상대 import
