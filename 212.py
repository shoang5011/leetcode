"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

"""

class TrieNode(): 
    def __init__(self): 
        self.children = {}
        self.end_node = False 

    def addWord(self,word):
        curNode = self
        for char in word: 
            if char not in curNode.children: 
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        curNode.end_node=True

class Solution:
    def findWords(self, board, words): 

        
        # def build_trie(words): 
        #     for word in words: 
        #         node = self.root
        #         for char in word: 
        #             if char not in node.children: 
        #                 node.children[char] = TrieNode()
        #             node = node.children[char]
        # build_trie(words)


        self.root = TrieNode()
        R,C = len(board),len(board[0])
        for word in words: 
            self.root.addWord(word)
        res = set()

        def recursive(r,c,node,word): 
            if r >= R or c >= C or r<0 or c<0 or board[r][c] == '#' or board[r][c] not in node.children : 
                return 
            char = board[r][c]
            board[r][c] = '#'
            node = node.children[char]
            word+=char
            if node.end_node: 
                res.add(word)

            recursive(r+1,c,node,word)
            recursive(r-1,c,node,word)
            recursive(r,c+1,node,word)
            recursive(r,c-1,node,word)

            board[r][c] = char

        for i in range(R): 
            for j in range(C): 
                if board[i][j] in self.root.children: 
                    recursive(i,j,self.root,"")

        return list(res)


sol = Solution()
sol.findWords()
