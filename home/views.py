from django.shortcuts import render

# Create your views here.
def homepage(request):
    response = request.get('http://localhost:8000/menu/')
    menu_items = response.json() if response.status_code == 200 else []

    return render(request, 'home.html', {'menu_items':menu_items})