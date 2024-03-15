class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        op = []
        if len(p) > len(s):
            return op
        
        # Count characters in the pattern
        pattern_counts = {}
        for char in p:
            pattern_counts[char] = pattern_counts.get(char, 0) + 1
        
        i = 0
        j = 0
        count = len(pattern_counts)
        match_count = 0
        
        # Iterate through the string
        while j < len(s):
            # Update match count
            if s[j] in pattern_counts:
                pattern_counts[s[j]] -= 1
                if pattern_counts[s[j]] == 0:
                    match_count += 1
            
            # Move the window
            if j - i + 1 > len(p):
                if s[i] in pattern_counts:
                    pattern_counts[s[i]] += 1
                    if pattern_counts[s[i]] == 1:
                        match_count -= 1
                i += 1
            
            # Check if anagram found
            if j - i + 1 == len(p):
                if match_count == count:
                    op.append(i)
                
            j += 1
        
        return op
