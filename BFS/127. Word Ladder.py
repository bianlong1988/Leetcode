class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = collections.deque([(1, beginWord)])
        visited = set()
        while q:
            n = len(q)
            for _ in range(n):
                steps, cur_word = q.popleft()
                if cur_word == endWord:
                    return steps
                for i in range(len(cur_word)):
                    for c in string.ascii_lowercase:
                        new_word = cur_word[:i] + c + cur_word[i+1:]
                        if new_word not in visited and new_word in wordset:
                            q.append((steps + 1,new_word))
                            visited.add(new_word)
        return 0
        