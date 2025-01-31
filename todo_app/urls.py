from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from todo_app.views import HomePageView, TagListView, TagCreateView

app_name="todo_app"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
