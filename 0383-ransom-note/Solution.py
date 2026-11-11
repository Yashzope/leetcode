class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rn = {}
        mg = {}
        for ch in ransomNote:
            rn[ch] = rn.get(ch,0) +1
        for ch in magazine:
            mg[ch] = mg.get(ch,0) +1
        for k,v in rn.items():
            if k not in mg or mg[k] < v:
                return False
        return True