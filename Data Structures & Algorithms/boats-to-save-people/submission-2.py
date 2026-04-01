class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort()
        # two pointer + greedy
        l, r = 0, len(people)-1
        while l <= r:
            # Each boat carries at most two people at the same time
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            count += 1
        
        return count