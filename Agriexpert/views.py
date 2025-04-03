from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcom Home page</h1>")

def about(request):
    return HttpResponse("<h1>Welcome  About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome e</h1>")
