class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        word = ""
        result = []
        for i in digits:
            word += str(i)
        num = int(word) +1
        for i in str(num):
            result.append(int(i))
        return result
