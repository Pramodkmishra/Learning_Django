from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def abc(request):
    print('abc')
    return render(request,'index.html')
