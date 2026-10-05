import sys
import math


def parse_real(text):
    if text is None:
        return None
    try:
        return float(str(text).strip().replace(",", "."))
    except ValueError:
        return None


def get_coefficient(name, arg_index):
    if len(sys.argv) > arg_index:
        value = parse_real(sys.argv[arg_index])
        if value is not None:
            return value
        print(f"Некорректное значение коэффициента {name} в командной строке: "
              f"{sys.argv[arg_index]!r}")

    while True:
        raw = input(f"Введите коэффициент {name}: ")
        value = parse_real(raw)
        if value is not None:
            return value
        print("Ошибка: коэффициент должен быть действительным числом.")


def solve_biquadratic(a, b, c):
    eps = 1e-12

    # Вырожденный случай: a = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return None
            return []

        t = -c / b

        if t < 0 and not math.isclose(t, 0.0, abs_tol=eps):
            return []

        if math.isclose(t, 0.0, abs_tol=eps):
            return [0.0]

        r = math.sqrt(t)
        return [-r, r]

    # Основной случай: a != 0
    d = b * b - 4 * a * c

    if d < 0 and not math.isclose(d, 0.0, abs_tol=eps):
        return []

    roots = []

    if math.isclose(d, 0.0, abs_tol=eps):
        t = -b / (2 * a)

        if t < 0 and not math.isclose(t, 0.0, abs_tol=eps):
            return []

        if math.isclose(t, 0.0, abs_tol=eps):
            roots.append(0.0)
        else:
            r = math.sqrt(t)
            roots.extend([-r, r])
    else:
        sqrt_d = math.sqrt(d)
        t1 = (-b - sqrt_d) / (2 * a)
        t2 = (-b + sqrt_d) / (2 * a)

        for t in (t1, t2):
            if t < 0 and not math.isclose(t, 0.0, abs_tol=eps):
                continue

            if math.isclose(t, 0.0, abs_tol=eps):
                roots.append(0.0)
            else:
                r = math.sqrt(t)
                roots.extend([-r, r])

    # Сортировка и удаление дубликатов
    roots.sort()
    unique_roots = []
    for x in roots:
        if not unique_roots or not math.isclose(x, unique_roots[-1], abs_tol=1e-9):
            unique_roots.append(x)

    return unique_roots


def main():
    a = get_coefficient("A", 1)
    b = get_coefficient("B", 2)
    c = get_coefficient("C", 3)

    print(f"\nУравнение: {a:g}x^4 + {b:g}x^2 + {c:g} = 0")

    roots = solve_biquadratic(a, b, c)

    if roots is None:
        print("Корней бесконечно много")
    elif not roots:
        print("Действительных корней нет.")
    else:
        print("Действительные корни:")
        for x in roots:
            print(f"x = {x:.10g}")


if __name__ == "__main__":
    main()