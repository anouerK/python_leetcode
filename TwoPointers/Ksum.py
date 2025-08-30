class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        maxOperations = 0 
        i = 0
        marked = {}
        for num in nums : 
            if  marked.get(k - num,0)>= 1:
                maxOperations += 1
                marked[k - num] -= 1
            else:
                marked[num]  = marked.get(num,0) + 1
        return maxOperations