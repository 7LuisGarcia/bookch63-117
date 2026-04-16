from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class InventoryListView(ListView):
    model = Book
    template_name = 'inventory/inventory.html'
    context_object_name = 'books_list'
    
class AddBookView(CreateView):    
    model = Book
    form_class = BookForm
    template_name = 'inventory/add_book.html'
    success_url = reverse_lazy('inventory')

class UpdateBookView(UpdateView):    
    model = Book
    form_class = BookForm
    template_name = 'inventory/edit_book.html'
    success_url = reverse_lazy('inventory')

class DeleteBookView(DeleteView):    
    model = Book
    template_name = 'inventory/delete_book.html'
    success_url = reverse_lazy('inventory')
