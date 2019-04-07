from django.shortcuts import render

# Create your views here.
def index(request):
    words = '欢迎光临~'
    return render(request, 'index.html', context={'words': words})