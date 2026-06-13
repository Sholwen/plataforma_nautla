from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def lista_eventos(request):
    return render(request, 'lista_eventos.html')

def detalle_evento(request):
    return render(request, 'detalle_evento.html')