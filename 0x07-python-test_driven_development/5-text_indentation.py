#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on ., ?, and :
    sentences = text.split(".")
    for sentence in sentences:
        questions = sentence.split("?")
        for question in questions:
            colons = question.split(":")
            for colon in colons:
                # Remove leading and trailing spaces
                colon = colon.strip()
                if colon:
                    print(colon)
        print("\n")  # Add two new lines after each sentence
