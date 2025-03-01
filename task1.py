if __name__ == "__main__":
    class Vehicle:
        """
        Базовый класс для транспортных средств.
        """

        def __init__(self, brand: str, max_speed: int):
            """
            Инициализация транспортного средства

            :param brand: Марка транспортного средства
            :param max_speed: Максимальная скорость
            """
            self.brand = brand
            self.max_speed = max_speed

        def __str__(self) -> str:
            """
            Возвращает строковое представление транспортного средства.

            :return: Строка формата "Транспортное средство {марка}. Максимальная скорость: {скорость} км/ч".
            """
            return f"Транспортное средство {self.brand}. Максимальная скорость: {self.max_speed} км/ч"

        def __repr__(self) -> str:
            """
            Возвращает строку, по которой можно инициализировать экземпляр транспортного средства.

            :return: Строка формата "Vehicle(brand={марка!r}, max_speed={скорость})".
            """
            return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed})"

        def start_engine(self) -> str:
            """
            Запускает двигатель транспортного средства.

            :return: Сообщение о запуске двигателя.
            """
            ...

        def stop_engine(self) -> str:
            """
            Останавливает двигатель транспортного средства.

            :return: Сообщение об остановке двигателя.
            """
            ...


    class Car(Vehicle):
        """
        Класс для легковых автомобилей.
        """

        def __init__(self, brand: str, max_speed: int, num_doors: int):
            """
            Инициализация легкового автомобиля.

            :param brand: Марка автомобиля.
            :param max_speed: Максимальная скорость (км/ч).
            :param num_doors: Количество дверей.
            """
            super().__init__(brand, max_speed)
            self.num_doors = num_doors

        def __str__(self) -> str:
            """
            Возвращает строковое представление легкового автомобиля.

            :return: Строка формата "Легковой автомобиль {марка}. Максимальная скорость: {скорость} км/ч. Дверей: {количество}".
            """
            return f"{super().__str__()} Дверей: {self.num_doors}"

        def __repr__(self) -> str:
            """
            Возвращает строку, по которой можно инициализировать автомобиль.

            :return: Строка формата "Car(brand={марка!r}, max_speed={скорость}, num_doors={двери})".
            """
            return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed}, num_doors={self.num_doors})"

        def open_trunk(self) -> str:
            """
            Открывает багажник автомобиля.

            :return: Сообщение об открытии багажника.
            """
            ...

        def start_engine(self) -> str:
            """
            Перегрузка метода start_engine для легкового автомобиля.
            Добавлено уведомление о проверке дверей перед запуском двигателя.

            :return: Сообщение о запуске двигателя с проверкой дверей.
            """
            ...


    class Truck(Vehicle):
        """
        Класс для грузовых автомобилей.
        """

        def __init__(self, brand: str, max_speed: int, load_capacity: float):
            """
            Инициализация грузового автомобиля.

            :param brand: Марка автомобиля.
            :param max_speed: Максимальная скорость (км/ч).
            :param load_capacity: Грузоподъемность (тонны).
            """
            super().__init__(brand, max_speed)
            self.load_capacity = load_capacity

        def __str__(self) -> str:
            """
            Возвращает строковое представление грузового автомобиля.

            :return: Строка формата "Грузовой автомобиль {марка}. Максимальная скорость: {скорость} км/ч. Грузоподъемность: {грузоподъемность} тонн".
            """
            return f"{super().__str__()} Грузоподъемность: {self.load_capacity} тонн"

        def __repr__(self) -> str:
            """
            Возвращает строку, по которой можно инициализировать грузовой автомобиль.

            :return: Строка формата "Truck(brand={марка!r}, max_speed={скорость}, load_capacity={грузоподъемность})".
            """
            return f"{self.__class__.__name__}(brand={self.brand!r}, max_speed={self.max_speed}, load_capacity={self.load_capacity})"

        def load_cargo(self, weight: float) -> str:
            """
            Загружает груз в автомобиль.

            :param weight: Вес груза (тонны).
            :return: Сообщение о загрузке груза.
            :raises ValueError: Если вес груза превышает грузоподъемность.
            """
            ...

        def stop_engine(self) -> str:
            """
            Перегрузка метода stop_engine для грузового автомобиля.
            Добавлено уведомление о проверке груза перед остановкой двигателя.

            :return: Сообщение об остановке двигателя с проверкой груза.
            """
            ...
    pass
