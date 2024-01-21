def multiplication_table():
    """Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм."""
    n = int(input("Введите число N: "))
    for i in range(1, n + 1):
        print(1, "*", i, "=", i)


if __name__ == '__main__':
    multiplication_table()

# Здесь представлены процедурная и структурная парадигмы.
# Структурная парадигма основана на последовательном исполнении хорошо структурированных “блоков” (цикл for)
# Процедурная парадигма обусловлена офомрлением кода в виде процедуры multiplication_table().