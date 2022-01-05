from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
    
class Postagem2(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    comentario = models.TextField()
    nota = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    date_post = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.titulo