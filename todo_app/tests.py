from django.test import TestCase
from django.urls import reverse
from .models import Task, Tag


class HomePageViewTests(TestCase):
    def test_sidebar_status_codes(self):
        response_home = self.client.get(reverse("todo_app:index"))
        self.assertEqual(response_home.status_code, 200)

        response_tags = self.client.get(reverse("todo_app:tag-list"))
        self.assertEqual(response_tags.status_code, 200)

    def test_task_creation(self):
        form_data = {
            "content": "Test content"
        }
        self.client.post(
            path=reverse("todo_app:task-create"),
            data=form_data
        )

        new_task = Task.objects.get(content__icontains=form_data["content"])
        self.assertEqual(new_task.content, form_data["content"])

    def test_retrieve_tasks(self):
        Task.objects.create(content="HelloTest1")
        Task.objects.create(content="HelloTest2")
        Task.objects.create(content="HelloTest3")

        response = self.client.get(reverse("todo_app:index"))
        tasks = Task.objects.all().order_by(
            "is_done", "-created_at"
        )
        self.assertEqual(
            list(response.context["tasks"]),
            list(tasks)
        )

    def test_tag_creation(self):
        form_data = {
            "name": "TestTag"
        }
        self.client.post(
            path=reverse("todo_app:tag-create"),
            data=form_data)

        new_tag = Tag.objects.get(name__icontains=form_data["name"])
        self.assertEqual(new_tag.name, form_data["name"])

    def test_retrieve_tags(self):
        Tag.objects.create(name="HelloTest1")
        Tag.objects.create(name="HelloTest2")
        Tag.objects.create(name="HelloTest3")

        response = self.client.get(reverse("todo_app:tag-list"))
        tags = Tag.objects.all()
        self.assertEqual(
            list(response.context["tags"]), list(tags)
        )
