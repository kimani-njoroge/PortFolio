from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    desc = models.TextField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects