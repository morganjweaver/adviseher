from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    mentee_mentor_both = models.IntegerField(default=2)
class Profile:
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=100)
    description = models.CharField(max_length=140)
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.Autofield(primary_key=True)
    question_text = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    upvotes = models.IntegerField(default=0)
class Review(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User)
    question_id = models.ForeignKey(Question)
    note_text = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)


