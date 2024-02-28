from django.shortcuts import render

from .models import DB

# Create your views here.
def home(req):
    db = DB.objects.all()
    return render(req, 'home.html', {'db':db})
