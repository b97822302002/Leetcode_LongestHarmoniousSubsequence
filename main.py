class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_dict = dict()
        for i in nums:
            if i in list_dict:
                list_dict[i] += 1
            else:
                list_dict[i] = 1

        list_dict = [(k,list_dict[k]) for k in sorted(list_dict.keys())]
        
        prev_k, prev_v = None, 0
        longest_count = 0
        for k, v in list_dict:
            if prev_k != None and abs(k - prev_k) == 1:
                count = v + prev_v
                if longest_count < count:
                    longest_count = count
            prev_k = k
            prev_v = v

        return longest_count
