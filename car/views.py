from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,"test/home.html")
def cars(request):
	return render(request,"test/cars.html")
def spare(request):
	return render(request,"test/spare.html")
def service(request):
	return render(request,"test/service.html")
def contact(request):
	return render(request,"test/contact.html")
def toyota(request):
	return render(request,"test/toyota.html")
def hyundai(request):
	return render(request,"test/hyundai.html")
def ford(request):
	return render(request,"test/ford.html")
def nissan(request):
	return render(request,"test/nissan.html")
def honda(request):
	return render(request,"test/honda.html")
def audi(request):
	return render(request,"test/audi.html")
def bmw(request):
	return render(request,"test/bmw.html")
def rollsroyce(request):
	return render(request,"test/rollsroyce.html")
def marutisuzuki(request):
	return render(request,"test/marutisuzuki.html")
def tata(request):
	return render(request,"test/tata.html")
def door(request):
	return render(request,"test/door.html")
def gear(request):
	return render(request,"test/gear.html")
def hyst(request):
	return render(request,"test/hyst.html")
def msbumper(request):
	return render(request,"test/msbumper.html")
def nw(request):
	return render(request,"test/nw.html")
