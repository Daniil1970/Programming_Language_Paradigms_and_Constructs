from tabulate import tabulate

from lab_python_oop import Rectangle, Circle, Square

# ЗАМЕНИ N на номер своего варианта по списку группы
N = 9


def main():
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    figures = [rectangle, circle, square]

    print("Информация о фигурах:")
    for figure in figures:
        print(figure)
        print("-" * 50)

    # Вызов внешнего пакета tabulate, установленного через pip
    rows = []
    for figure in figures:
        rows.append([figure.name(), repr(figure)])

    print("\nТаблица, построенная внешним пакетом tabulate:")
    print(tabulate(rows, headers=["Фигура", "Параметры"], tablefmt="grid"))


if __name__ == "__main__":
    main()
