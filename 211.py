"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 
"""
from collections import defaultdict

class TrieNode(): 
    def __init__(self): 
        self.children = {}
        self.end_node = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_node = True                
                
    def search(self, word: str) -> bool: 

        #### DFS 
        # def dfs(i,node): 
        #     # print(i,node.end_node)
        #     if i == len(word): 
        #         # print('end here')
        #         # print(node.end_node)
        #         return node.end_node
            
        #     if word[i] not in node.children: 
        #         if word[i] == '.': 
        #             # print('all children', node.children.keys())
        #             for child in node.children: 
        #                 print(child)
        #                 if dfs(i+1,node.children[child]): 
        #                     return True 
        #             return False
        #         else: 
        #             return False
        #     else: 
        #         return dfs(i+1,node.children[word[i]])
        # return dfs(0,self.root)


        ### bfs
        q = [self.root]
        for i,char in enumerate(word): 
            this_q = []
            for node in q: 
                for k,v in node.children.items(): 
                    if char == '.' or char == k: 
                        if i == len(word)-1 and v.end_node: 
                            return True 
                        this_q.append(v)
            q = this_q
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
# print('added')
param_2 = obj.search('b..')
print(param_2)