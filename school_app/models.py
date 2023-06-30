from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('М', 'М'),
        ('Ж', 'Ж'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='student_photos/', blank=True)

    def __str__(self):
        return self.email


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Grade(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='grades')
    students = models.ManyToManyField(Student, related_name='grades')

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    grades = models.ManyToManyField(Grade, related_name='school_grades')
    note = models.TextField()

    def __str__(self):
        return self.name
