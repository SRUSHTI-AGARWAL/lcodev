# from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home(request):
    return JsonResponse({'Course':'Django react Course','Name': 'Srishti'})