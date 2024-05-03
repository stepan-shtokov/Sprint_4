import pytest


class TestBooksCollector:

    def test_add_new_book_add_three_books_added(self, books_collection):
        books = ['Философский эксперимент', 'Водяной и его мечты', 'Римская империя']
        for book in books:
            books_collection.add_new_book(book)
        assert len(books_collection.get_books_genre()) == 3

    def test_add_new_book_have_no_genre(self, books_collection):
        book_to_add = 'О скитаниях вечных и о земле'
        books_collection.add_new_book(book_to_add)
        assert books_collection.get_book_genre(book_to_add) == ''

    @pytest.mark.parametrize('book', ['', 'Мастер всего,мастер ничего,может все и ничего'])
    def test_add_new_book_book_with_large_or_empty_name_not_added(self, book, books_collection):
        books_collection.add_new_book(book)
        assert len(books_collection.get_books_genre()) == 0

    def test_add_new_book_double_add_not_added(self, books_collection):
        books = ['Книга обо всем', 'Книга обо всем']
        for book in books:
            books_collection.add_new_book(book)
        assert len(books_collection.get_books_genre()) == 1

    def test_set_book_genre_genre_added(self, books_collection):
        book = 'Мгла'
        genre = 'Ужасы'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, genre)
        assert books_collection.get_book_genre(book) == genre

    def test_change_genre_genre_changed(self, books_collection):
        book = 'Мгла'
        initial_genre = 'Ужасы'
        new_genre = 'Комедии'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, initial_genre)
        books_collection.set_book_genre(book, new_genre)
        assert books_collection.get_book_genre(book) == new_genre

    def test_set_book_genre_with_excluded_genre(self, books_collection):
        book = 'Мой кот и его жизнь'
        excluded_genre = 'Жизнеописание'
        books_collection.add_new_book(book)
        books_collection.set_book_genre(book, excluded_genre)
        assert books_collection.get_book_genre(book) == ''

    def test_get_book_with_specific_genre_genre_specified(self, books_collection_5_books):
        assert books_collection_5_books.get_books_with_specific_genre('Ужасы') == ['Мгла']

    def test_get_book_with_wrong_genre_no_such_book(self, books_collection_5_books):
        assert len(books_collection_5_books.get_books_with_specific_genre('Адвенчура')) == 0

    def test_get_books_for_children_no_age_restricted_books(self, books_collection_5_books):
        books_for_children = books_collection_5_books.get_books_for_children()
        assert len(books_for_children) == 3 and books_for_children == ['Волшебство в Python', 'Основание', 'Гарри Поттер в QA']

    def test_add_book_in_favorites_added_one_book(self, books_collection):
        book = '12 Rules for Life.An Antidote to chaos'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        favorite_books = books_collection.get_list_of_favorites_books()
        assert len(favorite_books) == 1 and favorite_books[0] == book

    def test_add_book_in_favorites_twice_not_added(self, books_collection):
        book = '12 Rules for Life.An Antidote to chaos'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.add_book_in_favorites(book)
        favorite_books = books_collection.get_list_of_favorites_books()
        assert len(favorite_books) == 1 and favorite_books[0] == book

    def test_add_book_in_favorites_add_non_dict_book_not_added(self, books_collection):
        book = 'Beyond Order'
        books_collection.add_book_in_favorites(book)
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_is_deleted(self, books_collection):
        book = 'Delete me easily'
        books_collection.add_new_book(book)
        books_collection.add_book_in_favorites(book)
        books_collection.delete_book_from_favorites(book)
        assert len(books_collection.get_list_of_favorites_books()) == 0
