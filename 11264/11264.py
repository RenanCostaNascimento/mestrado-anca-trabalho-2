import sys
import os


class TestCase:
    def __init__(self, nCoins, strCoins):
        self.coins = []
        self.nCoins = nCoins
        self.coinsWithdrawed = []
        self.uniqueCoins = set([])

        for strCoin in strCoins.split(' '):
            coin = int(strCoin)
            self.coins.append(coin)

    def solve(self):
        amount = 0
        for index, coin in enumerate(self.coins):
            if index == 0 or index == self.nCoins - 1 or amount + coin < self.coins[index + 1]:
                amount += coin

        self.withdraw(amount)
        return len(self.uniqueCoins)

    def withdraw(self, amount):
        if amount == 0:
            return

        highestCoin = self.__findHighestCoinLowerThan(amount, 0, self.nCoins - 1)
        self.coinsWithdrawed.append(highestCoin)
        self.uniqueCoins.add(highestCoin)
        self.withdraw(amount - highestCoin)

    def __findHighestCoinLowerThan(self, amount, lowest, highest):
        if amount >= self.coins[highest]:
            return self.coins[highest]

        if highest - lowest == 1:
            return self.coins[lowest]

        middle = (lowest + highest) // 2

        if self.coins[middle] < amount:
            return self.__findHighestCoinLowerThan(amount, middle, highest)
        elif self.coins[middle] > amount:
            return self.__findHighestCoinLowerThan(amount, lowest, middle)
        else:
            return self.coins[middle]


def test():
    os.remove('./11264/output.txt')
    file = open('./11264/output.txt', 'a')
    sys.stdin = open('./11264/input.txt')
    testCases = []

    nTestCases = int(input())
    for _ in range(nTestCases):
        nCoins = int(input())
        coins = input()
        testCases.append(TestCase(nCoins, coins))

    for testCase in testCases:
        file.write('{n}\n'.format(n=testCase.withdraw(1000)))
        print('coins', testCase.coins)
        print('withdraws', testCase.coinsWithdrawed)
        print('uniques', len(testCase.uniqueCoins))
        print('--')

def run():
    testCases = []

    nTestCases = int(input())
    for _ in range(nTestCases):
        nCoins = int(input())
        coins = input()
        testCases.append(TestCase(nCoins, coins))

    for testCase in testCases:
        print(testCase.solve())


# test()
run()
