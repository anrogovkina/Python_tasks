## Кватернионы
Реализация класса кватернионов.

Кватернион имеет вид: 

q = s + xi + yj + zk ,

- где s, x, y, z - действительные числа,
- i, j, k - мнимые единицы.

## Методы
- **add** — сложение
- **sub** — вычитание
- **mul** — умножение
- **conj** — сопряжённый кватернион
- **norm** — норма (модуль)
- **normalize** — нормализация
- **invert** — обратный кватернион
- **rotate** — поворот вектора


## Пример использования
### Создание кватернионов
    quaternion1 = Quaternion(1, 2, 3, 4)
    quaternion2 = Quaternion(5, 6, 7, 8)
### Сложение
    res1 = quaternion1 + quaternion2
### Вычитание
    res2 = quaternion2 - quaternion1
### Умножение
    res3 = quaternion2 * quaternion1
### Сопряженное
    res4 = quaternion1.conj()
### Норма и нормализация
    res5 = quaternion2.norm()
    res6 = quaternion2.normalize()
### Обратный кватернион
    res7 = quaternion1.invert()
### Поворот вектора
    vector = (1, 2, 3)
    axis = (0, 0, 5)
    angle = math.radians(45)
    res8 = Quaternion.rotate(vector, angle, axis)

## Библиотеки
- math

## Запуск программы

```bash
python quaternion.py