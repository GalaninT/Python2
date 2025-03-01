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

        if not isinstance(name, str):
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


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список).
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги.

        :return: Идентификатор следующей книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с таким идентификатором не существует, возвращаем ошибку
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
