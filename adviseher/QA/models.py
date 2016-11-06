from django.db import models

class Question(models.Model):
    question_id = models.Autofield(primary_key=True)
    question_test = models.CharField(max_length=1000)