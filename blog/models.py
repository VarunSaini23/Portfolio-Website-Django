from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()

    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")
