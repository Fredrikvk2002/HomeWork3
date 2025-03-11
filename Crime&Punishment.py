import string


def load_text(file_path):
    """Reads the book content from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().lower()


def clean_text(text):
    """Removes punctuation and splits text into words."""
    punctuation = ",.?!';\":-=(){}"
    for p in punctuation:
        text = text.replace(p, " ")
    return text.split()


def count_unique_words(words):
    """Counts unique words in the text."""
    return len(set(words))


def analyze_books(book1_name, file_path1, book2_name, file_path2):
    """Loads two books from files, processes them, and compares unique word counts."""
    text1 = load_text(file_path1)
    text2 = load_text(file_path2)

    words1 = clean_text(text1)
    words2 = clean_text(text2)

    unique_words1 = count_unique_words(words1)
    unique_words2 = count_unique_words(words2)

    print(f"The book '{book1_name}' contains {unique_words1} unique words.")
    print(f"The book '{book2_name}' contains {unique_words2} unique words.")

    if unique_words1 > unique_words2:
        print(f"'{book1_name}' has more unique words.")
    elif unique_words2 > unique_words1:
        print(f"'{book2_name}' has more unique words.")
    else:
        print("Both books have the same number of unique words.")


if __name__ == "__main__":
    book1_name = "Crime and Punishment"
    file_path1 = "pg2554.txt"
    book2_name = "The Great Gatsby"
    file_path2 = "pg64317.txt"
    analyze_books(book1_name, file_path1, book2_name, file_path2)
