from string_package import reverse_string, capitalize_words, remove_punctuation
from string_package import count_characters, count_words, average_word_length

def main():
    s = input("Enter a sentence: ")

    reversed_s = reverse_string(s)
    capitalized_s = capitalize_words(s)
    cleaned_s = remove_punctuation(s)

    print("\nReversed:", reversed_s)
    print("Capitalized:", capitalized_s)

    print("\nCharacter count (no punctuation):", count_characters(cleaned_s))
    print("Word count:", count_words(cleaned_s))
    print("Average word length:", average_word_length(cleaned_s))

if __name__ == "__main__":
    main()
