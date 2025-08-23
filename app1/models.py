from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'persons'