def array_diff(a, b):
    result = [number for number in a if number not in b]
    return result


def spin_words(sentence: str):
    result = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return " ".join(result)


