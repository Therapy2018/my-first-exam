from django.db import models

# Create your models here.
class Task(models.Model):
    level = models.PositiveSmallIntegerField()
    topic = models.CharField(max_length=100)
    content = models.TextField()
    correct_answer = models.CharField(max_length=50)

class Answer(models.Model):
    content = models.TextField()
    user = models.CharField(max_length = 100, null = True)
    task = models.ForeignKey(
        'Task',
        on_delete=models.CASCADE,
    )
