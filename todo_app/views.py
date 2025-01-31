from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from todo_app.forms import TagForm, TaskForm
from todo_app.models import Task, Tag


class HomePageView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related(
        "tags"
    ).order_by("is_done", "-created_at")
    template_name = "todo_app/index.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:index")


class TaskCompleteView(DetailView):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_app:index")



class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:index")


class TagListView(ListView):
    model = Tag
    template_name = "todo_app/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")
