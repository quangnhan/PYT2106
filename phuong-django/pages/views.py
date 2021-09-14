from django.shortcuts import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse("Home Page")

def about_page(request):
    return HttpResponse("About Page")