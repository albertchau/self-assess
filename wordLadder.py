__author__ = 'achau1'


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        ladders = self.find_ladders([beginWord], endWord, wordList)
        shortest_length = 10000
        for path in ladders:
            if len(path) < shortest_length:
                shortest_length = len(path)
        rtn = []
        for path in ladders:
            if len(path) == shortest_length:
                rtn.append(path)
        return rtn

    def find_ladders(self, soFarList, endWord, remainingWords):
        if not remainingWords:
            return []
        if self.find_away(soFarList[-1], endWord) == 1:
            return [soFarList + [endWord]]
        rtn = []
        for w in remainingWords:
            if self.find_away(soFarList[-1], w) == 1:
                newRemaining = [r for r in remainingWords if r != w]
                newSoFarList = soFarList + [w]
                ladders = self.find_ladders(newSoFarList, endWord, newRemaining)
                for g in ladders:
                    rtn.append(g)
        return rtn

    def find_away(self, beginWord, endWord):
        if len(beginWord) != len(endWord):
            return 100000
        awayAwayAwayFromHere = 0
        for i in range(len(beginWord)):
            if beginWord[i] != endWord[i]:
                awayAwayAwayFromHere += 1
        return awayAwayAwayFromHere


x = Solution()
for row in x.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]):
    print(row)

