import time
import os

a = 10
target_dict = {
    "code": 20404,
    "main": 231
}

print("프로세스 유지 중... PID를 확인해서 외부에서 값을 확인해보세요.")
print("a의 주소:", id(a))
print("target_dict의 주소:", id(target_dict))
print("PID:", os.getpid())

while True:
    time.sleep(1)
