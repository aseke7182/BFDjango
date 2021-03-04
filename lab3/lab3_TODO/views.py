from django.shortcuts import render


# Create your views here.

def index(request):
    tasks = [
        {'name': 'Task1',
         'created': '22 Jan, 2021',
         'due_on': ' 23 Jan 2021',
         'owner': 'admin'
         },
        {'name': 'Task2',
         'created': '22 Jan, 2021',
         'due_on': ' 23 Jan 2021',
         'owner': 'admin'
         },
        {'name': 'Task3',
         'created': '22 Jan, 2021',
         'due_on': ' 23 Jan 2021',
         'owner': 'admin'
         },
        {'name': 'Task4',
         'created': '22 Jan, 2021',
         'due_on': ' 23 Jan 2021',
         'owner': 'admin'
         },
    ]

    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def completed(request):
    tasks = [
        {'name': 'Task0',
         'created': '22 Jan, 2021',
         'due_on': ' 23 Jan 2021',
         'owner': 'admin'
         }
    ]

    context = {
        'tasks': tasks
    }

    return render(request, 'completed.html', context)
