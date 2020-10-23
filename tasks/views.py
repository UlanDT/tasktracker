from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Task
from .tasks import task_expired


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def task_time():
    tasks = Task.objects.exclude(status="DONE").values_list('id', 'end_time')

    for task_id, end_time in tasks:
        if timezone.now() > end_time:
            task_expired.delay(task_id)

