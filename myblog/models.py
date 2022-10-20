from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "ID " + str(self.pk) + ": " + self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return "ID " + str(self.pk) + ": " + self.title
