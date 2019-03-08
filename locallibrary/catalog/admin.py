from django.contrib import admin
from .models import Book, BookInstance, Author, Genre

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ['id', 'book', 'imprint', 'due_back', 'status']

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

admin.site.register(Genre)



