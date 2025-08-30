class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matched_counter = 0 
        for char in t :
            if matched_counter == len(s):
                break
            if char == s[matched_counter]:
                matched_counter+=1

        return matched_counter == len(s)