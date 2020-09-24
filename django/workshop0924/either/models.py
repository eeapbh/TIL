from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    pick_a = models.CharField(max_length=200)
    pick_b = models.CharField(max_length=200)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()