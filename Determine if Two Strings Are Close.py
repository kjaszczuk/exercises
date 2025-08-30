class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # hmap1 = {}
        # hmap2 = {}
        # for i in word1:
        #     if i in hmap1:
        #         hmap1[i] += 1
        #     else:
        #         hmap1[i] = 1
        # for i in word2:
        #     if i in hmap2:
        #         hmap2[i] += 1
        #     else:
        #         hmap2[i] = 1
        # return hmap1.keys() == hmap2.keys() and sorted(hmap1.values()) == sorted(hmap2.values())
        if len(word1) != len(word2):
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if counter1.keys() != counter2.keys():
            return False
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True
