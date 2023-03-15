from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    UserID = models.IntegerField(null=True)
    Title = models.CharField(max_length=255, null=False)
    Content = models.CharField(max_length=255, null=False)
    Archived = models.BooleanField(default=False)
    DateOfCreate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title