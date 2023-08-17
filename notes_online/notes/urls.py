from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('',views.home, name="home"),
    path('themes/',views.ThemeListPostView.get, name="themes"),
    path('theme/get_update/<int:pk>/',views.ThemeGetPutDeleteView.get_update_detail_theme, name="theme_detail"),
    path('theme/delete/<int:pk>/',views.ThemeGetPutDeleteView.delete_theme, name="delete_theme"),
    path('notes_on_theme/<int:pk>/',views.ThemeListPostView.get_notes_on_themes, name="notes_on_theme"),
    path('create_theme/',views.ThemeListPostView.post, name="create_theme"),

    path('notes/',views.NotesListPostView.get, name="notes"),
    path('note/get_update/<int:pk>/',views.NotesGetPutDeleteView.get_update_detail_note, name="note_detail"),
    path('note/delete/<int:pk>/',views.NotesGetPutDeleteView.delete_note, name="delete_note"),
    path('create_note/',views.NotesListPostView.post, name="create_note"),

    path('register/',views.RegistrationView.post, name="register"),
    path('login/',views.RegistrationView.post, name="login"),


]

