with open("story.txt", "r") as storytxt:
    story = storytxt.read()




start = "<"
end = ">"

words = set()
start_of_word = -1

for i, char in enumerate(story):
    if char == start:
        start_of_word = i

    if char == end:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("enter a for " + word + ": ")
    
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])

print(story)

