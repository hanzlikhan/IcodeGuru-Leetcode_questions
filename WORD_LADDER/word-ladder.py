class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Preprocessing to build the adjacency list
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # Initialize visited set, queue, and result
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            # Iterate through words at current level
            for _ in range(len(q)):
                word = q.popleft()
                # Check if we reached the endWord
                if word == endWord:
                    return res
                # Generate all possible neighbors of current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in nei[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)
            # Increment result for each level of BFS
            res += 1
        
        # If we couldn't reach endWord
        return 0
                       