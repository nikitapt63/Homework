from random import randint


def array_diff(a, b):
    result = [number for number in a if number not in b]
    return result


def spin_words(sentence: str):
    result = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return " ".join(result)


def find_it(seq):
    result = list(filter(lambda x: seq.count(x) % 2 != 0, seq))
    return result[0]


def is_square(n):
    return True if n ** 0.5 == int(n ** 0.5) else False


def descending_order(num: int) -> int:
    int_lst_num = list(map(int, str(num)))
    int_lst_num.sort(reverse=True)
    str_lst_num = map(str, int_lst_num)
    return int("".join(str_lst_num))


def move_zeros(lst: list):
    result = [num for num in lst if num != 0]   # [1, 1, 2, 1, 3]
    delta = len(lst) - len(result)  # 2
    for _ in range(1, delta + 1):
        result.append(0)
    return result


from functools import reduce


def digital_root(n):
    if n <= 9:
        return n
    else:
        return digital_root(reduce(lambda x, y: int(x) + int(y), str(n)))





