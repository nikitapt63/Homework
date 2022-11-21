def array_diff(a, b):
    result = [number for number in a if number not in b]
    return result


def spin_words(sentence: str):
    result = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return " ".join(result)


def find_it(seq):
    result = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return result[0]


