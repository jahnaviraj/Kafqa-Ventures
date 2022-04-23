from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
       
def get_factorial(num:int=0):
    if int(num) < 0:
        return "Factorial does not exist for negative numbers."

    output = 1 
    for i in range(1, int(num) + 1 ):
        output *= i 

    return output

def factorial(req):
    num = req.GET.get("num") if req.GET.get("num") else 0

    try:
        num = int(num)
    except: 
        return HttpResponse("Only integer allowed.")

    response = get_factorial(num)
    return HttpResponse(response) 

def index(req):
    return render(req, "index.html")