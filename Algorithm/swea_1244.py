
def swap(rep):
    global max_value
    if rep == max_change:
        local_value = int("".join(cards))
        max_value = max(max_value, local_value)
        return

    for i in range(len(cards ) -1):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            local_value = int("".join(cards))
            if local_value not in visit[rep]:
                visit[rep].add(local_value)
                swap(rep + 1)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for case in range(1, T + 1):
    cards, max_change = input().split()
    cards = list(cards)
    max_change = int(max_change)
    visit = [set() for _ in range(max_change)]
    max_value = 0
    swap(0)
    print(f"#{case} {max_value}")
