class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        op = []
        if len(p) > len(s):
            return op
        d = {}
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        i = 0
        j = 0
        count = len(d)
        n = len(s)
        k = len(p)
        match_count = 0

        # Initialize the sliding window
        window = {}
        for j in range(n):
            if s[j] in d:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == d[s[j]]:
                    match_count += 1
            
            if j >= k:
                if s[i] in d:
                    window[s[i]] -= 1
                    if window[s[i]] == d[s[i]] - 1:
                        match_count -= 1
                i += 1
            
            if match_count == count:
                op.append(i)
        
        return op
