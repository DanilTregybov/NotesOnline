from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from .froms import ThemeForm, NoteForm
from .models import Theme, Note



# Create your views here.
def home(request):
    return render(request, "notes/home_page.html")
class ThemeListPostView(APIView):

    def get(request):
        themes = Theme.objects.all()
        return render(request, "notes/themes_list.html", {"themes": themes})

    def get_notes_on_themes(request,pk):
        themes = Theme.objects.get(pk=pk)
        notes = Note.objects.filter(topic=themes)
        return render(request, "notes/notes_list.html",{"notes": notes})#{"notes": notes}

    def post(request):
        error = ""
        if request.method == "POST":
            form = ThemeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("themes")
            else:
                error = "Form don`t valid"
        form = ThemeForm()
        context = {
            "form": form,
            "error": error
        }
        return render(request, "notes/create_th.html", context)

class ThemeGetPutDeleteView(APIView):

    def get_update_detail_theme(request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        if request.method == "POST":
            form = ThemeForm(request.POST, instance=theme)
            if form.is_valid():
                form.save()
                return redirect("themes")
        else:
            form = ThemeForm(instance=theme)
        return render(request, "notes/theme_detail.html", {"form": form, "theme": theme})

    def delete_theme(request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        if request.method == "POST":
            theme.delete()
            return redirect("themes")


class NotesListPostView(APIView):

    def get(request):
        notes = Note.objects.all()
        return render(request, "notes/notes_list.html",{"notes": notes})

    def post(request):
        error = ""
        if request.method == "POST":
            form = NoteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("notes")
            else:
                error = "Form don`t valid"
        form = NoteForm()
        context = {
            "form": form,
            "error": error
        }

        return render(request, "notes/create_nt.html", context)

class NotesGetPutDeleteView(APIView):

    def get_update_detail_note(request, pk):
        note = get_object_or_404(Note, pk=pk)
        if request.method == "POST":
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect("notes")
        else:
            form = NoteForm(instance=note)
        return render(request, "notes/note_detail.html", {"form": form, "note":note})

    def delete_note(request, pk):
        note = get_object_or_404(Note, pk=pk)
        if request.method == "POST":
            note.delete()
            return redirect("notes")
class RegistrationView(APIView):

    def post(request):
        return None



