from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models

class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_learners = models.IntegerField()
    def __str__(self): return self.user.username

class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    
    # Change this line from models.ImageField to this CharField:
    image = models.CharField(max_length=255, default='course_images/default.png')
    
    description = models.CharField(max_length=500)
    pub_date = models.DateField(null=True)
    instructors = models.ManyToManyField(Instructor)
    users = models.ManyToManyField(User, through='Enrollment')
    total_enrollment = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, default='honor')
    rating = models.FloatField(default=5.0)

class Lesson(models.Model):
    title = models.CharField(max_length=100, default="title")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=50)
    def __str__(self): return self.content

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self): return self.content

class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)