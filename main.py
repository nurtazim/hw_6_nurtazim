import cowsay
import requests
import django
from hw_6_nurtazim.university.library import Library
from hw_6_nurtazim.university.students import Students

s = Students("Loksli")
d = Students("Artur")

print(Library.books_list())

s.get_book(Library, "Пушкин")
print(Library.books_list())
d.get_book(Library, "Доброе утро Игорь")

print(Library.books_list())

s.retern_book(Library, "Пушкин")

print(Library.books_list())

d.get_book(Library, "Пушкин")

print(Library.books_list())


cowsay.tux("Well Done")


