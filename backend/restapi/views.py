from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .classes import Archivo
from .serializers import ArchivoSerializer
from rest_framework.decorators import api_view
from Tokenizer import Tokenizer
from django.http import JsonResponse
import ObsidianParser


# Create your views here.

# class ArchivoList(APIView):

# 	def post(self):
# 		archivos = Archivo.objects.all()
# 		serializer = ArchivoSerializer(archivos, many=True)
# 		return Response(serializer.data)

x = Tokenizer()
@api_view(['GET', 'POST'])
def rutas(request):
    if request.method == 'POST':
        d = dict(request.data)
        print "COMMING IN HOT WITH THE D"
        # print d['code'][0]

        ObsidianParser.main(d['code'][0])

        # criteria = []
        # #print d['variables_criteria'][0]
        # criteria.append(d['declaracion_criteria'][0])
        # criteria.append(d['comentariosAntes_criteria'][0])
        # criteria.append(d['constantes_criteria'][0])
        # criteria.append(d['funciones_criteria'][0])
        # criteria.append(d['variables_criteria'][0])
        # criteria.append(d['nombre_criteria'][0])
        # resultados = []
        # for fileitem in d['archivos[]']:
        #     resultados.append(x.evaluar(fileitem, criteria))

        # return JsonResponse({"archivos": resultados})

        return JsonResponse({"archivos": "SOMETHING"})

    elif request.method == 'GET':
        return Response({"message": "Hello, world!"})
