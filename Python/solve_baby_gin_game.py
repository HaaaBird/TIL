num = 112233 
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # count값이 3개 이상이면 triplet
        c[i] -= 3 # 요소 삭제
        tri += 1  # 트리플랫 변수 증가
    
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사. 카운트 변수 왼편(작은수)부터 접근하기 때매 뭐 따질거 없음)
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1        
        run += 1
        continue # run 도달하면 컨티뉴
    i += 1 
if run + tri == 2 : print("Baby Gin")
else: print("Lose")

str()