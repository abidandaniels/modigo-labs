def smart_title_case(sentence):
    # TODO: capitalize each word except connector words (a, an, the, of, in, on, and),
    # unless that connector word is the first word in the sentence
    if not sentence:
        return ""
    connector = {"a", "an", "the", "of", "in", "on", "and"}
    words = sentence.split(" ")
    result = []
    for i, word in enumerate(words):
        lower_word = word.lower()
        if i == 0 or lower_word not in connector:
            result.append(word.capitalize())
        else:
            result.append(lower_word)
    return " ".join(result)