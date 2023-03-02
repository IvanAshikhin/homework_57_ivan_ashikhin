from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, RedirectView

from webapp.models import Task

from webapp.forms import TaskForm


class TaskDetail(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index_page'

class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['tasks'])
        return context

    def post(self, request, *args, **kwargs):
        tasks = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            tasks.edit_time = datetime.now()
            tasks.save()
            form.save()
            return redirect('detail_task', pk=tasks.pk)
        return render(request, 'task_update.html', context={'form': form, 'tasks': tasks})


class TaskDelete(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        tasks = get_object_or_404(Task, pk=kwargs['pk'])
        tasks.type.clear()
        tasks.delete()


