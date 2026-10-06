import math
import unittest

from lab_python_oop import Rectangle, Circle, Square


class TestFigures(unittest.TestCase):
    def test_rectangle(self):
        r = Rectangle(3, 4, "синий")
        self.assertEqual(r.area(), 12)
        self.assertEqual(r.name(), "Прямоугольник")
        self.assertEqual(r.color.color, "синий")

    def test_circle(self):
        c = Circle(2, "зеленый")
        self.assertAlmostEqual(c.area(), math.pi * 4)
        self.assertEqual(c.name(), "Круг")
        self.assertEqual(c.color.color, "зеленый")

    def test_square(self):
        s = Square(5, "красный")
        self.assertEqual(s.area(), 25)
        self.assertEqual(s.name(), "Квадрат")
        self.assertEqual(s.color.color, "красный")


if __name__ == "__main__":
    unittest.main()
