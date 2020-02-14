from django.db import models

class Tutorial(models.Model):
    tut_title=models.CharField(max_length=200)
    tut_content=models.TextField()
    date_published=models.DateTimeField()

    def __str__(self):
        return self.tut_title