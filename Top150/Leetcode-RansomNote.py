from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterNote = Counter(ransomNote)
        counterMagazine = Counter(magazine)

        for key in counterNote.keys():
            if counterNote.get(key) > counterMagazine.get(key,0):
                return False
            
        return True