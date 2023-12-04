from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Task


def json_404():
    response = JsonResponse({"error": "record not found"})
    response.status_code = 404
    return response


class TasksView(View):
    def get(self, request):
        tasks = [task.as_json() for task in Task.objects.all()]
        return JsonResponse(tasks, safe=False)

    def post(self, request):
        task = Task.objects.create(name=request.POST["name"])
        response = JsonResponse(task.as_json())
        response.status_code = 201
        return response


class TaskView(View):
    def get(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return json_404()
        return JsonResponse(task.as_json())

    def post(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return json_404()
        task.name = request.POST["name"]
        task.done = request.POST.get("done", str(task.done)).lower() in (
            "yes",
            "true",
            "1",
        )
        task.save()
        return JsonResponse(task.as_json())


def _set_done(request, id, done):
    if request.method == "POST":
        try:
            task = Task.objects.get(id=id)
        except ObjectDoesNotExist:
            return json_404()
        task.done = done
        task.save()
        return JsonResponse(task.as_json())
    return json_404()


def set_done(request, id):
    return _set_done(request, id, True)


def set_not_done(request, id):
    return _set_done(request, id, False)
