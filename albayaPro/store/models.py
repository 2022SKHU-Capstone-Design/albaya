from csv import writer
from django.db import models
from join.models import *

# Create your models here.

class Notice(models.Model) :
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class NoticeCommnet(models.Model):
    notice_id = models.ForeignKey(Notice, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Suggestion(models.Model) :
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    writer = models.CharField(max_length=10)
    # writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='writer')
    body = models.TextField()

    def __str__(self):
        return self.title

class SuggestionCommnet(models.Model):
    notice_id = models.ForeignKey(Suggestion, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment