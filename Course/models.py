from django.db import models


class Student(models.Model):
    FIO = models.CharField(max_length=99)
    date_birth = models.DateField()

    def __str__(self):
        return self.FIO


class Mentor(models.Model):
    FIO = models.CharField(max_length=99)
    work_experience = models.IntegerField()

    def __str__(self):
        return self.FIO


class Course(models.Model):
    name = models.CharField(max_length=99)
    course_duration = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
