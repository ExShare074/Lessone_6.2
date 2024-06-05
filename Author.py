#Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в качестве объекта.

class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book():
    def __init__(self, tittle, author):
        self.tittle = tittle
        self.author = author

    def get_info_book(self):
        print(f"{self.tittle} - {self.author.name}")

author = Author("Пушкин", "Россия")
book = Book("Капитанская дочка", author)

print(author.name)
book.get_info_book()