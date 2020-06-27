class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        ls = len(strs)
        if ls ==0:
            return prefix
        first = strs[0]
        if ls ==1:
            return first
        
        lf = len(first)
        reached_max = False
        for i in range(lf):
            for j in range(1,ls):
                if i > len(strs[j])-1:
                    reached_max = True
                    break
                if first[i] !=strs[j][i]:
                    reched_max = True
                    break
                if j == ls-1:
                    prefix = prefix+first[i]
            if reached_max:
                break
                
        return prefix

c = Solution()
c.longestCommonPrefix(["aca","cba"])