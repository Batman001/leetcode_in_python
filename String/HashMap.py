# -*- coding:utf-8 -*-

def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    patterns = " ".join(pattern).split()
    strs = str.split()
    if len(patterns) != len(strs):
        return False

    used_patterns = []
    used_strs = []

    result_dict = {}

    for i in range(len(patterns)):

        if patterns[i] not in set(used_patterns) and strs[i] not in set(used_strs):
            used_patterns.append(patterns[i])
            used_strs.append(strs[i])
            result_dict[patterns[i]] = strs[i]

        elif patterns[i] not in set(used_patterns) and strs[i] in set(used_strs):
            return False
        elif patterns[i] in set(used_patterns) and strs[i] not in set(used_strs):
            return False
        else:
            if result_dict[patterns[i]] == strs[i]:
                pass
            else:
                return False

print(wordPattern("abba","dog cat cat fish"))
