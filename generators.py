# numbers  = range(11)
#
# for number in numbers:
#     print(number)


def generate_evens(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i += 1


for number in generate_evens(10):
    print(number)
