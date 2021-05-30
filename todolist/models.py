from django.db import models
from django.db.models.fields import CharField
 
# Create your models here.
class Todolist(models.Model):
    text = CharField(max_length = 45)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.text
            