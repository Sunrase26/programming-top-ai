from abc import ABC, abstractmethod
from datetime import datetime


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Название книги: '{self.title}', автор: {self.author}, год: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if isinstance(other, Book):
            return (
                self.title == other.title
                and self.author == other.author
                and self.year == other.year
            )
        return False

    def print_info(self):
        print(self.info())

    @property
    def age(self):
        return datetime.now().year - self.year

    @classmethod
    def from_string(cls, book_str):
        title, author, year = map(str.strip, book_str.split(","))
        return cls(title, author, int(year))


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"{super().info()}, формат файла: {self.format}"
