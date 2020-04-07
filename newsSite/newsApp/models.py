from django.db import models

# Create your models here.

class Story(models.Model):
    Headline_text = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.Headline_text, self.description, self.pub_date

