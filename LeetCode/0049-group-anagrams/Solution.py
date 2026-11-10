class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())