from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),  
    path('create/', views.create_note, name="create_note"),
    path('list/', views.note_list, name="note_list"),
    path('<int:pk>/', views.note_detail, name="note_detail"),
]



