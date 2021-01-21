from django.db import models

# Create your models here.


class ProjectInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    github = models.URLField()
    demo = models.URLField()
    image = models.FileField(upload_to="photos/")
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
