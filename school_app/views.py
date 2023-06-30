from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student, Teacher, Grade, School


class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/student_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/student_form.html'
    fields = '__all__'
    context_object_name = 'student'


    def get_success_url(self):
        return reverse_lazy('school_app:student_detail', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    context_object_name = 'student'
    success_url = reverse_lazy('school_app:student_list')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher/teacher_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:teacher_list')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/teacher_detail.html'
    context_object_name = 'teacher'


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher/teacher_form.html'
    fields = '__all__'
    context_object_name = 'teacher'

    def get_success_url(self):
        return reverse_lazy('school_app:teacher_detail', kwargs={'pk': self.object.pk})


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher/teacher_confirm_delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('school_app:teacher_list')


class GradeListView(ListView):
    model = Grade
    template_name = 'grade/grade_list.html'
    context_object_name = 'grades'


class GradeCreateView(CreateView):
    model = Grade
    template_name = 'grade/grade_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:grade_list')


class GradeDetailView(DetailView):
    model = Grade
    template_name = 'grade/grade_detail.html'
    context_object_name = 'grade'


class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'grade/grade_form.html'
    fields = '__all__'
    context_object_name = 'grade'

    def get_success_url(self):
        return reverse_lazy('school_app:grade_detail', kwargs={'pk': self.object.pk})


class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grade/grade_confirm_delete.html'
    context_object_name = 'grade'
    success_url = reverse_lazy('school_app:grade_list')


class SchoolListView(ListView):
    model = School
    template_name = 'school/school_list.html'
    context_object_name = 'schools'


class SchoolCreateView(CreateView):
    model = School
    template_name = 'school/school_form.html'
    fields = '__all__'
    success_url = reverse_lazy('school_app:school_list')


class SchoolDetailView(DetailView):
    model = School
    template_name = 'school/school_detail.html'
    context_object_name = 'school'


class SchoolUpdateView(UpdateView):
    model = School
    template_name = 'school/school_form.html'
    fields = '__all__'
    context_object_name = 'school'

    def get_success_url(self):
        return reverse_lazy('school_app:school_detail', kwargs={'pk': self.object.pk})


class SchoolDeleteView(DeleteView):
    model = School
    template_name = 'school/school_confirm_delete.html'
    context_object_name = 'school'
    success_url = reverse_lazy('school_app:school_list')


