from django.shortcuts import render, redirect
from .forms import PersonaForm, AutoForm, DireccionForm
from .models import Persona, Auto, Direccion

def listar_personas(request):
    personas = Persona.objects.prefetch_related('autos', 'direcciones').all()
    context = {'personas': personas}
    return render(request, 'miapp/listar_personas.html', context)

def insertar_datos(request):
    if request.method == 'POST':
        form_persona = PersonaForm(request.POST)
        form_auto = AutoForm(request.POST)
        form_direccion = DireccionForm(request.POST)
        if form_persona.is_valid() and form_auto.is_valid() and form_direccion.is_valid():
            persona = form_persona.save()
            auto = form_auto.save(commit=False)
            auto.persona = persona
            auto.save()
            direccion = form_direccion.save(commit=False)
            direccion.persona = persona
            direccion.save()
            return redirect('listar_personas')
    else:
        form_persona = PersonaForm()
        form_auto = AutoForm()
        form_direccion = DireccionForm()
    
    context = {
        'form_persona': form_persona,
        'form_auto': form_auto,
        'form_direccion': form_direccion,
    }
    return render(request, 'miapp/insertar_datos.html', context)

def borrar_datos(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    persona.delete()
    return redirect('listar_personas')