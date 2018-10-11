from django.shortcuts import render
from tasks.models import Task
from tasks.models import Answer

# Create your views here.
def start(request):
    all_tasks = Task.objects.filter(level=level)
    return render(request, 'tasks/start.html', {'all_tasks':all_tasks})

def exam(request, level):
    all_tasks = Task.objects.filter(level=level)
    return render(request, 'tasks/exam.html', {'all_tasks':all_tasks})

def result(request):
    print(request.POST)
    all_tasks = request.POST
    task_ids = []
    task_id_to_value = {}
    
    for key, value in all_tasks.items():
        if 'tiuri' in key:
            user = value
        # task-12, task-5, modllweefdfd
        if '-' in key:
            # task-3434
            task_id = int(key.split('-')[1])
            # 3434
            task_ids.append(task_id)
            task_id_to_value[task_id] = value

    tasks = Task.objects.filter(id__in = task_ids)
        # tasks=[Task()]
    answers = []
    for task_id, answer in task_id_to_value.items():
            answers.append(
                Answer.objects.create(
                content = answer,
                user = user,
 #           task = Task.objects.get(task_id=task_id),
                task_id = task_id,
                )
            )
    
    print(user)
    #all_answers = Task.objects.get(task_id=task_id)
    return render(request, 'tasks/result.html', {'answers':answers})
    
