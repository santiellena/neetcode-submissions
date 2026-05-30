class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            anagram = {}

            for char in string:
                anagram[char] = anagram.get(char, 0) + 1
        
            anagrams[string] = anagram

        saved = set()
        result = []
        for i, string in enumerate(strs): 
            row = []
            if string not in saved:
                saved.add(string)
                row.append(string)

                for j in range(i + 1, len(strs)):
                    if anagrams[string] == anagrams[strs[j]]:
                        row.append(strs[j])
                        saved.add(strs[j])
                    
                
                result.append(row)
        
        return result
                


