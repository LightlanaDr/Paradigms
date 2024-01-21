def sort_list_imperative(numbers: list) -> list:
    """Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки."""
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


def sort_list_declarative(numbers: list) -> list:
    """Написать точно такую же процедуру, но в декларативном стиле"""
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    numbers = [2, 6, 4, 9, 1]
    print("Императивный: ", sort_list_declarative(numbers))
    print("Декларативный: ", sort_list_declarative(numbers))
