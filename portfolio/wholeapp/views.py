from django.shortcuts import render

def home(request):
    return render(request,'wholeapp/index.html')
