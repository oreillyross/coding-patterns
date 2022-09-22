class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # left pointer 
        l = 0
        # keep a count to freq chars
        dict = {}
        # maintain result
        res = 0
        
        # use right pointer to move along the string
        for r in range(len(s)):
            # add each char to dict and initilize with 0 if not yet in dict
            dict[s[r]] = 1 + dict.get(s[r], 0) 
            # get maxChar count so far
            maxCount = max(dict.values())
            # get the smallest count of chars, check if we are overstepping window
            if ((r - l + 1) - maxCount) > k:
                # move left pointer as we are outside allowed window and remove char from dict
                dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
