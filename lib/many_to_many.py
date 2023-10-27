class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [cont for cont in Contract.all if cont.author == self]

    def books(self):
        return [author.book for author in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        earnings = [author.royalties for author in self.contracts()]
        return sum(earnings)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [cont for cont in Contract.all if cont.book == self]

    def authors(self):
        return [book.author for book in self.contracts()]


class Contract:
    all = []

    __slots__ = ("_author", "_book", "_date", "_royalties")

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # def __init__(self, **kwargs):
    #     for k, v in kwargs.items():
    #         setattr(self, k, v)
    #     self.save()
    #     Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Value must be an instance of Author class.")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("Value must be an instance of Book class.")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Value must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [cont for cont in cls.all if cont.date == date]
