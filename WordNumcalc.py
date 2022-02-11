allwords = {}
words = []
sums = []
sameVal = {}
valueList = []
sameValue = []

# lettersum() calculates the sum of every word in the txt file


def lettersum(s):
    g = (sum([ord(c)-96 for c in s]))

    allwords[s] = g
    sums.append(g)
    if g % 2 > 0:
        words.append(g)

# odd() prints out words with odd letter sums and the most common letter sum


def odd():
    print("There are {} odd words".format(len(words)))
    print("Most common letter sum is", max(set(sums), key=sums.count))
    same()


def same():
    for value in set(allwords.values()):

        sameVal[value] = ([k for k, v in allwords.items() if v == value])

    # create a dict with words of same values
    for k, v in sameVal.items():

        if len(v) > 1:
            valueList.append(v)
    for k, v in sameVal.items():
        print(k, v)
    # prints Value and list of words with same val


f = open("dictionary.txt")
dictionary = []
text = f.read()
for word in text.split():
    dictionary.append(word.lower())
print("There are a total of", len(dictionary), "words")
# goes trough every for in the dictionary and runs it trought lettersum
for s in dictionary:
    lettersum(s)
odd()
