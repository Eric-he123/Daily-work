# 从后往前来看，题中说了从前往后按照从大符号到小符号的，那从后往前看就应该是从小符号到大符号，而这样的话4、9的时候就是当前的符号级别小于前一符号级别，就减去当前符号

class Solution:
    def romanToInt(self, s: str) -> int:
        values = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        
        total = 0
        previous = 0

        for c in reversed(s):
            current = values[c]

            if current < previous:
                total -= current
            else:
                total += current

            previous = current
        
        return total
