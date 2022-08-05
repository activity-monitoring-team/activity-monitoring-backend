from django.db import models


class Projects(models.Model):
    
    title = models.CharField(max_length=250)
    about = models.TextField(max_length=500)
    image = models.ImageField()
    link = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'projects'
    
    
    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    


class Clients(models.Model):
    
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=30, blank=True, null=True)
    message = models.CharField(max_length=30, blank=True, null=True)
    lang = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        db_table = 'clients'