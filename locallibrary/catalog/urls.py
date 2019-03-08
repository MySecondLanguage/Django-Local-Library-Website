from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('author/<int:pk>', views.author_detail_view, name='author_detail'),
    path('author', views.AuthorListView.as_view(), name='author_list'),
    path('login/', views.user_login, name='user_login'),
    path('success', views.success, name='user_success'),
    path('user_logout', views.user_logout, name='user_logout'),
]