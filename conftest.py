import pytest
from main import BooksCollector


@pytest.fixture
def books_collection():
    books_collection = BooksCollector()
    return books_collection


@pytest.fixture
def books_collection_5_books(books_collection):
    collection = books_collection
    books = ['Мгла', 'Собака Баскервилей', 'Волшебство в Python', 'Основание', 'Гарри Поттер в QA']
    genre = ['Ужасы', 'Детективы', 'Комедии', 'Мультфильмы', 'Фантастика']
    for i in range(5):
        collection.add_new_book(books[i])

    for i in range(5):
        collection.set_book_genre(books[i], genre[i])

    return collection
