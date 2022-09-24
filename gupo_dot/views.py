from urllib import request
from rest_framework.decorators import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import status
import json
import time
palindromo =[]
@api_view(['POST'])
@permission_classes((AllowAny, ))
def palindromo(request):
    print(request.GET.get("my_name"))
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body["cadena"])
    cadena = body["cadena"]
    verificar_cadena(cadena,request)
    #print(palindormo)
    return Response(
            {
                "data":"sdsdsdsdsdsdsdsdsdsds",
                "RoEspec":"sdsdsdsdsdsdsdsdsdsds",
                "table":"sdsdsdsdsdsdsdsdsdsds",
                "df_tabla":"sdsdsdsdsdsdsdsdsdsds",
            }
        )
    
def verificar_cadena(cadena,request):
    paso =0
    for caracter in range(0,len(cadena)):
        paso += verificar_palindromo(cadena, caracter - 1, caracter + 1,request)
        paso += verificar_palindromo(cadena, caracter, caracter + 1,request)

def verificar_palindromo(cadena,caracter_ant,caracter_sig,request):
    paso = 0
    palindromo=[]
    while caracter_ant >= 0 and caracter_sig < len(cadena):
        if cadena[caracter_ant] != cadena[caracter_sig]:
            break
        palindromo.append(cadena[caracter_ant: caracter_sig + 1])
        #print(cadena[caracter_ant: caracter_sig + 1])
        #palindromo.append[cadena[caracter_ant: caracter_sig + 1]]
        paso += 1
        caracter_ant -= 1
        caracter_sig += 1
    my_name = "Nidhi"
    _mutable = request.GET._mutable
    request.GET._mutable = True
    request.GET['my_name'] = my_name
    return paso