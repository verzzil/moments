import random


def __generate_random_value(from_number=0, to_number=1000):
    return random.randint(from_number, to_number)


def __generate_random_positions(from_number=0, to_number=1000000, vars=100):
    result_set = set()
    for count in range(0, vars):
        generated_value = random.randint(from_number, to_number)
        if generated_value in result_set:
            generated_value += 20
        result_set.add(generated_value)
    return result_set

variables = int(input("Введите количество значений для алгоритма Alon-Matias-Szegedy: "))

random_positions = __generate_random_positions(vars=variables)

full_dict = {}

x_dict = {}

i = 0
for i in range(0, 1000000):
    # time.sleep(0.00002)

    current_value = __generate_random_value()
    if i in random_positions:
        if current_value in x_dict:
            i = 0
            while i < len(x_dict.get(current_value)):
                x_dict.get(current_value)[i] += 1
                i += 1
            x_dict[current_value].append(1)
        else:
            x_dict[current_value] = [1]

    if current_value in full_dict:
        full_dict.update({current_value: full_dict.get(current_value) + 1})
    else:
        full_dict.update({current_value: 1})

# print(x_dict)

print("0-th moment: ", len(full_dict))
print("1-th moment: ", sum(full_dict.values()))
print("2-nd moment: ", sum(
    map(
        lambda arr: sum(
            map(lambda elem: 1000000 * (2 * elem - 1), arr)
        ),
        x_dict.values()
    )
) / variables)

# Исследуя данный алгоритм на практике понял, что на больших наборах данных
#   он даёт далеко не точный результат

# test = {
#     "7": [2, 1],
#     "2": [1],
#     "5": [2, 1]
# }

# print(test.values())
#
# print(
# sum(
#     map(
#         lambda arr: sum(
#             map(lambda elem: 7 * (2 * elem - 1), arr)
#         ),
#         test.values()
#     )
# ) / 5)