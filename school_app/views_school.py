from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import School


@method_decorator(login_required, name='dispatch')
class SchoolListView(ListView):
    model = School
    template_name = 'school/school_list.html'
    context_object_name = 'schools'


@method_decorator(login_required, name='dispatch')
class SchoolCreateView(CreateView):
    model = School
    template_name = 'school/school_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:school_list')


@method_decorator(login_required, name='dispatch')
class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'
    context_object_name = 'school'


@method_decorator(login_required, name='dispatch')
class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school/school_form.html'
    fields = '__all__'
    context_object_name = 'school'

    def get_success_url(self):
        return reverse_lazy('school_app:school_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school/school_confirm_delete.html'
    context_object_name = 'school'
    success_url = reverse_lazy('school_app:school_list')