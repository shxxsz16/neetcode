class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        count = 0
        hashset = set()

        for end in range(len(s)):
            while s[end] in hashset:
                hashset.remove(s[start])
                start += 1
            
            hashset.add(s[end])

            count = max(count, end-start+1)

        return count