
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

# Libreria para debuggear
import pdb;

# todas las vistas reciben un request
def hello_world(request):
    """ Return a hello world """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh hi, current server time is {now}'.format(
        now=str(now)
    ))

def non_sorted_numbers(request):
    """" Return a text with the values passed in the URL by the user"""
    # pdb se detiene en la linea de codigo donde la llamamos y podemos hacer consultas al backend por consola
    # por ejemplo: para ver los valores de la request (request.META, request.GET, request.method, etc.)
    #pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse('Hi! this are your selected numbers: {numbers}'.format(numbers=str(numbers)))

def sorted_numbers(request):
    """ Return a list with the numbers of the URL in json format - like an API."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status' : 'ok',
        'numbers' : sorted_ints,
        'message' : 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), # espacio de identacion
        content_type='application/json'
    )
    
# Luego de la request, van los parametros que el usuario pasa en la URL y que definimos en urls.py
def say_hi(request, name, age):
    """"Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)

    return HttpResponse(message)

