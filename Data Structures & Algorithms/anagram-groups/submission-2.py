class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            key = [0] * 26

            for ch in word:
                index_key = ord(ch) - ord("a")

                key[index_key] += 1

            seen[tuple(key)].append(word)

        return list(seen.values())
            



       


