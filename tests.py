import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("name", [
        "Зов Ктулху",
        "Python за 3 дня"
    ])
    def test_add_new_books_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name', [
        'Чудесный костюм цвета шоколадного мороженого',
        'Бойня номер пять, или Крестовый поход детей'
    ])
    def test_add_longname_books_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_add_no_name_book_not_added(self):
        collector = BooksCollector()
        name = ''
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_new_book_have_no_genre(self):
        collector = BooksCollector()
        name = 'О скитаниях вечных и о земле'
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize('name, genre', [
        ('Python за 3 дня', 'Фантастика'),
        ('Зов Ктулху', 'Ужасы')
    ])
    def test_genre_set_genre_added(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_unreal_genre_set_genre_not_added(self):
        collector = BooksCollector()
        name = 'Невероятные приключения моей кошки'
        genre = 'Биография'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize('name, genre', [
        ('Как стать богатым за 1 день', 'Фантастика'),
        ('Попал под сокращение на работе', 'Ужасы')
    ])
    def test_get_genre_by_book_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_non_dict_book_has_no_genre(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Взломал Яндекс.Практикум') is None

    @pytest.mark.parametrize('name, genre', [
        ('Python за 3 дня', 'Фантастика'),
        ('Зов Ктулху', 'Ужасы'),
        ('Не сдал проект Яндекса', 'Ужасы')
    ])
    def test_get_books_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_genre = collector.get_books_with_specific_genre('Ужасы')
        assert 'Зов Ктулху', 'Не сдал проект Яндекса' in books_with_genre

    @pytest.mark.parametrize('name, genre', [
        ('Python за 3 дня', 'Фантастика'),
        ('Зов Ктулху', 'Ужасы'),
        ('Не сдал проект Яндекса', 'Ужасы')
    ])
    def test_no_books_by_unused_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_with_genre = collector.get_books_with_specific_genre('Детективы')
        assert books_with_genre == []

    @pytest.mark.parametrize('name, genre', [
        ('Выучил Python', 'Фантастика'),
        ('Зов военкомата', 'Ужасы'),
        ('Сдал проект Яндекса', 'Детективы')
    ])
    def test_get_book_genre_dict(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert isinstance(collector.get_books_genre(), dict)

    @pytest.mark.parametrize('name, genre', [
        ('Получил золотую медаль', 'Фантастика'),
        ('Зов военкомата', 'Ужасы'),
        ('Поступление на бюджет', 'Комедии')
    ])
    def test_no_age_restricted_books_for_kids(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        books_for_children = collector.get_books_for_children()
        assert 'Зов военкомата' not in books_for_children

    def test_add_book_to_favorites(self):
        collector = BooksCollector()
        name = 'Как я получил диплом Яндекса'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_non_dict_book_to_favorites_not_added(self):
        collector = BooksCollector()
        name = 'Как я не получил диплом Яндекса'
        collector.add_book_in_favorites(name)
        assert collector.favorites == []

    def test_add_book_twice_without_delete(self):
        collector = BooksCollector()
        name = 'Как я получил диплом Яндекса'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        name = 'Как я получил диплом Яндекса'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    @pytest.mark.parametrize("name", [
        "Стал тестировщиком",
        "Как получить диплом Яндекса"
    ])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorite_books = collector.get_list_of_favorites_books()
        assert name in favorite_books
