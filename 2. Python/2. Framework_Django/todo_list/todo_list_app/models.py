from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    taskContent = models.CharField(max_length=250, null=False)
    complete = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    dateOfCreated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title