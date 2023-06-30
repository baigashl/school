from django.urls import path
from django.contrib.auth import views as auth_views
from . import views_grade, views_school, views_student, views_teacher

app_name = 'school_app'

urlpatterns = [
    # student
    path('', views_student.StudentListView.as_view(), name='student_list'),
    path('students/create/', views_student.StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/', views_student.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', views_student.StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', views_student.StudentDeleteView.as_view(), name='student_delete'),
    path('students/search/', views_student.student_search, name='student_search'),
    path('students/send_email/', views_student.send_email_to_students, name='send_email'),
    # grade
    path('grades/', views_grade.GradeListView.as_view(), name='grade_list'),
    path('grades/create/', views_grade.GradeCreateView.as_view(), name='grade_create'),
    path('grades/<int:pk>/', views_grade.GradeDetailView.as_view(), name='grade_detail'),
    path('grades/<int:pk>/update/', views_grade.GradeUpdateView.as_view(), name='grade_update'),
    path('grades/<int:pk>/delete/', views_grade.GradeDeleteView.as_view(), name='grade_delete'),
    # school
    path('schools/', views_school.SchoolListView.as_view(), name='school_list'),
    path('schools/create/', views_school.SchoolCreateView.as_view(), name='school_create'),
    path('schools/<int:pk>/', views_school.SchoolDetailView.as_view(), name='school_detail'),
    path('schools/<int:pk>/update/', views_school.SchoolUpdateView.as_view(), name='school_update'),
    path('schools/<int:pk>/delete/', views_school.SchoolDeleteView.as_view(), name='school_delete'),
    # teacher
    path('teacher/registration/', views_teacher.TeacherRegistrationView.as_view(), name='teacher_registration'),
    path('accounts/login/', views_teacher.login_view, name='teacher_login'),
    path('logout/', views_teacher.logout_view, name='logout'),
    path('teachers/', views_teacher.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', views_teacher.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/', views_teacher.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/update/', views_teacher.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', views_teacher.TeacherDeleteView.as_view(), name='teacher_delete'),
]
