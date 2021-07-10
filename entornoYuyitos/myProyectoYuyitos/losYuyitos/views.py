from losYuyitos.models import Promocion
from django.shortcuts import render
import base64

# Create your views here.
def index(request):
    promocion = Promocion.objects.all()
    arreglo = []
    for i in promocion:
        data = {
            
            'imagen':base64.b64encode(i.imagen_promo).decode()
        }
        arreglo.append(data)
    return render(request,'web/base.html',{'promocion':arreglo})