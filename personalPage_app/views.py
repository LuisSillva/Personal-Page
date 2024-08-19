from django.shortcuts import render
from personalPage_app.models import PersonalInfo

# Create your views here.

def home(request):
    info = PersonalInfo.objects.first()
    print(info)
    return render(request, 'home.html', {'info':info})