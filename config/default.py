import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# default.py 파일 기준으로 projects/myproject/config/default.py에서
# os.path.dirname을 2번 사용했으므로 BASE_DIR에는 projects/myproject가 대입