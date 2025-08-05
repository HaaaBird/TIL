import random

class Pair():
    def __init__(self, deck):
        self.deck = deck
        self.run_set = []
        self.triplet_set = []
        self.baby_gin_set = []

    def check_and_append_deck(self, target_set, new_set):
        if self.deck_check(new_set) is True:
            if self.same_set_check(target_set, new_set) is not True:
                target_set.append(new_set)

    def same_set_check(self, target_set, new_set):
        return new_set in target_set

    def deck_check(self, new_set):
        return set(new_set).issubset(self.deck)

    def run_check(self):
        for card in self.deck:
            # 현재 카드가 맨 앞 요소인 run set
            self.check_and_append_deck(self.run_set, ([card, card+1, card+2]))
            # 현재 카드가 중간에 들어가는 run set 인지
            self.check_and_append_deck(self.run_set, ([card-1, card, card+1]))
            # 현재 카드가 가장 뒤에 있는 run set인지 확인
            self.check_and_append_deck(self.run_set, ([card-2, card-1, card]))

    def triplet_check(self):
        for card in self.deck:
            if self.deck.count(card) >= 3:
                if [card, card, card] not in self.triplet_set: self.triplet_set.append([card, card, card])
    
    def baby_gin_check(self):
        for run in self.run_set:
            temp = self.deck[:]
            for val in run:
                temp.remove(val)
            if temp in self.triplet_set:
                self.baby_gin_set.append([[run],[temp]])

            
if __name__ == "__main__":
    pair = Pair([random.randint(0,9) for _ in range(6)])
    pair.deck = [3, 3, 3, 4, 5, 6]
    print(pair.deck)
    pair.run_check()
    pair.triplet_check()
    pair.baby_gin_check()
    print(pair.run_set)
    print(pair.triplet_set)
    print(pair.baby_gin_set)