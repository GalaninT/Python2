import doctest


class Matrix:
    def __init__(self, rows: int, cols: int, data: list[float]):
        """
        Создание и подготовка к работе объекта "Матрица"

        :param rows: Количество строк матрицы
        :param cols: Количество столбцов матрицы
        :param data: Элемента матрицы,представленные в виде списка

        Примеры:
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        """
        if not isinstance(rows, int):
            raise TypeError("Количество строк должно быть типа int")
        if rows <= 0:
            raise ValueError("Количество строк должно быть положительным")
        self.rows = rows

        if not isinstance(cols, int):
            raise TypeError("Количество столбцов должно быть типа int")
        if cols <= 0:
            raise ValueError("Количество столбцов должно быть положительным")
        self.cols = cols

        if not isinstance(any(data), (int, float)):
            raise TypeError("Элементы матрицы должны быть типа int или float")
        if len(data) != rows * cols:
            raise ValueError("Количество элементов не соответствует размерам матрицы")
        self.data = data

    def determinant(self) -> float:
        """
        Вычисление определителя матрицы.

        :raise ValueError: Если количество строк не равно количеству столбцов, вызываем ошибку

        :return: Определитель матрицы

        Пример:
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.determinant()
        """
        if self.rows != self.cols:
            raise ValueError("Для вычисления определителя матрица должна быть квадратной")
        ...

    def mult_by_num(self, number: float) -> None:
        """
        Умножение матрицы на число

        :param number: Число, на которое умножается матрица

        :return: Матрица, умноженная на число

        Пример:
        >>> A = Matrix(2, 2, [1, 2, 3, 4])
        >>> A.mult_by_num(3)
        """
        if not isinstance(number, (int, float)):
            raise TypeError("Число должно быть типа int или float")
        ...


class Battery:
    def __init__(self, capacity: int, charge: int):
        """
        Создание и подготовка к работе объекта "Аккумулятор"

        :param capacity: Емкость аккумулятора
        :param charge: Заряд аккумулятора

        Пример:
        >>> battery = Battery(10000, 0)
        """
        if not isinstance(capacity, int):
            raise TypeError("Емкость аккумулятора должна быть типа int")
        if capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным числом")
        self.capacity = capacity

        if not isinstance(charge, int):
            raise TypeError("Заряд аккумулятора должен быть типа int")
        if charge <= 0:
            raise ValueError("Заряд аккумулятора должен быть положительным числом")
        if charge > capacity:
            raise ValueError("Заряд аккумулятора не может быть больше емкости")
        self.charge = charge

    def charge_battery(self, add_charge: int) -> None:
        """
        Зарядка аккумулятора.

        :param add_charge: Количество заряда, на которое пополняется аккумулятор

        :raise ValueError: Если итоговый заряд превышает емкость, вызываем ошибку

        :return: Заряд аккумулятора

        Пример:
        >>> battery = Battery(10000, 0)
        >>> battery.charge_battery(5000)
        """
        if not isinstance(add_charge, int):
            raise TypeError("Заряд должен быть типа int")
        if add_charge <= 0:
            raise ValueError("Заряд должнен быть положительным числом")
        if add_charge > self.charge + self.capacity:
            raise ValueError("Заряд аккумулятора не может быть больше емкости")
        ...

    def battery_is_charged(self) -> bool:
        """
        Метод, который проверяет, заряжен ли аккумулятор

        :return: Является ли аккумулятор заряженым

        Пример:
        >>> battery = Battery(10000, 0)
        >>> battery.battery_is_charged()
        """
        ...

    def battery_is_low(self) -> bool:
        """
        Метод, который проверяет, разряжен ли аккумулятор

        :return: Является ли аккумулятор разряженым

        Пример:
        >>> battery = Battery(10000, 0)
        >>> battery.battery_is_low()
        """
        ...

class Group:
    def __init__(self, group_number: str, number_of_students: int, students_list: list[str]):
        """
        Создание и подготовка к работе объекта "Группа"

        :param group_number: Номер группы
        :param number_of_students: Количество студентов
        :param students_list: Список студентов

        :raise ValueError: Если количество студентов меньше 1, вызываем ошибку

        Пример:
        >>>group = Group("1234", 2, ["Иван Иванов", "Петр Петров"])
        """
        self.group_number = group_number

        if not isinstance(number_of_students, int):
            raise TypeError("Количество студентов должно быть типа int")
        if number_of_students <= 0:
            raise ValueError("В группе должен быть хотя бы один студент")
        self.number_of_students = number_of_students

        self.students_list = students_list

    def add_student(self, name: str) -> None:
        """
        Метод добавляет студента в группу

        :param name: Имя студента
        :return: Обновленный список группы

        Пример:
        >>> group = Group("1234", 2, ["Иван Иванов", "Петр Петров"])
        >>> group.add_student("Семен Семенов")
        """
        ...

    def change_group_number(self, new_number: str) -> None:
        """
        Метод меняте номер группы
        :param new_number: Новый номер группы
        :return: Обновленный номер группы

        Пример:
        >>> group = Group("1234", 2, ["Иван Иванов", "Петр Петров"])
        >>> group.change_group_number("2345")
        """

if __name__ == "__main__":
    doctest.testmod()
    pass
