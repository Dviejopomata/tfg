from django import forms

class DireccionForm(forms.Form):
    calle = forms.CharField(label='calle', max_length=100)
    poblacion = forms.CharField(label='poblacion', max_length=100)


class AdjuntoForm(forms.Form):
    fecha = forms.DateField()
    hora = forms.TimeField()
    fechahora = forms.DateTimeField()
    fichero = forms.ImageField(widget=forms.FileInput())
    texto = forms.CharField(widget=forms.Textarea)
    
