import sys
import os


class TestCase:
    def __init__(self, missiles):
        self.missiles = missiles
        self.maxInterceptions = 0
        self.interceptions = {}

    def solve(self):
        for index, _ in enumerate(self.missiles):
            interceptions = self.interceptMissile(index)
            if interceptions > self.maxInterceptions:
                self.maxInterceptions = interceptions

        return self.maxInterceptions

    def interceptMissile(self, missilePosition):
        if self.interceptions.__contains__(missilePosition):
            return self.interceptions[missilePosition]

        maxInterceptions = 0

        for index in range(missilePosition + 1, len(self.missiles)):
            if self.missiles[index] <= self.missiles[missilePosition]:
                interceptions = self.interceptMissile(index)
                if interceptions > maxInterceptions:
                    maxInterceptions = interceptions

        self.interceptions[missilePosition] = maxInterceptions + 1
        return self.interceptions[missilePosition]


def test():
    os.remove('./00231/output.txt')
    file = open('./00231/output.txt', 'a')
    sys.stdin = open('./00231/input.txt')
    testCases = []

    while True:
        missiles = []
        missile = int(input())
        if missile == -1:
            break
        missiles.append(missile)

        while True:
            missile = int(input())
            if missile == -1:
                testCases.append(TestCase(missiles))
                break
            missiles.append(missile)

    for index, testCase in enumerate(testCases):
        file.write('Test #{n}:\n'.format(n=index + 1))
        file.write('  maximum possible interceptions: {n}\n'.format(
            n=testCase.solve()))
        if index != len(testCases) - 1:
            file.write('\n')


def run():
    testCases = []

    while True:
        missiles = []
        missile = int(input())
        if missile == -1:
            break
        missiles.append(missile)

        while True:
            missile = int(input())
            if missile == -1:
                testCases.append(TestCase(missiles))
                break
            missiles.append(missile)

    for index, testCase in enumerate(testCases):
        print('Test #{n}:'.format(n=index + 1))
        print('  maximum possible interceptions: {n}'.format(
            n=testCase.solve()))
        if index != len(testCases) - 1:
            print()


run()
# test()
