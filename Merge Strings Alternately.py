# String的添加直接在后面相加即可，这题考察的是双指针，时间复杂度是O(m+n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0

        merge = ""

        while i1 < len(word1) and i2 < len(word2):
            merge += word1[i1]
            merge += word2[i2]

            i1 += 1
            i2 += 1

        merge += word1[i1:]
        merge += word2[i2:]

        return merge
