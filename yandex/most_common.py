# Частый элемент
# Автор решения: Михаил Шушпанов mishush. Задачу решили 50% участников
#
# Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое чаще других встречается в массиве. Ограничение времени: 2 с, ограничение памяти: 256 МБ.
#
# Формат ввода
# В первой строке входных данных записано число n (1 ≤ n ≤ 300 000).
# Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).
#
# Формат вывода
# Выведите единственное число x, наибольшее из чисел, которое чаще других встречается в массиве a.

import collections

n = int(input())
numbers = [int(i) for i in input().split()]

numbers.sort(reverse=True)
counters = collections.Counter(numbers)
max_number, _ = counters.most_common()[0]
print(max_number)

# # serj @ NEWTONE in ~/PycharmProjects/exercises/yandex on git:master x [21:28:08]
# $ time python most_common.py < most_common.txt
# 975336935
# python most_common.py < most_common.txt   0,45s  user 0,08s system 101% cpu 0,529 total
# avg shared (code):         0 KB
# avg unshared (data/stack): 0 KB
# total (sum):               0 KB
# max memory:                53 MB
# page faults from disk:     0
# other page faults:         27540
