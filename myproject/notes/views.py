from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm


@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request,"notes/create_note.html",{"form":form})

def note_list(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user) | Note.objects.filter(visibility="public")
    else:
        notes = Note.objects.filter(visibility="public")
    return render(request,"notes/note_list.html",{"notes":notes})

def home(request):
    return render(request,'notes/home.html')

def note_detail(request,pk):
    note = get_object_or_404(Note,pk=pk)
    return render(request,'notes/note_detail.html',{'note':note})