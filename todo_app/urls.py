from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from todo_app.views import IndexView

app_name="todo_app"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
