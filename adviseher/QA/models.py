from django.db import models
from

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.Autofield(primary_key=True)
    question_text = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
    