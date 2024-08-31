from django.shortcuts import render
from .forms import SearchForm
from .models import Task
from django.views.generic import DetailView, CreateView


def main(request):
    return render(request, 'main.html')


def task_list_view(request):
    if request.method == "GET":
        search = request.GET.get('search', None)
        category = request.GET.get('category', None)
        search_form = SearchForm(request.GET)
        tasks = Task.objects.all()
        if search:
            tasks = tasks.filter(title__icontains=search)
        if category:
            tasks = tasks.filter(category__id=category)
        context = {'tasks': tasks, 'search_form': search_form}
        return render(request, 'tasks.html', context=context)
    

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = "__all__"
    success_url = '/tasks/'