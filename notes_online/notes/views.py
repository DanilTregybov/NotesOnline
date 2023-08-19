from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from rest_framework.exceptions import PermissionDenied

from .forms import ThemeForm, NoteForm, RegisterForm
from .models import Theme, Note
# from .service import send_email


# Create your views here.

def home(request):
    return render(request, "notes/home_page.html")

@login_required
def get_themes(request):
    themes = Theme.objects.filter(owner=request.user)
    return render(request, "notes/themes_list.html", {"themes": themes})

@login_required
def get_notes_on_themes(request, pk):
    themes = Theme.objects.get(pk=pk)
    if request.user == themes.owner:
        notes = Note.objects.filter(topic=themes)
        return render(request, "notes/notes_list.html", {"notes": notes})
    else:
        return redirect("themes")

@login_required
def post_theme(request):
    error = ""
    if request.method == "POST":
        form = ThemeForm(request.POST)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.owner = request.user
            theme.save()
            return redirect("themes")
        else:
            error = "Form don`t valid"
    form = ThemeForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, "notes/create_th.html", context)

@login_required
def get_update_detail_theme(request, pk):
    theme = get_object_or_404(Theme, pk=pk)
    if request.user == theme.owner:
        if request.method == "POST":
            form = ThemeForm(request.POST, instance=theme)
            if form.is_valid():
                form.save()
                return redirect("themes")
        else:
            form = ThemeForm(instance=theme)
        return render(request, "notes/theme_detail.html", {"form": form, "theme": theme})
    else:
        return redirect("themes")

@login_required
def delete_theme(request, pk):
    theme = get_object_or_404(Theme, pk=pk)
    if request.user == theme.owner:
        if request.method == "POST":
            theme.delete()
            return redirect("themes")
    else:
        return redirect("themes")

@login_required
def get_notes(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, "notes/notes_list.html", {"notes": notes})

@login_required
def post_note(request):
    error = ""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("notes")
        else:
            error = "Form don`t valid"
    form = NoteForm()
    owner_topic = Theme.objects.filter(owner=request.user)
    context = {
        "owner_topic": owner_topic,
        "form": form,
        "error": error
    }

    return render(request, "notes/create_nt.html", context)

@login_required
def get_update_detail_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.user == note.owner:
        if request.method == "POST":
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect("notes")
        else:
            form = NoteForm(instance=note)
        return render(request, "notes/note_detail.html", {"form": form, "note": note})
    else:
        return redirect("notes")

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.user == note.owner:
        if request.method == "POST":
            note.delete()
            return redirect("notes")
    else:
        return redirect("notes")


class RegisterUser(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    
    def form_valid(self, form):
        form.save()
        # send_email(form.instance.email)
        return super().form_valid(form)



