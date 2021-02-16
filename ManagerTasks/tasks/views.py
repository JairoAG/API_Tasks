from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def agregar_task(request):
    
    data = {
        'form' : TaskForm()
    }
    
    if request.method == 'POST':
        formulario  = TaskForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Tarea guardada correctamente"
            return redirect(to="listar_tasks")
        else:
            data["form"] = formulario
    

    return render(request, 'agregar.html', data)


def listar_tasks(request):
    tasks = Task.objects.all()

    data = {
        'tasks' : tasks
    }

    return render(request,'listar.html', data)


def editar_task(request,id):

    task = get_object_or_404(Task, id = id)

    data= {
        'form' : TaskForm(instance=task) 
    }

    if request.method == 'POST' :
        formulario= TaskForm(data=request.POST, instance=task, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_tasks")
        data["form"] = formulario

    return render(request, 'modificar.html',data)

def eliminar_task(request, id):
    task = get_object_or_404(Task, id = id)
    task.delete()
    return redirect(to='listar_tasks')

####################################################################################

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tasks = Task.objects.all().filter(descripcion=search)
        return render(request,'listar.html', {'tasks':tasks})


"""

    data= {'form' : TaskForm(instance=task)}
    if request.method == 'POST' :
        formulario= TaskForm(data=request.POST, instance=task, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_tasks")
        data["form"] = formulario
    return render(request, 'modificar.html',data)

"""

