from django.db import models

# Create your models here.
class Myapp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateTimeField("data published")
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]