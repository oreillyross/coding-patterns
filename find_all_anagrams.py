from collections import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
	# edge case in case p substring is bigger than s string
        if len(p) > len(s):
            return []
        
	# the below boiler plate sets up two empty hash maps
        pCount, sCount = {}, {}
        # iterate through p and populate both hahs maps with correct counts
        # the below uses the .get() method to ensure a default value can be used
        # if the item at the index in hash does not exist
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        # also setup logic, to initialise the result array, and already add 0 index
        # if the first substring is already an anagram.
        # in python one can directly compare tow hash maps for equality
        res = [0] if pCount == sCount else []
        
        # initialise the left pointer
        l = 0
        # iterate with right pointer and move the window of chars by one each time
        # if the char is 0 remove it from hash to prevent equalit checks failing
        # pCount always stays the same from first initialisation
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
             
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            # finally check the hash is now again same, i.e. new anagram found   
            if sCount == pCount:
                res.append(l)
        
        # return result array with start indexes found
        return res