class Solution(object):
    def numSpecial(self,mat):
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(row[j] for row in mat) == 1:
                    count += 1
        return count

sol = Solution()
mat = [[0,0,0,0,1,0,0,1,0,0],[0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0]]
print(sol.numSpecial(mat))