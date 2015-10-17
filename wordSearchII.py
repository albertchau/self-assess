__author__ = 'achau1'


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rtn = []
        for w in words:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == w[0]:
                        if self.findWord(board, i, j, w, "", []):
                            rtn.append(w)
        return rtn

    def findWord(self, board, i, j, endWord, soFarWord, soFarUsed):
        if soFarWord == endWord:
            return True
        if i >= len(board):
            return False
        if j >= len(board[0]):
            return False
        if [i, j] in soFarUsed:
            return False
        x = len(soFarWord)
        if x >= len(endWord):
            return False
        if board[i][j] != endWord[x]:
            return False
        if self.findWord(board, i + 1, j, endWord, soFarWord + board[i][j], soFarUsed + [i, j]):
            return True
        if self.findWord(board, i - 1, j, endWord, soFarWord + board[i][j], soFarUsed + [i, j]):
            return True
        if self.findWord(board, i, j - 1, endWord, soFarWord + board[i][j], soFarUsed + [i, j]):
            return True
        if self.findWord(board, i, j + 1, endWord, soFarWord + board[i][j], soFarUsed + [i, j]):
            return True
        return False


words = ["oath", "pea", "eat", "rain"]
board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

x = Solution()
print(x.findWords(board, words))
