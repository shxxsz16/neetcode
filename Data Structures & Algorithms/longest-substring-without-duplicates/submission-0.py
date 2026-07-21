class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 : return 0

        start,end = 0,0
        count = 1
        hashset = set()
        for i in range(len(s)):
            if s[i] in hashset:
                while s[start] != s[i]:
                    hashset.remove(s[start])
                    start += 1

                start += 1
                end += 1

            else:
                hashset.add(s[i])
                end += 1

            count = max(count, end - start)

        return count