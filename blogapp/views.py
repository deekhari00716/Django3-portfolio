from django.shortcuts import render
from .models import Inside

def all_blogs(request):

    inside = Inside.objects.order_by('-date')
    return render(request, 'blogapp/all_blogs.html',{'insides':inside})
# Create your views here.
