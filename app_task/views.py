from django.shortcuts import render
from parameter.celery import add
from app_task.tasks import sub
from celery.result import AsyncResult
from .tasks import send_email_task



# Display addition value after task execution
def index(request):
    result = add.delay(10, 30)
    send_email_task.delay('Sujet du mail', 'Corps du mail', ['pepexykabasele@gmail.com',])
    return render(request, "app_task/home_task.html", {'result':result})

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
#     print("Get: ", result.get())
    return render(request, 'app_task/result.html', {'result':result})
