# Function to read a text file and count word occurences
def count_words(filename):
    try:
        word_count = dict()
        with open(filename, "r") as file:
            words_in_file = file.read().split()
            for word in words_in_file:
                # Count the occurrences of each word in the file
                word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except FileNotFoundError:
        print("File not found.")
        return

# Function to format the word count as a list of dictionaries
def format_word_count(word_count):
    result = []
    for word, count in word_count.items():
        result.append({word: count})
    return result

filename = "file.txt"
word_count = count_words(filename)
list_of_dict = format_word_count(word_count)

print(list_of_dict)