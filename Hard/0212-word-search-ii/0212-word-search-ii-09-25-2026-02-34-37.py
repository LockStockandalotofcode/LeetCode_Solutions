class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores complete word at the end

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if not board or not words:
            return []
        
        # build trie node from word list
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        results = set()

        def helper(row: int, column: int,parent: TrieNode):
            char = board[row][column]
            curr_node = parent.children[char]

            # termination condition
            if curr_node.word:
                results.add(curr_node.word)
                curr_node.word = None # to prevent duplicate additions

            # mark cell as visited in board
            board[row][column] = "#"

            # explore 4 directional neighbors
            # recurse with current state
            neighbors = [[0,1], [1, 0], [0, -1], [-1, 0]]
            for r, c in neighbors:
                next_r, next_c = row + r, column + c
                if 0 <= next_r < rows and 0 <= next_c < cols:
                    if board[next_r][next_c] in curr_node.children:
                        helper(next_r, next_c, curr_node)
        
            # backtrack: undo all changes
            board[row][column] = char

            # optimization: 
            if not curr_node.children:
                parent.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    helper(r, c, root)

        return list(results)