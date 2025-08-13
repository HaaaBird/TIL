import time
import math

n = 1000
memo = [0] * (n+1) # fibo1 하기 전에 구할 크기만큼 memo를 0으로 초기화
memo[0] = 0
memo[1] = 1 # 위 두개는 기본값으로 깔고 간다.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
  
def fibo(num):
    if num < 2:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
def fibo1(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

if __name__ == "__main__":
    print(factorial(5))
    print(fibo(10))
    start_time = time.time()
    a = fibo1(50)
    print(a)
    print(round(start_time - time.time(),6))
    start_time = time.time()
    a = fibo1(85)
    print(a)
    print(round(start_time - time.time(),6))
    


