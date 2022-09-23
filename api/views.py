# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# from django.http import HttpResponse


def home(request):
    return JsonResponse({'Course':'Django react Course','Name': 'Srishti'})
    # return render(request, 'temp.html')
    # to fetch this name from DB
    return render(request, 'temp.html',{'name':'Srishti'})

# As we are getting data here in a request format, so we will send the data in response format.
# Above we have used JsonResponse, but we can also use HttpResponse  here by importing it.

# return HttpResponse("Watching Django Series from Telusko)