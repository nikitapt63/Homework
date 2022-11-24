import re
import string
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


def camel_case(string: str) -> str:
    string_title = string.title()
    return print(string_title.replace(" ", ""))


def palindromeD_Z(num: int) -> int:
 i = num + 1
 while str(i)[0] != str(i)[-1]:
    i += 1
 return print(i)



def order(array):
  words = [(int(l), w) for w in array.split() for l in w if l.isdigit()]
  words.sort(key=lambda t: t[0])
  return " ".join(t[1] for t in words)


def palin(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n


def line(text):
  text_arr = list(text)
  i = 0
  while i < len(text_arr):
    if text_arr[i] == '-' or text_arr[i] == '_':
      del text_arr[i]
      if i != len(text_arr) - 1 and text_arr[i].isalpha():
        text_arr[i] = text_arr[i].upper()
        i += 1
    else:
      i += 1
  return ''.join(text_arr)


def digit_in_word(word):
    return sorted(word)[0]

# 'is2 Thi1s T4est 3a' -> 'Thi1s is2 3a T4est'

def digit_in_word(word):
    return sorted(word)[0]

print(digit_in_word('Thi1s'))


def sort_for_digit_in_words(str):
    arr = str.split()
    print(arr)
    arr.sort(key=digit_in_word)
    return ' '.join(arr)


print(sort_for_digit_in_words('is2 Thi1s T4est 3a'))