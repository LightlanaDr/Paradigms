def binary_search(string: str, number: int) -> int:
    """Написать программу на любом языке в любой парадигме для
    бинарного поиска. На вход подаётся целочисленный массив и
    число. На выходе - индекс элемента или -1, в случае если искомого
    элемента нет в массиве."""

    my_list = [int(num) for num in string.split(",")]

    left = 0
    right = len(my_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if my_list[mid] == number:
            return mid
        elif my_list[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    string = input("Введите список значений через запятую: ")

    number = int(input("Введите число: "))

    print(binary_search(string, number))
