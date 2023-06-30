from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Grade


@method_decorator(login_required, name='dispatch')
class GradeListView(ListView):
    model = Grade
    template_name = 'grade/grade_list.html'
    context_object_name = 'grades'


@method_decorator(login_required, name='dispatch')
class GradeCreateView(CreateView):
    model = Grade
    template_name = 'grade/grade_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:grade_list')


@method_decorator(login_required, name='dispatch')
class GradeDetailView(DetailView):
    model = Grade
    template_name = 'grade/grade_detail.html'
    context_object_name = 'grade'


@method_decorator(login_required, name='dispatch')
class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'grade/grade_form.html'
    fields = '__all__'
    context_object_name = 'grade'

    def get_success_url(self):
        return reverse_lazy('school_app:grade_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grade/grade_confirm_delete.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('school_app:grade_list')