import sys
import os


class TestCase:
    def __init__(self):
        self.coins = [1, 5, 10, 25, 50]
        self.nCoins = len(self.coins)
        self.maxCents = 0
        self.changes = []
        for _ in range(self.nCoins + 1):
            self.changes.append([1])

    def solve(self, money):
        previousMaxCents = self.maxCents
        self.__addMissingValues(money)

        for coin in range(1, self.nCoins + 1):
            for cent in range(previousMaxCents + 1, money + 1):
                if self.coins[coin - 1] > cent:
                    self.changes[coin][cent] = self.changes[coin - 1][cent]
                else:
                    self.changes[coin][cent] = self.changes[coin - 1][cent] + \
                        self.changes[coin][cent - self.coins[coin - 1]]

        # for change in self.changes:
        #     print(change)
        # print()

        return self.changes[self.nCoins][money]

    def __addMissingValues(self, money):
        if money > self.maxCents:
            for coin in range(self.nCoins + 1):
                for _ in range(money - self.maxCents + 1):
                    self.changes[coin].append(0)
            self.maxCents = money


def test():
    os.remove('./00674/output.txt')
    file = open('./00674/output.txt', 'a')
    sys.stdin = open('./00674/input.txt')
    testCase = TestCase()

    while True:
        try:
            change = int(input())
            file.write('{n}\n'.format(n=testCase.solve(change)))
        except:
            break


def run():
    testCase = TestCase()

    while True:
        try:
            change = int(input())
            print(testCase.solve(change))
        except:
            break


run()
# test()
