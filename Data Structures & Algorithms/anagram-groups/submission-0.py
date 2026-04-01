class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        str_dict = {}
        for s in strs:
            character_count = [0] * 26
            for c in s:
                character_count[ord(c) - ord('a')] += 1
            tmp_tuple = tuple(character_count)
            if tmp_tuple not in str_dict:
                str_dict[tmp_tuple] = [s]
            else:
                str_dict[tmp_tuple].append(s)
        return list(str_dict.values())

