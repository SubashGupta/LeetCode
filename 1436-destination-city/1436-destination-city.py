class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        for i in paths:
            d[i[0]] = i[1]
        start = paths[0][0]
        while start:
            nexts = d.get(start,0)
            if nexts:
                start = nexts
            else:
                return start
        
                
            
            