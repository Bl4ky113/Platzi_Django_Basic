import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question (models.Model):
    question_str = models.CharField(max_length=256)
    publication_date = models.DateTimeField('date published')

    def __str__ (self):
        return str(self.question_str)

    def was_published_recently (self):
        return timezone.now() >= self.publication_date >= timezone.now() - datetime.timedelta(days=1)

class Choice (models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_str = models.CharField(max_length=128)
    choice_votes = models.IntegerField(default=0)

    def __str__ (self):
        return str(self.choice_str)
