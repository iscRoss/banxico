import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'index.html')

class Api(generics.ListAPIView):
    def get(self, request):
        list = []
        list_promedio = []
        list_number = []
        list_dolar = []
        list_promedio_dolar = []
        list_number_dolar = []
        list_tiie = []
        list_promedio_tiie = []
        list_number_tiie = []
        suma = 0
        suma_dolar = 0 
        suma_tiie =0

        f_inicial = self.request.query_params['f_inicial']
        f_final = self.request.query_params['f_final']
        if f_final > f_inicial:
            urlfechaRangoUDIS = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos/{f_inicial}/{f_final}/?token={settings.TOKEN}"
            urlfechaRangoDolar = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/{f_inicial}/{f_final}/?token={settings.TOKEN}"
            urlfechaRangoTIIE = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF61745/datos/{f_inicial}/{f_final}/?token={settings.TOKEN}"

            response = requests.get(urlfechaRangoUDIS)
            response_dolar = requests.get(urlfechaRangoDolar)
            response_tiie = requests.get(urlfechaRangoTIIE)

            if response.status_code == 200:
                response_json = json.loads(response.text)
                response_json_dolar = json.loads(response_dolar.text)
                response_json_tiie = json.loads(response_tiie.text)
                #Ciclo UDIS
                for i in response_json["bmx"]["series"]:
                    for j in i["datos"]:
                        context = {"fecha":j["fecha"], "dato":j["dato"]}
                        context_promedio = {float(j["dato"])}
                        list.append(context)
                        list_promedio.append(context_promedio)
                        list_number.append(float(j["dato"]))
                        suma = suma + float(j["dato"])
                    promedio = suma/len(list_promedio)
                    max_value = max(list_number)
                    min_value = min(list_number)
                #Ciclo dolar
                for a in response_json_dolar["bmx"]["series"]:
                    for b in a["datos"]:
                        context_dolar = {"fecha":b["fecha"], "dato":b["dato"]}
                        context_promedio_dolar = {float(b["dato"])}
                        list_dolar.append(context_dolar)
                        list_promedio_dolar.append(context_promedio_dolar)
                        list_number_dolar.append(float(b["dato"]))
                        suma_dolar = suma_dolar + float(b["dato"])
                    promedio_dolar = suma_dolar/len(list_promedio_dolar)
                    max_value_dolar = max(list_number_dolar)
                    min_value_dolar = min(list_number_dolar)
                #Ciclo dolar
                for z in response_json_tiie["bmx"]["series"]:
                    for x in z["datos"]:
                        context_tiie = {"fecha":x["fecha"], "dato":x["dato"]}
                        context_promedio_tiie = {float(x["dato"])}
                        list_tiie.append(context_tiie)
                        list_promedio_tiie.append(context_promedio_tiie)
                        list_number_tiie.append(float(x["dato"]))
                        suma_tiie = suma_tiie + float(x["dato"])
                    promedio_tiie = suma_tiie/len(list_promedio_tiie)
                    max_value_tiie = max(list_number_tiie)
                    min_value_tiie = min(list_number_tiie)
                data = {
                    "list":list,
                    "promedio":round(promedio, 6),
                    "max_value":max_value,
                    "min_value":min_value,
                    "list_dolar":list_dolar,
                    "promedio_dolar":round(promedio_dolar, 6),
                    "max_value_dolar":max_value_dolar,
                    "min_value_dolar":min_value_dolar,
                    "list_tiie":list_tiie,
                    "promedio_tiie":round(promedio_tiie, 6),
                    "max_value_tiie":max_value_tiie,
                    "min_value_tiie":min_value_tiie,
                }

                return JsonResponse(data, safe=False)
            else:
                messages.warning(
                    request, "Error")
            return JsonResponse("No encontrado", safe=False)
        else:
            messages.warning(
                    request, "Error")
            return JsonResponse("Error en fechas", safe=False)

class ApiRest(APIView):
    def get(self, request):
        list = []

        response = requests.get(urlfecha_)
        if response.status_code == 200:
            response_json = json.loads(response.text)
            for i in response_json["bmx"]["series"]:
                for j in i["datos"]:
                    context = {"fecha":j["fecha"], "dato":j["dato"]}
                    list.append(context)
        return JsonResponse(list, safe=False)
