class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        s = len(sentence)
        sw = len(searchWord)

        l = 0
        r = 0

        sentence_lst = []
        current_word = ""

        for character in sentence:
            if character != " ":
                current_word += character
            if character == " ":
                sentence_lst.append(current_word)
                current_word = ""
        if current_word:
            sentence_lst.append(current_word)

        i = 0
        for word in sentence_lst:
            j = 0
            if len(word) >= sw:
                while j < sw and word[j] == searchWord[j]:
                    j += 1
                    if j == sw:
                        return i + 1
                i += 1
            else:
                i += 1
                    
        return -1

            



        
        