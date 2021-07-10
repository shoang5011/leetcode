class Solution:
    def merge(self, intervals) :
        intervals.sort(key = lambda x:x[0])
        res = []
        res.append(intervals[0])
        cur = 0
        for i in range(1,len(intervals)): 
            if intervals[i][0] <= res[cur][1]: 
                res[cur][1] = max(res[cur][1],intervals[i][1])
            else: 
                res.append(intervals[i])
                cur+=1
                
        return res

inp = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
print(sol.merge(inp))