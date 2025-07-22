start_number = int(input()) 
answer_list = []

for second in range(1, start_number + 1):
    seq = [start_number, second]
    while True:
        next_val = seq[-2] - seq[-1]
        if next_val < 0:
            break
        seq.append(next_val)
    if len(seq) > len(answer_list):
        answer_list = seq

print(len(answer_list))
print(answer_list)
