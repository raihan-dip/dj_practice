from django.shortcuts import render

# Create your views here.

def courseinfo(request):
    return render(request,'course/courseinfo.html')