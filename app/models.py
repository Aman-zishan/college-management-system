from django.db import models
from authentication.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.ManyToManyField(Subject, related_name='teacher_subject')

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    title = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_note')
    note = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title


class QuestionPaper(models.Model):
    title = models.CharField(max_length=300)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_qp')
    qp = models.FileField(upload_to='questionpapers/')

    def __str__(self):
        return self.title


class Notification(models.Model):
    title = models.CharField(max_length=500)
    notification = models.FileField(upload_to='notification/')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=500)
    assignment = models.FileField(upload_to='assignments/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_assignment')

    def __str__(self):
        return self.title

