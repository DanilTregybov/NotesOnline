from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('themes/', views.get_themes, name="themes"),
    path('theme/get_update/<int:pk>/', views.get_update_detail_theme, name="theme_detail"),
    path('theme/delete/<int:pk>/', views.delete_theme, name="delete_theme"),
    path('notes_on_theme/<int:pk>/', views.get_notes_on_themes, name="notes_on_theme"),
    path('create_theme/', views.post_theme, name="create_theme"),

    path('notes/', views.get_notes, name="notes"),
    path('note/get_update/<int:pk>/', views.get_update_detail_note, name="note_detail"),
    path('note/delete/<int:pk>/', views.delete_note, name="delete_note"),
    path('create_note/', views.post_note, name="create_note"),

    path('register/', RegisterUser.as_view(), name="register"),



]

