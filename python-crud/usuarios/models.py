# usuarios/models.py

from django.db import models

class Usuario(models.Model):
    Id_user = models.AutoField(primary_key=True)
    Rut = models.CharField(max_length=10)
    Nombre = models.TextField()
    Apellido = models.TextField()
    
    class Meta:
        db_table = 'usuario'
        managed = False
    
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"