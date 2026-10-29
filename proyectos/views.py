from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import JsonResponse
from django.views import View
from .models import Proyecto

@method_decorator(csrf_exempt, name="dispatch")
class ProyectoView(View):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                proyecto = Proyecto.objects.get(pk=pk)
            except Proyecto.DoesNotExist:
                return JsonResponse( {"error": "Proyecto no encontrado"},status=404)

            return JsonResponse({
                "id": proyecto.pk,
                "nombre": proyecto.nombre,
                "descripcion": proyecto.descripcion
            })
        proyectos = Proyecto.objects.all()
        datos = [
            {
                "id": p.pk,
                "nombre": p.nombre,
                "descripcion": p.descripcion
            }
            for p in proyectos
        ]
        return JsonResponse(datos, safe=False)

    def post(self, request):
        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"error": "JSON invalido"},status=400)

        nombre = datos.get("nombre")
        descripcion = datos.get("descripcion")

        if not nombre or not descripcion:
            return JsonResponse({"error": "Nombre y descripcion son obligatorios"}, status=400)
        proyecto = Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )

        return JsonResponse({
            "mensaje": "Proyecto creado",
            "id": proyecto.pk,
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion
        }, status=201)

    def put(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({"error": "Proyecto no encontrado"},status=404)

        try:
            datos = json.loads(request.body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"error": "JSON invalido"}, status=400)

        nombre = datos.get("nombre")
        descripcion = datos.get("descripcion")

        if not nombre or not descripcion:
            return JsonResponse( {"error": "Se requieren nombre y descripcion"}, status=400 )

        proyecto.nombre = nombre
        proyecto.descripcion = descripcion
        proyecto.save()

        return JsonResponse({
            "mensaje": "Proyecto actualizado",
            "id": proyecto.pk,
            "nombre": proyecto.nombre,
            "descripcion": proyecto.descripcion
        })

    def delete(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse( {"error": "Proyecto no encontrado"}, status=404)

        proyecto.delete()

        return JsonResponse({
            "mensaje": "Proyecto eliminado"
        })