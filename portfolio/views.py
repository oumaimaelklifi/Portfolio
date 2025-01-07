from django.shortcuts import render

def Home_Page(request):
    # Chargez la page HTML (sans appel récursif)
    return render(request, 'index.html')
