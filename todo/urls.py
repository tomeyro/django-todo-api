from django.urls import path
from .views import TasksView, TaskView, set_done, set_not_done

urlpatterns = [
    path("tasks/", TasksView.as_view()),
    path("tasks/<int:id>/", TaskView.as_view()),
    path("tasks/<int:id>/done/", set_done),
    path("tasks/<int:id>/not_done/", set_not_done),
]
