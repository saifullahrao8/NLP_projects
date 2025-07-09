def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sample_text = "This is a simple natural language processing project."
    count = word_count(sample_text)
    print(f"Word count: {count}")

