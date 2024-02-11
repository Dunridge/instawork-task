from django.urls import path
from .views import add, delete, edit, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/<int:member_index>/', edit, name='edit'),
    path('delete/<int:member_id>/', delete, name='delete')
]