from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student


@method_decorator(login_required, name='dispatch')
class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/student_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:student_list')


@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/student_form.html'
    fields = '__all__'
    context_object_name = 'student'


    def get_success_url(self):
        return reverse_lazy('school_app:student_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('school_app:student_list')


@login_required
def student_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('q')
        students = Student.objects.filter(full_name__icontains=search_query)
        return render(request, 'student/student_list.html', {'students': students})


@login_required
def send_email_to_students(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        students = Student.objects.all()
        emails = [student.email for student in students]
        send_mail(subject, message, 'baigashkaevi02@gmail.com', emails)
        return HttpResponseRedirect(reverse_lazy('school_app:student_list'))
    return render(request, 'student/send_email.html')