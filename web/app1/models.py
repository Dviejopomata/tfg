from django.db import models

class Cliente(models.Model):
    identificacion = models.CharField(max_length=12)
    nombre = models.CharField(max_length=60)

class Familia(models.Model):
    identificacion = models.CharField(max_length=12)
    nombre = models.CharField(max_length=60)
    descuento = models.DecimalField(decimal_places=2, max_digits=4)

class Producto(models.Model):
    identificacion = models.CharField(max_length=12)
    nombre = models.CharField(max_length=60)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE)
    precio = models.DecimalField(decimal_places=2, max_digits=10)

class Venta(models.Model):
    numero = models.CharField(max_length=12)
    fecha = models.CharField(max_length=60)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(decimal_places=2, max_digits=4)


class VentaLinea(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(decimal_places=2, max_digits=10)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    descuento = models.DecimalField(decimal_places=2, max_digits=4)
    iva = models.DecimalField(decimal_places=2, max_digits=4)

    def importe_bruto(self):
        return round(self.cantidad * self.precio, 2)

    def importe_descuento(self):
        return round(self.importe_bruto * self.descuento, 2)

    def importe_con_descuento(self):
        return (self.importe_bruto - self.importe_descuento)

    def importe_iva(self):
        return round(self.importe_con_descuento * self.iva, 2)

    def importe_total(self):
        return self.importe_con_descuento - self.importe_iva
