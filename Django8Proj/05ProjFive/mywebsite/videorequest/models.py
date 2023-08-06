from django.db import models
from django.utils import timezone

# Create your models here.
class Video(models.Model):
    vtitle = models.CharField(max_length=20)
    vdesc = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.vtitle, self.id)
