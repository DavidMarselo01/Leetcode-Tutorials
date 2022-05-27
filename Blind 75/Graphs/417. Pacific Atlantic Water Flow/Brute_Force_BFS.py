#This will give you a Time Limit Exceeded on Leetcode
#But this is a correct Brute Force Solution, you can try it with various examples from
#Leetcode and it works
#Test it in your IDE with the long example I gave at the end

from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        num_row, num_col = len(heights), len(heights[0])
        
        def get_neighbors(node):
            r,c = node
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, -1, 0, 1]
            
            for i in range(len(delta_row)):
                row = r + delta_row[i]
                col = c + delta_col[i]
                if row in range(num_row) and col in range(num_col):
                    yield (row, col)
        
        def bfs(start):
            reached_atlantic = False
            reached_pacific = False
            queu = deque([start])
            visited = set([start])
            while queu:
                node = queu.popleft()
                node_row, node_col = node 
                if node_row == 0 or node_col == 0:
                    reached_pacific = True
                if node_row == num_row - 1 or node_col == num_col -1:
                    reached_atlantic = True
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    r,c = neighbor
                    if heights[node_row][node_col] >= heights[r][c]:
                        queu.append((r,c))
                visited.add(node)
            return reached_atlantic and reached_pacific
                    
        result = []
        for row in range(num_row):
            for col in range(num_col):
                if bfs((row, col)):
                    result.append([row, col])
                    
        return result


testcase = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,18],
[63,120,121,122,123,124,125,126,127,128,129,130,131,132,133,80,19],
[62,119,168,169,170,171,172,173,174,175,176,177,178,179,134,81,20],
[61,118,167,208,209,210,211,212,213,214,215,216,217,180,135,82,21],
[60,117,166,207,240,241,242,243,244,245,246,247,218,181,136,83,22],
[59,116,165,206,239,264,265,266,267,268,269,248,219,182,137,84,23],
[58,115,164,205,238,263,280,281,282,283,270,249,220,183,138,85,24],
[57,114,163,204,237,262,279,288,289,284,271,250,221,184,139,86,25],
[56,113,162,203,236,261,278,287,286,285,272,251,222,185,140,87,26],[
    55,112,161,202,235,260,277,276,275,274,273,252,223,186,141,88,27],
    [54,111,160,201,234,259,258,257,256,255,254,253,224,187,142,89,28],
    [53,110,159,200,233,232,231,230,229,228,227,226,225,188,143,90,29],
    [52,109,158,199,198,197,196,195,194,193,192,191,190,189,144,91,30],
    [51,108,157,156,155,154,153,152,151,150,149,148,147,146,145,92,31],
    [50,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,32],
    [49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33]]
s = Solution()
x = s.pacificAtlantic(testcase)
print(x)