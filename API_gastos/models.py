from django.db import models

# Create your models here.
class Gasto(models.Model):
    detalle = models.TextField()
    fecha = models.DateTimeField()
    tipo = models.TextField() # Ej: INGRESO, EGRESO
    forma_pago = models.TextField()
    monto = models.DecimalField(max_digits=10, decimal_places=2) # Mejor para dinero
    banco = models.TextField()
    tipo_movimiento = models.TextField()
    categoria = models.TextField()

    class Meta:
        managed = False
        db_table = 'hoja_gastos_neon_ready'

    def __str__(self):
        return f"{self.id}"
