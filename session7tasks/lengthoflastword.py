class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.strip()
        new_text = text.split(" ")
        return len(new_text[-1])

# s="luffy is still joyboy"
# text=s.strip()
# new_text = text.split(" ")
# print(new_text)
# print(new_text[-1])
# print(len(new_text[-1]))       