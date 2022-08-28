# Create your views here.
from django.shortcuts import render
from datetime import date

from AppFamiliares.models import Familiar


# Create your views here.


def get_familiares(request):

    # return HttpResponse("Hola")
    # return render(request, "Familiares/familiares.html")
    familiares = []
    familiar_1 = Familiar(nombre="Marcelo", apellido="Loray",
                          fecha_nacimiento="1998-22-02")
    familiar_2 = Familiar(nombre="Gabriela", apellido="Mendiburu",
                          fecha_nacimiento="1998-22-02")
    familiar_3 = Familiar(nombre="Camila", apellido="Loray",
                          fecha_nacimiento="1998-22-02")
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    # familiar1.save()
    familiares.append(familiar_1)
    familiares.append(familiar_2)
    familiares.append(familiar_3)
    diccionario = {"familiares": familiares}
    return render(request, 'AppFamiliares/profesores.html', diccionario)
