from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
       
def get_factorial(num:int):
    output = 1 
    for i in range(1, num + 1 ):
        output *= i 
    return output

def factorial(req):
    num = req.GET.get("num")
    if num:
        try:
            int(num)
            if int(num) == 0:
                return HttpResponse(1) 
            elif int(num) < 0:
                return HttpResponse("Factorial does not exist for negative numbers.")
            else:
                return HttpResponse(get_factorial(int(num))) 
        except ValueError: 
            return HttpResponse("Only integer allowed.")
    else:
        return HttpResponse("Provide a number using num as the keyword") 
