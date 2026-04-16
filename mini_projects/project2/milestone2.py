
stop_words = [
    "i", "me", "my", "mine", "you", "your", "yours",
    "he", "him", "his", "she", "her", "hers",
    "it", "its", "we", "us", "our", "ours", "they", "them", "their", "theirs",

    "the", "a", "an", "and", "or", "but",
    "on", "in", "at", "to", "for", "of", "from", "by", "with", "about", "as",

    "is", "are", "was", "were", "be", "been", "being",
    "do", "does", "did", "doing",
    "have", "has", "had", "having",

    "this", "that", "these", "those",
    "am", "im", "youre", "theyre", "we're",

    "so", "just", "now", "then", "than", "too", "very",
    "can", "could", "should", "would", "will",

    "got", "get", "gets", "getting"
]

adlibs = [
    "yeah", "uh", "ooh", "oh", "woah", "ayy", "ah"
]

def load_file(filename):
    file = open(filename) # open file
    text = file.read()
    return text

def clean_text(text):       # create a function to clean up the text
    text = text.lower()     ## make all lowercase
    
    text = text.replace(",", "") # remove commas
    text = text.replace(".", "") # remove periods
    text = text.replace("!", "") # remove exclamation points
    text = text.replace("?", "") # remove question marks
    text = text.replace("'", "") # remove apostrophes
    text = text.replace('"', "") # remove quotation marks
    text = text.replace("(", "") # remove parentheses
    text = text.replace(")", "") # remove parentheses
    text = text.replace("-", " ") # replace hyphens with spaces (so that hyphenated words are counted as separate words)
    text = text.replace("\n", " ") # replace newlines with spaces (so that words at the end of lines are counted as separate words)
   
    return text


# function to count the number of occurrences of each word in the list of words, and store the counts in a dictionary
def count_words(words, stop_words, adlibs):

    word_count = {}         ## create a dictionary to store the count of each word, with the word as the key and the count as the value

    for word in words:
        if word not in stop_words and word not in adlibs: # filter out stop words and adlibs
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

def top_words(word_count, n):
    sorted_words = sorted(word_count, key=word_count.get, reverse=True) # sort the keys in word_count by their corresponding values, in descending order
    return sorted_words[:n]

def analyze_lyrics(filename, stop_words, adlibs):
    file = load_file(filename)
    text = clean_text(file)
    words = text.split()    ## split the text into a list of words, using whitespace as the separator
    
    word_count = count_words(words, stop_words, adlibs)

    total_words = len(words)
    unique_words = len(word_count)
    vocab_richness = unique_words / total_words
    
    print("Song:", filename)
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Vocabulary richness:", round(vocab_richness, 2))

    print("\nTop 10 words:")
    top_10_words = top_words(word_count, 10)
    for word in top_10_words:
        print(word, ":", word_count[word])

    return top_10_words, vocab_richness

# run analysis on multiple songs
top_10_no_idea, richness_no_idea = analyze_lyrics("mini_projects/project2/no_idea.txt", stop_words, adlibs)
top_10_smoke, richness_after_party = analyze_lyrics("mini_projects/project2/after_party.txt", stop_words, adlibs)


# simple comparison
print("\n--- Comparison ---")
print("No Idea richness:", round(richness_no_idea, 2))
print("After Party richness:", round(richness_after_party, 2))

if richness_no_idea > richness_after_party:
    print("No Idea has more diverse vocabulary.")
else:
    print("After Party has more diverse vocabulary.")