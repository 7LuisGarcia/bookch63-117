from django.urls import path
from .views import (
    InventoryListView,
    AddBookView,
    UpdateBookView,
    DeleteBookView
)

urlpatterns = [
    path('', InventoryListView.as_view(), name="inventory"),
    path('add/', AddBookView.as_view(), name="add_book"),
    path('edit_book/<int:pk>/', UpdateBookView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
]
