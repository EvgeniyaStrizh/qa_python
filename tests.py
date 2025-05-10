from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_invalid_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        collector.add_new_book('К' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_book_genre_invalid(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert sorted(collector.get_books_with_specific_genre('Фантастика')) == sorted(['Дюна', '1984'])
        assert collector.get_books_with_specific_genre('Детективы') == []

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький Мук')
        collector.set_book_genre('Маленький Мук', 'Фантастика')
        collector.add_new_book('Ужасы для делей')
        collector.set_book_genre('Ужасы для детей', 'Ужасы')
        assert collector.get_books_for_children() == ['Маленький Мук']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_invalid(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['1984']

    