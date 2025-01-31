from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from todo_app.forms import TagForm
from todo_app.models import Task, Tag


class HomePageView(ListView):
    model = Task
    template_name = "todo_app/index.html"
    context_object_name = "tasks"


class TagListView(ListView):
    model = Tag
    template_name = "todo_app/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_app:tag-list")