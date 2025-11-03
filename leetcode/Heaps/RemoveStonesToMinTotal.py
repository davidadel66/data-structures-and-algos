"""
You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the largest integer that is smaller than or equal to x (i.e., rounds x down).
"""


import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        iteration = 0
        maxPiles = [-num for num in piles]
        heapq.heapify(maxPiles)
        
        while iteration < k:
            iteration += 1
            largestPile = abs(heapq.heappop(maxPiles))
            
            heapq.heappush(maxPiles, - (largestPile - math.floor(largestPile/2)))
            
        return -sum(maxPiles) 
