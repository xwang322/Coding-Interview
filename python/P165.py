class Solution(object):
    def compareVersion(self, version1, version2):
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        overlap = max(len(version1_list), len(version2_list))
        for x in range(overlap):
            v1_tok = 0
            if x < len(version1_list):
                v1_tok = int(version1_list[x])
            v2_tok = 0
            if x < len(version2_list):
                v2_tok = int(version2_list[x])
            if v1_tok < v2_tok:
                return -1
            if v1_tok > v2_tok:
                return 1
        return 0