from django.db import models
from PIL import Image

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/images")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Skills(models.Model):
    name = models.CharField(max_length=75)
    basico = 'BASICO'
    intermedio = 'INTERMEDIO'
    avanzado = 'AVANZADO'
    levels_choices = [(basico, "Básico"), (intermedio, "Intermedio"), (avanzado, "Avanzado")]
    levels = models.CharField(max_length=10,choices=levels_choices,default=basico)
    icon = models.ImageField(upload_to="portafolio/icons",null=True)

    def save(self,*args, **kwargs):
        if self.icon:
            img = Image.open(self.icon)
            img = img.resize((150,150), Image.ANTIALIAS)
            img.save(self.icon.path)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

