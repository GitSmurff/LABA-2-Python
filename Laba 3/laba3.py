def count_l(word):
        s = sum(c != ' ' for c in word)
        print(word, "-", s)
        return word

for word in input().split():
    count_l(word)

