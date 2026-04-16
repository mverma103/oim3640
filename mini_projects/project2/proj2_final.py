import matplotlib.pyplot as plt

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
    "am", "im", "youre", "theyre", "were",

    "so", "just", "now", "then", "than", "too", "very",
    "can", "could", "should", "would", "will",

    "got", "get", "gets", "getting"
]

adlibs = [
    "yeah", "uh", "ooh", "oh", "woah", "ayy", "ah"
]


def load_file(filename):
    file = open(filename)
    text = file.read()
    file.close()
    return text


def clean_text(text):
    text = text.lower()

    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("!", "")
    text = text.replace("?", "")
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("-", " ")
    text = text.replace("\n", " ")

    return text


def count_words(words, stop_words, adlibs):
    word_count = {}

    for word in words:
        if word not in stop_words and word not in adlibs:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


def top_words(word_count, n):
    sorted_words = sorted(word_count, key=word_count.get, reverse=True)
    return sorted_words[:n]


def analyze_lyrics(filename, stop_words, adlibs):
    text = load_file(filename)
    text = clean_text(text)
    words = text.split()

    word_count = count_words(words, stop_words, adlibs)

    total_words = len(words)
    unique_words = len(word_count)
    vocab_richness = unique_words / total_words

    print("\nSong:", filename)
    print("Total words:", total_words)
    print("Unique words:", unique_words)
    print("Vocabulary richness:", round(vocab_richness, 2))
    print("Vocabulary richness means the percentage of unique words in the song.")
    print("A higher value suggests the song uses a wider variety of words.")
    print("\nTop 10 words:")

    top_10_words = top_words(word_count, 10)
    for word in top_10_words:
        print(word, ":", word_count[word])

    return filename, total_words, unique_words, vocab_richness, top_10_words, word_count


def compare_songs(song_results):
    print("\n--- Comparison ---")

    highest_song = song_results[0]

    for song in song_results:
        filename = song[0]
        richness = song[3]
        print(filename, "- Vocabulary richness:", round(richness, 2))

        if richness > highest_song[3]:
            highest_song = song

    print("\nSong with the most diverse vocabulary:")
    print(highest_song[0])


def graph_vocab_richness(song_results):
    song_names = []
    richness_values = []

    for song in song_results:
        song_names.append(song[0])
        richness_values.append(song[3])

    plt.bar(song_names, richness_values)
    plt.title("Vocabulary Richness by Song")
    plt.xlabel("Songs")
    plt.ylabel("Vocabulary Richness")
    plt.xticks(rotation=45)
    plt.show()


def main():
    print("Welcome to the Lyrics Analysis App")
    print("This program analyzes song lyrics by cleaning text, removing stop words and adlibs,")
    print("and comparing vocabulary richness across songs.")

    num_songs = int(input("\nHow many songs would you like to analyze? "))

    song_results = []

    for i in range(num_songs):
        filename = input("Enter the file path for song " + str(i + 1) + ": ")
        result = analyze_lyrics(filename, stop_words, adlibs)
        song_results.append(result)

    if len(song_results) > 1:
        compare_songs(song_results)

    graph_vocab_richness(song_results)


main()