from django.shortcuts import render
from .models import Contact

def Home_Page(request):
    
    if request== 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('Message')

         
        if name and email and message :
            contact=Contact(name=name , email=email , message=message)
            contact.save()
            context={'Success' :True}
        else : 
            context=context = {'error': 'Tous les champs sont obligatoires.'}
        return render (request, 'index.html' ,context)
 

    return render(request, 'index.html')  
