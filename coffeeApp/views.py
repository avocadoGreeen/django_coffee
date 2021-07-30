from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'coffeeApp/index.html')

def catalog(request):
    return render(request, 'coffeeApp/catalog.html')

def gallery(request):
    return render(request, 'coffeeApp/gallery.html')
