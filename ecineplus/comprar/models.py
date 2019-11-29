from django.db import models

class Cliente(models.Model):
    id_Cliente = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=30, null=False, default=False)
    p_apellido = models.CharField(max_length=50, null=False, default=False)
    m_apellido = models.CharField(max_length=50, null=False, default=False)
    edad = models.IntegerField(null=False, default=False)
    email = models.EmailField(max_length=254, null=False)
    fecha = models.DateTimeField('Fecha de registro', auto_now = True, auto_now_add=False, null=False)

    class Meta:
        verbose_name='Cliente'
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    id_Pelicula = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    dia = models.CharField(max_length=10,null=False, default=False)
    horario = models.CharField(max_length=25, null=False, default=False)
    sala = models.CharField(max_length=20, null=False, default=False)
    clasificacion = models.CharField(max_length=15, null=False)

    class Meta:
        verbose_name='Pelicula'
    def __str__(self):
        return self.nombre
    

class Boleto(models.Model):
    class Meta:
        unique_together = (('id_Boleto', 'asiento'),)
    id_Boleto = models.AutoField(primary_key=True, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    precio = models.IntegerField(null=False, default=False)
    asiento = models.IntegerField(null=False)
    