opposite = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
def get_allow_list_2(dice, idx):
    allow_face = dice.copy()
    allow_face.remove(dice[opposite[idx]])
    allow_face.remove(dice[idx] )
    return allow_face

T = int(input())
first_dice = list(map(int, input().split()))
dices = []
for case in range(T-1):
    dices.append(list(map(int, input().split())))

final_result = 0

for top_idx in range(6):
    now_anser = max(get_allow_list_2(first_dice, top_idx))
    next_bottom_val = first_dice[opposite[top_idx]]
    for dice in dices:
        now_anser += max(get_allow_list_2(dice, dice.index(next_bottom_val)))
        next_bottom_val = dice[opposite[dice.index(next_bottom_val)]]
    if final_result < now_anser:
        final_result = now_anser
print(final_result)