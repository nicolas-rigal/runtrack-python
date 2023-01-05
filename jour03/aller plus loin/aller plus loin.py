def reverseword(word):
        ch=""
        for i in range((len(word)) -1, -1, -1):
                ch = ch + word[i]
        return ch

print(reverseword("nikana"))

word=(input('Quel mot voulez vous inverser ?'))
print(reverseword(word))
