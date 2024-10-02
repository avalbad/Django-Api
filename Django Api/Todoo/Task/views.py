from django.shortcuts import render , redirect , get_list_or_404
from Task.models import TodoTask ,Category
from Task.forms import TaskTodoForm
from django.http import HttpResponseRedirect
from django.views.generic import DetailView , DeleteView


def sho_task(request):
    query = TodoTask.objects.all().order_by('created_at')
    form  = TaskTodoForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form =  TaskTodoForm()

    dic = {
      'query' : query,
      'form' : form,
          }
    return render(request,"task/home.html",dic)


class TaskDtail(DetailView):
    model = TodoTask
    template_name = "task/task_detail.html"
    

# def TaskDelete(request,id):
#     task = get_list_or_404(TodoTask,id=id)
#     task.delete()
#     return redirect('Task:sho_task')

def TaskDelete(request, pk):
    try:
        task = TodoTask.objects.get(id=pk)
        task.delete()
        return redirect('Task:sho_task')
    except TodoTask.DoesNotExist:
        return redirect('Task:sho_task')

    


