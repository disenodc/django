from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view
def home(request):
	return HttpResponse("Hello")
	#return render(request, "home.html", {}) #response