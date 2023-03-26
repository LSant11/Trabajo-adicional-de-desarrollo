from django.db import models

# Create your models here.
class Ferreteria (models.Model):
    id = models.AutoField(primary_key=True)
    Nombre=models.CharField(max_length=100,verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    descripcion =models.TextField(verbose_name="Descripcion",null=True)

    def __str__(self):
        fila = "Nombre:" + self.Nombre + " - " + "Descripcion: " + self.descripcion
        return fila

    def delete (self, using=None , keep_parents=False ):
         self.imagen.storage.delete(self.imagen.name)
         super().delete()
        
class Usuario (models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=100)
    password= models.CharField(max_length=50)
    nombre =models.CharField(max_length=50)
    tipousu =models.IntegerField()
    
class Registro (models.Model):
    id = models.AutoField(primary_key=True)
    usuario1=models.CharField(max_length=100)
    password1= models.CharField(max_length=50)
    repepaswor=models.CharField(max_length=50)
    emagi =models.EmailField()