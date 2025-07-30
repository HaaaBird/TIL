class BankAccount:
    interest_rate = 0.02 # 기본 이자율. 클래스 변수

    def __init__(self, owner, balance):
        self.owner = owner # 계좌 소유자
        self.balance = balance # 계좌 잔고
        # 입금
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("돈이 부족해!")
    
    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate
    @staticmethod
    def is_positive(amount):
        return amount > 0


if __name__ == "__main__":
    # 개좌 계설
    alice_acc = BankAccount("Alice", 1000)

    # 입금 및 출금(인스턴스 메서드 호출)
    alice_acc.deposit(500) # 500원 입금. 1500
    alice_acc.withdraw(200) # 출금 1300

    # 잔액 확인
    print(alice_acc.balance) # 1300

    # 이자율 변경
    BankAccount.set_interest_rate(0.05)
    print(BankAccount.interest_rate) # 0.03

    # 잔액이 양수인지 확인(static method)
    print(BankAccount.is_positive(alice_acc.balance)) # True