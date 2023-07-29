from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
import json

def index(request):

    return HttpResponse("<h1>Curriculum Lucy</h1>")

class Inicio  (View):
    template_name="index.html"

    def post(self,request):
        return render (request)
    

    def get(self,request):
        datos = {
        "nombres" : "Lucy",
        "primer_apellido" : "Padilla",
        "segundo_apellido" : "Mendoza",
        "fecha_nacimiento" : "08/11/1983",
        "celular" : 331365580,
        "correo" : "lucybrit@gmail.com",
        "domicilio" : "Guarnicion 21",
        "genero" : "Femenino",
        "Objetivo" : "Aprender Python",
        "Salario Esperado": "$100,000,000"
        }
   
        skills= {
            "skills_2" : ("WAS", "SQL", "K8", "Jenkins")
            }

        trabajos = {
        "lugar_trabajo" : "Amdocs",
        "año_inicio": "2016",
        "año_fin" : "indefinido",
        "puesto": "Technology Engineer"
        }

        dicmaster={
            **datos,
            **skills,
            **trabajos
        }




        return render (request,self.template_name, dicmaster)

    