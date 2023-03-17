from django.db import models

# Create your models here.


class FormQuestion(models.Model):
    revName = models.CharField(max_length=50)
    revSurname = models.CharField(max_length=50)
    revEmail = models.EmailField(max_length=100)
    revQuestion = models.CharField(max_length=1000)
    revTime = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.revEmail
