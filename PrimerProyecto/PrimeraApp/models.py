from django.db import models
from datetime import datetime

# Create your models here.
class Type(models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):  #Cual será el atributo que representará a la tabla 'Employes'
        return self.name

    class Meta:         #No siempre es necesario, para propiedades de la tabla
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']     #ordenamiento ascendente, si queremos descendente:'-id'

class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    def __str__(self):  #Cual será el atributo que representará a la tabla 'Employes'
        return self.name

    class Meta:         #No siempre es necesario, para propiedades de la tabla
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
        ordering=['id']     #ordenamiento ascendente, si queremos descendente:'-id'

class Employes(models.Model):
    categ=models.ManyToManyField(Category) #Relación muchos a muchos
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    names=models.CharField(max_length=150, verbose_name='Nombres',default='sin nombre')
    dni=models.CharField(max_length=8, unique=True,verbose_name='Dni')
    date_joined=models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    date_creation=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField(default=0)
    gender=models.CharField(max_length=50)
    salary=models.DecimalField(default=0.00, max_digits=8,decimal_places=2)
    state=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae=models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):  #Cual será el atributo que representará a la tabla 'Employes'
        return self.names

    class Meta:         #No siempre es necesario, para propiedades de la tabla
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id']     #ordenamiento ascendente, si queremos descendente:'-id'
