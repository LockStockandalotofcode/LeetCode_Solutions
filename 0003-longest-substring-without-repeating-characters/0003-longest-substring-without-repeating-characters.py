class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        back_ptr, front_ptr = 0, 0
        max_len = 0
        current_chars = set()
        while front_ptr < len(s):
            while s[front_ptr] in current_chars:
                current_chars.discard(s[back_ptr])
                back_ptr += 1
            current_chars.add(s[front_ptr])

            max_len = max(max_len, front_ptr - back_ptr + 1)
            front_ptr += 1

        return max_len