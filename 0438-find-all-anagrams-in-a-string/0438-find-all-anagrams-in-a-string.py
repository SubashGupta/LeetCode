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
        
        # Function to check if two dictionaries are equal
        def compare_dicts(d1, d2):
            for key in d1:
                if key not in d2 or d1[key] != d2[key]:
                    return False
            return True

        window = {}
        while j < n:
            if s[j] in d:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == d[s[j]]:
                    count -= 1
            if j < k + i - 1:
                j += 1
            elif j == k + i - 1:
                if count == 0:
                    op.append(i)
                if s[i] in window:
                    if window[s[i]] == d[s[i]]:
                        count += 1
                    window[s[i]] -= 1
                i += 1
                j += 1
            else:
                if s[i] in window:
                    if window[s[i]] == d[s[i]]:
                        count += 1
                    window[s[i]] -= 1
                if s[j - k] in d:
                    window[s[j - k]] += 1
                    if window[s[j - k]] == d[s[j - k]]:
                        count -= 1
                i += 1
                j += 1
        return op