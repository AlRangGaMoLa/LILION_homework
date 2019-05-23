from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('published date')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Thisisapp(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

