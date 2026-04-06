import math


class Quaternion:
    def __init__(self, s, x, y, z):
        self.s = s
        self.x = x
        self.y = y
        self.z = z

    # Сложение
    def __add__(self, other):
        return Quaternion(
            self.s + other.s,
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # Вычитание
    def __sub__(self, other):
        return Quaternion(
            self.s - other.s,
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # Умножение
    def __mul__(self, other):
        return Quaternion(
            self.s * other.s - self.x * other.x - self.y * other.y - self.z * other.z,
            self.s * other.x + self.x * other.s + self.y * other.z - self.z * other.y,
            self.s * other.y - self.x * other.z + self.y * other.s + self.z * other.x,
            self.s * other.z + self.x * other.y + self.y * other.x + self.z * other.s
        )

    # Сопряженное
    def conj(self):
        return Quaternion(
            self.s,
            - self.x,
            - self.y,
            - self.z
        )

    # Норма
    def norm(self):
        return math.sqrt(self.s ** 2 + self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Нормализация
    def normalize(self):
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError
        return Quaternion(
            self.s / n,
            self.x / n,
            self.y / n,
            self.z / n
        )

    # Обратный кватернион
    def invert(self):
        c = self.conj()
        n = self.norm()
        return Quaternion(
            c.s / n ** 2,
            c.x / n ** 2,
            c.y / n ** 2,
            c.z / n ** 2
        )

    # Поворот
    @staticmethod
    def rotate(vector, angle, axis):
        ax = axis[0]
        ay = axis[1]
        az = axis[2]
        # axis normalization
        length = math.sqrt(ax ** 2 + ay ** 2 + az ** 2)
        ax = ax / length
        ay = ay / length
        az = az / length
        q = Quaternion(
            math.cos(angle / 2),
            ax * math.sin(angle / 2),
            ay * math.sin(angle / 2),
            az * math.sin(angle / 2)
        )
        q_invert = q.conj()
        p = Quaternion(0, vector[0], vector[1], vector[2])
        rotation = q * p * q_invert
        return rotation.x, rotation.y, rotation.z

    # Формат вывода
    def __repr__(self):
        return f"({self.s:.2f}, {self.x:.2f}i, {self.y:.2f}j, {self.z:.2f}k)"

    # Пример использования
if __name__ == "__main__":
    quaternion1 = Quaternion(1, 2, 3, 4)
    quaternion2 = Quaternion(5, 6, 7, 8)
    res1 = quaternion1 + quaternion2
    res2 = quaternion2 - quaternion1
    res3 = quaternion2 * quaternion1
    res4 = quaternion1.conj()
    res5 = quaternion2.norm()
    res6 = quaternion2.normalize()
    res7 = quaternion1.invert()
    vector = (1, 2, 3)
    axis = (0, 0, 5)
    angle = math.radians(45)
    res8 = Quaternion.rotate(vector, angle, axis)
    print(f"Сумма кватернионов: {quaternion1} + {quaternion2} =", res1)
    print(f"Разность кватернионов: {quaternion1} - {quaternion2} =", res2)
    print(f"Произведение кватернионов: {quaternion1} - {quaternion2} =", res3)
    print(f"Сопряженное кватерниона {quaternion1}:", res4)
    print(f"Норма кватерниона {quaternion2}:", res5)
    print(f"Нормализованный кватернион {quaternion2}:", res6)
    print(f"Обратный кватернион {quaternion1}:", res7)
    print("---Поворот---")
    print(f"Вектор:{vector}")
    print(f"Угол:{angle}")
    print(f"Ось вращения:{axis}")
    print(f"Новый вектор:", res8)