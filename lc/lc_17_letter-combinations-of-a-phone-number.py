# 不用使用回溯，直接用最简单的组合的规则即可

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        t = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if digits == '':
            return []
        pre = ['']
        for digit in digits:
            r = []
            for c in t[digit]:
                for s in pre:
                    r.append(f'{s}{c}')
            pre = r
        return pre

if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations(digits))