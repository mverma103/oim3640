
file = open("mini_projects/project2/song_test.txt") # open file
text = file.read()

text = text.lower()     ## make all lowercase
words = text.split()    ## split the text into a list of words, using whitespace as the separator
word_count = {}         ## create a dictionary to store the count of each word, with the word as the key and the count as the value

# function to count the number of occurrences of each word in the list of words, and store the counts in a dictionary
def count_words(words):
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

## find top 10 words
word_count = count_words(words)
sorted_words = sorted(word_count, key=word_count.get, reverse=True) # sort the keys in word_count by their corresponding values, in descending order
top_10_words = sorted_words[:10]

# calculate & print total words and unique words
total_words = len(words)
unique_words = len(word_count)

print("Total words:", total_words)
print("Unique words:", unique_words)

# loop to print the top 10 words and their counts
print("\nTop 10 words:")
for i in range(10):
    word = top_10_words[i]
    count = word_count[word]
    print(word, ":", count)

"""
Notes for next milestone:
- pretty simple and will need more data

- when I ran this code, I get a pretty unfiltered list, which includes common words and adlibs that would need to be filtered
- also, words with punctuation attachted to them are counted as different words, so I would need to filter out the punctuation
- I can create a list of stop words (common words that I want to ignore) and filter out the words in that list from our word count
- I can also filter out adlibs by creating a list of adlibs and either ignoring those words as well or making another analysis out of it
- I can also create a list of words that I want to specifically analyze, such as words related to 
love, heartbreak, etc. and count the occurrences of those words in the lyrics (depending on the genre)

"""