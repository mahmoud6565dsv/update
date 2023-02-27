from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Calc (models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE , null=True , blank=True)
    title = models.CharField(max_length=200 )
    description = models.TextField(null= True , blank=True)
    created = models.DateTimeField(blank=True , default= datetime.datetime.now)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed']
    