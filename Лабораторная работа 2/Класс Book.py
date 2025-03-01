BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        if not isinstance(id_, int):
            raise TypeError("Идентификатор книги дожен быть типа int")
        if id_ <= 0:
            raise ValueError("Индентификатор книги должен быть числом больше 0")
        self.id = id_

        if not isinstance(name, int):
            raise TypeError("Название книги дожено быть типа str")
        self.name = name

        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге дожено быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает название книги.

        :return: Строка формата 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать экземпляр книги.

        :return: Строка формата 'Book(id_=..., name=..., pages=...)'.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
