class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        frequency = collections.Counter(words)
        
        total = 0
        middle = 0

        for word in frequency.keys():
            if word[0] == word[1]:
                if frequency[word] % 2 == 1:
                    middle = 1
                
                total += (frequency[word] // 2) * 4
            else:
                reversedWord = word[1] + word[0]
                total += min(frequency[word], frequency[reversedWord]) * 2

        return total + middle * 2