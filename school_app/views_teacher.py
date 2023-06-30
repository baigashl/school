from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password, check_password
from .forms import TeacherRegistrationForm
from .models import Teacher


class TeacherRegistrationView(CreateView):
    model = Teacher
    form_class = TeacherRegistrationForm
    template_name = 'teacher/teacher_registration.html'
    success_url = reverse_lazy('school_app:teacher_login')

    def form_valid(self, form):
        # Сохранение учителя и его аутентификация после успешной регистрации
        response = super().form_valid(form)
        self.object.set_password(form.cleaned_data['password1'])
        self.object.save()
        self.object.backend = 'django.contrib.auth.backends.ModelBackend'
        self.request.session['teacher_id'] = self.object.id
        return response


def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        techer = Teacher.objects.get(phone_number=phone_number)
        # if techer:
        if check_password(password, techer.password):
            print('login')
            login(request, techer)
            return HttpResponseRedirect(reverse_lazy('school_app:student_list'))
        else:
            return render(request, 'teacher/teacher_login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'teacher/teacher_login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('core:login'))


@method_decorator(login_required, name='dispatch')
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'


@method_decorator(login_required, name='dispatch')
class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher/teacher_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:teacher_list')


@method_decorator(login_required, name='dispatch')
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/teacher_detail.html'
    context_object_name = 'teacher'


@method_decorator(login_required, name='dispatch')
class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher/teacher_form.html'
    fields = '__all__'
    context_object_name = 'teacher'

    def get_success_url(self):
        return reverse_lazy('school_app:teacher_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher/teacher_confirm_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('school_app:teacher_list')