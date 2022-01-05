from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        index = -1
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[i] = 0

            else:
                hash_map[i] += 1
                
        return index

s = Solution()
a = "aabb"
print(s.firstUniqChar(a))