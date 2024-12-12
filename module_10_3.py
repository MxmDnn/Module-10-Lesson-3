import threading
import time
from random import randint


class Bank :
    def __init__(self) :
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self) :
        for i in range(100) :
            v_random = randint(50, 500)
            self.balance += v_random
            print(f'Пополнение : {v_random}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked() :
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100) :
            v_random = randint(50, 500)
            print(f'Запрос на {v_random}.')
            if v_random <= self.balance :
                self.balance -= v_random
                print(f'Снятие {v_random}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
