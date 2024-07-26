from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse
from .models import Application
import pdb
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        
       
        passport_number = request.POST.get('passport_number')

        # Validate and process the data
        if passport_number and Application.objects.filter(visa_application_number=passport_number).exists():
            return redirect('form_display', passport_number=passport_number)
        else:
            return HttpResponse("nothing")
    return render(request, "VisaManagementSystem/home.html")

def form_display(request, passport_number):
    # Filter your database based on the passport number
    application = get_object_or_404(Application, visa_application_number=passport_number)
    
    # Render the form with the application details
    return render(request, 'VisaManagementSystem/form_display.html', {'field': application})


