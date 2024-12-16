"""Практическая ВВПД 5"""
ITERATIONS = 100

def maclaurin_ln1(x: float) -> float:
    """
    Вычисляет значение ln(1-x) с помощью ряда Маклорена.

    Аргументы:
        x (float): Значение переменной x. Граничные значения: -1 < x <= 1.

    Возвращаемое значение:
        float: Приближённое значение ln(1-x).
    """
    if not (-1 < x <= 1):
        raise ValueError("x должен быть в пределах -1 < x <= 1")

    result = 0.0
    for n in range(1, ITERATIONS + 1):
        result -= (x ** n) / n
    return result

def maclaurin_arctg(x: float) -> float:
    """
    Вычисляет значение arctg(x) с помощью ряда Маклорена.

    Аргументы:
        x (float): Значение переменной x. Граничные значения: -1 <= x <= 1.

    Возвращаемое значение:
        float: Приближённое значение arctg(x).
    """
    if not (-1 <= x <= 1):
        raise ValueError("x должен быть в пределах -1 <= x <= 1")

    result = 0.0
    for n in range(ITERATIONS):
        result += ((-1) ** n * (x ** (2 * n + 1))) / (2 * n + 1)
    return result

def user_menu():
    """
    Отображает меню для пользователя и позволяет выбрать функцию и ввести x.
    """
    while True:
        print("\nВыберите функцию для вычисления:")
        print("1. ln(1-x)")
        print("2. arctg(x)")
        print("3. Выход")

        choice = input("Введите номер функции (1-3): ")

        match choice:
            case '1':
                try:
                    x = float(input("Введите x (-1 < x <= 1): "))
                    print(f"Результат ln(1-x): {maclaurin_ln1(x)}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            case '2':
                try:
                    x = float(input("Введите x (-1 <= x <= 1): "))
                    print(f"Результат arctg(x): {maclaurin_arctg(x)}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            case '3':
                print("Выход из программы.")
                break
            case _:
                print("Некорректный ввод. Попробуйте снова.")

user_menu()
